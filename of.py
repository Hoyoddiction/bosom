first_word = input('First Word: ')
second_word = input('Second word: ')

link = ""

for i in range(1, min(len(first_word), len(second_word)) + 1):
    if first_word[-i:] == second_word[:i]:
        link = first_word[-i:]

if link:
    print("Length of the first word",len(first_word))
    print(first_word)
    print("Length of the second word",len(second_word))
    print(second_word)
    print("both word can be connected with", str(link))
else:
    print("Length of the first word",len(first_word))
    print(first_word)
    print("Length of the second word",len(second_word))
    print(second_word)
    print("Both words cannot be linked")
