# Cipher python assignment Dylan Lade

cipher = {
    "a" : "0",
    "b" : "1",
    "c" : "2",
    "d" : "3",
    "e" : "4",
    "f" : "5",
    "g" : "6",
    "h" : "7",
    "i" : "8",
    "j" : "9",
    "k" : "!",
    "l" : "@",
    "m" : "#",
    "n" : "$",
    "o" : "%",
    "p" : "^",
    "q" : "&",
    "r" : "*",
    "s" : "(",
    "t" : ")",
    "u" : "-",
    "v" : "+",
    "w" : "<",
    "x" : ">",
    "y" : "?",
    "z" : "="
}

# Invert the cipher object for decoding
inv_cipher = {v: k for k, v in cipher.items()}


def getString(choice): # Pull input based off the choice provided
    while(1):
        if(choice == 1):
            string = input("Enter a message to encode: ")
            return string
        if(choice == 2):
            string = input("Enter a message to decode: ")
            return string
        if(choice == 3):
            exit(0)
        else:
            print("Please choose and option from the table!")

def encodeString(string): # Make a translation table from the dictionary
    table = string.maketrans(cipher)
    encode = string.translate(table)

    return encode

def decodeString(string): # Make the inverted translation table 
    reverse = string.maketrans(inv_cipher)
    decode = string.translate(reverse)

    return decode

def main():
    while(1):
        print("\nWelcome to the Secret Message Encoder/Decoder")
        print("1.Encode a message")
        print("2.Decode a message")
        print("3.Exit\n")
        
        choosing = True 
        while(choosing):
            try:
                choice = int(input("What would you like to do? "))
                if(choice in range(1,4)):
                    choosing = False
                    break
                print(str(choice) + " is not a valid choice")
                choosing = True
            except ValueError:
                print("Please enter a number between 1 and 3.")
                choosing = True
            
        message = getString(choice)

        if(choice):
            message = encodeString(message)
        if(choice == 2):
            message = decodeString(message)

        print("\nEncoded message: " + message + "\n")

if __name__ == "__main__":
    main()