"""In this project, I will be writing a code that encrypt and decrypts the user's input"""

# Things needed to complete this project:
# functions:
#     the first one is for the main code
#     the second one will be a loop

# I will also walk you through the steps I took

# first we need a list of the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f',
            'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
            'w', 'x', 'y', 'z']

# Now to define the function
def code(user_input, num_shift, position):
    """user_input is for he user message
    num_shift is for the number of time the user wants the code to shift
    position will either encrypt or decrypt."""
    message = ""
    for letter in user_input:
        if letter in alphabet:
            index = alphabet.index(letter)
            if position == "encode":
                new_position = index + num_shift
            else:
                new_position = index - num_shift
            message += alphabet[new_position]
        else:
            message += letter
    print(f"Your {position} text is: {message}")


def main():
    while True:
        user = input("Do you what to encode your message (y/n): ").lower()
        if user == "y":
            message = input("Enter your message: ").lower()
            num_of_shift = int(input("Enter number of shift: "))
            direction = input("Encode or Decode: ").lower()
            code(message, num_of_shift, direction)
        else:
            print("Thank You!")
            break

"""Note, in order for someone to decode your message, 
you must provide them with the number of shifts you used to 
encode the text. Thank you, and enjoy."""
if __name__ == '__main__':
    main()