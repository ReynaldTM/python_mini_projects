import random
import time


OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3 # permanent, unchanging variables
MAX_OPERAND = 12
TOTAL_PROBLEM = 10


def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + str(operator) + " " + str(right)
    answer = eval(expr)
    print(expr)
    return expr, answer



wrong = 0
input("Press enter to start!")
print("---------------------------------------")

start_time = time.time()

for i in range(TOTAL_PROBLEM):
    expr, answer = generate_problem()
    while True:
        guess = input(f"Problem #{str(i + 1)}: {expr} = ")
        if guess == str(answer):
            break
        wrong +=1

end_time = time.time()
total_time = round(end_time - start_time, 2)


print("---------------------------------------")
print(f"Good work! You finished {total_time} seconds)")