import os
import time
global screen
screen=0
global coin
coin=0
global al
al=0
global again
again=0
path = os.getcwd()+"/"
coin_img=loadImage(path+"coin.png")
bomb_img=loadImage(path+"bomb.png")
arrow1_img=loadImage(path+"Arrow_1.png")
arrow2_img=loadImage(path+"Arrow_2.png")
arrow3_img=loadImage(path+"Arrow_3.png")
gameover=loadImage(path+"gameover.jpg")
win_img=loadImage(path+"win.jpg")
global ans_x
global ans_y
global ans_h
global ans_w
global appear
appear=1
ans_x=0
ans_y=0
ans_h=0
ans_w=0
global click
click=0
global change
change=0

global life
life=3

class Coin:     #class for points
    global coin
    def __init__(self): 
           
        image(coin_img, 750, 50, 100, 100)
        fill(255, 215, 0)
        textSize(70)
        textFont(mono)
        text(": "+str(coin),850, 120)
        
class Lives:    #class for number of lives
    
    def __init__(self,number):
        if screen!=0:
            fill(0)
            textSize(30)
            textFont(mono)
            self.number=number
            alert_img=loadImage(path+"alert.jpg")
        
            
            if al==1:
                
                textSize(40)
                image(alert_img,0,450,600,200)
                textFont(mono)
                
            else:
                fill(255, 0, 0)
                textFont(mono)
                text("Lives:"+str(self.number),35,550)
            
            
            
            
        
class Button:       #class for the 4 buttons and other answers
    global ans_x
    global ans_y
    global ans_h
    global ans_w
    global click
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
        
    def display(self):       #displays the options
        global click
        global coin
        if screen!=11:
            
            if self.txt!="":
                fill(self.clr_box[0], self.clr_box[1], self.clr_box[2])
            
            else:
                noFill()
            noStroke()
            rect(self.x,self.y,self.w,self.h,10)
            fill(self.clr_text[0], self.clr_text[1], self.clr_text[2])
        if screen==10:
            textFont(bonus)
        else:
            textFont(mono)
        
        if len(self.txt)>12:
            textSize(32)
            text(self.txt,self.x+20,self.y+40)
        else:
             textSize(self.font_size)
             text(self.txt,self.x+40,self.y+70)

        if(mouseX>self.x and mouseX <self.x+self.w and mouseY>self.y and mouseY <self.y+self.h and screen!=11):  #changes fontsize and color when dragged over answer
            if self.txt!= ("THE ANSWER" ) :
                stroke(255,255,0)
                strokeWeight(10)
                
                fill(self.clr_box[0], self.clr_box[1], self.clr_box[2])
                rect(self.x,self.y,self.w,self.h, 15)
                fill(self.clr_text[0], self.clr_text[1], self.clr_text[2])
                if screen==10:
                    textFont(bonus)
                else:
                    textFont(mono)
                textSize(self.font_size+5)
                
                if len(self.txt)>12:
                    textSize(self.font_size+5)
                    text(self.txt,self.x+40,self.y+30)
                else:
                    textSize(self.font_size+5)
                    text(self.txt,self.x+40,self.y+70)
        
        
            
        
        if flag==0:      #checks if answer is correct and increases points otherwise life is gone and moves to next screen; flag is a global variable for clicking
            global screen
            global flag
            global coin
            
            if(mouseX>self.x and mouseX <self.x+self.w and mouseY>self.y and mouseY <self.y+self.h):
                if screen!=11:
                    stroke(255,20,147)
                    strokeWeight(10)
                    fill(self.clr_box[0], self.clr_box[1], self.clr_box[2])
                    rect(self.x,self.y,self.w,self.h, 15)
                    fill(self.clr_text[0], self.clr_text[1], self.clr_text[2])
                    textFont(mono)
                    textSize(self.font_size+10)
                    text(self.txt,self.x+20,self.y+70)
                global life
                
                if self.ans==0:  #wrong answr
                    life-=1
                    click=0
                    flag=1
                if self.ans==2:
                    life=0
                    
                if self.ans==1 and screen!=10:  #right answer and if not specific to question10
                    
                    screen+=1
                    flag=1
                    click=0
                    if self.txt=="Try again?":
                        global again
                        again=1
                    
                    if self.txt=="YES!!":
                        coin-=70
                        life+=1
                
                u=0
                if self.txt=='WHAT DO\nYOU MEAN?'and flag==0:   #right answer
                    if (mouseX>230 and mouseX <270 and mouseY>390 and mouseY <430):
                        click=0
                        u=1
                        screen+=1
                        flag=1
                    else:
                        life-=1
                        click=0
                        flag=1       
                        
                if (screen!=1 and (self.ans==1 and u==1)) or (screen!=1 and self.ans==1):
                    if self.txt!="NAH":
                        coin+=10    
                    


    
    


