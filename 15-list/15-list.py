# list -> used to store multiple items in a single variable

food = ["pizza","hamburger","hotdog","spaghetti","pudding"]

print(food[0]) #pizza
print(food[1]) #hamburger
print(food[2]) #hotdog
#print(food[6]) #indexError

food[0] = "sushi"
print(food[0]) #sushi

#food.append("ice cream")
#food.remove("hotdog")
#food.pop() # it removes last index
#food.insert(0,"cake") #it will convert index which you choose. Converts sushi to cake
#food.sort()
#food.clear()


print("*************")

for i in food:
    print(i)





