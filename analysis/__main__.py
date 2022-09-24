from views import question_one, question_two, question_three, question_four

selection = input(
    "Hello Bink! Enter '1','2','3' or '4' (followed by the Enter key) to run a question, or just hit the Enter key to run all of them:"
)
if selection == '1':
    question_one()
elif selection == '2':
    question_two()
elif selection == '3':
    question_three()
elif selection == '4':
    question_four()
elif selection == '':
    question_one()
    question_two()
    question_four()
    question_four()
else:
    print("Invalid selection!")
