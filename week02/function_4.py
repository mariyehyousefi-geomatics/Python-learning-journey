def book_info(title,author,year):
    return f"'{title}' was written by {author} in year {year}."
message1=book_info("Python Basics","John Smith",2020)
print(message1)
message2=book_info(year=2024,author="Sara Ahmadi",title="GIS with Python")
print(message2)

