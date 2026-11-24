"""Generate the PWA icons (icon-192.png, icon-512.png, apple-touch-icon.png)."""
from PIL import Image, ImageDraw, ImageFont

def icon(size, path, pad=0.0):
    img = Image.new("RGB", (size, size), (28, 30, 34))
    d = ImageDraw.Draw(img)
    m = int(size * (0.08 + pad))
    d.rounded_rectangle([m, int(size * 0.30), size - m, int(size * 0.70)], radius=int(size * 0.06), fill=(20, 8, 6))
    font = ImageFont.load_default(size=int(size * 0.30))
    text = "P-6"
    w = d.textlength(text, font=font)
    d.text(((size - w) / 2, size * 0.335), text, fill=(255, 90, 54), font=font)
    for i in range(16):
        x0 = m + i * (size - 2 * m) / 16
        d.rectangle([x0 + 1, size * 0.78, x0 + (size - 2 * m) / 16 - 2, size * 0.86], fill=(233, 235, 238))
    img.save(path)

icon(192, "icon-192.png")
icon(512, "icon-512.png")
icon(180, "apple-touch-icon.png")
