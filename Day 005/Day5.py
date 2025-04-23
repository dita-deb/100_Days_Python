# For Loops with Python Lists
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)            #steping through the code with just this prints Apple in the first iteration
    print(fruit + " pie")   #adds pie to the item in the list for each iteration till the loop is finished

print(fruits)               #prints only after the end of the loop

# Highest Score
student_scores = [150, 142, 185, 120, 171, 184, 149, 24, 59, 68, 199, 78, 65, 89, 86, 55, 91, 64, 89]
print(range(1, 10))

#Option 1
total_exam_score = sum(student_scores)      #sum function
print(total_exam_score)

#Option 2
sum = 0                                     #initialize sum
for score in student_scores:                #loop through items in student_scores
    sum += score                            #sum values of all items in student_scores
print(sum)                                  #print sum after loop ends

#Max Score Function
print(max(student_scores))

#Check Max Score with For Loop
max_score = 0                               #initalize max_score as 0
for score in student_scores:                #iterate through list
    if score > max_score:                   #if score is greater than current max_score
        max_score = score                   #replace max_score with score (otherwise no change)
print(max_score)

# For Loops with Range
for number in range(1,10):    #numbers 1-10 not including 10
    print(number)

for number in range(1,11,3):  #numbers 1-11 not including 11 #step 3 means print every 3 numbers til the end
    print(number)             # will print 1,4,7,10

#Gauss challenge
total = 0
for number in range(1, 101):
    total += number
print(total)

# FizzBuzz Challenge
def fizzbuzz():
    for i in range(1, 101):  # Loop from 1 to 100
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
fizzbuzz()

