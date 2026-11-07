"""
RECORD CHECK  -  my version
===========================

Name  : Enrique Goromondo
Lane  : IT      
Date  :07/11/2026
"""

def parse_line(raw_line):
    """Clean and parse one status record."""
    line = raw_line.strip()
    hostname_part, rest = line.split(",", 1)
    record = {"hostname": hostname_part.strip().lower()}

    for piece in rest.split(","):
        key, value = piece.split("=", 1)
        record[key.strip().lower()] = float(value.strip())

    return record

def status_of(record):
    """Return the usage status for the record."""
    percentage = record["used"] / record["total"] * 100
    if percentage >= 100:
        return "OVER LIMIT"
    if percentage >= 90:
        return "WARNING"
    return "OK"


raw_records = [
    "  Srv-01 , used=87 , total=100  ",
    "SRV-02,USED=105,TOTAL=100",
    "  sRv-03, used = 42, TOTAL = 80 ",
    "Srv-04 , USED=  ninety , total=100",
    "  SRV-05,used=90,total=100  ",
]
flagged = 0

for raw_record in raw_records:
    try:
        record = parse_line(raw_record)
        status = status_of(record)
        print(record, status)
        if status != "OK":
            flagged += 1
    except ValueError:
        print("Could not parse:", raw_record)

print(f"Records: {len(raw_records)}, flagged: {flagged}")



