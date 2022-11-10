def compress(original):
    results = ""
    current_run_character = ""
    run_length = 0
    for i in range(len(original)):
        if i == 0:
            current_run_character = original[i]
            run_length = 1
        else:
            current_char = original[i]
            if current_char == current_run_character:
                run_length +=1
            else:
                results += current_run_character +str(run_length)
                current_run_character = current_char
                run_length = 1
    results += current_run_character + str(run_length)
    return results


original_text = input("Enter the text:")
print("Original text:" + original_text)
print("")

print("Compressing...")
compressed_text = compress(original_text)
print("Compressed: " + compressed_text)




