# AT THE END OF LESSON, COPY YOUR CODE FROM MINECRAFT HERE.
# THIS IS SO THAT YOU HAVE A RECORD OF YOUR CODE FROM MINECRAFT CODE BUILDER

# comments start with hashtags


def teleport():
    agent.teleport_to_player()
player.on_chat("come", teleport)

# agent move forward
def forward(count):
    agent.move(FORWARD, count)
player.on_chat("fw", forward)

# BACK, "back"
def back(count):
    agent.move(BACK, count)
player.on_chat("back", back)

# UP, "up"
def up(count):
    agent.move(UP, count)
player.on_chat("up", up)

# DOWN, "down"
def down(count):
    agent.move(DOWN, count)
player.on_chat("down", down)





# tl : turn left
def tl():
    agent.turn(LEFT)
player.on_chat("tl", tl)

# tr: turn right
def tr():
    agent.turn(RIGHT)
player.on_chat("tr", tr)



def chop():
    for count in range(6):
        agent.destroy(FORWARD)
        agent.collect_all()
        agent.move(UP, 1)
    agent.teleport_to_player()

player.on_chat("chop", chop)