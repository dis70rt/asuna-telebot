import os
import requests
from PIL import Image

dirname = os.path.dirname(__file__)

def download(user_id,URL):

    filename = os.path.join(dirname, f'image\\{user_id}.png')
    image = requests.get(URL).content

    with open(filename, 'wb') as handler:
        handler.write(image)
        picture = Image.open(filename)
        picture.save(filename, 
                 optimize = True, 
                 quality = 1)
    
    return filename