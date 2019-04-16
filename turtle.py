import graphics as gr

window = gr.GraphWin("Igor Z project", 400, 400)

def rectangle_blue():
    rectangle_blue = gr.Rectangle(gr.Point(0, 0), gr.Point(400, 200))
    rectangle_blue.setFill('blue')
    rectangle_blue.draw(window)

def rectangle_grey():
    rectangle_grey = gr.Rectangle(gr.Point(0, 200), gr.Point(400, 400))
    rectangle_grey.setFill('grey')
    rectangle_grey.draw(window)

def sun():
    my_sun = gr.Circle(gr.Point(350, 50), 30)
    my_sun.setFill('yellow')
    my_sun.draw(window)

def clouds():
    my_cloud1 = gr.Circle(gr.Point(50, 50), 10)
    my_cloud2 = gr.Circle(gr.Point(65, 50), 11)
    my_cloud3 = gr.Circle(gr.Point(75, 50), 12)

    my_cloud1.setFill('white')
    my_cloud1.draw(window)
    my_cloud2.setFill('white')
    my_cloud2.draw(window)
    my_cloud3.setFill('white')
    my_cloud3.draw(window)

def make_pic():
    rectangle_blue()
    rectangle_grey()
    sun()
    clouds()

    window.getMouse()
    window.close()

make_pic()

