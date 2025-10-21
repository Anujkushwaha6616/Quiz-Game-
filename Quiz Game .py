# Quiz Game

questions = {
    "1. What is the capital of India?": "b",
    "2. Which language is used for web apps?": "c",
    "3. Who developed Python?": "a",
    "4. What is 5 + 7?": "b",
    "5. What is The capital of Madhaya pradesh?":"a",
    "6. What is the capital of Mharashtra?":"b"
    }

options = [
    ["a) Mumbai", "b) New Delhi", "c) Kolkata"],
    ["a) C++", "b) Java", "c) Python","d) All of the above"],
    ["a) Guido van Rossum", "b) Dennis Ritchie", "c) Narendra Modi"],
    ["a) 10", "b) 12", "c) 15","d) 14"],
    ["a) Bhopal","b) Indore","c) Sagar"],
    ["a) Pune","b) Mumbai","c) Nagpur","d) Thane"]
]

score = 0
for i, (q, ans) in enumerate(questions.items()):
    print("\n" + q)
    for opt in options[i]:
        print(opt)
    user = input("Enter your answer (a/b/c): ").lower()
    if user == ans:
        print("Correct!✅")
        score += 1
    else:
        print("Wrong!❌")
print(f"\nYour Final Score: {score}/{len(questions)}")
print("Thank you for playing the Quize Game ")
