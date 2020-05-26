import random

name = input("Please enter your name: ")
qtns = int(input("How many questions do you want to attempt? "))
d = int(input("Please indicate the degree of difficulty from 1 to 5: "))

count = 0 #stores the number of times the answer is correct

#looping through the number of attemps providing 1 question at a time
for attempts in range(qtns):
  num1 = random.randint(d, d*100)
  num2 = random.randint(d, d*100)
  answer = num1 + num2 #storing the correct value

  print('Question ', attempts + 1)
  userAnswer = int(input(str(num1) + " + " + str(num2) + " = ? Type your answer here: "))

  #checking for the correct answer then incrementing the count!
  if userAnswer == answer:
    count = count + 1
    print("Correct")
  else:
    print("Incorrect")

#final message
print("Hello "+name+ ", You solved "+str(count)+ " out of "+str(qtns)+ " questions!")

    
  



