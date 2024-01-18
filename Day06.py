def count_vowels(s):
    vowels = "aeiouAEIOU"
    vowel_count = 0

    for char in s:
        if char in vowels:
            vowel_count += 1

    return vowel_count

input_string = "Hello World"
result = count_vowels(input_string)
print(f"The number of vowels in '{input_string}' is: {result}")
