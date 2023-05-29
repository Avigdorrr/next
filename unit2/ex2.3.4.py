class Pixel:

    def __init__(self, x=0, y=0, red=0, green=0, blue=0):
        """
        _x - x coordinate
        _y - y coordinate
        _red - a value between 0 and 255
        _green - a value between 0 and 255
        _blue - a value between 0 and 255
        """
        self._x = x
        self._y = y
        self._red = red
        self._green = green
        self._blue = blue

    def set_coords(self, x, y):
        self._x = x
        self._y = y

    def set_grayscale(self):
        average = (self._red + self._green + self._blue) // 3
        self._red = average
        self._green = average
        self._blue = average

    def print_pixel_info(self):
        color_names = ["Red", "Green", "Blue"]
        colors = [self._red, self._green, self._blue]
        color_dictionary = dict(zip(colors, color_names))
        color_info = f"({self._red}, {self._green}, {self._blue})"
        non_zero_colors = list(filter(lambda color: color != 0, colors))
        if len(non_zero_colors) == 1 and non_zero_colors[0] > 50:
            color_info += " " + color_dictionary[non_zero_colors[0]]
        print(f"X: {self._x}, Y: {self._y}, Color: ({color_info})")


def main():
    p = Pixel(5, 6, 250)
    p.print_pixel_info()
    p.set_grayscale()
    p.print_pixel_info()


if __name__ == '__main__':
    main()