import glob

myfiles = glob.glob("files/*.txt")

for file in myfiles:
    with open(file, 'r') as files:
        print(files.read())
