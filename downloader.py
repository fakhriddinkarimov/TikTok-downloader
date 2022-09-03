import json
import requests

# link = "https://www.tiktok.com/@nor10122/video/7037155617491913986"
def tk(link):
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "5d48a6d9a9msh30f54453ffac47bp11ef44jsn175c16ba5e00",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    result = response.text
    rest = json.loads(result)
    return {"video": rest['video'][0],"music": rest['music'][0]}
    # return type(result)

# print(tk(link))