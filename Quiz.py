import time
quiz = {
    "question1":{
        "question"  :  "What is the capital of England: ",
        "answer"    :   "London",
    },
    "question2":{
        "question"  :   "What is the capital of Germany: ",
        "answer"    :   "Berlin",
    },
    "question3": {
        "question"  : "What is the capital of Spain: ",
        "answer"    :  "Madrid"
    },
    "question4": {
            "question"  : "What is the capital of Italy: ",
            "answer"    :  "Rome"
        },
    "question5": {
            "question"  : "What is the capital of Portugal: ",
            "answer"    :  "Lisbon"
        },
    "question6": {
            "question"  : "What is the capital of Scotland: ",
            "answer"    :  "Edinburgh"
        },
    "question7": {
            "question"  : "What is the capital of Wales: ",
            "answer"    :  "Cardiff"
        },
    "question8": {
            "question"  : "What is the capital of Norway: ",
            "answer"    :  "Oslo"
        },
    "question9": {
            "question"  : "What is the capital of Turkey: ",
            "answer"    :  "Ankara"
        },
    "question10": {
            "question"  : "What is the capital of Switzerland: ",
            "answer"    :  "Latvia"
        }
}
score = 0

for key, value in quiz.items():
    print("")
    print(value["question"])
    ans = input("Answer: ").lower()

    if ans.lower() == value["answer"].lower():
        print("Correct")
        score = score + 1
        print(f'your score is : {score}')
        print("\n")
    else:
        print("Wrong")
        print((f'The correct answer is : {value["answer"]}'))
        print(f'your score is {score}')
        print("\n")
time.sleep(1)
print(f"Your final score is {score}/6")
print(f"Your percentage is {(score/6 * 100)}")
time.sleep(4)




