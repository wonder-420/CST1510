"""
RECORD CHECK  -  my version
===========================

Name  : Enrique Goromondo
Lane  : IT      
Date  : 08/10/2026
"""

def status_of(percent, warning_at=90):
    """returns a keyword when percent is at a certain threshhold"""
    if percent > 100:
        return("OVER LIMIT")

    elif percent >= warning_at:
        return("WARNING")
    else:
        return("OK")

def check(value, limit):
    """returning difference and percentage as 2 different values"""
    difference = value - limit
    percent =(value/limit)*100
    return difference, percent

def print_report(label, value, limit, difference,percent, status):
     print(f"{label:<15}\n value={value:<15.2f}\n limit={limit:<15.2f}\n "
          f"difference={difference:<+15.2f}\n percent={percent:<15.2f}%\n status={status:<15}\n")


label = input(" What is your name? : ")      
value = float(input("Enter the number used : "))     
limit = float(input("Enter the total:"))

difference, percent = check(value,limit)
status = status_of(value,limit)

record = (print_report)
print()
print("=" * 34)
print(f"  RECORD CHECK  -  {label}")
print("=" * 34)

print_report(label, value, limit, difference, percent, status)

print("=" * 34)

