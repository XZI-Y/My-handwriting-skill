# Accepted rendering recipe

## Acceptance and reference roles

On 2026-10-16 the user said they were satisfied with **only the modified results** of the two assignments. Accepted deliverables are `组合学HW4-符号与精简修订版.pdf` and `组合学HW5-笔迹与符号修订版.pdf`. The earlier HW5 full-handwriting PDF and first mild edit are not accepted style targets. See [provenance](accepted-revisions.json) for source files and representative page hashes.

Default inputs, inspect once:

1. [Revised HW4 page 3](accepted-hw4-revised-page-03.png): primary target for page color, narrow letterforms, informal symbols and placement.
2. [Actual handwriting sample](hw2-revised-page-1.png): secondary reference for thin angular symbol strokes and irregularity. Its printed question and unverified mathematical content are not to be copied.

The [revised HW5 page 1](accepted-hw5-revised-page-01.png) illustrates product/union signs and local letter-size changes; [revised HW5 page 4](accepted-hw5-revised-page-04.png) illustrates Sigma, fraction, inequalities, bars and varied placement. Open only when the relevant visual distinction needs checking. Do not treat an old historical rejection note as invalidating these newer accepted pages.

The two main observations from HW5: anchoring an edit to the neat rejected target retained too much regularity; rendering directly from the accepted HW4 reference plus the actual stroke reference produced the accepted stronger revision. Use the successful conditioning from the outset. For a small content correction, an edit target is appropriate but explicitly preserve the surrounding stroke style.

## Default prompt

Adapt the header reservation and content to each page; the percentages below are appearance cues, not a rigid layout grid. Keep the exact answer in a separate block. Do not send a full PDF to image generation or ask it to reproduce printed questions.

> Use case: style-transfer. Create a portrait A4 English mathematics answer page in loose, irregular handwritten pen strokes. Image 1 is the desired revised HW4 paper and letterforms. Image 2 is an actual handwritten symbol/stroke reference. Copy the thin scratchy angular quality of the handwriting in image 2 and the pale ivory lightly worn paper of image 1. Do not copy their text or printed questions.
>
> Use narrow quick letters with visible local width/height changes, roughly 15-25% in some occurrences, unequal word gaps and thin mildly inconsistent ink. Make mathematical symbols as casual as the prose. Pi is a rough horizontal cap over two unequal legs, without feet or serifs. Sigma starts nearly horizontally, without an upward leading flick. Cardinality bars lean independently or bow slightly. Parentheses are asymmetric, sometimes angular. Equals strokes have unequal lengths; inequality arms and their short underbars are individually placed. Union cups have uneven arms; brackets and Greek letters are imperfect but identifiable. Superscripts/subscripts are small, varied and correctly attached. Every fraction is vertically stacked, including inline and script fractions; preserve binomial nesting.
>
> Write on gently rising/falling local baselines. Change some left starts between about 4%, 7% and 10%; give formula blocks differing offsets around 12-28%. Use unequal paragraph/line gaps, not a uniform margin or centered equation grid. Do not apply uniform random jitter or rotate a tidy page. Keep mathematics legible; no invented errors, missing words or crossings-out.
>
> Reserve the top {HEADER_PERCENT}% as completely blank paper for a separately composited original question. Keep answer strokes below that reservation, with about 4% side/bottom margins. No title, cover, page number or extra writing. Preserve every word, sign, bound, index and mathematical meaning below; line breaks may change.
>
> EXACT ANSWER: {PAGE_TEXT}

Header reservation must come from measured crop height plus a safe gap. If the answer cannot fit comfortably, split it first rather than squeezing it into the page. In composition, restore only the actual question area; the generator may start a little earlier than requested, so inspect the real clearance.

## Internal pilot acceptance

Before extending to the full assignment, compare the pilot to the accepted HW4/HW5 pages:

- Fine narrow pen writing rather than thick rounded generic handwriting.
- Visible differences within repeated symbols and letterforms; no Pi/Sigma serif feet or mirror-image delimiters.
- Baselines, line starts, word gaps and equation offsets visibly differ. A slight global tilt alone fails.
- No slash fractions, missing summation limits, accidental subscripts in products, printed math repair or corrupted transpose/inverse.
- Complete exact content with space under the original question crop.

If it fails style, revise the pilot with one concrete defect description, then use the improved recipe for subsequent pages. Do not first batch the entire assignment and knowingly depend on a second user prompt to make it loose. If a local formula repair introduces print-style fragments, repair just that region with the same thin pen; never conceal the defect with paper ageing.

Keep correctness checks independent of style checks. This recipe improves the initial conditioning; it does not guarantee that every generation passes without local repair.
