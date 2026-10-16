"""
RECORD CHECK  -  my version
===========================

Name  :Enrique Goromondo
Lane  :IT      
Date  :16/10/2026
"""
def check(value, limit):
    """returning difference and percentage as 2 different values"""
    difference = value - limit
    percent =(value/limit)*100
    return difference, percent

def status_of(percent, warning_at=90):
    """returns a keyword when percent is at a certain threshhold"""
    if percent > 100:
        return("OVER LIMIT")

    elif percent >= warning_at:
        return("WARNING")
    else:
        return("OK")


def print_report(label, value, limit, status):
    """Prints all inputed values and calculations"""
    print(f"{label:<15}\n value={value:<15.2f}\n limit={limit:<15.2f}\n  status={status:<15}\n")

def load_records(path):
    """Read label,value and limit from a file and return a list of dicts."""
    records = []
    path = "LAB/file.txt"
    with open(path) as f:
        for line in f:
            label, value, limit = line.strip().split(",")
            records.append({"label": label, "value": float(value), "limit": float(limit)})
            return(records)

with open("LAB/file.txt") as f:
    """attempting to return a value"""
    text = f.read()
records = ["LAB/file.txt"]
line = "R-001,6,100"
label, value, limit = line.split(",")
value = float(value)
limit = float(limit)
status = status_of(value, limit)

for record in records:
    check(value,limit)
    print_report(label, value, limit, status)

