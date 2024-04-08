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
  stroke(252,255,3) #yellow
  line(c.x,c.y,a.x,a.y)
  stroke(108,212,163)  #olive green
  line(b.x,b.y,a.x,a.y)
  stroke(181,143,227) #purple
  line(b.x,b.y,c.x,c.y)
  noStroke()
  fill("blue")
  a.draw() 
  fill("pink")
  b.draw()
  fill("orange")
  c.draw()
  # a and c -----> (a.x,a.y)    (c.x,c.y)
  distYellow= distance(a,c) 
  distGreen= distance(a,b)
  distPurple= distance(b,c)

  fill("white")
  if distYellow==distPurple and distGreen==distPurple:
    text("This is an equilateral triangle", 100 ,height-100)
    
  elif distYellow== distGreen or distYellow==distPurple or distGreen==distPurple:
    text("This is an isosceles triangle", 100,height-100)
    
  else:
    text("This is a scalene triangle", 100,height-100)
    
    


  midPointYellowX= (a.x+c.x)/2
  midPointYellowY= (a.y+c.y)/2
  fill("black")
  rect(midPointYellowX,midPointYellowY,40,20)
  fill(252,255,3)
  text(distYellow,midPointYellowX, midPointYellowY)

  midPointGreenX=(a.x+b.x)/2
  midPointGreenY=(a.y+b.y)/2
  fill("black")
  rect(midPointGreenX,midPointGreenY,40,20)
  fill(108,212,163)
  text(distGreen,midPointGreenX, midPointGreenY)

  midPointPurpleX=(b.x+c.x)/2
  midPointPurpleY=(b.y+c.y)/2
  fill("black")
  rect(midPointPurpleX,midPointPurpleY,40,20)
  fill(181,143,227)
  text(distPurple,midPointPurpleX,midPointPurpleY)
  

 
  

#functions with some return value
def distance(p,q):
  d=round(sqrt((p.x-q.x)**2 + (p.y-q.y)**2))
  return d


 
  '''
  jamboard:
  https://jamboard.google.com/d/1yDyCfkYIY3LCCH1bOcD_hblbEwKyFPk6DrMOrQyg3zA/viewer?mtt=axnreovu33m5&f=3
  
  '''
