from pip.backwardcompat import raw_input

Quiz = [
    {"q": "Which of these is not a fruit?",
     "answers": ['Banana', 'Strawberry', 'Tomato', 'Apple'],
     "correct": 'Strawberry'
    },
    {"q": "Is Portland Weird?",
     "answers": ['Yes', 'No'],
     "correct": 'Yes'
    }
]

for question in Quiz:

    print(question["q"])

    for answer in question["answers"]:
        print(answer)

    ans = raw_input('case sensitive> ')

    if ans == question["correct"]:
        print("correct")
    else:
        print("incorrect")