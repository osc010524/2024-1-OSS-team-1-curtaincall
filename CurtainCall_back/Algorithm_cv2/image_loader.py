import requests
from io import BytesIO
from PIL import Image

def prepare_image(photo, width=260, height=260, convert_mode='None'):
    photo = photo.resize((width, height))
    if convert_mode != 'None':
        photo = photo.convert(convert_mode)
    return photo


def load_image(fileurl):
    # 이미지 데이터를 웹에서 받아옵니다.
    response = requests.get(fileurl)
    image_bytes = BytesIO(response.content)

    img = Image.open(image_bytes)

    return img