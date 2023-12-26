# Mutability

filenames = ["1.Raw Data.txt", "2.Report.txt", "3.Presentation.txt"]

for item in filenames:
    item = item.replace('.', '-', 1)
    print(item)
