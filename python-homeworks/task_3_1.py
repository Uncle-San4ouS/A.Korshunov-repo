
tr_dict = {"zero": "нуль", "one": "один", "three": "три",
           "four": "четыре", "five": "пять", "six": "шесть",
           "seven": "семь", "eight": "восемь", "nine": "девять", "ten": "десять"}

def num_translate(word):
    in_word = word.lower()
    if word.istitle() and in_word in tr_dict:
        return tr_dict.get(in_word).title()
    return tr_dict.get(word)

print(num_translate(input("Enter number: ")))
