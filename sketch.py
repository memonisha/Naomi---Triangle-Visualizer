from p5 import *


def setup():
  createCanvas(windowWidth, windowHeight)
  global a,b,c 
  a=createMovableCircle(200,300,20)
  b=createMovableCircle(300,200,20)
  c=createMovableCircle(100,200,20)
  
  

def draw():
  global a
  background('black')
  drawTickAxes()

  textSize(22)
  fill("blue")
  text(f"({a.x},{a.y})",width-200,height-100)
  fill("pink")
  text(f"({b.x},{b.y})",width-200,height-150)
  fill("orange")
  text(f"({c.x},{c.y})",width-200,height-200)
  
  
  stroke("white")
  strokeWeight(3)
  line(c.x,c.y,a.x,a.y)
  line(b.x,b.y,a.x,a.y)
  line(b.x,b.y,c.x,c.y)
  noStroke()
  fill("blue")
  a.draw() 
  fill("pink")
  b.draw()
  fill("orange")
  c.draw()
  
  #circle(200,200,20)
  #circle(100,150,20)
  #circle(300,150,20)
