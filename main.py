from io import BytesIO

import pygame
import sys

import requests



class App:
    def __init__(self):
        pygame.init()
        self.width, self.height = 600, 450
        self.surface = pygame.display.set_mode((self.width, self.height))

        pygame.display.set_caption("Yandex maps")

        self.x_coord, self.y_coord = 50, 50
        self.get_image(self.x_coord, self.y_coord)

    def run(self):
        while True:
            map = pygame.transform.scale(self.image, (self.width, self.height))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    self.move_screen(event, self.x_coord, self.y_coord, (0.1, 0.1))
            self.surface.blit(map, (0, 0))
            pygame.display.flip()

    def get_image(self, x_coord: float, y_coord: float, size_x: float = 0.1, size_y: float = 0.1) -> BytesIO or str:
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

        self.image = pygame.image.load(BytesIO(response.content))

    def move_screen(self, i, x_coord: float, y_coord: float, spn: (float, float)):
        print(i.key)
        if i.key == pygame.K_UP:
            self.get_image(x_coord, y_coord + spn[1], spn[0], spn[1])
        elif i.key == pygame.K_DOWN:
            self.get_image(x_coord, y_coord - spn[1], spn[0], spn[1])
        elif i.key == pygame.K_RIGHT:
            self.get_image(x_coord + spn[0], y_coord, spn[0], spn[1])
        elif i.key == pygame.K_LEFT:
            self.get_image(x_coord - spn[0], y_coord, spn[0], spn[1])

        else:
            self.get_image(x_coord, y_coord, spn[0], spn[1])


if __name__ == '__main__':
    app = App()
    app.run()