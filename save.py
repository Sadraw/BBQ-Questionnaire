from questionnaire_data import questions
import sys

def ask_question(question_number, file=None):
    question_id = sorted(questions.keys())[question_number - 1]
    question_text = questions[question_id]
    if question_number :
        print(f"{question_number}: {question_text}) "
        print Antwoord met 'ja' of 'nee')")
        user_input = validate_ja_nee_answer(input("Uw antwoord: "))
    else:
        print(f"{question_number}: {question_text}")
        user_input = input("Uw antwoord: ")

    if file:
        file.write(f"{question_number}: {question_text}\n")
        file.write(f"Uw antwoord: {user_input}\n\n")

    return user_input

def validate_ja_nee_answer(answer):
    valid_answers = ["ja", "nee"]
    while answer.lower() not in valid_answers:
        print("Ongeldig antwoord. Vul a.u.b. 'ja' of 'nee' in.")
        answer = input("Uw antwoord (ja/nee): ")
    return answer

def questionnaire():
    userName = input("Give me a name for the file: ")
    with open(userName + ".txt", "w") as file:
        user_input = ask_question(1, file)
        user_input = ask_question(2, file)
        user_input = ask_question(3, file)
        user_input = ask_question(4, file)

        if user_input.lower() == "ja":
            user_input = ask_question(5, file)
            user_input = ask_question(6, file)
            user_input = ask_question(7, file)
            user_input = ask_question(8, file)
        else:
            user_input = ask_question(8, file)

        if user_input.lower() == "ja":
            user_input = ask_question(9, file)
            user_input = ask_question(10, file)
            user_input = ask_question(11, file)
            user_input = ask_question(12, file)
            user_input = ask_question(13, file)
            user_input = ask_question(17, file)
            user_input = ask_question(20, file)
            user_input = ask_question(21, file)
        else:
            user_input = ask_question(14, file)

        if user_input.lower() == "ja":
            user_input = ask_question(15, file)
            user_input = ask_question(16, file)
            user_input = ask_question(19, file)
            user_input = ask_question(21, file)
        else:
            user_input = ask_question(10, file)
            user_input = ask_question(11, file)
            user_input = ask_question(12, file)
            user_input = ask_question(13, file)
            user_input = ask_question(17, file)
            user_input = ask_question(20, file)

        if user_input.lower() == "ja":
            user_input = ask_question(26, file)
        else:
            user_input = ask_question(22, file)
            user_input = ask_question(23, file)
            user_input = ask_question(24, file)
            user_input = ask_question(25, file)
            user_input = ask_question(29, file)
            user_input = ask_question(28, file)
            user_input = ask_question(30, file)

        if user_input.lower() == "ja":
            user_input = ask_question(27, file)
            user_input = ask_question(28, file)
            user_input = ask_question(30, file)
        else:
            user_input = ask_question(22, file)
            user_input = ask_question(23, file)
            user_input = ask_question(24, file)
            user_input = ask_question(25, file)
            user_input = ask_question(29, file)
            user_input = ask_question(28, file)
            user_input = ask_question(30, file)

        if user_input.lower() == "ja":
            user_input = ask_question(34, file)
            if user_input.lower() == "ja":
                user_input = ask_question(37, file)

        else:
            user_input = ask_question(31, file)
            user_input = ask_question(32, file)
            user_input = ask_question(33, file)
            user_input = ask_question(35, file)
            if user_input.lower() == "ja":
                user_input = ask_question(36, file)
                user_input = ask_question(37, file)
            else:
                user_input = ask_question(37, file)

        if user_input.lower() == "ja":
            user_input = ask_question(38, file)
            user_input = ask_question(39, file)
            user_input = ask_question(40, file)
        else:
            user_input = ask_question(40, file)

        if user_input.lower() == "ja":
            user_input = ask_question(41, file)
            user_input = ask_question(42, file)
        else:
            user_input = ask_question(42, file)

        if user_input.lower() == "ja":
            user_input = ask_question(43, file)
            user_input = ask_question(44, file)
            user_input = ask_question(45, file)
            user_input = ask_question(46, file)
            user_input = ask_question(48, file)
            user_input = ask_question(47, file)
        else:
            user_input = ask_question(47, file)

        if user_input.lower() == "ja":
            user_input = ask_question(49, file)
            if user_input.lower() == "ja":
                user_input = ask_question(53, file)
        else:
            user_input = ask_question(50, file)
            user_input = ask_question(51, file)
            user_input = ask_question(52, file)
            user_input = ask_question(53, file)

        if user_input.lower() == "ja":
            user_input = ask_question(55, file)
        else:
            user_input = ask_question(54, file)
            user_input = ask_question(55, file)

        if user_input.lower() == "ja":
            user_input = ask_question(56, file)
            user_input = ask_question(57, file)
        else:
            user_input = ask_question(57, file)

        if user_input.lower() == "ja":
            user_input = ask_question(58, file)
            user_input = ask_question(59, file)
            user_input = ask_question(60, file)
        else:
            user_input = ask_question(60, file)

        if user_input.lower() == "ja":
            user_input = ask_question(64, file)
        elif user_input.lower() == "nee":
            user_input = ask_question(61, file)
            user_input = ask_question(62, file)
            user_input = ask_question(63, file)
            print("Einde vragenlijst")
            sys.exit()
        else:
            user_input = ask_question(61, file)
            user_input = ask_question(62, file)
            user_input = ask_question(63, file)
            print("Einde vragenlijst")
            sys.exit()


# Call the questionnaire function to start the process
questionnaire()
