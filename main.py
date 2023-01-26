from io import BytesIO

import pygame
import sys

import requests
from PIL import Image


class App:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 450
        self.surface = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Yandex maps")
        self.image = self.get_image(50, 50)

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

    def update(self):
        pass

    @staticmethod
    def get_image(x_coord: float, y_coord: float, zoom: int = 10) -> BytesIO or str:
        coords = ",".join([str(x_coord), str(y_coord)])

        search_api_server = "http://static-maps.yandex.ru/1.x/"

        apikey = "40d1649f-0493-4b70-98ba-98533de7710b",

        search_params = {
            "l": 'map',
            "apikey": apikey,
            "ll": coords,
            "z": zoom
        }

        response = requests.get(search_api_server, params=search_params)

        if not response or response.status_code != 200:
            return "Ошибка"

        Image.open(BytesIO(response.content)).show()

        return BytesIO(response.content)


if __name__ == '__main__':
    app = App()
    app.run()
