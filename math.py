def maths():
    questions = [
        "Q.1. What is 2+2?",
        "Q.2. What is 9/3?",
        "Q.3. What is 50 percent of 100?",
        "Q.4. What is the interest when, P=100,R=10 percent,Time= 1 year?",
        "Q.5. What is the value of x when x+2=10",
        "Q.6. What is the value of the angle of one side of a triangle when other two sides are 90 and 45?"
    ]

    options = [
        ["A. 1", "B. 2", "C. 3", "D. 4"],
        ["A. 0", "B. 3", "C. 2", "D. 9"],
        ["A. 50", "B. 100", "C. 2", "D. None of the above"],
        ["A. 200", "B. 100", "C. 1000", "D. 350"],
        ["A. 10", "B. 8", "C. 7", "D. 4"],
        ["A. 90", "B. 70", "C. 25", "D. 45"]
    ]

    answers = ["D", "B", "A", "B", "B", "D"]
    score = 0

    for i in range(6):
        print(questions[i])
        for k in range(4):
            print(options[i][k])
        print("--------------------------------------------------------------")

        user_input = input("Enter your answer: ").upper()

        while user_input.upper() not in ['A', 'B', 'C', 'D']:
            print("Enter a valid choice.")
            user_input = input("Enter your answer again: ").upper()

        print("Your answer is ", user_input, '.')

        if user_input == answers[i]:
            score += 4
        else:
            score -= 1

    return score  
