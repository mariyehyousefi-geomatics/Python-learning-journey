numbers=[10,20,40,60]
numbers.append(80)
numbers.insert(1,25)
numbers.remove(40)
last_item=numbers.pop()
print("deleted item:",last_item)
del numbers[0]
numbers.sort()
numbers.reverse()
print(numbers)
print("length of the list:",len(numbers))

if 60 in numbers:
    print("60 exsists in numbers")



