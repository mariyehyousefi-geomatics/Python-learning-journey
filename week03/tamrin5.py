def user_info(*scores, **intro):
    total = sum(scores)
    avg = total / len(scores)
    return total, avg, intro
total, average, info = user_info(
    20, 15, 30, 10, 25,
    name="Mariyeh",
    age=42,
    city="Tehran"
)

print("average:", average)
print("total:", total)

print("user info")
for k, v in info.items():
    print(f"{k}: {v}")