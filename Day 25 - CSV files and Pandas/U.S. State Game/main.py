import turtle as t
import pandas as p

ALL_STATES_COUNT = 50

image = "./blank_states_img.gif"
screen = t.Screen()
screen.title(titlestring="U.S. State Game")
screen.addshape(image)
screen.listen()

t.shape(image)
map_writer = t.Turtle()
map_writer.hideturtle()
map_writer.penup()

states_df = p.read_csv("./50_states.csv")
states_list = states_df.state.to_list()

correct_answers = 0
guessed_list = []

while correct_answers < ALL_STATES_COUNT:

    answer = screen.textinput(title=f"{correct_answers}/{ALL_STATES_COUNT} States Correct", prompt="What's another state?").title()

    if answer == "Exit":
        not_guessed_states = []

        for state in states_list:
            if state not in guessed_list:
                not_guessed_states.append(state)

        states_to_learn = p.DataFrame(not_guessed_states)
        states_to_learn.to_csv("./states_to_learn.csv")

        break

    if answer in states_list:
        guessed_list.append(answer)
        correct_answers += 1
        state_row = states_df[states_df.state == answer]
        state_x, state_y = state_row.values[0][1:]
        map_writer.goto(x=state_row.x.item(), y=state_row.y.item())
        map_writer.write(arg=answer)
