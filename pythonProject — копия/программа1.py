slov = {"й": "j", "ц": "c", "у": "u", "к": "k", "е": "e", "н": "n",
         "г": "g", "ш": "sh", "щ": "shh", "з": "z", "х": "h", "ъ": "#",
         "ф": "f", "ы": "y", "в": "v", "а": "a", "п": "p", "р": "r",
         "о": "o", "л": "l", "д": "d", "ж": "zh", "э": "je", "я": "ya",
         "ч": "ch", "с": "s", "м": "m", "и": "i", "т": "t", "ь": "'", "б": "b",
         "ю": "ju", "ё": "jo"}
answer = {}

for elem in slov.keys():
    answer[elem.capitalize()] = slov[elem].capitalize()

a = ['ш', 'ж', 'э', 'ё', 'я', 'ч', 'ю']
A = ['Ш', 'Ж', 'Э', 'Ё', 'Я', 'Ч', 'Ю']

with open("cyrillic.txt", encoding="utf-8") as f, open("transliteration.txt", "w") as f1:
    lines = f.readlines()
    for line in lines:

        line = line.rstrip()
        dlina = len(line)
        counter = 0

        while counter < dlina:

            if line[counter] in slov.keys():
                if line[counter] == 'щ':
                    dlina += 2
                elif line[counter] in a:
                    dlina += 1
                line = line.replace(line[counter], slov[line[counter]])

            elif line[counter] in answer.keys():
                if line[counter] == 'Щ':
                    dlina += 2
                elif line[counter] in A:
                    dlina += 1
                line = line.replace(line[counter], answer[line[counter]])

            counter += 1

        if counter == 1:
            f1.write('\n')

        f1.write(line + '\n')

    f.close()
    f1.close()

