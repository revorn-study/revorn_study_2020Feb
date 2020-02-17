import urllib.request
from urllib.error import URLError
from io import BytesIO
from keras.preprocessing import image


def load_image(url, target_size=(28, 28), current_scheme_host=None):
    try:
        with urllib.request.urlopen(url) as response:
            img = image.load_img(BytesIO(response.read()), grayscale=True, target_size=target_size)
    except ValueError:
        try:
            with urllib.request.urlopen(current_scheme_host + url) as response:
                img = image.load_img(BytesIO(response.read()), grayscale=True, target_size=target_size)
        except URLError:
            with urllib.request.urlopen('http://django:8000' + url) as response:
                img = image.load_img(BytesIO(response.read()), grayscale=True, target_size=target_size)

    return image.img_to_array(img)
    