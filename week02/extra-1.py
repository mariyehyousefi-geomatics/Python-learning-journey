coordinates = [(523456, 3945678), (523789, 3945123), (524012, 3946234)]
print(coordinates[0])
print(coordinates[-1])
print(coordinates[0:2])
# دسترسی به X و Y اولین نقطه
first_point = coordinates[0]
x = first_point[0]  # یا coordinates[0][0]
y = first_point[1]  # یا coordinates[0][1]
print(f"X= {x},Y= {y}")