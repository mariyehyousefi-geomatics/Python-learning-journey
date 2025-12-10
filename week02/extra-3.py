station = ("ST-001", 523456.78, 3945678.12, 1285.5)
# (id، X، Y، elevation)
print(station[0])
x=station[1]
y=station[2]
print(f"x={x}, y={y}")

station_list=list(station)
station_list[3]=1290
print(station_list)

