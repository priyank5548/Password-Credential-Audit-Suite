def leet_mutations(word):
    return [
        word.replace("a", "@"),
        word.replace("e", "3"),
        word.replace("i", "1"),
        word.replace("o", "0")
    ]
