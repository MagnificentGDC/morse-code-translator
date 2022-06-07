# Imports
import clipboard

# Global variables
translate_to_morse = False

# Running variables
inputs = []
exit = ""
count = 0

# Creates alphabet, numbers, and punctuation objects
class alpha:
    def __init__(self, symbol, code):
        self.symbol = symbol
        self.code = code

class num:
    def __init__(self, symbol, code):
        self.symbol = symbol
        self.code = code

class pun:
    def __init__(self, symbol, code):
        self.symbol = symbol
        self.code = code

# Assigns symbols and morse code to the following classes
alphabet = [
    alpha("a", ".-"),
    alpha("b", "-..."),
    alpha("c", "-.-."),
    alpha("d", "-.."),
    alpha("e", "."),
    alpha("f", "..-."),
    alpha("g", "--."),
    alpha("h", "...."),
    alpha("i", ".."),
    alpha("j", ".---"),
    alpha("k", "-.-"),
    alpha("l", ".-.."),
    alpha("m", "--"),
    alpha("n", "-."),
    alpha("o", "---"),
    alpha("p", ".--."),
    alpha("q", "--.-"),
    alpha("r", ".-."),
    alpha("s", "..."),
    alpha("t", "-"),
    alpha("u", "..-"),
    alpha("v", "...-"),
    alpha("w", ".--"),
    alpha("x", "-..-"),
    alpha("y", "-.--"),
    alpha("z", "--.."),
]

numbers = [
    num("0", "-----"),
    num("1", ".----"),
    num("2", "..---"),
    num("3", "...--"),
    num("4", "....-"),
    num("5", "....."),
    num("6", "-...."),
    num("7", "--..."),
    num("8", "---.."),
    num("9", "----.")
]

punct = [
    pun(".", ".-.-.-"),
    pun("-", "-....-"),
    pun("/", "-..-."),
    pun(" ", "/"),
    pun(",", "--..--"),
    pun("?", "..--.."),
    pun("'", ".----."),
    pun("!", "-.-.--"),
    pun("(", "-.--."),
    pun(")", "-.--.-"),
    pun("&", ".-..."),
    pun(":", "---..."),
    pun(";", "-.-.-."),
    pun("=", "-...-"),
    pun("+", ".-.-."), 
    pun("_", "..--.-"),
    pun('"', ".-..-."),
    pun("$", "...-..-"),
    pun("@", ".--.-."),
    pun("¿", "..-.-"),
    pun("¡", "--...-")
]

# Runs program
while exit != "e":
    # Runs the inputs
    inputs.append(input("Insert [Text / Morse Code] to get Translation:\n\n"))

    # Determines whether program continues or stops
    if inputs[count] == "e" or inputs[count] == "exit":
        exit = "e"
    else:
        # Searches to see if the user wants to translate to morse code or vise versa
        for each in range(len(alphabet)):
            if alphabet[each].symbol in inputs[count]:
                translate_to_morse = True
        for each in range(len(numbers)):
            if numbers[each].symbol in inputs[count]:
                translate_to_morse = True
        for each in range(5, len(punct)):
            if punct[each].symbol in inputs[count]:
                translate_to_morse = True
        
        # Determines whether or not to translate to morse code or vise versa
        if translate_to_morse:
            message = list(inputs[count])
            send_message = ""
            
            for message_symbol in range(len(message)):
                for each in range(len(alphabet)):
                    if alphabet[each].symbol == message[message_symbol] or alphabet[each].symbol.upper() == message[message_symbol]:
                        send_message += alphabet[each].code + " "
                for each in range(len(numbers)):
                    if numbers[each].symbol == message[message_symbol] or numbers[each].symbol.upper() == message[message_symbol]:
                        send_message += numbers[each].code + " "
                for each in range(len(punct)):
                    if punct[each].symbol == message[message_symbol] or punct[each].symbol.upper() == message[message_symbol]:
                        send_message += punct[each].code + " "

            print()
            print(send_message)
            print()
        else:
            message = inputs[count].split(" ")
            send_message = ""
            
            for message_symbol in range(len(message)):
                for each in range(len(alphabet)):
                    if alphabet[each].code == message[message_symbol]:
                        send_message += alphabet[each].symbol
                for each in range(len(numbers)):
                    if numbers[each].code == message[message_symbol]:
                        send_message += numbers[each].symbol
                for each in range(len(punct)):
                    if punct[each].code == message[message_symbol]:
                        send_message += punct[each].symbol

            print()
            print(send_message)
            print()
        
        clipboard.copy(send_message)
        translate_to_morse = False

    count += 1