class Basic:   #basic 4 option question class
    def __init__(self, image_file, x, y, w, h, txt):
        self.img = loadImage(path+image_file)
        self.x=x
        self.y=y
        self.w=w
        self.h=h
        self.txt=txt
  
    def display(self):  #to display image
        image(self.img, self.x, self.y, self.w, self.h)
        
    def question(self):  #to displkay the question
        fill(51, 153, 255)
        textSize(70)
        textFont(mono)
        text(self.txt,35,120)

global x_q6
global y_q6
global within
within=False
x_q6=270
y_q6=150
flag=1
global win
win=0
def mousePressed():  #changes variable flag to 0 when mouse pressed
    global click
    click=1

    global flag
    flag=0
    
def keyPressed():  #specific to question 10, if key pressed is 1 then answer is correct and accordingly works
    if keyCode==49 and screen==11:
        global screen
        global life
        global coin
        screen+=1
        flag=1
        click=0
        coin+=10
        
def mouseReleased():  #when mouse released flag variable changes back
    global flag
    global life
    flag=1

def Gameover():
    global again
    global screen
    screen=0
    coin=0
    life=3
    
    
def setup():
    time = millis()
    size(1000,600)
    background(240, 255, 240)
    global mono
    global bonus
    mono = loadFont("InkFree-70.vlw")
    bonus = loadFont("Serif-48.vlw")



