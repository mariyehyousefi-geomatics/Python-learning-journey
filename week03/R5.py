def first_last(numbers):
    if len(numbers)<2:
        return None, None
    first, *mid, last=numbers
    return first, mid, last
data=first_last([10,20,30,40,50])
print(data)