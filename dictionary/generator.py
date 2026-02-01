def generate_dictionary(username, year):
    words = set()

    if username:
        words.add(username.lower())
        words.add(username.capitalize())
        words.add(username.upper())

    if username and year:
        words.add(username + year)
        words.add(username.capitalize() + year)

    return list(words)
