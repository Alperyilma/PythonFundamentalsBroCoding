# dictionary -> A changeable, unordered collection of unique key:value pairs
#               Fast because they use hashing, allow us to access a value quickly.

capitals = {"USA":"Washington DC",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"Moscow"}

print(capitals["Russia"]) # Moscow
#print(capitals["Germany"]) #KeyError
print(capitals.get("Germany")) #None
print(capitals.keys()) #dict_keys(['USA', 'India', 'China', 'Russia'])
print(capitals.values()) #dict_values(['Washington DC', 'New Delhi', 'Beijing', 'Moscow'])
print(capitals.items()) #dict_items([('USA', 'Washington DC'), ('India', 'New Delhi'), ('China', 'Beijing'), ('Russia', 'Moscow')])

capitals.update({"Germany":"Berlin"})
capitals.update({"USA":"Las Vegas"}) #It will make overriding and than Washigton DC converts to Las Vegas
#capitals.pop("China") # It helps to delete it

for key,value in capitals.items():
    print(key, value)  # USA Las Vegas
                       # India New Delhi
                       # China Beijing
                       # Russia Moscow
                       # Germany Berlin






