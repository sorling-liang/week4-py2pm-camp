# Write all your codes for Day 4 here.
# COMMENT out the previous task before going on to the next task
print("hello from day4")

########################################################################
# Task 1:

import random
import time

for count in range(10):
    print(random.randint(1, 999))

########################################################################
# Task 2:

# while True:
#     print("Hello there!")

question = "What do you call a deer with no eye?"
hidden_answer = "no idea"
reply = "no"

while reply != hidden_answer:
    reply = input(question)
    if reply == hidden_answer:
        print("you got it")
    else:
        print("wrong! try again.")


########################################################################
# Additional exercises: