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

# question = "What do you call a deer with no eye?"
# hidden_answer = "no idea"
# reply = "no"

# while reply != hidden_answer:
#     reply = input(question)
#     if reply == hidden_answer:
#         print("you got it")
#     else:
#         print("wrong! try again.")

import random
score = 0
question = "What do you call a deer with no eye?"
hidden_answer = "no idea"
reply = "no"

print("you shall not pass unless you answer my math questions correctly")
while score < 3:
    num1 = random.randint(1,10)
    num2 = random.randint(1,3)
    question = "what is " + str(num1) + "+" + str(num2) + "? "
    hidden_answer = num1 + num2
    reply = input(question)
    if reply == hidden_answer:
        print("you got it")
        score = score +1
    else:
        print("wrong! try again.")

########################################################################
# Additional exercises: