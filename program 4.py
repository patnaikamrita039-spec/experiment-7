
sequence = "Programming"

uppercase = list(map(str.upper, sequence))
lowercase = list(map(str.lower, sequence))


unique_uppercase = list(dict.fromkeys(uppercase))
unique_lowercase = list(dict.fromkeys(lowercase))

print("Uppercase:", unique_uppercase)
print("Lowercase:", unique_lowercase)
