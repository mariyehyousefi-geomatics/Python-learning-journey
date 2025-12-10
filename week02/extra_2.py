elevations = [1250, 1380, 1156, 1420, 1189, 1505]
avg=sum(elevations)/len(elevations)

high_elevations = []
for elev in elevations:
    if elev > 1300:
        high_elevations.append(elev)

print(f"average= {avg:.2f}")
print(f"elevations higher than 1300: {high_elevations}")
print(f"num of eleves: {len(high_elevations)}")
print(f"min-elevations= {min(elevations)}")
print(f"max_elevations= {max(elevations)}")
print(f"range_elevations={max(elevations)-min(elevations)}")

for elev in elevations:
    print(elev)