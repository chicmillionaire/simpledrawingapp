import turtle

# Each of the command classes below hold information for one of the
# types of commands found in a graphics file. For each command there must
# be a draw method that is given a turtle and uses the turtle to draw
# the object. By having a draw method for each class, we can
# polymorphically call the right draw method when traversing a sequence of
# these commands. Polymorphism occurs when the "right" draw method gets
# called without having to know which graphics command it is being called on

class GoToCommand:
# Here the constructor is defined with default values for width and color.
# This means we can construct a GoToCommand objects as GoToCommand(10,20),
# or GoToCommand(10,20,5), or GoToCommand(10,20,5,"yellow").
    def __init__(self,x,y,width=1,color="black"):
        self.x = x
        self.y = y
        self.width = width
        self.color = color

    def draw(self,turtle):
        turtle.width(self.width)
        turtle.pencolor(self.color)
        turtle.goto(self.x,self.y)

class CircleCommand:
    def __init__(self,radius,width=1,color="black"):
        self.radius = radius
        self.width = width
        self.color = color

    def draw(self,turtle):
        turtle.circle(self.radius)
        turtle.pencolor(self.color)
        turtle.width(self.width)

class BeginFillCommand:
    def __init__(self, color):
        self.color = color

    def draw(self,turtle):
        turtle.fillcolor(self.color)
        turtle.begin_fill()

class EndFillCommand:
    def __init__(self):
        # pass is a statement placeholder and does nothing. We have nothing
        #  # to initialize in this class because all we want is the polymorphic
        # behavior of the draw method.
        pass

    def draw(self,turtle):
        turtle.end_fill()

class PenUpCommand:
    def __init__(self):
        pass

    def draw(self,turtle):
        turtle.penup()

class PenDownCommand:
    def __init__(self):
        pass

    def draw(self,turtle):
        turtle.pendown()

class PyList:
    def __init__(self):
        self.items = []

    def append(self, item):
        self.items = self.items + [item]

    # if we want to iterate over this sequence, we define the special method
    # called __iter__(self). Without this we’ll get "builtins.TypeError:    
    #  # ’PyList’ object is not iterable" if we try to write
    # for cmd in seq:
    # where seq is one of these sequences. The yield below will yield an
    # element of the sequence and will suspend the execution of the for
    # loop in the method below until the next element is needed. The ability
    # to yield each element of the sequence as needed is called "lazy" evaluation
    # and is very powerful. It means that we only need to provide access to as
    # many of elements of the sequence as are necessary and no more.
    def __iter__(self):
        for c in self.items:
            yield c

def main():
    filename = input("Please enter drawing filename: ")
    
    t = turtle.Turtle()
    screen = t.getscreen()
    file = open(filename, "r")

    # Create a PyList to hold the graphics commands that are 
    # read from the file.
    
    graphicsCommand = PyList()
    command = file.readline().strip()

    while command != " ":

        # Now we must read the rest of the record and then process it. Because
        # # records are variable length, we’ll use an if-elif to determine which
        # type of record it is and then we’ll read and process the record.
        # In this program, processing the record means creating a command object
        # using one of the classes above and then adding that object to our
        # graphicsCommands PyList object.

        if command == "goto":
            x = float(file.readline())
            y = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = GoToCommand(x, y, width, color)

        elif command == "circle":
            radius = float(file.readline())
            width = float(file.readline())
            color = file.readline().strip()
            cmd = CircleCommand(radius, width, color)

        elif command == "beginfill":
            color = file.readline().strip()
            cmd = BeginFillCommand(color)

        elif command == "endfill":
            cmd = EndFillCommand()

        elif command == "penup":
            cmd = PenUpCommand()

        elif command == "pendown":
            cmd = PenDownCommand()

        else:
            raise RuntimeError("Unknown Command: " + command)

        graphicsCommand.append(cmd)

        command = file.readline().strip()

    for cmd in graphicsCommand:
        cmd.draw(t)

    file.close()
    t.ht()
    screen.exitonclick()
    print("Program Execution Completed.")

if __name__ =="__main__":
    main()        