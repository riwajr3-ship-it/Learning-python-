#this is to define a new function

def hello(to):
    print("Hello i am,", to , "and i coded this")

name = input("What is your name? ")
hello(name.strip().title())


#one more new function
def main():
    x=int(input ("what is the number?"))
    print(f"the square of the number is , {exp(x): ,}") 

def exp(n):
    return n * n


main()