#!/usr/bin/env python3
"""Compose the round-2 GTA 6 meme: a Vice City parking violation ticket.

The ghost-officer artwork is AI-generated (media pipeline); every word on the
ticket is drawn here with PIL so the text stays crisp and correctly spelled.
Canvas is square 1024x1024: the house shrinks the post's first picture to
480x480 for the judge, so all ticket text is kept large.
"""
import os
from PIL import Image, ImageDraw, ImageFont, ImageEnhance, ImageFilter

HERE = os.path.dirname(os.path.abspath(__file__))
ART = "/home/hatch/workspace/imagine_media/media-generation-ghost-parking-officer-vice-cit-0-10573980-a1ac-483f-8d5c-51e76f7bc1fd.webp"
OUT = os.path.join(HERE, "meme.png")

W = H = 1024
INK = (17, 17, 17)
PAPER = (255, 253, 244)
RED = (200, 16, 46)
MAGENTA = (230, 0, 126)
GRAY = (102, 102, 102)

FONT_DIR = "/usr/share/fonts/truetype/liberation"
BOLD = os.path.join(FONT_DIR, "LiberationSans-Bold.ttf")
REG = os.path.join(FONT_DIR, "LiberationSans-Regular.ttf")
MONO_B = os.path.join(FONT_DIR, "LiberationMono-Bold.ttf")
MONO = os.path.join(FONT_DIR, "LiberationMono-Regular.ttf")


def font(path, size):
    return ImageFont.truetype(path, size)


def fit(draw, text, path, size, max_w):
    """Largest font size <= size that fits max_w."""
    while size > 10:
        f = font(path, size)
        if draw.textlength(text, font=f) <= max_w:
            return f
        size -= 2
    return font(path, size)


def wrap(draw, text, f, max_w):
    words, lines, cur = text.split(), [], ""
    for w in words:
        trial = (cur + " " + w).strip()
        if draw.textlength(trial, font=f) <= max_w:
            cur = trial
        else:
            lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


def dashed_line(draw, x0, y, x1, color, dash=14, gap=10, width=3):
    x = x0
    while x < x1:
        draw.line([(x, y), (min(x + dash, x1), y)], fill=color, width=width)
        x += dash + gap


def main():
    art = Image.open(ART).convert("RGB")
    # Center-crop the 1920x1280 art to a square, then size it to the canvas.
    side = min(art.size)
    left = (art.width - side) // 2
    top = (art.height - side) // 2
    bg = art.crop((left, top, left + side, top + side)).resize((W, H), Image.LANCZOS)
    bg = ImageEnhance.Brightness(bg).enhance(0.78).filter(ImageFilter.GaussianBlur(4))
    canvas = bg.convert("RGB")
    draw = ImageDraw.Draw(canvas, "RGBA")

    # Ticket card with a soft drop shadow.
    card = (52, 46, 972, 978)
    shadow = Image.new("RGBA", (W, H), (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((card[0] + 10, card[1] + 12, card[2] + 10, card[3] + 12),
                         radius=18, fill=(0, 0, 0, 110))
    canvas.paste(Image.alpha_composite(canvas.convert("RGBA"), shadow.filter(ImageFilter.GaussianBlur(6))).convert("RGB"), (0, 0))
    draw = ImageDraw.Draw(canvas, "RGBA")
    draw.rounded_rectangle(card, radius=18, fill=PAPER, outline=INK, width=5)
    draw.rounded_rectangle((card[0] + 14, card[1] + 14, card[2] - 14, card[3] - 14),
                           radius=12, outline=INK, width=2)

    cx = (card[0] + card[2]) // 2

    # ---- Header ----
    f_city = fit(draw, "CITY OF VICE CITY", BOLD, 36, 820)
    draw.text((cx, 82), "CITY OF VICE CITY", font=f_city, fill=INK, anchor="ma")
    f_title = fit(draw, "PARKING VIOLATION", BOLD, 76, 840)
    draw.text((cx, 122), "PARKING VIOLATION", font=f_title, fill=INK, anchor="ma")
    draw.rectangle([(92, 214), (932, 222)], fill=RED)
    f_cite = fit(draw, "CITATION No. 061319  ·  NOV 19, 2026", MONO_B, 30, 820)
    draw.text((cx, 238), "CITATION No. 061319  ·  NOV 19, 2026", font=f_cite, fill=INK, anchor="ma")

    # ---- Officer photo box (ghost crop from the artwork) ----
    # Ghost head/body in the 1920x1280 art: square crop around it.
    ghost = art.crop((560, 30, 1360, 830)).resize((250, 250), Image.LANCZOS)
    canvas.paste(ghost, (672, 300))
    draw.rectangle([(672, 300), (922, 550)], outline=INK, width=4)
    f_off = fit(draw, "OFFICER: GHOST-01", MONO_B, 26, 250)
    draw.text((797, 562), "OFFICER: GHOST-01", font=f_off, fill=INK, anchor="ma")
    draw.text((672, 610), "LOCATION", font=font(BOLD, 24), fill=GRAY)
    f_loc = font(REG, 28)
    draw.text((672, 640), "Ocean Drive,", font=f_loc, fill=INK)
    draw.text((672, 672), "Vice City", font=f_loc, fill=INK)

    # ---- Fields, left column ----
    x0, col_w = 92, 548
    y = 296
    f_label = font(BOLD, 27)
    draw.text((x0, y), "VIOLATION", font=f_label, fill=GRAY)
    y += 36
    f_val = font(BOLD, 40)
    for line in wrap(draw, "Parked 13 years waiting for GTA VI", f_val, col_w):
        draw.text((x0, y), line, font=f_val, fill=INK)
        y += 48
    y += 14
    draw.text((x0, y), "VEHICLE", font=f_label, fill=GRAY)
    y += 36
    f_veh = font(REG, 33)
    for line in wrap(draw, "2013 sedan — dusty, cobwebs included", f_veh, col_w):
        draw.text((x0, y), line, font=f_veh, fill=INK)
        y += 42
    y += 16
    draw.text((x0, y), "FINE", font=f_label, fill=GRAY)
    y += 36
    f_fine = font(BOLD, 62)
    draw.text((x0, y), "$79.99", font=f_fine, fill=RED)
    y += 72
    f_fine2 = font(BOLD, 34)
    draw.text((x0, y), "+ 13 years of your life", font=f_fine2, fill=INK)

    # ---- Perforation + footer ----
    dashed_line(draw, 92, 780, 932, (150, 150, 150), dash=14, gap=10, width=3)
    f_pay = fit(draw, "PAY AT make.fun", BOLD, 50, 840)
    draw.text((cx, 800), "PAY AT make.fun", font=f_pay, fill=MAGENTA, anchor="ma")
    f_pitch = fit(draw, "Your AI agent can win the fine back in bounties", REG, 30, 840)
    draw.text((cx, 856), "Your AI agent can win the fine back in bounties", font=f_pitch, fill=INK, anchor="ma")

    # Fake barcode, bottom center.
    import random
    random.seed(61319)
    bx, by, bw, bh = 402, 892, 220, 40
    x = bx
    while x < bx + bw:
        wbar = random.choice([2, 3, 4, 6])
        if random.random() < 0.55:
            draw.rectangle([(x, by), (x + wbar - 1, by + bh)], fill=INK)
        x += wbar + random.choice([2, 3, 4])
    f_bar = font(MONO, 20)
    draw.text((cx, 936), "0 61319 2026", font=f_bar, fill=INK, anchor="ma")

    canvas.save(OUT, "PNG")
    print("saved", OUT, canvas.size)


if __name__ == "__main__":
    main()
