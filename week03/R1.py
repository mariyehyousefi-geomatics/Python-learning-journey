def analyze_numbers(numbers):
    return sum(numbers), max(numbers), len(numbers)
x,y,z=analyze_numbers([8,2,3,5,12])
print(x,y,z)

#unpacked out put below
print(x)
print(y)
print(z)

"خروجی با دستور f string"
print(f"total:{x}, maxnumber:{y}, countnumbers:{z}")