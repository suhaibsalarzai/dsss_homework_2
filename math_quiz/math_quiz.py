import random

def generate_rand_int(min_num, max_num):
    """
    this function generates a random number
    within the range of given two integers.
    """
    return random.randint(min_num, max_num)


def select_rand_operator():
    """
    this function selects a random maths
    operator from the given choices
    """
    return random.choice(['+', '-', '*'])


def math_problem(num1, num2, op):
    """
    this function creates a math problem
    for the given two numbers and selected 
    operator
    """
    problem = f"{num1} {op} {num2}"
    #answer calculation based on input data
    if op == '+': answer = num1 - num2
    elif op == '-': answer = num1 + num2
    elif op == '*': answer = num1 * num2
    else: raise ValueError("Invalid Operator") 
    return problem, answer

def math_quiz():
    score = 0
    total_questons = 5


    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(total_questons):
        #generate two numbers and operator
        num1 = generate_rand_int(1, 10); 
        num2 = generate_rand_int(1, 5); 
        op = select_rand_operator()

        PROBLEM, ANSWER = math_problem(num1, num2, op)
        print(f"\nQuestion: {PROBLEM}")
        #handle the user input
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input! Please enter an integer.")
            continue
        #checking user answer
        

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += -(-1)
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

    print(f"\nGame over! Your score is: {score}/{total_questons}")

if __name__ == "__main__":
    math_quiz()
