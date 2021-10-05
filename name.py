name="ada lovelace"
print(name.title())

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"Hello, {full_name.title()}!")
message = f"Hello, {full_name.title()}!"
print(message)

full_name = "{} {}".format(first_name, last_name)
print(full_name)

print("Languages:\n\tPython\n\tC\n\tJavaScript")

kbcs =' a b c d e f g '
print(kbcs.rstrip())
print(kbcs.lstrip())
print(kbcs.strip())

#case2-3
name = "eric"
lanuage = "Python"
print(f"Hello {name.title()}, would you like to learn some {lanuage} today?")
#case2-4
first_name = "sun"
last_name = "wu"
print(f"{first_name.upper()} {last_name.upper()}")
print(f"{first_name.lower()} {last_name.lower()}")
print(f"{first_name.title()} {last_name.title()}")
#case2-5
print('Albert Einstein once said,"A people who never made a mistike never tried anything new."')
#case2-6
famous_person = "Albert Einstein"
message = f'{famous_person} once said,"A people who never made a mistike never tried anything new."'
print(message)
#case2-7
name = "\nsun wu  \t"
print(name)
print(name.lstrip())
print(name.rstrip())
print(name.strip())