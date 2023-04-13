mystr=input()
dict = {}
for letter in mystr:
    if letter in dict:
        dict[letter] += 1
    else:
        dict[letter]==1
print(dict)


