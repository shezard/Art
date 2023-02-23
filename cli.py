import requests
import hashlib
import os
import sys
from pathlib import Path
from ascii_magic import AsciiArt
import json


def parse_arguments():
    url = sys.argv[1]

    if not url:
        exit(1)

    # TODO url validation

    __, extension = os.path.splitext(url)

    return [url, extension]


def fetch_image(url, extension):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0',
        'Referer': 'https://manga-scan.ws/'
    }

    res = requests.get(url, stream=True, headers=headers)

    content = res.raw
    md5hash = hashlib.md5(content.data).hexdigest()

    file_name = Path(os.getcwd()) / 'data' / (md5hash + extension)

    return [file_name, md5hash, content]


def save_image(file_name, content):
    with open(file_name, 'wb') as file:
        file.write(content.data)


def display_image(file_name):
    img = AsciiArt.from_image(file_name)
    img.to_terminal()


def get_tags():
    return input("Please enter tags list (e.g tags1, tags2, tags3): ")


def save_tags(md5hash, tags):
    try:
        with open(Path(os.getcwd()) / 'data' / 'data.json', 'r+') as data_file:
            try:
                data = json.load(data_file)
                data_file.seek(0)
            except json.decoder.JSONDecodeError:
                data = {}
            save_data_to_data_file(md5hash, tags, data_file, data)

    except FileNotFoundError:
        with open(Path(os.getcwd()) / 'data' / 'data.json', 'w') as data_file:
            save_data_to_data_file(md5hash, tags, data_file, {})


def save_data_to_data_file(md5hash, tags, data_file, data):
    data[md5hash] = list(map(lambda x: x.strip(), tags.split(',')))

    json.dump(data, data_file)
