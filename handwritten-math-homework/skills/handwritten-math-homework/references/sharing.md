# Share and install

The ZIP contains one complete `handwritten-math-homework/` directory, including SKILL.md, the default style images, the profile manager and sampling sheet. Sharing SKILL.md alone omits the handwriting references. The portable package contains no checkpoints, CUDA environment, API keys, creator-machine runtime paths or custom personal profiles.

## Simple local installation

Unzip and put the whole directory under your personal Codex skills location. Current official documentation lists `~/.agents/skills/` for user skills; on Windows this is `%USERPROFILE%\.agents\skills\`. The resulting entrypoint is `~/.agents/skills/handwritten-math-homework/SKILL.md`. A project-specific installation can use `.agents/skills/handwritten-math-homework/` inside the project instead. Avoid a duplicate copy with the same name in multiple discovered locations.

Start a new conversation and say: `Use $handwritten-math-homework on this PDF with the default style.` Codex detects skills; if it does not appear, restart the app. You can also ask Codex to install the folder or, after it is placed in a Git repository, ask `$skill-installer` to install from that repository path.

The host needs image generation/editing and local PDF/file tools. Installing this skill does not provide those capabilities or make image generation available to an account that lacks it. Built-in image generation needs no separate API key. Other agents can read the instructions, but capability compatibility has not been tested on every host.

## Public distribution

For casual sharing, send the ZIP or publish its contents in a Git repository. For installable public distribution beyond a repository, OpenAI recommends packaging skills as a plugin. This ZIP is a local skill bundle, not a published plugin or marketplace listing. Publication and redistribution terms are separate decisions; no repository or listing was created automatically.

Official guide checked 2026-10-16: https://learn.chatgpt.com/docs/build-skills

## Create personal handwriting

Tell the agent: `Initialize profile alex from these handwriting samples and show a calibration page.` Upload 2-4 sample pages. See [profile workflow](profiles.md) and [sampling sheet](sampling-sheet.md). Once the page is accepted, later requests can simply say `Use profile alex`. Default remains the bundled creator style when no profile is specified.

Only bundled default references are included here. Personal samples created after installation stay outside the shared skill and are not automatically shared with others. Image-generation tools still receive the selected samples when used for calibration/rendering.
