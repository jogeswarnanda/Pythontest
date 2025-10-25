with open ("./Inputf/letters/invited_names.txt", "r") as names_file:
    content = names_file.readlines()

for name in content:
    stripped_name = name.strip()
    #print(stripped_name)
    
    with open ("./Inputf/letters/starting_letter.txt", "r") as letter_file:
        letter_content = letter_file.read()
        #print(letter_content)
        
        new_letter = letter_content.replace("[User]", stripped_name)
        #print(new_letter)
        
    with open (f"./Outputf/ReadytoSend/letter_for_{stripped_name}.txt", "w") as send_file:
        send_file.write(new_letter)
