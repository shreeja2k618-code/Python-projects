def greet():
    print("welcome")
greet()

def greeting(message):
    print(message)
greeting("Welcome")

def calc(a,b):
    
    return a+b,a*b
total,product=calc(10,20)
print(total)
print(calc(5,10))

def greeting(name="guest"):
    print("welcome",name)
greeting("Shreeja")
greeting()