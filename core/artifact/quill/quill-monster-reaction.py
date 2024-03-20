import json
import re

from django.utils.text import slugify

print("Processando")
try:
    with open("core/artifact/5e-database-main/5e-SRD-Monsters.json", 'r') as input_f:
        card_data = json.load(input_f)
except Exception as e:
    print("Erro")
    print("open - 5e-SRD-Monsters.json")
    print(e)

try:
    with open("core/artifact/quill/monster-reaction-results.json", 'w') as index_output_f:
        index_output_f.write('[\n')

        for card in card_data:
            try:
                for ability in card["reactions"]:
                    index_output_f.write('{')
                    index_output_f.write('"slug":"'+slugify(ability["name"])+'-'+card["index"]+'",\n')
                    index_output_f.write('"name":"'+ability["name"]+'",\n')
                    index_output_f.write('"desc":"<p>'+ability["desc"]+'</p>"\n')
                    index_output_f.write('},\n')
            except:
                pass

        index_output_f.write(']')
except Exception as e:
    print("Erro")
    print(e)

print("Finalizado")
