def safe_average(*numbers):
    if len(numbers)<2:
        return "the input must contain at least two numbers."
    return sum(numbers)/len(numbers)
x= safe_average(20)
y= safe_average(10,20,15,18)
print(x)
print(y)
