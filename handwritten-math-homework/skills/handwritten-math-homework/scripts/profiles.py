"""Portable handwriting sample/profile manager; no model training or image rewriting."""
import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys

SKILL = Path(__file__).resolve().parents[1]

def stamp():
    return datetime.now(timezone.utc).isoformat()

def safe_id(value):
    if not re.fullmatch(r'[a-z0-9][a-z0-9-]{0,47}', value):
        raise ValueError('Profile ID must be 1-48 lowercase letters/digits/hyphens.')
    if value.split('.')[0].upper() in {'CON','PRN','AUX','NUL',*(f'COM{i}' for i in range(1,10)),*(f'LPT{i}' for i in range(1,10))}:
        raise ValueError('Reserved profile ID.')
    return value

def location(args):
    safe_id(args.id)
    if args.id == 'default':
        if args.command != 'show':
            raise ValueError('Bundled default is read-only; create a personal profile instead.')
        return SKILL/'profiles/default'
    root = Path(args.root or os.environ.get('HANDWRITING_PROFILE_HOME') or Path.home()/'.handwritten-math-homework/profiles').expanduser().resolve()
    dest = (root/args.id).resolve()
    if dest.parent != root:
        raise ValueError('Profile must stay inside its root.')
    return dest

def read(folder):
    data = json.loads((folder/'profile.json').read_text(encoding='utf-8'))
    return data

def save(folder, data):
    data['updated_at'] = stamp()
    tmp = folder/'profile.json.tmp'
    tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding='utf-8')
    tmp.replace(folder/'profile.json')

def attach(folder, src, kind):
    src = Path(src).expanduser().resolve(strict=True)
    if not src.is_file():
        raise ValueError('Expected a regular file.')
    allowed = {'.png','.jpg','.jpeg','.webp','.pdf'} if kind == 'samples' else {'.png','.jpg','.jpeg','.webp'}
    if src.suffix.lower() not in allowed:
        raise ValueError('Unsupported sample/reference format.')
    digest = hashlib.sha256(src.read_bytes()).hexdigest()
    sub = folder/kind
    sub.mkdir(exist_ok=True)
    dst = sub/(digest+src.suffix.lower())
    if not dst.exists():
        shutil.copy2(src,dst)
    return {'path':dst.relative_to(folder).as_posix(),'sha256':digest}

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', help='Personal profiles directory, not the skill directory')
    subs = parser.add_subparsers(dest='command', required=True)
    for name in ('init','add','prepare','accept','show'):
        sub = subs.add_parser(name)
        sub.add_argument('id')
        if name == 'init': sub.add_argument('--name', default='Personal handwriting')
        if name == 'add': sub.add_argument('--samples', nargs='+', required=True)
        if name == 'prepare': sub.add_argument('--notes', required=True)
        if name == 'accept':
            sub.add_argument('--reference', required=True)
            sub.add_argument('--evidence', required=True)
    args = parser.parse_args()
    folder = location(args)
    if args.command == 'init':
        if folder.exists(): raise ValueError('Profile already exists; no files overwritten.')
        folder.mkdir(parents=True)
        data = {'schema_version':1,'id':args.id,'display_name':args.name,'status':'collecting','method':'reference-conditioning','samples':[],'accepted_references':[],'style_notes':None,'approval':None,'created_at':stamp()}
        save(folder,data)
        shutil.copy2(SKILL/'references/sampling-sheet.md',folder/'sampling-sheet.md')
    else:
        data = read(folder)
        if args.command == 'add':
            # Adding new samples invalidates prior calibration without deleting it.
            items = [attach(folder,s,'samples') for s in args.samples]
            known = {x['sha256'] for x in data['samples']}
            for item in items:
                if item['sha256'] not in known:
                    data['samples'].append(item); known.add(item['sha256'])
            data['status'] = 'collecting'
        elif args.command == 'prepare':
            if not data['samples']: raise ValueError('Add source samples before preparing calibration.')
            notes = Path(args.notes).read_text(encoding='utf-8').strip()
            if not notes: raise ValueError('Style observations cannot be empty.')
            (folder/'style.md').write_text(notes+'\n',encoding='utf-8')
            data['style_notes'] = 'style.md'
            data['status'] = 'ready-for-review'
        elif args.command == 'accept':
            if data['status'] != 'ready-for-review': raise ValueError('Inspect samples and prepare style observations first.')
            if not args.evidence.strip(): raise ValueError('Human approval or explicit waiver evidence is required.')
            ref = attach(folder,args.reference,'accepted')
            data['accepted_references'] = [ref]
            data['approval'] = {'evidence':args.evidence,'recorded_at':stamp()}
            data['status'] = 'accepted'
        if args.command != 'show': save(folder,data)
    print(json.dumps({'profile_directory':str(folder),'profile':data},ensure_ascii=False,indent=2))

if __name__ == '__main__':
    try: main()
    except (ValueError,OSError,KeyError) as exc:
        print(str(exc),file=sys.stderr)
        sys.exit(1)
