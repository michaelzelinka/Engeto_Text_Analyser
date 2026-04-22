TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]

separator = "-" * 40

user_creds = {
  "bob": "123",
  "ann": "pass123",
  "mike": "password123",
  "liz": "pass123"
  }

input_username = input("Username: ")
input_password = input("Password: ")
print(separator)

if input_username not in user_creds:
    print("unregistered user, terminating the program...")
    exit()
elif user_creds[input_username] != input_password:
    print("incorrect password, terminating the program...")
    exit()
else: 
    print(f"Welcome, {input_username}!")

text_count = len(TEXTS)
print(f"Analysing {text_count} texts.")
text_analyse = input(f"Choose number between 1 and {text_count}: ")
try:
    choice = int(text_analyse)
    if choice < 1 or choice > text_count:
        print("Invalid choice, terminating program...")
        exit()
except ValueError: 
    print("Invalid choice, terminating program...")
    exit()

selected_text = TEXTS[choice - 1]

sum_title_w = 0
sum_upp_w = 0 
sum_low_w = 0
sum_num_str = 0 
sum_num = 0
words = selected_text.split()
sum_w = len(words)
graph = {}

for word in words:
    trim_word = word.strip(".,")
    length = len(trim_word)
    graph[length] = graph.get(length, 0) +1
    if trim_word.istitle():
        sum_title_w += 1
    if trim_word.isupper():
        sum_upp_w += 1
    if trim_word.islower():
        sum_low_w += 1
    if trim_word.isnumeric():
        sum_num += int(trim_word)
        sum_num_str += 1

print(separator)
print(f"There are {sum_w} words in the selected text.")
print(f"There are {sum_title_w} titlecase words.")
print(f"There are {sum_upp_w} uppercase words.")
print(f"There are {sum_low_w} lowercase words.")
print(f"There are {sum_num_str} numeric strings.")
print(f"The sum of all the numbers {sum_num}")
print(separator)
print("LEN|          OCCURRENCES|  NR")
print(separator)

for length in sorted(graph):
    count = graph[length]
    print(f"{length}| {'*' * count} |{count}")
