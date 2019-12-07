import os
global screen
screen=0
coin=0
path = os.getcwd()+"/"
coin_img=loadImage(path+"coin.png")

class Coin:
    def __init__(self):    
        image(coin_img, 750, 50, 100, 100)
        fill(255, 215, 0)
        textSize(70)
        textFont(mono)
        text(": "+str(coin),850, 120)
        
class Button:
    def __init__(self, txt, x, y, h, w, clr_box, clr_text, font_size=48, ans=0):
        self.txt=txt
        self.x=x
        self.y=y
        self.h=h
        self.w=w
        self.clr_box=clr_box
        self.clr_text=clr_text
        self.font_size=font_size
        self.ans=ans
        self.qsn=0
        
    def display(self):
        fill(self.clr_box[0], self.clr_box[1], self.clr_box[2])
        noStroke()
        rect(self.x,self.y,self.w,self.h,10)
        fill(self.clr_text[0], self.clr_text[1], self.clr_text[2])
        textFont(mono)
        textSize(self.font_size)
        text(self.txt,self.x+20,self.y+70)

        if(mouseX>self.x and mouseX <self.x+self.w and mouseY>self.y and mouseY <self.y+self.h):
                stroke(255,255,0)
                strokeWeight(10)
                fill(self.clr_box[0], self.clr_box[1], self.clr_box[2])
                rect(self.x,self.y,self.w,self.h, 10)
                fill(self.clr_text[0], self.clr_text[1], self.clr_text[2])
                textFont(mono)
                textSize(self.font_size+10)
                text(self.txt,self.x+20,self.y+70)

        if mousePressed:
            if(mouseX>self.x and mouseX <self.x+self.w and mouseY>self.y and mouseY <self.y+self.h ):
                stroke(255,20,147)
                strokeWeight(10)
                fill(self.clr_box[0], self.clr_box[1], self.clr_box[2])
                rect(self.x,self.y,self.w,self.h)
                fill(self.clr_text[0], self.clr_text[1], self.clr_text[2])
                textFont(mono)
                textSize(self.font_size+10)
                text(self.txt,self.x+20,self.y+70)
                
                if self.ans==1:
                    self.qsn+=1
    def get_qsn(self):
        return self.qsn

                
                



class Basic:
    def __init__(self):
        self.img = loadImage(path+"onion.jpg")
  
    def display(self):
        image(self.img, 350, -10, 300, 200)
        
    def question(self):
        fill(51, 153, 255)
        textSize(70)
        textFont(mono)
        text("Q1: What is                ?",35,120)



def setup():

    
    size(1000,600)
    background(240, 255, 240)
    global mono
    mono = loadFont("InkFree-70.vlw")



def draw():
    global screen
    global mono
    print(screen)
    if screen==0:   #Start Page
        fill(175, 100, 220)
        textSize(80)
        textFont(mono)
        text("aN eAsY QuIZz", 220, 250)
        fill(255,255,224)
        noStroke()
        rect(320,350,300,75,20)
        fill(255,105,180)
        textSize(70)
        textFont(mono)
        text("START!!",340,410)
        if mousePressed:
            if(mouseX>320 and mouseX <620 and mouseY>350 and mouseY <425) and screen==0:
                stroke(255,20,147)
                strokeWeight(10)
                rect(320,350,300,75)
                fill(255,20,147)
                textFont(mono)
                text("START!!",340,410)
                screen+=1

        
    
    elif screen==1:  #1st Question

        background(240, 255, 240)
        coin=Coin()
        basic=Basic()
        basic.display()
        basic.question()
        button1=Button("     28", 150, 200, 100, 300, [255,222,173], [255,20,147] )
        button1.display()
        button2=Button("CARROT", 550, 200, 100, 300, [255,222,173], [255,20,147] )
        button2.display()
        button3=Button("SHALLOTS", 150, 350, 100, 300, [255,222,173], [255,20,147], 43, 1 )
        button3.display()
        
        button4=Button("  3.14", 550, 350, 100, 300, [255,222,173], [255,20,147] )
        button4.display()
        if button3.get_qsn()==1:
            screen+=1
            
        
            
    elif screen==2:
        background(240, 255, 240)
        text("yay", 100, 200)
        
            
            

      
