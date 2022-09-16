import glob, qrcode, os, time, datetime, requests, socket, json
from PIL import Image, ImageDraw, ImageFont
from font_fredoka_one import FredokaOne
from inky.auto import auto
from inky import InkyPHAT
from requests.structures import CaseInsensitiveDict
from inspect import getsourcefile
from os.path import abspath

def read_config():
    abspath(getsourcefile(lambda:1))
    Str = str(abspath(getsourcefile(lambda:0)))
    l = len(Str)
    directory = Str[:l-8]
    path = str(directory + "/resources/")

    with open(directory + "/config.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        jsonfile.close()
    
    data['directory_path'] = path # Updating, before it was 11/09/2020
    print("Path directory updated to" + directory)
    with open(directory + "/config.json", "w") as jsonfile:
        myJSON = json.dump(data, jsonfile, sort_keys=True, indent=4) # Writing to the file
        print("Write successful")
        jsonfile.close()


    with open(directory + "/config.json", "r") as jsonfile:
        data = json.load(jsonfile) # Reading the file
        print("Parsing config.json successful")
        jsonfile.close()

    return data

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

def get_crypto_ticker(data):

    if data['ticker_enabled'] == "true":
        url="https://api.livecoinwatch.com/coins/single"
        headers = CaseInsensitiveDict()
        headers["content-type"]="application/json"
        headers["x-api-key"] = data['x-api-key']
        data = data['x-api-data']
        resp = requests.post(url, headers=headers, data=data)
        data = json.loads(resp.text)
        parseData = json.dumps(resp.json())
        priceObj = json.loads(parseData)
        B = priceObj["rate"]
        Z = round(B, 3)
        current_price_info = str(Z)

    else: 
        current_price_info = str("\^o^/")
    
    return current_price_info

def get_pihole_stats(board_info):
    api_path = "http://" + board_info["ip_address"] + "/admin/api.php?summary"
    pihole_stats = dict()
    query_fields = ["unique_clients", "dns_queries_today", "ads_blocked_today", "ads_percentage_today"]
    try:
        api_raw = requests.get(api_path, verify=False, timeout=5).json()
        pihole_stats["status"] = "Connected"
        for field in query_fields:
            pihole_stats[field] = api_raw[field]
    except:
        pihole_stats["status"] = "DOWN"
        for field in query_fields:
            pihole_stats[field] = "-----"
    return pihole_stats

def get_compose_image(board_info, time_info, current_price_info, pihole_stats, data):
    img = qrcode.make("http://"+ board_info["ip_address"] + "/admin")
    print(type(img))
    print(img.size)
    print(pihole_stats["ads_blocked_today"])
    # <class 'qrcode.image.pil.PilImage'>
    # (120, 120)
    img.save(data['directory_path'] + "/qr.png", dpi=(300,300))
    #compose qr code on top of background troplet
    im1 = Image.open(data['directory_path'] + "/inky-losaurus.png")
    im2 = Image.open(data['directory_path'] + "/qr.png")
    newsize = (122, 122)
    im3 = im2.resize(newsize)
    im1.paste(im3, (0,0), mask = im3)
    im1.save(data['directory_path'] + "/final.png",dpi=(300,300))
    img = Image.open(data['directory_path'] + "/final.png")
    draw = ImageDraw.Draw(img)
    # add text to background-droplet
    font = ImageFont.truetype(data['directory_path'] + "/ARIAL.TTF", 30)

    draw.text((20, 0), time_info)

    # mini pihole dashboard
    draw.text((120, 90), (str("Blocked " + "  >" + str(pihole_stats["dns_queries_today"]))))
    draw.text((120, 100), (str("Percent" + "   >" + str(pihole_stats["ads_percentage_today"]))))
    draw.text((120, 110), (str(pihole_stats["status"] + " >" + str(pihole_stats["unique_clients"]))))
    draw.text((20, 110), board_info["ip_address"])
    draw.text((120, 60), "" + current_price_info + "€", font = font)
    img.save(data['directory_path'] + "/final.png")
    # rotate image
    Original_Image = Image.open(data['directory_path'] + "/final.png")

    if data['display_flipped'] == "true":
        rotated_image_info = Original_Image.transpose(Image.ROTATE_180)
        
    else: 
        rotated_image_info = Original_Image

    
    return rotated_image_info

def display_info(rotated_image_info):
    inky_display = auto()
    inky_display.set_border(inky_display.BLACK)
    # compose qr code 
    inky_display.set_image(rotated_image_info)
    inky_display.show()


if __name__ == "__main__":
    board_info = get_board_info()
    time_info = get_time()
    data = read_config()
    pihole_stats = get_pihole_stats(board_info)
    current_price_info = get_crypto_ticker(data)
    rotated_image_info = get_compose_image(board_info, time_info, current_price_info, pihole_stats, data)
    display_info(rotated_image_info)