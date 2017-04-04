import random

def roll():
   random_num = random.randrange(1,7)
   cond = True
   while (cond):
      print random_num
      random_num = random.randrange(1,7)

      ask = raw_input("Do you want to roll again ? : Yes or No : ")

      if ask == "Yes":
         cond = True
      else:
         cond = False

roll()
