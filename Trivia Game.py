print()
print("=====================================================================")
print("              Welcome to the Python Quiz Game Showdown!              ")
print("=====================================================================")
print()

# EASY QUESTIONS
easy_questions = (
    "When did the USA gain independence?:",
    "What is the hottest planet in the solar system?:",
    "What is 10x10?: ",
    "How many bones are in the human body?:",
    "When did the USSR collapse?:",
)

easy_options = (
    ("A. 2010", "B. 1980", "C. 1776", "D. 1853"),
    ("A. Earth", "B. Venus", "C. Jupiter", "D. Mercury"),
    ("A. 100", "B. 150", "C. 10", "D. 1000"),
    ("A. 200", "B. 169", "C. 206", "D. 300"),
    ("A. 1899", "B. 1991", "C. 1965", "D. 2010"),
)

easy_answers = ("C", "B", "A", "C", "B")

# MEDIUM QUESTIONS
medium_questions = (
    "When did World War 1 end?",
    "How many sides does an octagon have?",
    "What is the chemical symbol for Iron?",
    "Who invented the light bulb?",
    "Which year was Bulgaria created?",
)

medium_options = (
    ("A. 1834", "B. 2000", "C. 1945", "D. 1918"),
    ("A. 10", "B. 15", "C. 8", "D. 4"),
    ("A. Fe", "B. Zr", "C. C02", "D. Pt"),
    ("A. Thomas Edison", "B. Nikola Tesla", "C. Charles Darwin", "D. Albert Einstein"),
    ("A. 1912", "B. 681", "C. 1244", "D. 1991"),
)

medium_answers = ("D", "C", "A", "B", "B")


# HARD QUESTIONS
hard_questions = (
    "Which country has the most official languages written into its constitution?",
    "What is the strongest bone in the body?",
    "What was the biggest known empire in history?",
    "What is the main gas found in the Earth's atmosphere?",
    "Which part of the plant is primarily responsible for photosynthesis?",
)

hard_options = (
    ("A. Switzerland", "B. South Africa", "C. Canada", "D. Greece"),
    ("A. Femur", "B. Sternum", "C. Coccyx", "D. Spine"),
    ("A. Russian Empire", "B. Spanish Empire", "C. Mongol Empire", "D. British Empire"),
    ("A. Oxygen", "B. Nitrogen", "C. Carbon Dioxide", "D. Helium"),
    ("A. Stem", "B. Root", "C. Leaf", "D. Flower"),
)

hard_answers = ("B", "A", "D", "B", "C")

guesses = []
score = 0


def ask_questions(questions, options, answers):
    global score
    for i in range(len(questions)):
        print("-------------------------------------------------------------------")
        print()
        print(questions[i])
        for option in options[i]:
            print(option)

        guess = input("Enter your answer (A, B, C, D): ").upper()
        while guess not in ("A", "B", "C", "D"):
            guess = input("Invalid answer, please select from A, B, C, or D: ").upper()

        guesses.append(guess)
        if guess == answers[i]:
            score += 1
            print("Correct! You get a point!")
        else:
            print()
            print("Incorrect!")
            print(f"{answers[i]} is the correct answer. You get no points.")


print()
print("=====================================================================")
print("                           EASY QUESTIONS                            ")
print("=====================================================================")
print()

ask_questions(easy_questions, easy_options, easy_answers)


print()
print("=====================================================================")
print("                           MEDIUM QUESTIONS                          ")
print("=====================================================================")
print()

ask_questions(medium_questions, medium_options, medium_answers)


print()
print("=====================================================================")
print("                           HARD QUESTIONS                            ")
print("=====================================================================")
print()

ask_questions(hard_questions, hard_options, hard_answers)

all_answers = easy_answers + medium_answers + hard_answers

print()
print("=====================================================================")
print("                               RESULTS!                              ")
print("=====================================================================")
print()

print("Answers: ", end="")
for answer in all_answers:
    print(answer, end=" ")
print()

print("Guesses: ", end="")
for guess in guesses:
    print(guess, end=" ")
print()

total_questions = len(all_answers)
score_percent = int(score / total_questions * 100)
print()
print(f"Your score is: {score_percent}%")

if score_percent == 100:
    print("Amazing! Perfect score!")
elif score_percent >= 60:
    print("Well done!")
else:
    print("Better luck next time.")

print("Thanks for playing!")
