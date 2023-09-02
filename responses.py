from datetime import datetime
import random

def dateandtime():
    now = datetime.now()

    # dd/mm/YY H:M:S
    dt_string = now.strftime("%d/%m/%Y")
    return "Now it is: "+ dt_string
def time():
    now = datetime.now()

    # dd/mm/YY H:M
    dt_string = now.strftime("%H:%M")
    return "Now it is: "+ dt_string

# Long responses
R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "Leaders never use the word failure, They look upon setbacks as learning experiences"
R_DATE = dateandtime()
R_TIME = time()

# Select an random msg when the input is not understood and return it
def unknown():
    responses = ["Sorry, I couldn't get an response, could you please search the same in the search box above..."]
    return responses[random.randrange(len(responses))]

