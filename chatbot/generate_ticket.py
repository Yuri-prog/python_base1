from io import BytesIO

import requests
from PIL import Image, ImageDraw, ImageFont

TEMPLATE_PATH = 'files/ticket_base.png'
FONT_PATH = 'files/Roboto-Regular.ttf'
FONT_SIZE = 20

BLACK = (0, 0, 0, 255)
NAME_OFFSET = (350, 715)
EMAIL_OFFSET = (350, 765)

AVATAR_SIZE = 100
AVATAR_OFFSET = (100, 100)
# TODO стиль кода + надо лишнее удалить
def generate_ticket(name, email):
    base = Image.open(TEMPLATE_PATH).convert("RGBA")
    font = ImageFont.truetype(FONT_PATH, FONT_SIZE)

    draw = ImageDraw.Draw(base)
    draw.text(NAME_OFFSET, name, font=font, fill=BLACK)
    draw.text(EMAIL_OFFSET, email, font=font, fill=BLACK)

    #response = requests.get(url='files/1.png')
    # avatar_file_like = BytesIO(response.content)
    # avatar = Image.open(avatar_file_like)
    #base.paste(avatar, AVATAR_OFFSET)
    # base.show()
    # with open('files/ticket_example.png', 'wb') as f:
    #     base.save(f, 'png')
    # return f
    temp_file = BytesIO()
    base.save(temp_file, 'png')
    temp_file.seek(0)
    return temp_file