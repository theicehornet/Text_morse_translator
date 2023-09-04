from logo import logo
import os


def clean_console():
    os.system('cls')


def converter(texto):
    morse_dict = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".", "F": "..-.", "G": "--.", "H": "....", "I": "..",
        "J": ".---", "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---", "P": ".--.", "Q": "--.-", "R": ".-.",
        "S": "...", "T": "-", "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--", "Z": "--..", "1": ".----",
        "2": "..---", "3": "...--", "4": "....-", "5": ".....", "6": "-....", "7": "--...", "8": "---..", "9": "----.",
        "0": "-----"
    }
    final_text = ""
    for letter in texto:
        letter = letter.upper()
        if letter == " ":
            final_text += " / "
        else:
            try:
                final_text += morse_dict[letter] + " "
            except KeyError:
                return f"This key '{letter}' cannot convert to morse"
    return final_text


while True:
    clean_console()
    print(logo)
    print("Welcome!!")
    text = input("Enter a text to converter to a morse code\n")
    print(converter(text))
    option = input("Press enter 0 to finish the program or enter to continue\n")
    if option == "0":
        break
