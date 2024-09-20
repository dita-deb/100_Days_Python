# Random Module
import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

#print(my_module.my_favorite_number)   #this is how you'd call a module into the main file
random_number_0_to_1 = random.random() * 10
print(random_number_0_to_1)

random_float = random.uniform(1, 10)
print(random_float)

random_heads_or_tails = random.randint(0, 1)
if random_heads_or_tails == 0:
    print("Heads")
else:
    print("Tails")

# Lists
#Creating a list and printing it
fruits = ["Cherry", "Apple", "Pear"]
print(fruits)

#Accessing items in a list
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
print(states_of_america[0]) #index starts at 0

#can alter items in list using this syntax
states_of_america[1]= "Pencilvania"
print(states_of_america)

#can add to the list
states_of_america.append("Angelaland")
print(states_of_america)

#extending the list it's different in that it can be iterable 
states_of_america.extend(["LaLaLand","Wonderland"])
print(states_of_america)

#Negative Indices
print(fruits[-1]) #this will be "Pear"  #roll over of the list from 0 to -1 as the last item in list

# Banker Roulette
import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]

#Option 1
print(random.choice(friends))       #picks a random item from the list

#Option 2
random_index = random.randint(0,4)      #picks a random integer from 0 - 4 including 0 and 4
print(friends[random_index])                  #prints the friend associated with the randomly chosen integer

# IndexError
states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]

# print(states_of_america[50]) # will result in a huge error in that the list index is our of range of the value we are trying to pull from

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinnach"]
fruits_and_veg = [fruits, veg]
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinnach"]]
print(fruits_and_veg)
