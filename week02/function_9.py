def describe_person(name,**details):
    print(f"Name: {name}")
    for key,value in details.items():
        print(key,":->",value)
describe_person("Mariyeh",Age=42,City="Tehran",Job="Engineer")
