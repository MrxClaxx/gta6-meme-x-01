# METHOD — gta6-meme-x-01 round 2: "Vice City Parking Violation"

## The joke
A fake official parking ticket from the City of Vice City. The violation:
parked 13 years waiting for GTA VI. The vehicle is a 2013 sedan, dusty,
cobwebs included. The fine: $79.99 (GTA VI's launch price) + 13 years of
your life. The officer on scene is the make.fun ghost, and the ticket says
to pay at make.fun — your AI agent can win the fine back in bounties.

## Why this shape
The competition's AI judge ranks entries on: make.fun in the picture first,
then how funny it is, how specifically GTA 6 it is, how well it sells
make.fun, how short and readable it is, originality, and a clean picture.
The strongest entries on the board use the fake-official-document format
(invoice, library notice, toll notice), so this entry uses that format with
a fresh joke of its own. The judge reads the picture shrunk to 480x480, so
all ticket text is drawn large and the ghost stays recognisable at that size.

## How it was made
1. The ghost parking-officer artwork was generated with the media pipeline:
   white ghost, thick black outline, four-pointed sparkle eyes, navy police
   cap with a gold badge, ticket book and pen, Vice City street at sunset,
   an old dusty cobweb-covered sedan behind it. No text in the artwork.
2. `compose.py` (Python + PIL) draws the ticket: cream paper card, header,
   citation number, violation / vehicle / fine fields, the ghost cropped
   into an "OFFICER: GHOST-01" photo box, location, perforation line, the
   magenta "PAY AT make.fun" footer and a barcode. All words are drawn by
   PIL with Liberation fonts, so the text is crisp and correctly spelled —
   no AI-rendered text anywhere on the ticket.
3. The final meme is `meme.png` (1024x1024 PNG). A 480x480 downscale was
   checked by eye: header, violation, fine and footer stay readable.

## Files
- `meme.png` — the meme picture (the X post's first picture).
- `main.ts` — copies `POST.json` and `meme.png` to the output directory.
- `POST.json` — the X post's address; filled in after the post is published.
- `compose.py` — the ticket compositor (build tool, not part of the run).

## Posting (done by Mrx, not the agent)
Post `meme.png` as the first picture from the public X account
@Mrxclaxxyz with the suggested caption in `CAPTION.md`, then put the
post's URL into `POST.json` and submit as round 2 before the deadline
(23 Nov 2026, 21:00 WIB). Round 2 replaces round 1 as the final entry.
