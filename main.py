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

        self.x_coord, self.y_coord = 37.639540, 55.739407
        self.spn = 0.05, 0.05
        self.mode = 'map'
        self.get_image(self, self.x_coord, self.y_coord, self.mode, self.spn[0], self.spn[1])

    def run(self):
        while True:
            map = pygame.transform.scale(self.image, (self.width, self.height))
            self.surface.blit(map, (0, 0))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYUP:
                    self.move_screen(event)
            pygame.display.flip()

    @staticmethod
    def get_image(self, x_coord: float, y_coord: float, mode: str, size_x: float = 0.1, size_y: float = 0.1):
        coords = ",".join([str(x_coord), str(y_coord)])
        spn = ",".join([str(size_x), str(size_y)])

        search_api_server = "http://static-maps.yandex.ru/1.x/"

        apikey = "40d1649f-0493-4b70-98ba-98533de7710b",

        search_params = {
            "l": mode,
            "apikey": apikey,
            "ll": coords,
            "spn": spn
        }

        response = requests.get(search_api_server, params=search_params)

        if not response or response.status_code != 200:
            return "Ошибка"

        self.image = pygame.image.load(BytesIO(response.content))

    def move_screen(self, event):
        if event.key == pygame.K_UP:
            self.y_coord += self.spn[1]
        elif event.key == pygame.K_DOWN:
            self.y_coord -= self.spn[1]
        elif event.key == pygame.K_RIGHT:
            self.x_coord += self.spn[0]
        elif event.key == pygame.K_LEFT:
            self.x_coord -= self.spn[0]
        elif event.key == pygame.K_PAGEDOWN:
            self.spn = tuple(map(lambda x: x * 2, self.spn))
        elif event.key == pygame.K_PAGEUP:
            self.spn = tuple(map(lambda x: x / 2, self.spn))
        elif event.key == pygame.K_m:
            if self.mode == 'map':
                self.mode = 'sat'
            elif self.mode == 'sat':
                self.mode = 'sat,skl'
            else:
                self.mode = 'map'

        self.get_image(self, self.x_coord, self.y_coord, self.mode, self.spn[0], self.spn[1])


if __name__ == '__main__':
    app = App()
    app.run()
