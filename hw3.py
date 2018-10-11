# The goal of this homework assignment is to flex your lists, strings, and string manipulation skills we are learning in class
# Avoid writing any loops (aside from the one I have provided for you).

print('''
Welcome to Saint John's Northwestern Military Academy!
This is your Academic Planner Program that will help you keep your assignments in line

''')

homework_to_do=[]
homework_due_dates=[]

tests_quizzes=[]
tests_quiz_dates=[]

while(True):
    '''
    problem 1)
    '''
    print('''enter an option
    1) Add homework
    2) Add Quiz/Test
    3) Display all homeworks, quizzes and tests
    ''')
    
    choice = int(input("?"))
    if(choice == 1):
        print("Adding homework")
        homework = input("What is your homework?")
        homework_to_do.append(homework)
        due_date = input("When is your homework due?")
        homework_due_dates.append(due_date)
    elif(choice == 2):
        print("Adding Quizzes/Test")
        quiz = input("What is your Quiz/Test?")
        tests_quizzes.append(quiz)
        due_date = input("When is your Quiz/Test?")
        tests_quiz_dates.append(due_date)
    elif(choice == 3):
        print("Displaying all homeworks, quizzes and tests")
        print("your homework is as follows")
        print(homework_to_do)
        print(homework_due_dates)
        print("your quizzes are as follows")
        print(tests_quizzes)
        print(tests_quiz_dates)
    else:
        print("Invalid option, please try again")



