
questions = (
    "Which is the largest ocean on Earth?: ",
    "Who developed the theory of relativity?: ",
    "What is the capital city of Australia?: ",
    "Which organ in the human body produces insulin?: ",
    "Which metal is liquid at room temperature?: "
)

options = (
    ("A. Atlantic", "B. Indian", "C. Pacific", "D. Arctic"),
    ("A. Isaac Newton", "B. Albert Einstein", "C. Galileo Galilei", "D. Nikola Tesla"),
    ("A. Sydney", "B. Melbourne", "C. Canberra", "D. Brisbane"),
    ("A. Liver", "B. Pancreas", "C. Kidney", "D. Heart"),
    ("A. Mercury", "B. Sodium", "C. Aluminum", "D. Lead")
)

answers = ("C", "B", "C", "B", "A")
guesses = []
score = 0
que_num = 0


for question in questions:
    print("-------------------------------------------")
    print(question)
    
    for option in options[que_num]:
        print(option) 

    
    guess = input("Enter answer (A, B, C, D): ").upper()

    if guess not in ("A", "B", "C", "D"):
        print("Option doesnot exists.")
        
    else:
        guesses.append(guess)

    if guess == answers[que_num]:
        score += 1
        print("CORRECT")

    else:
        print("INCORRECT")
        print(f"{answers[que_num]} is the correct answer")
    que_num +=1    

print("RESULTS")

print("answers: ", end=" ")
for answer in answers:
    print(answer, end=" ")
print()

print("guesses: ", end=" ")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your Score is: {score}%")