import random

# Dictionary of questions and answers
questions = {
    "What is the capital of France?": "Paris",
    "Who painted the Mona Lisa?": "Leonardo da Vinci",
    "What is the largest planet in our solar system?": "Jupiter",
    "What is the chemical symbol for gold?": "Au",
    "Who wrote the play Romeo and Juliet?": "William Shakespeare"
}

# Initialize score
score = 0

# Loop through each question-answer pair in the dictionary
for question, answer in questions.items():
    # Get the user's answer
    user_answer = input(question + " ")
    
    # Compare user's answer with the correct answer (case-insensitive)
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is " + answer)

# Display final score
print("Your final score is " + str(score))
