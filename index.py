import csv

with open("2025-06-09T0930_Grades-SDF-PT09P4.csv") as SDF_PT09:
    reader = csv.DictReader(SDF_PT09)

    for _ in range(9):
        print(next(reader))
