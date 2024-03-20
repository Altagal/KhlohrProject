import json
import re

from django.utils.text import slugify

print("Processando")
try:
    with open("core/artifact/5e-database-main/5e-SRD-Magic-Items.json", 'r') as input_f:
        card_data = json.load(input_f)
except Exception as e:
    print("Erro")
    print("open - 5e-SRD-Magic-Items.json.json")
    print(e)

try:
    with open("core/artifact/quill/magic-item-results.json", 'w') as index_output_f:
        index_output_f.write('[\n')

        for magic_item in card_data:
            try:
                index_output_f.write('{')
                index_output_f.write('"slug":"' + slugify(magic_item["name"]) + '",\n')
                index_output_f.write('"name":"' + magic_item["name"] + '",\n')
                index_output_f.write('"type": {"slug": "magic_item","name": "Magic Item"},\n')
                index_output_f.write('"desc":"')
                for desc in magic_item["desc"][1:]:
                    index_output_f.write('<p>' + desc + '</p>')
                index_output_f.write('",\n')
                index_output_f.write('"rarity":{"slug":"' + slugify(magic_item["rarity"]["name"]) + '", "name":"' + magic_item["rarity"]["name"] + '"},\n')
                index_output_f.write('"category":{"slug":"' + magic_item["equipment_category"]["index"] + '", "name":"' + magic_item["equipment_category"]["name"] + '"},\n')
                index_output_f.write('"requires_attunement": false,\n')
                index_output_f.write('"source": {"slug": "PHB","name": "Player\'s Handbook"}\n')

                index_output_f.write('},\n')
            except:
                pass

        index_output_f.write(']')
except Exception as e:
    print("Erro")
    print(e)

print("Finalizado")
