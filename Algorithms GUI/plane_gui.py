# This code was written by Maya Schlesinger(maya.schlesinger@gmail.com)
# on 8/7/2016.
# This is a library for basic graphics on a plane using tkinter.
import tkinter
import math
import random


class ColorMap:
    """
    This class acts as a color palate with n colors.
    """
    DEFAULT_COLOR = "#000000"
    DEFAULT_COLOR_MAP = [DEFAULT_COLOR, "#ff0000", "#00ff00", "#0000ff", "#00ffff", "#ff00ff", "#ffff00"]
    DEFAULT_N = len(DEFAULT_COLOR_MAP)

    def __init__(self, n=DEFAULT_N):
        """
        :param n: Int - The number of colors in the palate.
        """
        self.n = n
        self.color_map = self.get_random_color_map(n) if n > self.DEFAULT_N else self.DEFAULT_COLOR_MAP

    def __getitem__(self, item):
        return self.color_map[item]

    @staticmethod
    def get_random_color():
        return "#" + hex(random.randrange(1, 256**3-1))[2:].zfill(6)

    @staticmethod
    def get_random_color_map(k):
        return [ColorMap.DEFAULT_COLOR]+[ColorMap.get_random_color() for i in range(k-1)]


class Window:
    """
    This class is used for dealing with most of the gui, it creates the window, the canvas and does basic drawing.
    """
    DEFAULT_MIN_X = 0
    DEFAULT_MIN_Y = 0
    DEFAULT_SCALE = 10
    COLOR_NUM = 5
    DO_NOTHING = lambda x: 0

    def __init__(self, min_x=DEFAULT_MIN_X, min_y=DEFAULT_MIN_Y,
                 scale=DEFAULT_SCALE, color_num=COLOR_NUM, update_func=DO_NOTHING):
        """
        :param min_x: Int - The min x coordinate (left side of the screen).
        :param min_y: Int - The min y coordinate (bottom side of the screen).
        :param scale: Int - The scale between the screen pixels and the plane.
        :param color_num: Int - The number of colors.
        """
        self.min_x = min_x
        self.min_y = min_y
        self.scale = scale
        self.color_map = ColorMap(color_num)

        self.root = tkinter.Tk()
        self.win_height = self.root.winfo_screenheight()
        self.win_width = self.root.winfo_screenwidth()

        self.max_x = math.floor(self.win_width / self.scale) - self.min_x - 1
        self.max_y = math.floor(self.win_height / self.scale) - self.min_y - 1

        self.root.attributes("-fullscreen", True)
        self.canvas = tkinter.Canvas(self.root, width=self.win_width, height=self.win_height)
        self.canvas.pack()
        self.root.bind("<space>", update_func)
        self.root.bind("<Escape>", lambda x: self.root.destroy())

    def mainloop(self):
        """
        This method starts the window's mainloop.
        """
        self.root.mainloop()

    def get_max_x(self):
        """
        :return: Int - The maximal x axis value viewable on the screen.
        """
        return self.max_x

    def get_max_y(self):
        """
        :return: Int - The maximal x axis value viewable on the screen.
        """
        return self.max_y

    def to_canvas_coords(self, x, y):
        """
        This method converts normal plane coordinates to those of the canvas.
        :param x: Int - The x coordinate to convert.
        :param y: Int - The y coordinate to convert.
        :return: Int, Int - The canvas compatible x and y coordinates.
        """
        return x*self.scale, (self.max_y - y)*self.scale

    def draw_dot(self, loc, color_index):
        """
        This method draws the dot(outline only) at the specified coordinates with the specified color index.
        :param loc: Tuple (x,y) - The normal plane coordinate of the dot.
        :param color_index: Int - The color index of the color to draw the dot with.
        """
        x, y = loc
        x_0, y_0 = self.to_canvas_coords(x, y)
        x_1, y_1 = self.to_canvas_coords(x+1, y+1)
        self.canvas.create_oval(x_0, y_0, x_1, y_1, outline=self.color_map[color_index])

    def draw_all_dots(self, list_of_dots, color_assignments):
        """
        This method draws all the dots given to it.
        :param list_of_dots: List of Tuples (x,y) - The dots to draw.
        :param color_assignments: List of Ints - The number at index i is the color index of the dot at list_of_dots[i]
        """
        for i in range(len(list_of_dots)):
            self.draw_dot(list_of_dots[i], color_assignments[i])

    def clear(self):
        """
        clears the GUI of all drawings made.
        """
        self.canvas.delete("all")

    def draw_square(self, loc, color_index):
        """
        This method draws the square(with filling) at the specified coordinates with the specified color index.
        :param loc: Tuple (x,y) - The normal plane coordinate of the square.
        :param color_index: Int - The color index of the color to draw the square with.
        """
        x, y = loc
        x_0, y_0 = self.to_canvas_coords(x, y)
        x_1, y_1 = self.to_canvas_coords(x+1, y+1)
        self.canvas.create_rectangle(x_0, y_0, x_1, y_1, fill=self.color_map[color_index])

    def draw_all_squares(self, list_of_squares, color_assignments):
        """
        This method draws all the squares given to it.
        :param list_of_squares: List of Tuples (x,y) - The squares to draw.
        :param color_assignments: List of Ints - The number at index i is
        the color index of the square at list_of_squares[i].
        """
        for i in range(len(list_of_squares)):
            self.draw_square(list_of_squares[i], color_assignments[i])
