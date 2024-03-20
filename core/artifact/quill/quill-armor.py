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
    with open("core/artifact/quill/armor-results.json", 'w') as index_output_f:
        index_output_f.write('[\n')

        for equip in card_data:
            if equip["equipment_category"]["index"] == "armor":
                try:
                    index_output_f.write('{')
                    index_output_f.write('"slug":"' + slugify(equip["name"]) + '",\n')
                    index_output_f.write('"name":"' + equip["name"] + '",\n')
                    index_output_f.write('"type": {"slug": "armor","name": "Armor"},\n')
                    index_output_f.write('"desc": "",\n')
                    index_output_f.write('"cost": {"quantity": ' + str(equip["cost"]["quantity"]) + ',"unit": "' + equip["cost"]["unit"] + '"},\n')
                    index_output_f.write('"armor_class":' + str(equip["armor_class"]["base"]) + ',\n')
                    index_output_f.write('"dex_bonus":' + str(equip["armor_class"]["dex_bonus"]) + ',\n')
                    try:
                        index_output_f.write('"dex_max_bonus":' + str(equip["armor_class"]["max_bonus"]) + ',\n')
                    except:
                        index_output_f.write('"dex_max_bonus": false,\n')

                    try:
                        if equip["str_minimum"] == 0:
                            index_output_f.write('"str_min": false,\n')
                        else:
                            index_output_f.write('"str_min":' + str(equip["str_minimum"]) + ',\n')
                    except:
                        index_output_f.write('"str_min": false,\n')

                    index_output_f.write('"stealth_disadvantage":' + str(equip["stealth_disadvantage"]) + ',\n')

                    try:
                        index_output_f.write('"weight":' + str(equip["weight"]) + ',\n')
                    except:
                        index_output_f.write('"weight": false,\n')

                    index_output_f.write('"armor_category": {"slug": "' + slugify(equip["armor_category"]) + '","name": "' + equip["armor_category"] + '"},\n')
                    index_output_f.write('"source": {"slug": "PHB","name": "Player\'s Handbook"}\n')

                    index_output_f.write('},\n')
                except Exception as e:
                    print(e)

        index_output_f.write(']')
except Exception as e:
    print("Erro")
    print(e)

print("Finalizado")
