from io import BytesIO


import pygame
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



def move_screen(i, x_coord: float, y_coord: float, spn: tuple[float, float]) -> BytesIO:
    if i.type == pygame.K_UP:
        return get_image(x_coord, y_coord + spn[1], spn[0], spn[1])
    elif i.type == pygame.K_DOWN:
        return get_image(x_coord, y_coord - spn[1], spn[0], spn[1])
    elif i.type == pygame.K_RIGHT:
        return get_image(x_coord + spn[0], y_coord, spn[0], spn[1])
    elif i.type == pygame.K_LEFT:
        return get_image(x_coord - spn[0], y_coord, spn[0], spn[1])

    else:
        return get_image(x_coord, y_coord, spn[0], spn[1])

Image.open(get_image(50, 50)).show()

