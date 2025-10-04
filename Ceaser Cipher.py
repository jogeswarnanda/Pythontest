alphabet = "abcdefghijklmnopqrstuvwxyz"

def encrypt(text,shift):
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index + shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char
    return result       

def decrypt(text,shift):
    result = ""
    for char in text:
        if char in alphabet:
            index = alphabet.index(char)
            new_index = (index - shift) % len(alphabet)
            result += alphabet[new_index]
        else:
            result += char
    return result


def main():
    should_continue = True
    while should_continue:
        text = input("Enter the text: ")
        shift = int(input("Enter the shift: "))
        function = input("Enter the function: ")
        if function == "encrypt":
            print(encrypt(text,shift))
        elif function == "decrypt":
            print(decrypt(text,shift))
        else:
            print("Invalid function")
        should_continue = input("Do you want to continue? (yes/no): ").lower()
        if should_continue == "no":
            should_continue = False
            print("Goodbye! See you next time.")
        else:
            #print("Invalid input")
            should_continue = True

main()