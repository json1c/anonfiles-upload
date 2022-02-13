import io
import qrcode
import requests
import argparse
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser(description="Upload file to AnonFiles")
parser.add_argument("files", metavar="FILE", type=argparse.FileType("r"), nargs="+", help="file to upload")
parser.add_argument("--qr", action="store_true", help="gen QR code for every file")
parser.add_argument("--direct", action="store_true", help="get direct link to download")

args = parser.parse_args()

for file in args.files:
    response = requests.post(
        "https://api.anonfiles.com/upload",
        files={"file": file}
    ).json()

    url = response["data"]["file"]["url"]["full"]

    if args.direct:
        page = requests.get(url)
        soup = BeautifulSoup(page.text, "html.parser")
        url = soup.find(id="download-url").attrs["href"]

    print(f"{file.name}: {url}")

    if args.qr:
        qr = qrcode.QRCode()
        qr.add_data(url)
        f = io.StringIO()
        qr.print_ascii(invert=True, out=f)
        f.seek(0)
        print(f.read())

print()
