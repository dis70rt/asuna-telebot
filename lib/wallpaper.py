from urllib.request import urlopen
import json

def wallpaper(TYPE: str):
    URL = f"https://meme-api.herokuapp.com/gimme/{TYPE}"
    response = urlopen(URL)
    data = json.loads(response.read())
    
    if data.get('nsfw') == False:
        return data.get('url')           