import pgzrun

WIDTH=700
HEIGHT=700


ship=Actor("plane.png")
ship.pos=350,530
def draw():
    screen.clear()
    screen.fill("blue")
    ship.draw()

    
    







pgzrun.go()