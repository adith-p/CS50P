import emoji

# prompts the user for a str in English

user_input = input("Input: ")


#  and then outputs the “emojized” version of that str, converting any codes (or aliases) therein to their corresponding emoji.
print(emoji.emojize(user_input))
