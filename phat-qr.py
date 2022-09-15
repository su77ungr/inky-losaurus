import glob
import os
import time
from sys import exit
from font_fredoka_one import FredokaOne
from inky.auto import auto
from inky import InkyPHAT
from PIL import Image, ImageDraw, ImageFont
import qrcode
from PIL import Image, ImageDraw, ImageFilter
import requests, json
from requests.structures import CaseInsensitiveDict
import datetime
import socket
import os, requests, socket



def get_board_info():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    board_info = dict()
    board_info["hostname"] = socket.gethostname()
    board_info["ip_address"] = s.getsockname()[0]
    return board_info


def get_time():
    e = datetime.datetime.now()
    time_info = "%s/%s//%s:%s:%s" % (e.day, e.month, e.hour, e.minute, e.second)
    return time_info


def display_info(board_info, time_info):
    inky_display = auto()
    inky_display.set_border(inky_display.BLACK)
    # compose qr code 
    # data = input("Enter text:")
    img = qrcode.make("http://192.168.2.228/admin")
    print(type(img))
    print(img.size)
    # <class 'qrcode.image.pil.PilImage'>
    # (120, 120)
    img.save('/home/kube-worker-1/Pimoroni/inky/examples/phat/resources/images/wow.png', dpi=(300,300))

    #compose qr code on top of background troplet
    im1 = Image.open('/home/kube-worker-1/Pimoroni/inky/examples/phat/resources/inky-bcs.png')
    im2 = Image.open('/home/kube-worker-1/Pimoroni/inky/examples/phat/resources/images/wow.png')
    newsize = (122, 122)
    im3 = im2.resize(newsize)
    im1.paste(im3, (0,0), mask = im3)
    im1.save('/home/kube-worker-1/Pimoroni/inky/examples/phat/resources/images/666.png',dpi=(300,300))
    img = Image.open('/home/kube-worker-1/Pimoroni/inky/examples/phat/resources/images/666.png')
    draw = ImageDraw.Draw(img)

    #api request
    url="https://api.livecoinwatch.com/coins/single"
    headers = CaseInsensitiveDict()
    headers["content-type"]="application/json"
    headers["x-api-key"] = "52d21667-5475-4a08-9ed2-2756e79470db"
    data = '{"currency":"EUR","code":"XCH","meta":false}'
    resp = requests.post(url, headers=headers, data=data)
    data = json.loads(resp.text)
    parseData = json.dumps(resp.json())
    priceObj = json.loads(parseData)
    B = priceObj["rate"]
    z = round(B, 3)
    f = str(z)
    print(f)

    # add text to background-droplet
    font = ImageFont.truetype(r'/home/kube-worker-1/Pimoroni/inky/examples/phat/resources/ARIAL.TTF', 40)
    draw.text((20, 0), time_info)
    draw.text((20, 110), board_info["ip_address"])
    draw.text((120, 40), f, font = font)

    img.save("/home/kube-worker-1/Pimoroni/inky/examples/phat/resources/images/666.png")

    # rotate image
    Original_Image = Image.open("/home/kube-worker-1/Pimoroni/inky/examples/phat/resources/images/666.png")
    rotated_image1 = Original_Image.transpose(Image.ROTATE_180)
    img = Image.open(("/home/kube-worker-1/Pimoroni/inky/examples/phat/resources/images/666.png")).resize(inky_display.resolution)

    # Display the data on Inky pHAt
    inky_display.set_image(rotated_image1)
    inky_display.show()

if __name__ == "__main__":
    board_info = get_board_info()
    time_info = get_time()
    display_info(board_info, time_info)
