#This is just a practise for psuedocode and varible,output and input and bit of methods of string too.
#Remove the whitespace and Capitalizing
name = input('Enter your name').strip().title()
#spilting the strings
first,last = name.split()

print('Hello and welcome', name)
print('Hello, '+ first)
print('Hello,', end='')
print(name)

#formate string method
print(f"Hello, {first}")
# NOTES 
#we have given an input and stored it in the variable of "name", variable is storage to store a value to return the value in the output
#As we can see there are different ways to get the similar outputs 
#Here a problem occurs when we give the input and have too much spacing of the letter in not capital then the varible or input takes it as it is and does not fix it 
#therefore we use the string function to fix it here we used variable.strip() for the spacing problem and we can use .capitalize or.title make the first alphabet of user's name capitalize
#We can shorten the code by giving method to the varible directly.