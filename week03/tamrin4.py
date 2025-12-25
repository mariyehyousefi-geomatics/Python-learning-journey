def numbers(*num):
    if len(num)<2:
        return None
    return min(num), sum(num)/len(num), max(num), len(num)
result= numbers(84,93,52,80,79,64)
if result is None:
    print("Not enough numbers")
else:
    x, y, z, r = result
    print(f"minimum:{x}, average:{y}, maximum={z}, count:{r}")
