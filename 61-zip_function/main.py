# zip(*iterables) -> aggregate elements from two or more iterables (list, tuples, sets, etc.)
#                    creates a zip object with paired elements stored in tuples for each element

usernames = ["Dude", "Bro", "Mister"]
passwords = ("p@ssword", "abc123", 12345)
login_date = ["1/1/2021", "1/2/2021", "1/3/2021"]

users = dict(zip(usernames, passwords))  # You can convert it by list, dict(dictionary) or set.
                                         # You can write it what type you want
print(type(users)) #<class 'zip'>

for key,value in users.items():
    print(key,":",value) # Dude : p@ssword
                         # Bro : abc123
                         # Mister : 12345


date_of_users = list(zip(usernames,passwords,login_date))

for i in date_of_users:
    print(i)  #('Dude', 'p@ssword', '1/1/2021')
              #('Bro', 'abc123', '1/2/2021')
              #('Mister', 12345, '1/3/2021')

