import requests
import shutil
import argparse


def download_file(url, filename):
    with requests.get(url, stream=True) as r:
        with open(filename, 'wb') as f:
            shutil.copyfileobj(r.raw, f)

parser = argparse.ArgumentParser()
parser.add_argument('--url', required=True)
parser.add_argument('--filename', required=True)

args = parser.parse_args()
url = args.url
filename = args.filename

print(f'Downloading from {url} into {filename} ...')
download_file(url, filename)
print('Done')