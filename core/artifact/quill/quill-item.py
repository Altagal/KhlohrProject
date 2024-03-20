import json
import re

from django.utils.text import slugify

print("Processando")
try:
    with open("core/artifact/5e-database-main/5e-SRD-Equipment.json", 'r') as input_f:
        card_data = json.load(input_f)
except Exception as e:
    print("Erro")
    print("open - 5e-SRD-Equipment.json")
    print(e)

try:
    with open("core/artifact/quill/item-results.json", 'w') as index_output_f:
        index_output_f.write('[\n')

        for equip in card_data:
            try:
                index_output_f.write('{')
                index_output_f.write('"slug":"' + slugify(equip["name"]) + '",\n')
                index_output_f.write('"name":"' + equip["name"] + '",\n')
                index_output_f.write('"type": {"slug": "item","name": "Item"},\n')
                index_output_f.write('"desc": "<p></p>",\n')
                index_output_f.write('"cost": {"quantity": ' + str(equip["cost"]["quantity"]) + ',"unit": "' + equip["cost"]["unit"] + '"},\n')
                try:
                    index_output_f.write('"weight":' + str(equip["weight"]) + ',\n')
                except:
                    index_output_f.write('"weight": false,\n')

                try:
                    index_output_f.write('"category": "' + equip["tool_category"] + '",\n')
                except:
                    index_output_f.write('"category": false,\n')
                index_output_f.write('"source": {"slug": "PHB","name": "Player\'s Handbook"}\n')

                index_output_f.write('},\n')
            except Exception as e:
                print(e)

        index_output_f.write(']')
except Exception as e:
    print("Erro")
    print(e)

print("Finalizado")
