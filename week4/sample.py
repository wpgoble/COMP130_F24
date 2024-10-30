from graphics import *

window = GraphWin("My Window", 500, 500)
window.setCoords(0, 0, 500, 500)

circ = Circle(Point(100, 100), 50)
circ.draw(window)

window.getMouse()
window.close()