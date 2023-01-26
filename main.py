from io import BytesIO

import requests
from PIL import Image


def get_image(x_coord: float, y_coord: float, size_x: float = 0.1, size_y: float = 0.1) -> BytesIO or str:
    coords = ",".join([str(x_coord), str(y_coord)])
    spn = ",".join([str(size_x), str(size_y)])

    search_api_server = "http://static-maps.yandex.ru/1.x/"

    apikey = "40d1649f-0493-4b70-98ba-98533de7710b",

    search_params = {
        "l": 'map',
        "apikey": apikey,
        "ll": coords,
        "spn": spn
    }

    response = requests.get(search_api_server, params=search_params)

    if not response or response.status_code != 200:
        return "Ошибка"

    return BytesIO(response.content)


Image.open(get_image(50, 50)).show()
