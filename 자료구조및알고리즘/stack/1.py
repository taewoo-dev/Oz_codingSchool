input_question = [
    'How are you today?',
    'Quite well, thank you, how about yourself?',
    'I live at number twenty four.',
    '#'
]

aeiou_dict = {'a': True, 'e': True, 'i': True, 'o': True, 'u': True}
after_u_dict = map(ord,{'v': True, 'w': True, 'x': True, 'y': True, 'z': True})

print(after_u_dict)
for i in after_u_dict:
    print(i)

def aeiou_count(question):
    question = question.lower()
    count = 0

    if question == "#":
        return None

    list(question).sort()

    for letter in question:
        if aeiou_dict.get(letter):
            count += 1

        if after_u_dict.get(letter):
            break

    return count


for question in input_question:
    print(aeiou_count(question=question))