def draw():
    global screen
    global mono
    global ans_x
    global ans_y
    global ans_h
    global ans_w
    global life
    
    if screen==0:   #Start Page
        global flag
        fill(175, 100, 220)
        textSize(80)
        textFont(mono)
        text("aN eAsY QuIZz", 220, 250)
      
        button_start=Button("START",320, 350, 75, 300 ,[255,255,224], [255, 20, 147],50, 1 )
        ans_x=320
        ans_y=350
        ans_h=75
        ans_w=300
        button_start.display()
        
        

    if screen==1:  #1st Question
        background(240, 255, 240)
        ans_x=150
        ans_y=350
        ans_h=100
        ans_w=300
        basic=Basic("onion.jpg", 350, -10, 300, 200, "Q1: What is                ?")
        basic.display()
        basic.question()
        button3=Button("SHALLOTS", 150, 350, 100, 300, [255,222,173], [255,20,147], 43, 1 )
        button3.display()
        button1=Button("     28", 150, 200, 100, 300, [255,222,173], [255,20,147] )
        button1.display()
        button2=Button("CARROT", 550, 200, 100, 300, [255,222,173], [255,20,147] )
        button2.display()
        button4=Button("  3.14", 550, 350, 100, 300, [255,222,173], [255,20,147] )
        button4.display()
        
            
    if screen==2:  #2nd Question  
        background(240, 255, 240)
        ans_x=550
        ans_y=200
        ans_h=100
        ans_w=300
        basic=Basic("abundance.png", 400, -10, 200, 200, "Q2: What is                ?")
        
        basic.display()
        basic.question()
        
        button1=Button("CUPCAKE", 150, 200, 100, 300, [255,222,173], [255,20,147], 38 )
        button1.display()
        button2=Button("ABUNDANCE", 550, 200, 100, 300, [255,222,173], [255,20,147], 38, 1 )
        button2.display()
        button3=Button("FAIRY CAKE", 150, 350, 100, 300, [255,222,173], [255,20,147], 38)
        button3.display()
        button4=Button("BALLET BUN", 550, 350, 100, 300, [255,222,173], [255,20,147], 38)
        button4.display()
        
    if screen==3: #3rd Question
        background(240, 255, 240)
        ans_x=550
        ans_y=200
        ans_h=100
        ans_w=300

        textFont(mono)
        textSize(50)
        fill(51, 153, 255)
        text("Q3:   .SDRAWKCAB\nNOITSEUQ SIHT\n          REWSNA", 180, 50 )
        
        button1=Button("WELL..", 150, 200, 100, 300, [255,222,173], [255,20,147], 38 )
        button1.display()
        button2=Button("K.O", 550, 200, 100, 300, [255,222,173], [255,20,147], 38, 1 )
        button2.display()
        button3=Button("TENNIS ELBOW", 150, 350, 100, 300, [255,222,173], [255,20,147], 35)
        button3.display()
        button4=Button("YES", 550, 350, 100, 300, [255,222,173], [255,20,147], 38)
        button4.display()
        
    if screen==4:   #4th Question
        background(240, 255, 240)
        ans_x=280
        ans_y=40
        ans_h=100
        ans_w=300

        textFont(mono)
        textSize(50)
        fill(51, 153, 255)
        text("Q4: CLICK ", 35, 120 )
        
        button1=Button("OUT OF ORDER", 150, 200, 100, 300, [255,222,173], [255,20,147], 32 )
        button1.display()
        button2=Button("OUT OF ORDER", 550, 200, 100, 300, [255,222,173], [255,20,147], 32 )
        button2.display()
        button3=Button("OUT OF ORDER", 150, 350, 100, 300, [255,222,173], [255,20,147], 32)
        button3.display()
        button4=Button("OUT OF ORDER", 550, 350, 100, 300, [255,222,173], [255,20,147], 32)
        button4.display()
        button5=Button("THE ANSWER", 240, 47, 100, 300, [240, 255, 240], [51, 153, 255], 50,1)
        button5.display()
        
        textFont(mono)
        textSize(50)
        fill(51, 153, 255)
        text("Q4: CLICK ", 35, 120 )
        
    if screen==5: #5th Question
        global change
        global al
        al=1
        
        
            
        background(0)
        fill(240, 255, 240)
        rect(0,550,300,50)
        
        
        textSize(80)
        textFont(mono)
        fill(255, 255, 0)
        text("Q5: Put the mouse...", 220, 250)
        text("...on here -->", 500, 400)
    
        stroke(51, 153, 255)
        noFill()
        circle(950, 380, 80)
    
        noStroke()
        fill(220, 20, 60)
        circle(950, 380, 30)
        
        if change==0:
            
            if 910 < mouseX < 990 and 340 < mouseY < 420:
                change=1
            
        if change==1:
            background(51, 153, 255)
            textSize(32)
            
            fill(0,255,0)
            circle(950, 380, 110)
            circle(10, 300, 150)
            fill(0)
            text("GO",930,420)
            
            fill(220, 20, 60)
            circle(950, 380, 30)
            circle(10, 300, 30)
            fill(0)
            textSize(32)
            text("NEXT",0,210)
            
            text("QUESTION",20,400)
           
            
            
            textSize(80)
            textFont(mono)
            textSize(60)
            fill(173, 216, 255)
            
        
            text("DON'T TOUCH", 250, 300)
            text("THE BLUE!!",300,350)
            

            if not ((-20<mouseX<30 and 260<mouseY<330) or (910 < mouseX < 1000 and 340 < mouseY < 420)):
                global life
                life=0
                
            elif -10<mouseX<30 and 270<mouseY<320:
                screen+=1
                flag=1
    
                
    if screen==6:   #6th Question
        global al
        global x_q6
        global y_q6
        global appear
        ans_x=270
        ans_y=150
        ans_h=70
        ans_w=300
        al=0
        background(240, 255, 240)
        fill(51, 153, 255)
        textSize(60)
        text("Q6: WHAT HAPPENS IF\n       YOU P...P...PICK UP\n          ", 90, 50)
        pengans_img=loadImage(path+"pengans.png")
            
        penguin_img=loadImage(path+"penguin.png")
        image(penguin_img, x_q6, y_q6, 400, 70 )
        
        if x_q6!=270 and y_q6!=150:
            image(pengans_img, 180, 150, 100, 70 )  
            if flag==1:  
                appear=0
                
        if appear==0:
            
            button5=Button("NEXT QUESTION",300, 150, 100, 300, [255,222,173], [255,20,147], 28,1)
            button5.display()

            
        button1=Button("NOTHING", 150, 280, 100, 300, [255,222,173], [255,20,147], 32 )
        button1.display()
        button2=Button("IT PECKS YOUR \n FACE OFF", 550, 280, 100, 300, [255,222,173], [255,20,147], 28 )
        button2.display()
        button3=Button("IT FILLS \n YOUR STOMACH", 150, 400, 100, 300, [255,222,173], [255,20,147], 28)
        button3.display()
        button4=Button("PENGUIN POO", 550, 400, 100, 300, [255,222,173], [255,20,147], 32)
        button4.display()
        
        if flag==0:
            
            if x_q6 < mouseX < x_q6+300 and y_q6< mouseY < y_q6+70:
    
                deltax= mouseX - pmouseX
                deltay= mouseY - pmouseY
                
                x_q6+=deltax
                y_q6+=deltay
        global p
        p=millis()
            
                
    if screen==7:  #7th Question
        
        global p
        background(240, 255, 240)
        m =  millis()-p
        seconds =  m / 1000
        fill(51, 153, 255)
        text("Q7: 23 - 16 =?", 200, 100 )

        starttime = 10-seconds
        
        if starttime==7:
            button5=Button("", 30, 40, 100, 100, [240, 255, 240], [240, 255, 240], 35, 1 )
            noStroke()
            button5.display()
            
        if starttime<0:
            life=0
            
        fill(0)
        textSize(50)
        text(starttime, 100, 100)
        image(bomb_img, 20, 40, 80, 80)
        
        button1=Button("    4", 150, 200, 100, 300, [255,222,173], [255,20,147], 35 )
        button1.display()
        button2=Button("    WALRUS", 550, 200, 100, 300, [255,222,173], [255,20,147], 35 )
        button2.display()
        button3=Button("I DONT KNOW", 150, 350, 100, 300, [255,222,173], [255,20,147], 35)
        button3.display()
        button4=Button("All of above", 550, 350, 100, 300, [255,222,173], [255,20,147], 35)
        button4.display()
        


        
            
            
    if screen==8:  #8th Question
        background(240, 255, 240)
        fill(51, 153, 255)
        textSize(50)
        text("Q8: What is the answer to Q2?", 40, 120 )
        
        button1=Button("This one", 150, 200, 100, 300, [255,222,173], [255,20,147], 38 )
        button1.display()
        button2=Button("Or this one", 550, 200, 100, 300, [255,222,173], [255,20,147], 38, 1 )
        button2.display()
        button3=Button("This?", 150, 350, 100, 300, [255,222,173], [255,20,147], 38)
        button3.display()
        button4=Button("Maybe this", 550, 350, 100, 300, [255,222,173], [255,20,147], 38)
        button4.display()
        
        image(arrow1_img, 700, 300, 80, 60)
        image(arrow2_img, 450, 260, 110, 80)
        image(arrow3_img, 450, 350, 100, 60)
        
        
    if screen==9:  #Bonus for life
       background(240, 255, 240)
       fill(255, 0, 0)
       textFont(bonus)
       textSize(60)
       text("BONUS!! Do you want to\nredeem 1 life for 60 points?", 70, 120 )
       
       button1=Button("YES!!", 150, 300, 100, 300, [255,222,173], [255,20,147], 40, 1 )
       button1.display()
       button2=Button("NAH", 550, 300, 100, 300, [255,222,173], [255,20,147], 40, 1 )
       button2.display()
       
    if screen==10:  #9th question
        ans_x=200
        ans_y=400
        ans_h=40
        ans_w=40
        background(240, 255, 240)
        fill(51, 153, 255)
        textFont(bonus)
        textSize(60)
        
        text("Q9: The answer is\n       a horseshoe.", 70, 90 )
        
        button1=Button("HOOF", 150, 200, 100, 300, [255,222,173], [255,20,147], 30 )
        button1.display()
        
        button2=Button("A horseshoe", 550, 200, 100, 300, [255,222,173], [255,20,147], 30 )
        button2.display()

        button3=Button("WHAT DO\nYOU MEAN?", 150, 350, 100, 300, [255,222,173], [255,20,147], 30, 1)
        button3.display()
        
        button4=Button("HORSES WEAR\nSHOES??", 550, 350, 100, 300, [255,222,173], [255,20,147], 30)
        button4.display()
        
        global prev
        prev=millis()
        
    if screen==11:  #10th Question
        
        global prev
        background(240, 255, 240)
        text("ok", 300, 350)
        
        m =  millis()- prev
        seconds =  m / 1000
        traffic=loadImage(path+"traffic.png")
        
        fill(255,0,0)
        textFont(mono)
        textSize(80)
        
        text("Q10. QUICK!!\n PRESS ONE", 200, 90 )
        image(traffic, 0, 250, 1000, 200)
        
        button1=Button("", 150,300,100,150, [255,222,173], [255,20,147], 50 )
        button1.display()
        
        button2=Button("", 550,300,100,150, [255,222,173], [255,20,147], 50 )
        button2.display()

        button3=Button("", 350,300,100,150, [255,222,173], [255,20,147], 50)
        button3.display()
        
        button4=Button("", 750,300,100,150, [255,222,173], [255,20,147], 50)
        button4.display()
        
        starttime = 5-seconds
        
        if starttime==7:
            button5=Button("", 30, 40, 100, 100, [240, 255, 240], [240, 255, 240], 35, 1 )
            noStroke()
            button5.display()
            
        if starttime<0:
            life=0
        fill(0)
        textSize(50)
        text(starttime, 120, 130)
        image(bomb_img, 30, 50, 100, 100)
                
    if screen==12: #Win
        background(0)
        fill(255, 0, 0)
        textSize(50)
        text("Final Question!\nAnswer this question wrong to win!", 50, 90 )
        text("23 - 16?", 50, 220 )
        
        button1=Button("7", 150, 300, 100, 300, [255,222,173], [255,20,147], 30, 2 )
        button1.display()
        
        button2=Button("A horseshoe", 550, 300, 100, 300, [255,222,173], [255,20,147], 30 )
        button2.display()
            
        if life==4:
           win=1
        

        

    gamelife=Lives(life)
    
    if screen==13:
        image(win_img, 0, 0, 1000, 600)
        noLoop()
    if life<=0: #Game over page
        global win
        if screen!=12 and screen!=13:  
            image(gameover, 0, 0, 1000, 600)

        elif win==1:
            screen+=1
            
        elif win==0:

            image(gameover, 0, 0, 1000, 600)
            

    
    if screen!=0: #to display coin except for start page
        coin1=Coin()
        global coin
