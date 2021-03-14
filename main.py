import turtle
import pandas
screen = turtle.Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)

data = pandas.read_csv("50_states.csv")

print(data)

turtle.shape(image)
gameIsOn = True
guessedStates = []
while len(guessedStates) < 50:
    userGuess = turtle.textinput("Your Guess","Guess a state")
    states = data.state.to_list()
    if userGuess in states:
        newX = int(data[data.state == userGuess].x)
        newY = int(data[data.state == userGuess].y)
        stateName = turtle.Turtle()
        stateName.penup()
        stateName.ht()
        stateName.goto(newX, newY)
        stateName.write(userGuess, align="center", font=("Arial", 10, "normal"))
        guessedStates.append(userGuess)
    elif userGuess == "exit":
        statesToLearn = [i for i in states if i not in guessedStates]
        # for i in states:
        #     if i not in guessedStates:
        #         statesToLearn.append(i)
        df = pandas.DataFrame(statesToLearn)
        df.to_csv("statesToLearn.csv")
        exit(0)




screen.exitonclick()