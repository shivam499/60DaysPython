# chosen to be empty

contents = ['Hello', 'Good Bye', 'Good morning']

filenames = ['greet.txt', 'bye.txt', 'morning.txt']

for content, filename in zip(contents, filenames):
    file = open(f"files/{filename}", 'w')
    file.write(content)
