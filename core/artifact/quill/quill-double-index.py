import json

print("Processando")
try:
    with open("core/artifact/deck/index.json", 'r') as input_f:
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

print(double_list)

print("Finalizado")
