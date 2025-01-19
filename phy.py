def phy():
    questions = [
        "Q.1. What is the unit of force?",
        "Q.2. What is the speed of light in vacuum?",
        "Q.3. Which of these is a scalar quantity?",
        "Q.4. What is the law of conservation of energy?",
        "Q.5. What is the gravitational constant (G)?",
        "Q.6. What is the SI unit of electric current?"
    ]

    options = [
        ["A. Newton", "B. Joule", "C. Pascal", "D. Watt"],
        ["A. 3 x 10^8 m/s", "B. 3 x 10^6 m/s", 
         "C. 3 x 10^5 m/s", "D. 3 x10^9 m/s"],
        ["A. Mass","B. Temperature","C. Speed","D. Distance"],
        ["A. Energy cannot be created or destroyed","B. Energy can be created and destroyed",
          "C. Energy can only be transformed",  "D. None of these"],
        ["A. 6 .67x10^-11 N(m/kg)^2","B. 9 .81 N/kg",
          "C. 1 .6x10^-19 N(m/kg)^2", "D. 8 .31 J/(mol·K)"],
        ["A. Volt","B. Ampere","C. Ohm","D. Coulomb"]
    ]

    answers=["A","A","D","A","A","B"]
    score = 0

    for i in range(6):
        print(questions[i])
        for k in range(4):
            print(options[i][k])
        print("--------------------------------------------------------------")

        user_input = input("Enter your answer: ").upper()

        while user_input not in ['A', 'B', 'C', 'D']:
            print("Enter a valid choice.")
            user_input = input("Enter your answer again: ").upper()

        print("Your answer is ", user_input, '.')

        if user_input == answers[i]:
            score += 4
        else:
            score -= 1

    return score
