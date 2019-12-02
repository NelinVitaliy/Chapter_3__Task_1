text = input('Enter the your text here: ')
upper = 0
lower = 0
for i in text:
    if ord(i) >=97 and ord(i) <= 122:
        lower += 1
    elif ord(i) >= 65 and ord(i) <= 90:
            upper += 1

number_in_letter = upper + lower
percent_of_lower = lower / number_in_letter * 100
percent_of_upper = upper / number_in_letter * 100
percent_of_lower = int(percent_of_lower)
percent_of_upper = int(percent_of_upper)
# print(type(percent_of_lower))
print(str(percent_of_lower) + "% lower letters")
print(str(percent_of_upper) + "% upper letters")
