# this app is good for highlighting the use of CLASSES , OBJECTS, LISTS in real world scenarios

# Logic behind this app
# 1) group the questions in a list. List is good for groupings
# 2) define what is a question. It has 2 components, prompt and answer
# 3) define another group listing with the correct answers
# 4) define a loop through function to accummulate tally


#Create a list with 3 questions. Good for groupings. Anything you can group, put it in a list
question_prompts=[
    "What colour are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n" ,
    "What colour are bananas?\n(a) Yellow\n(b) Purple\n(c) Orange\n\n",
    "What colour are strawberrees?\n(a) Red/Green\n(b) Purple\n(c) red\n\n"
]

class Question:
    # question has 2 components
    def __init__(self, prompt, answer):
        self.prompt=prompt
        self.answer=answer


# almost like a key value scenario, group the question with the right answer
questions=[
    # this is the first question object and pass the 1st list item plus the real answer. Build the answer list
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "a"),
    Question(question_prompts[2], "c")
]

# now a function to run the test

# first parameter takes a list of questions
def run_test(questions):
    score=0

    for question in questions:
        answer=input(question.prompt)

        #now check if user got question right
        if answer==question.answer:
            #increment if correct
            score+=1

    print("You got " + str(score) + "/" + str(len(questions)) + " correct")


# now run the program passing the questions list


run_test(questions)





