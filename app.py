import requests
import hashlib
import os
import sys
from pathlib import Path
from ascii_magic import AsciiArt

url = sys.argv[1]

if not url:
    exit(1)

# TODO url validation

__, extension = os.path.splitext(url)

headers = headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
    'Referer' : 'https://manga-scan.ws/'
}

res = requests.get(url, stream = True, headers = headers)

print(res.status_code)
content = res.raw
hash = hashlib.md5(content.data).hexdigest()

file_name = Path(os.getcwd()) / 'data' / (hash + extension);

if res.status_code == 200:
    with open(file_name,'wb') as file:
        file.write(content.data)
    print('Image sucessfully Downloaded: ', file_name)
else:
    print('Image Couldn\'t be retrieved')

img = AsciiArt.from_image(file_name)
img.to_terminal()

tags = input("Please enter tags list (e.g tags1, tags2, tags3): ")

print(tags)