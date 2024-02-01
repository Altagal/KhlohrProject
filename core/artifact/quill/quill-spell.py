import json

print("Começou")
try:
    with open("core/artifact/5e-database-main/5e-SRD-Spells.json", 'r') as input_f:
        card_data = json.load(input_f)
except Exception as e:
    print(e)

try:
    with open("test_index.json", 'w') as index_output_f:
        for card in card_data:
            index_output_f.write("  {\n")
            index_output_f.write('    "slug": "' + card["index"] + '",\n')
            index_output_f.write('    "type": "spell"\n')
            index_output_f.write("  },\n")

except Exception as e:
    print("open - test_index.json")
    print(e)

try:
    with open("test.json", 'w') as output_f:
        output_f.write("[\n")
        for card in card_data:
            output_f.write("  {\n")
            output_f.write('    "slug": "' + card["index"] + '",\n')
            output_f.write('    "name": "' + card["name"] + '",\n')
            output_f.write('    "type": "spell",\n')

            output_f.write('    "desc": ')
            output_f.write('"')
            for desc in card["desc"]:
                output_f.write('<p>' + desc.replace('"', '\\"') + '</p>')
            output_f.write('"')
            output_f.write(',\n')

            try:
                output_f.write('    "at_higher_level": "' + card["higher_level"][0] + '",\n')
            except:
                pass

            output_f.write('    "level": ' + str(card["level"]) + ',\n')
            output_f.write('    "range": "' + card["range"] + '",\n')
            output_f.write('    "casting_time": "' + card["casting_time"] + '",\n')
            output_f.write('    "duration": "' + card["duration"].replace('Up to ', '') + '",\n')

            output_f.write('    "is_verbal": true,\n') if "V" in card["components"] else output_f.write('    "is_verbal": false,\n')
            output_f.write('    "is_somatic": true,\n') if "S" in card["components"] else output_f.write('    "is_somatic": false,\n')
            try:
                output_f.write('    "required_material": "' + card["material"] + '",\n')
            except:
                pass

            output_f.write('    "is_concentration": true,\n') if card["concentration"] else output_f.write('    "is_concentration": false,\n')

            output_f.write('    "is_ritual": true,\n') if card["ritual"] else output_f.write('    "is_ritual": false,\n')
            output_f.write('    "is_chronomancy": false,\n')
            output_f.write('    "is_renaissance": false,\n')

            output_f.write('    "magic_school": {\n')
            output_f.write('      "slug":"' + card["school"]["index"] + '" ,\n')
            output_f.write('      "name":"' + card["school"]["name"] + '" \n')
            output_f.write('    },\n')

            output_f.write('    "caster": [')
            first = True
            for caster in card["classes"]:
                if first:
                    first = False
                    output_f.write('\n         {\n')
                else:
                    output_f.write(',\n         {\n')

                output_f.write('            "slug":"' + caster["index"] + '",\n')
                output_f.write('            "name":"' + caster["name"] + '"')
                output_f.write('\n         }')
            output_f.write('\n     ],\n')

            output_f.write('    "source": "Player\'s Handbook"\n')

            output_f.write("  },\n")
        output_f.write("\n]")
except Exception as e:
    print("open - test.json")
    print(e)

print("Terminou")
