from graphics import *

if __name__ == "__main__":
    my_window = GraphWin("My Canvas", 500, 500)
    my_circ = Circle(Point(1, 1), 20)
    my_circ.draw(my_window)
    my_window.getMouse()
    my_window.close()