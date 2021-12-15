import os
import requests

dirname = os.path.dirname(__file__)

def download(user_id,URL):

    filename = os.path.join(dirname, f'image\\{user_id}.png')
    image = requests.get(URL).content

    with open(filename, 'wb') as handler:
        handler.write(image)
    
    return filename