import pygame as pg

class DrawPolygons:
    def __init__(self):
        self.polygon_names = []
        self.center_points = []

        self.polygon_names.append("square")
        self.polygon_names.append("triangle")
        self.polygon_names.append("rectangle")

        self.center_points.append(Point(100, 100))
        self.center_points.append(Point(150, 150))
        self.center_points.append(Point(100, 200))

    def paint(self, surface: pg.Surface):
        white = (255,255,255)
        black = (0,0,0)
        surface.fill(white)
        for i in range(len(self.polygon_names)):
            current_polygon = self.polygon_names[i]
            current_center = self.center_points[i]
            if current_polygon == "square":
                pg.draw.rect(surface, black,
                             pg.Rect(current_center.x-10, current_center.y-10, 20, 20), 2)
            elif current_polygon == "triangle":
                pg.draw.line(surface, black,
                             (current_center.x, current_center.y-10),
                             (current_center.x-10, current_center.y+10), 2)
                pg.draw.line(surface, black,
                             (current_center.x-10, current_center.y+10),
                             (current_center.x+10, current_center.y+10), 2)
                pg.draw.line(surface, black,
                             (current_center.x+10, current_center.y+10),
                             (current_center.x, current_center.y-10), 2)
            elif current_polygon == "rectangle":
                pg.draw.rect(surface, black,
                             pg.Rect(current_center.x-20, current_center.y-10, 40, 20), 2)


def main():
    pg.init()
    screen: pg.Surface = pg.display.set_mode([300,300])
    polygons: DrawPolygons = DrawPolygons()

    polygons.paint(screen)
    pg.display.flip()

    running = True
    while running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


if __name__ == "__main__":
    main()
