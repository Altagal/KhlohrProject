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
    with open("core/artifact/quill/weapon-results.json", 'w') as index_output_f:
        index_output_f.write('[\n')

        for weapon in card_data:
            if weapon["equipment_category"]["index"] == "weapon":
                try:
                    index_output_f.write('{')
                    index_output_f.write('"slug":"' + slugify(weapon["name"]) + '",\n')
                    index_output_f.write('"name":"' + weapon["name"] + '",\n')
                    index_output_f.write('"type": {"slug": "weapon","name": "Weapon"},\n')
                    index_output_f.write('"desc": "",\n')

                    index_output_f.write('"cost": {"quantity": ' + str(weapon["cost"]["quantity"]) + ',"unit": "' + weapon["cost"]["unit"] + '"},\n')

                    try:
                        index_output_f.write('"weight":' + str(weapon["weight"]) + ',\n')
                    except:
                        index_output_f.write('"weight": false,\n')

                    try:
                        index_output_f.write('"damage": {"damage_dice": "' + str(weapon["damage"]["damage_dice"]) + '","damage_type": {"slug":"' + slugify(weapon["damage"]["damage_type"]["name"]) + '", "name":"' + weapon["damage"]["damage_type"]["name"] + '"}},\n')
                    except:
                        index_output_f.write('"damage": false,\n')

                    index_output_f.write('"weapon_category": {"slug": "' + slugify(weapon["weapon_category"]) + '","name": "' + weapon["weapon_category"] + '"},\n')
                    index_output_f.write('"weapon_range": {"slug": "' + slugify(weapon["weapon_range"]) + '","name": "' + weapon["weapon_range"] + '"},\n')

                    try:
                        if weapon["range"]["long"]:
                            index_output_f.write('"ammunition": {')
                            index_output_f.write('"min_range":' + str(weapon["range"]["normal"]) + ',\n')
                            index_output_f.write('"max_range":' + str(weapon["range"]["long"]) + ',\n')
                            index_output_f.write('},\n')
                    except:
                        index_output_f.write('"ammunition": false,\n')

                    try:
                        if weapon["throw_range"]:
                            index_output_f.write('"throw": {')
                            index_output_f.write('"min_range":' + str(weapon["throw_range"]["normal"]) + ',\n')
                            index_output_f.write('"max_range":' + str(weapon["throw_range"]["long"]) + ',\n')
                            index_output_f.write('},\n')
                    except:
                        index_output_f.write('"thrown": false,\n')

                    try:
                        if weapon["special"]:
                            index_output_f.write('"special":"')
                            for txt in weapon["special"]:
                                index_output_f.write('<p>' + txt + '</p>')
                            index_output_f.write('",\n')
                    except:
                        index_output_f.write('"special": false,')

                    index_output_f.write('"weapon_properties": [')
                    for prop in weapon["properties"]:
                        index_output_f.write('{"slug": "' + prop["index"] + '","name": "' + prop["name"] + '"},')

                    index_output_f.write('],\n')

                    index_output_f.write('"source": {"slug": "PHB","name": "Player\'s Handbook"}\n')

                    index_output_f.write('},\n')
                except Exception as e:
                    print(e)

        index_output_f.write(']')
except Exception as e:
    print("Erro")
    print(e)

print("Finalizado")
