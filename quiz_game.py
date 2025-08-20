def quiz_game():
    print("🎓 Welcome to the Python Quiz Game!")
    name = input("Enter your name: ")
    print(f"\nHello, {name}! Let's start the quiz.\n")

    questions = [
        {"q": "What is the capital of France?", "options": ["A) Paris", "B) London", "C) Rome", "D) Berlin"], "ans": "A"},
        {"q": "Which language is this program written in?", "options": ["A) Java", "B) Python", "C) C++", "D) Ruby"], "ans": "B"},
        {"q": "What is 5 * 6?", "options": ["A) 11", "B) 30", "C) 56", "D) 65"], "ans": "B"},
        {"q": "Who developed Python?", "options": ["A) Dennis Ritchie", "B) Guido van Rossum", "C) Elon Musk", "D) James Gosling"], "ans": "B"},
        {"q": "What is the capital of Japan?", "options": ["A) Beijing", "B) Tokyo", "C) Seoul", "D) Bangkok"], "ans": "B"},
        {"q": "Which year did World War II end?", "options": ["A) 1945", "B) 1939", "C) 1918", "D) 1965"], "ans": "A"},
        {"q": "What is the chemical symbol for Gold?", "options": ["A) Au", "B) Ag", "C) Gd", "D) Go"], "ans": "A"},
        {"q": "Which planet is known as the Red Planet?", "options": ["A) Earth", "B) Venus", "C) Mars", "D) Jupiter"], "ans": "C"},
        {"q": "What is 12 + 28?", "options": ["A) 30", "B) 38", "C) 40", "D) 50"], "ans": "C"},
        {"q": "Which is the largest mammal?", "options": ["A) Elephant", "B) Whale Shark", "C) Blue Whale", "D) Giraffe"], "ans": "C"},
        {"q": "Who wrote 'Hamlet'?", "options": ["A) Charles Dickens", "B) William Shakespeare", "C) Mark Twain", "D) Leo Tolstoy"], "ans": "B"},
        {"q": "Which gas do humans breathe in?", "options": ["A) Oxygen", "B) Carbon Dioxide", "C) Nitrogen", "D) Hydrogen"], "ans": "A"},
        {"q": "How many continents are there?", "options": ["A) 5", "B) 6", "C) 7", "D) 8"], "ans": "C"},
        {"q": "What is the square root of 81?", "options": ["A) 7", "B) 8", "C) 9", "D) 10"], "ans": "C"},
        {"q": "Who painted the Mona Lisa?", "options": ["A) Pablo Picasso", "B) Vincent Van Gogh", "C) Leonardo da Vinci", "D) Michelangelo"], "ans": "C"},
        {"q": "Which is the fastest land animal?", "options": ["A) Cheetah", "B) Lion", "C) Horse", "D) Tiger"], "ans": "A"},
        {"q": "Which ocean is the largest?", "options": ["A) Atlantic", "B) Pacific", "C) Indian", "D) Arctic"], "ans": "B"},
        {"q": "Which programming language is called 'Mother of all languages'?", "options": ["A) Python", "B) Assembly", "C) C", "D) Java"], "ans": "C"},
        {"q": "What is H2O commonly known as?", "options": ["A) Salt", "B) Water", "C) Oxygen", "D) Hydrogen"], "ans": "B"},
        {"q": "Which country invented pizza?", "options": ["A) USA", "B) France", "C) Italy", "D) Spain"], "ans": "C"},
        {"q": "Which bird is a universal symbol of peace?", "options": ["A) Crow", "B) Dove", "C) Eagle", "D) Parrot"], "ans": "B"},
        {"q": "Which is the tallest mountain in the world?", "options": ["A) K2", "B) Kanchenjunga", "C) Mount Everest", "D) Kilimanjaro"], "ans": "C"},
        {"q": "Which element has the symbol 'O'?", "options": ["A) Oxygen", "B) Osmium", "C) Ozone", "D) Oxide"], "ans": "A"},
        {"q": "What is the national sport of India?", "options": ["A) Cricket", "B) Hockey", "C) Football", "D) Kabaddi"], "ans": "B"},
        {"q": "How many hours are in a day?", "options": ["A) 12", "B) 24", "C) 48", "D) 60"], "ans": "B"}
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}: {q['q']}")
        for opt in q["options"]:
            print(opt)
        answer = input("👉 Enter your answer (A/B/C/D): ").upper()

        if answer == q["ans"]:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {q['ans']}")

    percentage = (score / len(questions)) * 100
    print("\n🏆 Quiz Completed!")
    print(f"Player: {name}")
    print(f"Correct Answers: {score}/{len(questions)}")
    print(f"Percentage: {percentage:.2f}%")

if __name__ == "__main__":
    quiz_game()
