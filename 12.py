a = 20
def welcome():
   global a
   a = 10
   print(a)

welcome()
print(a)