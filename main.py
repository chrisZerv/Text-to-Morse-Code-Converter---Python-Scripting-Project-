# Morse Code Dictionary
MORSE_CODE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
    'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
    'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.', ', ': '--..--', '.': '.-.-.-',
    '?': '..--..', '/': '-..-.', '-': '-....-', '(': '-.--.', ')': '-.--.-', '&': '.-...',
    ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '!': '-.-.--', '@': '.--.-.', ' ': '/'
}

def string_to_morse(input_string):
    # Convert the input string to uppercase
    input_string = input_string.upper()

    # Initialize an empty string for the Morse code output
    morse_code_output = ""

    # Convert each character in the input string to Morse code
    for char in input_string:
        if char in MORSE_CODE_DICT:
            morse_code_output += MORSE_CODE_DICT[char] + " "
        else:
            morse_code_output += "? "  # Use ? for unknown characters

    return morse_code_output.strip()

if __name__ == "__main__":
    # Take input from the user
    user_input = input("Enter a string to convert to Morse Code: ")

    # Convert the string to Morse code
    morse_code = string_to_morse(user_input)

    # Print the Morse code
    print(f"Morse Code: {morse_code}")
