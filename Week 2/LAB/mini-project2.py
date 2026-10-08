"""
RECORD CHECK  -  my version
===========================

Name  : Enrique Goromondo
Lane  : IT      (delete two)
Date  :
04/10/2026
"""

label = input("Enter your name: ")
value = float(input("Enter number used: "))
limit = float(input("Enter the limit: "))

difference = limit - value   
percent = (value/limit)*100


if percent >= 90:
        status = print("WARNING!")

elif percent < 95:
        status = print("OK")   
elif percent > 100:
        status = print("OVER LIMIT")


print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print(f"Used: {value:>20.2f}")
print(f"Total: {limit:>20.2f}")
print(f"Free: {difference:>+20.2f}")
print(f"Percentage: {percent:>20.2f} % ")
print(f"{"Congratulations! You have completed your check!.":>20}")

print("=" * 34)
