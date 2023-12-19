import random
import math

#taking bound input
lower = int(input("Enter lower bound - "))
upper = int(input("Enter upper bound - "))

#choosing random number
x = random.randint(lower, upper)

print("You've only", round(math.log(upper - lower + 1, 2)), "chances left to guess!")

#initiliazing the number of guesses
count = 0

while count < math.log(upper - lower + 1, 2):
  count = count  + 1

  #taking guessing number as the input
  guess = int(input("Guess a number - "))

  #condition testing
  if x==guess:
    print("Congratulations, you've guessed the correct number in ", count, " tries.")
    #once guessed right, loop will break
    break

  elif x > guess:
    print("you've guessed too low.")
  elif x < guess:
    print("you've guessed too high.")

if count >= math.log(upper - lower + 1, 2):
  print("The number is %d" % x)
  print("Better luck next time!")

#Another guessing gaming idea is BIASED number guessing game