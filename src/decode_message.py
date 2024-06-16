def decode(message_file):
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    # Create a dictionary to map numbers to words
    number_to_word = {}
    for line in lines:
        number, word = line.split()
        number_to_word[int(number)] = word
    
    # Print the dictionary for debugging
    print("Number to Word Mapping:")
    print(number_to_word)
    
    # Determine the pyramid structure and collect the ending numbers
    index = 1
    current_sum = 0
    line_endings = []
    while current_sum + index <= len(number_to_word):
        current_sum += index
        line_endings.append(current_sum)
        index += 1
    
    # Print the line endings for debugging
    print("Line Endings:")
    print(line_endings)
    
    # Collect words corresponding to the line endings
    message_words = [number_to_word[i] for i in line_endings if i in number_to_word]
    
    # Join the words into a single string separated by spaces
    decoded_message = ' '.join(message_words)
    
    return decoded_message

# Decoding the message from the file
decoded_message = decode("coding_qual_input.txt")
print(decoded_message)
