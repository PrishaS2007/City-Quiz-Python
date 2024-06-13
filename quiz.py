def quiz():
    # List of questions along with options and the correct answer
    questions = [
        {
            "question": "What's the capital of France?",
            "options": ["Berlin", "Madrid", "Paris", "Rome"],
            "answer": 'c'
        },
        {
            "question": "What is the capital of Germany?",
            "options": ["Berlin", "Frankfurt", "Munich", "Bremen"],
            "answer": 'a'
        },
        {
            "question": "What is the capital of Haiti?",
            "options": ["Bissau", "San Salvador", "Banjul", "Port Au Prince"],
            "answer": 'd'
        },
        {
            "question": "What is the capital of Gambia?",
            "options": ["Asmara", "Banjul", "Malabo", "New Delhi"],
            "answer": 'b'
        },
        {
            "question": "What is the capital of Jordan?",
            "options": ["Amman", "Jakarta", "Beirut", "Tripoli"],
            "answer": 'a'
        },
        {
            "question": "What is the capital of Liberia?",
            "options": ["Valleta", "Tehran", "Monrovia", "Riga"],
            "answer": 'c'
        },
        {
            "question": "What is the capital of North Korea?",
            "options": ["Belfast", "Pyongyang", "Edmonton", "Hong Kong"],
            "answer": 'b'
        },
        {
            "question": "What is the capital of Portugal?",
            "options": ["Lisbon", "Mallorca", "Porta", "Evora"],
            "answer": 'a'
        },
        {
            "question": "What is the capital of Sweden?",
            "options": ["Greenland", "Paramaribo", "Cardiff", "Stockholm"],
            "answer": 'd'
        },
        {
            "question": "What is the capital of Japan?",
            "options": ["Beijing", "Seoul", "Bangkok", "Tokyo"],
            "answer": 'd'
        }
    ]
    
    score = 0
    option_labels = ['a', 'b', 'c', 'd']
    
    # Loop through each question
    for i, q in enumerate(questions):
        print(f"Question{i+1}: {q['question']}")
        for j, option in enumerate(q["options"]):
            print(f"  {option_labels[j]}) {option}")
        
        user_answer = input("Your answer: ").strip().lower()
        
    # Check if each question is correct
        if user_answer == q["answer"]:
            score += 1
            print("Correct! 🌟\n")
        else:
            correct_option = q["options"][option_labels.index(q["answer"])]
            print(f"Incorrect. The correct answer is {correct_option}.\n")
    
    # Scoring
    print(f"You scored {score} out of 10.")
    percentage = (score / 10) * 100
    print(f"Your percentage is {percentage:.2f}%.")

    # Encouragement Message
    if percentage == 100:
        print("Excellent! You got a perfect score!")
    elif percentage >= 80:
        print("Great job! You scored very well.")
    elif percentage >= 50:
        print("Good effort! You passed.")
    else:
        print("Better luck next time. Keep practicing!")
    
if __name__ == "__main__":
    quiz()