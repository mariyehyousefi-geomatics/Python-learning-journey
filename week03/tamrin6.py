def process_numbers(*nums):
    if len(nums)==0:
        return None
    return len(nums), sum(nums), sum(nums)/len(nums), max(nums), min(nums)
result= process_numbers(31,18,53,28,42,30)
if result is None:
    print ("there is no mumber to analyze")
else:
    x,y,z,r,s=result
    print (f"count:{x}, total:{y}, average:{z}, maximum:{r}, minimum:{s}")

