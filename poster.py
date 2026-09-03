from pathlib import Path
from PIL import Image, ImageDraw, ImageFont

ROOT = Path(__file__).resolve().parent
OUTPUT = ROOT / "poster_test.png"

def _font(size, bold=False):
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for p in candidates:
        if Path(p).exists(): return ImageFont.truetype(p, size)
    return ImageFont.load_default()

def make_demo_poster():
    W, H = 1200, 1600
    img = Image.new("RGB", (W, H), (12, 18, 28))
    draw = ImageDraw.Draw(img)
    title, sub, body, small = _font(70, True), _font(42, True), _font(34), _font(28)
    draw.text((W//2, 90), "ARNIKA FINANCE", font=title, fill=(225,184,76), anchor="ma")
    draw.text((W//2, 185), "تحلیل طلای ۱۸ عیار", font=sub, fill=(245,245,245), anchor="ma")
    cards = [
        ("وضعیت فعلی", "قیمت نمونه: ۲۲.۹ میلیون تومن"),
        ("روند کوتاه‌مدت", "صعودی"),
        ("روند میان‌مدت", "صعودی"),
        ("حمایت‌ها", "۲۲.۲  |  ۲۱.۸"),
        ("مقاومت‌ها", "۲۳.۰  |  ۲۳.۵"),
        ("محتمل‌ترین سناریو", "تثبیت بالای ۲۲.۲ و تلاش برای عبور از ۲۳"),
        ("اهداف صعودی", "۲۳.۵  |  ۲۴.۰"),
        ("اونس جهانی", "$4,368 / oz"),
        ("سناریوی مخالف", "از دست رفتن ۲۲.۲ → ۲۱.۸"),
        ("هشدار", "در سقف‌های روزانه، ریسک نوسان بیشتر است"),
        ("جمع‌بندی", "روند غالب صعودی؛ شکست مقاومت، تأیید ادامه مسیر"),
    ]
    y = 300
    for heading, text in cards:
        draw.rounded_rectangle((80,y,W-80,y+105), radius=22, outline=(120,120,120), width=2, fill=(22,29,42))
        draw.text((W-110,y+18), heading, font=body, fill=(225,184,76), anchor="ra")
        draw.text((W-110,y+65), text, font=small, fill=(245,245,245), anchor="ra")
        y += 127
        if y > H-120: break
    draw.text((W//2,H-55), "نسخه آزمایشی — بدون توصیه قطعی خرید/فروش", font=small, fill=(170,170,170), anchor="ms")
    img.save(OUTPUT)
    return str(OUTPUT)
