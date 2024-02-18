import json

type_name = input("Enter your type name:")

print("Processando")
try:
    with open("core/artifact/deck/" + type_name + ".json", 'r') as input_f:
        card_data = json.load(input_f)
except Exception as e:
    print(e)

try:
    with open("core/artifact/quill/index-results.json", 'w') as index_output_f:
        for card in card_data:
            index_output_f.write("  {\n")
            index_output_f.write('    "slug": "' + card["slug"] + '",\n')
            index_output_f.write('    "type": "' + type_name + '"\n')
            index_output_f.write("  },\n")

except Exception as e:
    print("open - test_index.json")
    print(e)


print("Finalizado")
