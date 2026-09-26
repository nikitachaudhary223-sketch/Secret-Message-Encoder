
def encode_message(message, shift):
    result = ""

    for char in message:
        if char.isalpha():
            if char.isupper():
                start = ord('A')
            else:
                start = ord('a')

            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char

    return result


def decode_message(message, shift):
    return encode_message(message, -shift)


def main():
    print("==============================")
    print("  SECRET MESSAGE ENCODER")
    print("==============================")

    while True:
        print("\n1. Encode Message")
        print("2. Decode Message")
        print("3. Exit")

        choice = input("\nEnter your choice: ")

        if choice == "1":
            message = input("Enter your message: ")

            try:
                shift = int(input("Enter shift number: "))

                secret = encode_message(message, shift)

                print("\nOriginal Message:", message)
                print("Encrypted Message:", secret)

            except ValueError:
                print("Please enter a valid number!")

        elif choice == "2":
            message = input("Enter secret message: ")

            try:
                shift = int(input("Enter shift number: "))

                original = decode_message(message, shift)

                print("\nSecret Message:", message)
                print("Decoded Message:", original)

            except ValueError:
                print("Please enter a valid number!")

        elif choice == "3":
            print("\nThank you for using Secret Message Encoder!")
            break

        else:
            print("Invalid choice! Please select 1, 2, or 3.")


main()
