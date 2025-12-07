def movie_info(title,director,year,country="USA"):
    return f"'{title}' directed by {director}, made in {year}, from {country}."
msg1=movie_info("Inception","Nolan",2010)
print(msg1)
msg2=movie_info("About Elly","Farhadi",2009,"Iran")
print(msg2)
