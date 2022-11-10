def encode(message):
    encoded_message = ""
    symbol_message = ""
#shows that variable encoded_message is string
    i = 0
#we are defining i as strart index
    while (i <= len(message) - 1):
#if i is less or equal to message length count should be pointed as 1 and
#char should be i [index] of the message and
#j should be equal to i
        count = 1
        char = message[i_of_external]
        j = i
        while (j < len(message) - 1):
#as long as j is less then massage length -1
#and if the character in j [index] is the same with character in j+1 index
#count increases by 1
            if (message[j] == message[j + 1]):
            count = count + 1
            j = j + 1
            else:
                break
#if the character j [index] is not equal to j+1 [index] we break this cycle
        encoded_message = encoded_message + str(count) + char
#after the cycle breaks we add this massage to encoded massage and add number of counts and character
# know we increase i [index] so, know we will work other characters in the text
#i now will be equal to j+1 which will be another character
#we will repeat the process for all characters untill i will be higher than length of the message
        i = j + 1
    return encoded_message


encoded_my = encode("ABBBBCCCCCCCCAB")
print(encoded_my)
#I failed to add * into my code I am gonna try again