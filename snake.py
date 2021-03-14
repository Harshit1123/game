from turtle import Screen ,Turtle
import random
# import time

# screen = Screen()
# screen.setup(width=600,height=600)
# screen.bgcolor("black")
# screen.title("My Snake Game")
# screen.tracer(0)

# 

# segments = []

# for positions in starting_positions:
#     new_segment = Turtle("square")
#     new_segment.color("white")
#     new_sestarting_positions = [(0,0),(-20,0),(-40,0)]gment.penup()
#     new_segment.goto(positions)
#     segments.append(new_segment)


# game_is_on = True

# while game_is_on:
#     screen.update()
#     time.sleep(0.1)
    # for seg_num in range(len(segments)-1,0,-1):
    #     new_x = segments[seg_num-1].xcor()
    #     new_y = segments[seg_num-1].ycor()
    #     segments[seg_num].goto(new_x,new_y)
    # segments[0].forward(20)    


STARTING_POSITIONS = [(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT =  180
RIGHT = 0
colours= ['#FF007F','#FFFF00','#CC00CC','#00FFFF','#80FF00','#FF8000']

class Snake():

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:   
            self.add_segment(position)         
            

    def add_segment(self,position):        
        new_segment = Turtle("square")
        new_segment.color(random.choice(colours))
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

            
    def extend(self):
        self.add_segment(self.segments[-1].position())



    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x = self.segments[seg_num-1].xcor()
            new_y = self.segments[seg_num-1].ycor()
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DISTANCE) 


    def up(self): 
        if self.head.heading() != DOWN:
            self.head.setheading(UP)     
        
    def down(self): 
        if self.head.heading() != UP:
            self.head.setheading(DOWN)     

    def right(self): 
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)     

    def left(self): 
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)     


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.color("deeppink")
        self.speed("fastest")
        self.refresh()
        

    def refresh(self):
        random_x = random.randint(-280,280)
        random_y = random.randint(-280,280)
        self.goto(random_x,random_y)


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,269)        
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score = {self.score}",align="center",font=("Courier" , 22 , "normal"))

    def gameover(self):
        self.goto(0,0)    
        self.write(f"GAME OVER",align="center",font=("Courier" , 22 , "normal"))

        
    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()










