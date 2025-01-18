def chem():
    questions = [
        "Q.1. What is the formula name of water?",
        "Q.2. What is chemical formula of methanol?",
        "Q.3. Which of these is highly reactive in open atmosphere?",
        "Q.4. Which of these is the reason for depleting the ozone layer?",
        "Q.5. What is the weight of Carbon?",
        "Q.6. Which of these carbocations is the highest stable carbocation?"
    ]

    options = [
        ["A. D2O", "B. H2O", "C. HO", "D. DO"],
        ["A. CH3OH", "B. C2H5OH", "C. C2H2", "D. C2H4"],
        ["A. Fe", "B. H2O", "C. K", "D. Cu"],
        ["A. CFC", "B. Fire", "C. Fluorine", "D. CO2"],
        ["A. 10", "B. 8", "C. 7", "D. 12"],
        ["A. 2 degree", "B. 3 degree", "C. 1 degree", "D. None of These"]
    ]

    answers = ["B", "A", "C", "A", "D", "B"]
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
