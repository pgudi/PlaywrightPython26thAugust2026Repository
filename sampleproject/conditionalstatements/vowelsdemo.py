character="E"

match character:
    case "A" | "E" | "I" | "O" | "U":
        print(character," is a Vowel")
    case _:
        print("It is not a Vowel")
    