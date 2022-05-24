from questions import quiz


def check_ans(Question, ans, attempts, score):
    """
    Takes the arguments, and confirms if the Answer provided by user is correct.
    Converts all Answers to lower case to make sure the quiz is not case sensitive.
    """
    if quiz[Question]['Answer'].lower() == ans.lower():
        print(f"Correct Answer! \nYour score is {score + 1}!")
        return True
    else:
        print(f"Wrong Answer :( \nYou have {attempts - 1} left! \nTry again...")
        return False


def print_dictionary():
    for Question_id, ques_Answer in quiz.items():
        for key in ques_Answer:
            print(key + ':', ques_Answer[key])


def intro_message():
    """
    Introduces user to the quiz and rules, and takes an input from customer to start the quiz.
    Returns true regardless of any key pressed.
    """
    print("Welcome to this fun food quiz! \nAre you ready to test your knowledge?")
    input("Press any key to start the fun ;) ")
    return True


# python project.py
intro = intro_message()
while True:
    score = 0
    for Question in quiz:
        attempts = 3
        while attempts > 0:
            print(quiz[Question]['Question'])
            Answer = input("Enter Answer (To move to the next Question, type 'skip') : ")
            if Answer == "skip":
                break
            check = check_ans(Question, Answer, attempts, score)
            if check:
                score += 1
                break
            attempts -= 1

    break

print(f"Your final score is {score}!")
print("Thanks for playing!")
print("Want to know the correct Answers? Please see them below! ;)")
print_dictionary()