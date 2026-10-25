"""
RECORD CHECK  -  my version
===========================

Name  : Enrique Goromondo
Lane  : IT      
Date  :25/10/2026
"""

class Record:
    def __init__(self, label, value, limit):
        self.label = label
        self.value = value
        self.limit = limit

def status(self):
        """Return the record status based on its value and limit."""
        percent = (self.value / self.limit) * 100
        if percent >= 100:
            return "OVER LIMIT"
        elif percent >= 90:
            return "WARNING"
        return "OK"

def over_limit_count(self):
    """Return True if the record's value exceeds its limit, otherwise False."""
    return self.value > self.limit



records = [
    Record("srv-01", 87, 120),
    Record("srv-02", 120, 120),
]

over_limit_count = 0

for record in records:
    result = status(record)
    if result == "OVER LIMIT":
        over_limit_count += 1

    print()
    print("=" * 34)
    print(f"  RECORD CHECK - {record.label}")
    print(f"  Used: {record.value} GB")
    print(f"  Total: {record.limit} GB")
    print(f"  Status: {result}")
    print("=" * 34)

print(f"OVER LIMIT records: {over_limit_count}") 


