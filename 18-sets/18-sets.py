# set -> collection which is unordered, unindexed. No duplicate values.

utensils = {"fork","spoon","knife","knife","knife"} # Even if you put more than one index with same name, It will get
                                                    # only one as the output.

dishes = {"bowl","plate","cup","knife"}
#utensils.add("napkin")
#utensils.remove("fork")
#utensils.clear()
#utensils.update(dishes) # it merges two sets
#dinner_table = utensils.union(dishes) # it merges two sets like update(). But there is a difference.
                                    # if you use a new variable with your two sets, so you have to merge them with union()

#print(utensils.difference(dishes)) #{'fork', 'spoon'}
#print(dishes.difference(utensils)) #{'plate', 'cup', 'bowl'}

print(utensils.intersection(dishes)) #{'knife'} -> Returns same index


for i in utensils:
   print(i)




