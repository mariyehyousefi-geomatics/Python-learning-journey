def show_info(**data):
    print(data)
    for key,value in data.items():
        print(key,"->",value)

show_info(name="Mariyeh", age=42, city="Tehran")
    
