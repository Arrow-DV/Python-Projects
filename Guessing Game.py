# Import Needed Libarys
import random
# Make Needed Variables
score    = 10
gameover = False
# Make Lists Questions And Answers
questions = [
    "What is the capital of France?",
    "Who wrote the novel 'Pride and Prejudice'?",
    "What is the chemical symbol for gold?",
    "Who painted the Mona Lisa?",
    "What is the largest planet in our solar system?",
    "Who is the current President of the United States?",
    "What is the formula for calculating the area of a circle?",
    "In which country is the Taj Mahal located?",
    "Who discovered penicillin?",
    "What is the tallest mountain in the world?",
    "Which planet is known as the Red Planet?",
    "Who was the first person to step on the moon?",
    "What is the currency of Japan?",
    "Who painted the ceiling of the Sistine Chapel?",
    "What is the chemical formula for water?",
    "Which playwright wrote Romeo and Juliet?",
    "What is the capital of Australia?",
    "Who is the author of the Harry Potter series?",
    "What is the largest ocean on Earth?",
    "Who invented the telephone?",
    "What is the national bird of the United States?",
    "Who wrote the play 'Hamlet'?",
    "What is the largest organ in the human body?",
    "Who is the Greek god of thunder?",
    "What is the formula for calculating the volume of a sphere?",
    "In which year did World War II end?",
    "What is the currency of Germany?",
    "Who painted the Starry Night?",
    "What is the chemical symbol for oxygen?",
    "Who is the author of 'To Kill a Mockingbird'?",
    "What is the capital of India?",
    "Who founded Microsoft?",
    "Who is the current Prime Minister of the United Kingdom?",
    "What is the longest river in the world?",
    "Who painted the Last Supper?",
    "What is the chemical formula for carbon dioxide?",
    "Which scientist discovered the theory of relativity?",
    "What is the largest desert in the world?",
    "Who is the author of '1984'?",
    "What is the capital of Brazil?",
    "Who is the lead singer of the band Queen?",
    "What is the chemical symbol for iron?",
    "Who painted the Birth of Venus?",
    "What is the formula for calculating density?",
    "Who invented the light bulb?",
    "What is the national animal of China?",
    "Who wrote the play 'Macbeth'?",
    "What is the largest country in the world by land area?",
    "What is the square root of 64?"
]
answers = [
    "Paris",
    "Jane Austen",
    "Au",
    "Leonardo da Vinci",
    "Jupiter",
    "The answer may vary depending on the current year.",
    "πr²",
    "India",
    "Alexander Fleming",
    "Mount Everest",
    "Mars",
    "Neil Armstrong",
    "Japanese yen",
    "Michelangelo",
    "H2O",
    "William Shakespeare",
    "Canberra",
    "J.K. Rowling",
    "Pacific Ocean",
    "Alexander Graham Bell",
    "Bald eagle",
    "William Shakespeare",
    "Skin",
    "Zeus",
    "4/3πr³",
    "1945",
    "Euro",
    "Vincent van Gogh",
    "O",
    "Harper Lee",
    "New Delhi",
    "Bill Gates",
    "The answer may vary depending on the current year.",
    "Nile",
    "Leonardo da Vinci",
    "CO2",
    "Albert Einstein",
    "Sahara",
    "George Orwell",
    "Brasília",
    "Freddie Mercury",
    "Fe",
    "Sandro Botticelli",
    "Mass/volume",
    "Thomas Edison",
    "Giant panda",
    "William Shakespeare",
    "Russia",
    "8"
]
# Show Random Question
def random_question():
    global score,gameover
    if score == 0 : gameover = True
    _random_ = random.randint(0,len(questions))
    print(questions[_random_])
    answer = input("Answer: ").lower()
    if(answers[_random_].lower() == answer):
        print("Correct! 50 Score Added")
        score += 50
    else:
        score -= 10
        print(f"Incorrect You Have Lost 10 Score\nCurrent Score {score} ")
while gameover == False:
    random_question()
else:
    score = 0 if score < 0 else score # If Score Like Less Than 0 It Makes It 0
    print(f"GameOver.. You Had Got {score} Score")
    