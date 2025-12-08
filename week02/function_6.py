def analyze_numbers(a, b, c):
    max_value=max(a,b,c)
    sum=a+b+c
    mean=sum/3
    return max_value, sum, mean
x, y, z = analyze_numbers(3, 10, 7)
Results=(x,y,z)

print(Results)