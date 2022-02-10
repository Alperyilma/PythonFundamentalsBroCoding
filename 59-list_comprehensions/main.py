# list comprehension -> a way create a new list with less syntax
#                       can mimic certain lambda functions, easier to read
#                       list = [expression for item in iterable]
#                       list = [expression for item in iterable if conditional]
#                       list = [expression if/else for item in iterable]

students = [100,90,80,70,60,50,40,30,0]

# passed_students = list(filter(lambda x: x>=60, students))

#Best way
passed_students = [i for i in students]
print(passed_students) #[100, 90, 80, 70, 60, 50, 40, 30, 0]

passed_students_2 = [i for i in students if i >= 60]
print(passed_students_2) #[100, 90, 80, 70, 60]

passed_students_3 = [i if i >= 60 else "Failed" for i in students]
print(passed_students_3) #[100, 90, 80, 70, 60, 'Failed', 'Failed', 'Failed', 'Failed']


