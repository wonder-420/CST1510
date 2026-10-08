"""
RECORD CHECK  -  my version
===========================

Name  :Enrique Goromondo
Lane  : IT     
Date  :25/09/2026
""" 


label = input(" What is your name? : ")      
first = float(input("Enter the number used : "))     
second = float(input("Enter the total:"))    

difference = second - first   
percent = ((first / second) * 100)       


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Used: {first:>20.2f}")
print(f"Total: {second:>20.2f}")
print(f"Free: {difference:>+20.2f}")
print(f"Percentage: {percent:>20.2f} % ")
print(f"{"Congratulations! You have completed your check!.":>20}")

print("=" * 34)

