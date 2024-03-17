import json

type_name = input("Enter deck name:")

print("Processando")
try:
    with open("core/artifact/deck/" + type_name + ".json", 'r') as input_f:
        card_data = json.load(input_f)
except Exception as e:
    print("open - index.json")
    print(e)

seen = []
double_list = []
for card in card_data:
    if card['slug'] in seen:
        double_list.append(card['slug'])
    else:
        seen.append(card['slug'])

if not double_list:
    print("There are no duplicates.")
else:
    counted = []
    for slug in double_list:
        if slug not in counted:
            counted.append(slug)
            print(str(double_list.count(slug) + 1) + " - " + slug)

print("Finalizado")
