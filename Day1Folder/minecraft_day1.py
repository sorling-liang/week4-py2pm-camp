# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER
################# Function Section #############################

# comments start with hashtags

def addition(num1, num2):
    player.say(num1 * num2)

addition(12, 9)
 
def teleport():
    agent.teleport_to_player()
player.on_chat("come", teleport)

# tl : turn left
def tl():
    agent.turn(LEFT)
player.on_chat("tl", tl)

# tr: turn right
def tr():
    agent.turn(RIGHT)
player.on_chat("tr", tr)

################## On Chat Commands Section #####################
