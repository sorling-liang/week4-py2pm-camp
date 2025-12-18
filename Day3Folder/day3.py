# Write all your codes for Day 3 here.
# COMMENT out the previous task before going on to the next task
print("hello from day3")

########################################################################
# Task 1:

# yourname = input("What is your name?")
# title = input("What is your title?")
# task = input("What is the task?")

# print() use string concatenation +
# print(title, yourname, "orders the peasants to", task)

########################################################################
# Task 2:



########################################################################
# Task 3:

# calculator
# num1 = input("what is the first number?")
# num2 = input("what is the second number?")
# # conversion int()
# answer = int(num1) * int(num2) 
# print("the answer is", answer)


########################################################################
# Task 4:



########################################################################
# Task 5:

hidden_password = "passme"
is_correct = False
for count in range(3):
    guess = input("do you know my password?")

    if hidden_password == guess:
        print("please come in")
        is_correct = True
        break
    else:
        print("its okay, try again!")

if is_correct == False:
    print("your account is locked. I have recorded your face in the video")

########################################################################
# Task 6:



########################################################################
# Task 7:



########################################################################
# Task 8:



########################################################################
# Additional exercises: