from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw

BOTTOM_TEXT = "BOTTOM TEXT"

img = Image.open("img/test.jpg")
draw = ImageDraw.Draw(img)

impact = ImageFont.truetype("fonts/impact.ttf", 150)
draw.text((1000,750), BOTTOM_TEXT, (255, 255, 255), font=impact)
img.save("static/btm-txt.jpg")
