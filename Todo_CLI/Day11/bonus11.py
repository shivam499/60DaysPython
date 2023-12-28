def get_average():
    with open('temps.txt', 'r') as file:
        data = file.readlines()[1:]

        values = [float(i) for i in data]

        average = sum(values)/ len(values)

    return average


avg = get_average()
print(avg)
