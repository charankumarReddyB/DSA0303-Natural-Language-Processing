def pluralize(word):

    if word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"

    elif word.endswith("y") and len(word) > 1 and word[-2].lower() not in "aeiou":
        return word[:-1] + "ies"

    elif word.endswith("f"):
        return word[:-1] + "ves"

    elif word.endswith("fe"):
        return word[:-2] + "ves"

    else:
        return word + "s"


word = input("Enter a singular noun: ")

print("Plural:", pluralize(word))