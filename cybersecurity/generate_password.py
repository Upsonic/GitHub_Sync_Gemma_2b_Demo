def generate_password(length=10, include_punctuation=True, include_digits=True, include_uppercase=True):
    characters = string.ascii_lowercase

    if include_punctuation:
        characters += string.punctuation

    if include_digits:
        characters += string.digits

    if include_uppercase:
        characters += string.ascii_uppercase

    first = ''.join((random.choice(characters) for i in range(length)))


    return 
