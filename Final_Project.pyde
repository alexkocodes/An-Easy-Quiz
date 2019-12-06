global screen
screen=0










def setup():

    
    size(1000,600)
    background(255,255,255)
    global mono
    mono = loadFont("InkFree-70.vlw")



def draw():
    global screen
    global mono
    
    if screen==0:   #Start Page
        fill(175, 100, 220)
        textSize(80)
        textFont(mono)
        text("aN eAsY QuIz!", 250, 250)
        fill(255,255,224)
        noStroke()
        rect(320,350,300,75)
        fill(255,105,180)
        textSize(70)
        textFont(mono)
        text("START!!",340,420)
        
        if(mousePressed):
            if(mouseX>320 and mouseX <620 and mouseY>350 and mouseY <425):
                stroke(255,20,147)
                strokeWeight(10)
                rect(320,350,300,75)
                fill(255,20,147)
                textFont(mono)
                text("START!!",340,420)
                screen+=1
    
    elif screen==1:  #1st Question
        fill(0)
        background(255,255,255)
        textFont(mono)
        textSize(80)
        text("Question 1", 180, 250)

        
            
            

      
