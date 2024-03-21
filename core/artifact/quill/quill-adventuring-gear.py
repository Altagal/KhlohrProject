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
    with open("core/artifact/quill/gear-results.json", 'w') as index_output_f:
        index_output_f.write('[\n')

        for gear in card_data:
            if gear["equipment_category"]["index"] == "adventuring-gear":
                try:
                    index_output_f.write('{')
                    index_output_f.write('"slug":"' + slugify(gear["name"]) + '",\n')
                    index_output_f.write('"name":"' + gear["name"] + '",\n')
                    index_output_f.write('"type": {"slug": "adventuring_gear","name": "Adventuring Gear"},\n')

                    try:
                        if gear["desc"]:
                            index_output_f.write('"desc": "')
                            for desc in gear["desc"]:
                                index_output_f.write('<p>' + desc + '</p>')
                            index_output_f.write('",\n')
                    except:
                        index_output_f.write('"desc": "",')

                    index_output_f.write('"cost": {"quantity": ' + str(gear["cost"]["quantity"]) + ',"unit": "' + gear["cost"]["unit"] + '"},\n')

                    try:
                        index_output_f.write('"weight":' + str(gear["weight"]) + ',\n')
                    except:
                        index_output_f.write('"weight": false,\n')

                    try:
                        index_output_f.write('"gear_category": {"slug":"' + slugify(gear["gear_category"]["name"]) + '", "name":"' + gear["gear_category"]["name"] + '"},\n')
                    except:
                        index_output_f.write('"gear_category": false,\n')

                    index_output_f.write('"source": {"slug": "PHB","name": "Player\'s Handbook"}\n')

                    index_output_f.write('},\n')
                except Exception as e:
                    print(e)

        index_output_f.write(']')
except Exception as e:
    print("Erro")
    print(e)

print("Finalizado")
