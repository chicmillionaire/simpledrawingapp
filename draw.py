import turtle

def main():
    filename = input("Please enter drawing filename: ")

    #Create Turtle Graphics Window to draw in
    t = turtle.Turtle()
    screen = t.getscreen()
    file = open('image.txt', "r")
    for line in file:
        #Removes newline character at the end of the line and any spaces
        #at the beginning or the ending of the line
        text = line.strip()

        commandList = text.split(",")
        command = commandList[0]

        if command == "goto":
            x = float(commandList[1])
            y = float(commandList[2])
            width = float(commandList[3])
            color = commandList[4].strip()
            t.width = width
            t.pencolor(color)
            t.goto(x,y)
        elif command == "circle":
            radius = float(commandList[1])
            width = float(commandList[2])
            color = commandList[3].strip()
            t.width = width
            t.pencolor(color)
            t.circle(radius)
        elif command == "beginfill":
            color = commandList[1].strip()
            t.fillcolor(color)
            t.begin_fill()
        elif command == "endfill":
            t.end_fill()
        elif command == "penup":
            t.penup()
        elif command == "pendown":
            t.pendown()
        else:
            print ("Unknown command found in file:", command)
        
    #closes file
    file.close()

    #hides turtle
    t.ht()

    screen.exitonclick()
    print("Program Execution Completed.")

#call main function
if __name__ == "__main__":
    main()



