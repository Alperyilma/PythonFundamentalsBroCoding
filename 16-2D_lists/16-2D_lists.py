# 2D lists -> a list of list

drinks = ["coffee","soda","tea"]
dinner = ["pizza","hamburger","hotdog"]
dessert = ["cake","ice cream"]

food = [drinks,dinner,dessert]

print(food) #[['coffee', 'soda', 'tea'], ['pizza', 'hamburger', 'hotdog'], ['cake', 'ice cream']]
print(food[0]) #['coffee', 'soda', 'tea']
print(food[0][0]) #coffee
print(food[0][1]) #soda
#print(food[2][2]) #IndexError
