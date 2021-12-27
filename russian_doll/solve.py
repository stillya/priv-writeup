import pyqrcode
import zipfile
from pyzbar.pyzbar import decode
from PIL import Image
import cv2
import pyzipper

GLOBAL_PATH = 'extracted/'

def from_qr(path):
    img = cv2.imread(path)
    det = cv2.QRCodeDetector()
    val, pts, st_code = det.detectAndDecode(img)
    print('password - ' + val)
    return val


def unzip(path):
    path = GLOBAL_PATH + path
    print('archive - ' + path + '.zip')
    with pyzipper.AESZipFile(path + '.zip', 'r', compression=pyzipper.ZIP_DEFLATED, encryption=pyzipper.WZ_AES) as extracted_zip:

        extracted_zip.extractall(pwd=str.encode(
            from_qr(path + '.png')), path=GLOBAL_PATH)


for i in range(999, 0, -1):
    unzip(str(i))
