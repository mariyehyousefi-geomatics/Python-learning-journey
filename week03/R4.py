def numbers_info(*nums):
    if len(nums) == 0:
        return 0, 0

    total = sum(nums)
    avg = total / len(nums)
    return total, avg
total,avg=numbers_info(12,11,9,16,20)
print(f"total:{total}, average:{avg}")