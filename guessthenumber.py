import random
userin = int(input("what number should it be between? "))
number = int(random.random() * userin)
iscorrect= 0
while iscorrect == 0:
  guess = int(input("what is your guess? "))
  if guess < number:
    print("your guess is lower then the number")  
  elif guess > number:
    print("your guess is higher then the number")
  elif guess == number:
    print("your guess is correct!")
    iscorrect = 1