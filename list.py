students = ["Hermione","Harry","Ron"]
# Above is know as a list as all the names are inside the square bracket.

#we can use a for loop to print out the name in a ordered manner
for student in students:
    print(student)

#we also use the range of the list by using 'len' as for length of the list.
for i in range(len(students)):
    print(i+1,students[i])
