cities = ["Tehran", "Karaj", "Shiraz", "Mashhad", "Tabriz", "Isfahan", "Yazd"]

del cities[3]
print(cities)

cities.append("Qom")
print(cities)

cities.insert(2,"Rasht")
print(cities)

cities.sort()
print(cities)

print("First3:",cities[0:3])

print("Last2:",cities[-2:])