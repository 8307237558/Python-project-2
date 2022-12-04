import random
lowerBound=int(input("Enter Lower Bound:"))
upperBound=int(input("Enter Upper Bound:"))
a=random.randrange(lowerBound,upperBound)
i = 0
while i >=0:
  num=int(input("Enter for your chance: "))
  if(num>a):
    print("have one more try")
  elif(num<a):
    print("have one more try")
  else:
    print("congrats You had won the contest your winning score is"+str(a))
    break
  i += 1
  if(i%3==0):
    print("Better Luck Next Time!")