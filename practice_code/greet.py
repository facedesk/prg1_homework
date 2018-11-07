'''
write a function that creates a simple email message greeting someone.
'''

def message(recipient,sender):
    print("Hello"+recipient+", How are you? What is up?")
    print("-"+sender)
    


student = "Patrick Walmsley"
teacher = "Mr. Gold"

message(student,teacher)
message(teacher,student)

message(teacher,teacher)