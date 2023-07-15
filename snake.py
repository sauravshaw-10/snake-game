from turtle import Turtle

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def right(self):
        current_position = self.head.heading()
        if current_position == 90:
            new_position = current_position - 90
            self.head.setheading(new_position)
        elif current_position == 270:
            new_position = current_position + 90
            self.head.setheading(new_position)

    def left(self):
        current_position = self.head.heading()
        if current_position == 90:
            new_position = current_position + 90
            self.head.setheading(new_position)
        elif current_position == 270:
            new_position = current_position - 90
            self.head.setheading(new_position)

    def up(self):
        current_position = self.head.heading()
        if current_position == 0:
            new_position = current_position + 90
            self.head.setheading(new_position)
        elif current_position == 180:
            new_position = current_position - 90
            self.head.setheading(new_position)

    def down(self):
        current_position = self.head.heading()
        if current_position == 0:
            new_position = current_position - 90
            self.head.setheading(new_position)
        elif current_position == 180:
            new_position = current_position + 90
            self.head.setheading(new_position)







