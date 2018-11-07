def a(list_num):
     list_num[0] +=1
     print(list_num[0])
def a1(b):
    a(b)
    a(b)
def a2(b):
    a1(b)
    a1(b)
def a3(b):
    a2(b)
    a2(b)
x = [0]
a3(x)
print(x)
