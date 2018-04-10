# Program to test if the project i


text = input("Enter a text: ")
# reverse_text = text[::-1] # shortcut

reverse_text = ''

for c in text:
    reverse_text = c + reverse_text
    # reverse_text = 'a' + ''
    # reverse_text = 'r' + 'a'
    # reverse_text = 'e' + 'ra'
    # reverse_text = 'era'

if text == reverse_text:
    print(text, " is a palindrome")
else:
    print(text, " is not a palindrome")




















