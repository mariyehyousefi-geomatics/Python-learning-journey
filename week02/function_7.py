def analyze_all(*numbers):
    total=sum(numbers)
    max_num=max(*numbers)
    avg=total/len(numbers)
    return total,max_num,avg

x,y,z=analyze_all(3,7,10,20)

print("SUM:",x)
print("MAX:",y)
print("Average:",z)