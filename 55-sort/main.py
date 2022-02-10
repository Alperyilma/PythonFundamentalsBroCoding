# sort() method -> used with lists
# sort() method -> used with iterables

students = ["Squidward","Sandy","Patrick","Spongebob","Mr.Krabs"]

students.sort()

for i in students:
    print(i, end=" ") # Mr.Krabs Patrick Sandy Spongebob Squidward

print()
students.sort(reverse=True)

for i in students:
    print(i, end=" ") # Squidward Spongebob Sandy Patrick Mr.Krabs

print()

#--------------------------
# Sort it with tuple
students_tuple = ("Squidward","Sandy","Patrick","Spongebob","Mr.Krabs")

sorted_students = sorted(students_tuple, reverse=True)
for i in sorted_students:
    print(i, end=" ") #Squidward Spongebob Sandy Patrick Mr.Krabs

#--------------------------
# We will sort by indexes, I use tuple for different indexes.
students_list_tuple = [("Squidward", "F", 60),
                       ("Sandy", "A", 33),
                       ("Patrick", "D", 36),
                       ("Spongebob", "B", 20),
                       ("Mr.Krabs", "C", 78)]

age = lambda age: age[2]

students_list_tuple.sort(key=age, reverse=True)

for i in students_list_tuple:
    print(i) #('Squidward', 'F', 60)
             #('Patrick', 'D', 36)
             #('Sandy', 'A', 33)
             #('Spongebob', 'B', 20)

