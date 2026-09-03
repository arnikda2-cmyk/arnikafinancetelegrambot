
from PIL import Image, ImageDraw, ImageFont
from pathlib import Path
import math

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "poster_test.png"

# قالب آزمایشی؛ در مرحله بعد همین ساختار با فایل‌های اصلی ۱۲ کادر نهایی جایگزین می‌شود.
W, H = 1080, 1920
img = Image.new("RGB", (W, H), "#111318")
draw = ImageDraw.Draw(img)

def font(size):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/noto/NotoSansArabic-Regular.ttf",
    ]
    for p in candidates:
        if Path(p).exists():
            return ImageFont.truetype(p, size)
    return ImageFont.load_default()

title = font(52)
head = font(34)
body = font(28)
small = font(22)

# 12 fixed cards: 3 columns x 4 rows
margin = 36
gap = 18
cw = (W - 2*margin - 2*gap) // 3
ch = (H - 2*margin - 3*gap) // 4

cards = [
    ("01", "آرنیکا فایننس", "تحلیل گرم طلای ۱۸ عیار"),
    ("02", "وضعیت فعلی", "قیمت: 22.9 میلیون تومن"),
    ("03", "روند", "کوتاه‌مدت: صعودی\nمیان‌مدت: صعودی"),
    ("04", "حمایت", "22.2\n21.8\n21.1"),
    ("05", "مقاومت", "22.95–23.0"),
    ("06", "محتمل‌ترین سناریو", "حفظ 22.2 و تلاش برای شکست 23"),
    ("07", "هدف کوتاه‌مدت", "23.5 → 24"),
    ("08", "اونس جهانی", "حدود 4,368 دلار"),
    ("09", "سناریوی مخالف", "زیر 22.2 → 21.8"),
    ("10", "هدف میان‌مدت", "25 → 26 میلیون تومن"),
    ("11", "دنبال گن", "P → 9 → 17 → 26 → 33\nریست با P جدید"),
    ("12", "جمع‌بندی", "ساختار صعودی؛ 23 گره اصلی"),
]

for i, (num, h, b) in enumerate(cards):
    r, c = divmod(i, 3)
    x = margin + c*(cw+gap)
    y = margin + r*(ch+gap)
    draw.rounded_rectangle((x, y, x+cw, y+ch), radius=24, outline="#D6B15E", width=3)
    draw.text((x+22, y+18), num, font=small, fill="#D6B15E")
    draw.text((x+22, y+58), h, font=head, fill="white")
    yy = y + 120
    for line in b.split("\n"):
        draw.text((x+22, yy), line, font=body, fill="#E7E7E7")
        yy += 48

img.save(OUT, quality=95)
return_path = OUT
