#8.String slicing = create a substring by extracting elements from another string
                    # indexing[] or slice()
                    #[start:stop:step]

name = "Bro Code"

first_letter = name[0:1]
first_name = name[0:3]
last_name = name[4:] #[4:end]
funcky_name = name[::2] #BoCd
reversed_name = name[::-1] #edoC orB

print(first_letter)
print(first_name)
print(last_name)
print(funcky_name)
print(reversed_name)

website1 = "http://google.com"
website2 = "http://youtube.com"

slice = slice(7,-4)
print(website1[slice]) #google
print(website2[slice]) #youtube

