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
    with open("core/artifact/quill/monster-results.json", 'w') as index_output_f:
        index_output_f.write('[\n')

        for card in card_data:

            alignment = card["alignment"]

            try:
                desc = card["desc"]
            except:
                desc = ""

            languages = card["languages"].split(', ')

            try:
                subtype = '"' + card["subtype"].capitalize() + '"'
            except:
                subtype = "false"

            index_output_f.write("{\n")
            index_output_f.write('"slug": "' + card["index"] + '",\n')
            index_output_f.write('"name": "' + card["name"] + '",\n')
            index_output_f.write('"type": {"slug": "monster","name": "Monster"},\n')
            # index_output_f.write('"desc": "' + desc + '",\n')
            index_output_f.write('"desc": "",\n')
            index_output_f.write('"size": "' + card["size"] + '",\n')
            index_output_f.write('"monster_type":{"slug": "' + card["type"] + '","name": "' + card["type"].capitalize() + '"},\n')
            index_output_f.write('"monster_subtype": ' + subtype + ',\n')
            index_output_f.write('"alignment": "' + card["alignment"] + '",\n')

            index_output_f.write('"challenge_rating": ' + str(card["challenge_rating"]) + ',\n')
            index_output_f.write('"proficiency_bonus": ' + str(card["proficiency_bonus"]) + ',\n')
            index_output_f.write('"xp": ' + str(card["xp"]) + ',\n')

            index_output_f.write('"hit_points": ' + str(card["hit_points"]) + ',\n')
            index_output_f.write('"hit_dice": "' + card["hit_dice"] + '",\n')
            index_output_f.write('"hit_points_roll": "' + card["hit_points_roll"] + '",\n')

            index_output_f.write('"armor_class":[')
            for armor_class in card["armor_class"]:
                index_output_f.write('{"type": "' + armor_class["type"] + '","value": "' + str(armor_class["value"]) + '"},\n')
            index_output_f.write('],')

            index_output_f.write('"speed": [')
            try:
                txt = re.findall(r'\d+', card["speed"]["walk"])
                walk = txt[0]
                index_output_f.write('{"type":false, "value":' + str(walk) + '},')
            except:
                index_output_f.write('{"type":false, "value":0},')

            try:
                hover = card["speed"]["hover"]
                if hover == True:
                    hover = ',"hover": true'
            except:
                hover = ''
            try:
                txt = re.findall(r'\d+', card["speed"]["fly"])
                fly = txt[0]

                index_output_f.write('{"type":"fly", "value":' + str(fly) + hover + ' },')
            except:
                pass

            try:
                txt = re.findall(r'\d+', card["speed"]["swim"])
                swim = txt[0]
                index_output_f.write('{"type":"swim", "value":' + str(swim) + '},')
            except:
                pass

            try:
                txt = re.findall(r'\d+', card["speed"]["burrow"])
                burrow = txt[0]
                index_output_f.write('{"type":"burrow", "value":' + str(swim) + '},')
            except:
                pass

            try:
                txt = re.findall(r'\d+', card["speed"]["climb"])
                climb = txt[0]
                index_output_f.write('{"type":"climb", "value":' + str(swim) + '},')
            except:
                pass

            index_output_f.write('],')

            index_output_f.write('"stats": {"strength": ' + str(card["strength"]) + ', "dexterity": ' + str(card["dexterity"]) + ', "constitution": ' + str(card["constitution"]) + ', "intelligence": ' + str(card["intelligence"]) + ', "wisdom": ' + str(card["wisdom"]) + ', "charisma": ' + str(card["charisma"]) + '},\n')
            index_output_f.write('"senses": [')
            try:
                txt = re.findall(r'\d+', card["senses"]["darkvision"])
                darkvision = txt[0]
                index_output_f.write('{"type":"Darkvision", "value":' + str(darkvision) + '},')
            except:
                pass

            try:
                txt = re.findall(r'\d+', card["senses"]["blindsight"])
                blindsight = txt[0]
                index_output_f.write('{"type":"Blindsight", "value":' + str(blindsight) + '},')
            except:
                pass

            try:
                txt = re.findall(r'\d+', card["senses"]["truesight"])
                truesight = txt[0]
                index_output_f.write('{"type":"Truesight", "value":' + str(truesight) + '},')
            except:
                pass

            try:
                txt = re.findall(r'\d+', card["senses"]["tremorsense"])
                tremorsense = txt[0]
                index_output_f.write('{"type":"Tremorsense", "value":' + str(tremorsense) + '},')
            except:
                pass
            index_output_f.write('],\n')
            index_output_f.write('"passive_perception": ' + str(card["senses"]["passive_perception"]) + ',')

            index_output_f.write('"languages":[')
            for language in languages:
                index_output_f.write('"' + language + '",')
            index_output_f.write('],')

            index_output_f.write('"damage_vulnerabilities":[')
            for damage_vulnerabilities in card["damage_vulnerabilities"]:
                index_output_f.write('{"slug": "' + damage_vulnerabilities + '","name": "' + damage_vulnerabilities.capitalize() + '"},\n')
            index_output_f.write('],')

            index_output_f.write('"damage_resistances":[')
            for damage_resistances in card["damage_resistances"]:
                index_output_f.write('{"slug": "' + damage_resistances + '","name": "' + damage_resistances.capitalize() + '"},\n')
            index_output_f.write('],')

            index_output_f.write('"damage_immunities":[')
            for damage_immunities in card["damage_immunities"]:
                index_output_f.write('{"slug": "' + damage_immunities + '","name": "' + damage_immunities.capitalize() + '"},\n')
            index_output_f.write('],')

            index_output_f.write('"condition_immunities":[')
            for condition_immunities in card["condition_immunities"]:
                index_output_f.write('{"slug": "' + condition_immunities["index"] + '","name": "' + condition_immunities["name"].capitalize() + '"},\n')
            index_output_f.write('],')

            try:
                actions = card["actions"]
            except:
                actions = []

            try:
                special_abilities = card["special_abilities"]
            except:
                special_abilities = []
            index_output_f.write('"special_abilities":[')
            for special_ability in special_abilities:
                index_output_f.write('{"slug": "' + slugify(special_ability["name"]) + '-' + card['index'] + '","name": "' + special_ability["name"] + '" },\n')
            index_output_f.write('],')

            index_output_f.write('"actions":[')
            for action in actions:
                index_output_f.write('{"slug": "' + slugify(action["name"]) + '-' + card['index'] + '","name": "' + action["name"] + '" },\n')
            index_output_f.write('],')

            try:
                reactions = card["reactions"]
            except:
                reactions = []
            index_output_f.write('"reactions":[')
            for reaction in reactions:
                index_output_f.write('{"slug": "' + slugify(reaction["name"]) + '-' + card['index'] + '","name": "' + reaction["name"] + '" },\n')
            index_output_f.write('],')

            try:
                legendary_actions = card["legendary_actions"]
            except:
                legendary_actions = []
            index_output_f.write('"legendary_actions":[')
            for legendary_action in legendary_actions:
                index_output_f.write('{"slug": "' + slugify(legendary_action["name"]) + '-' + card['index'] +'","name": "' + legendary_action["name"] + '" },\n')
            index_output_f.write('],')

            index_output_f.write('"source": {"slug": "PHB","name": "Player\'s Handbook"}\n')

            index_output_f.write("},\n")
        index_output_f.write(']')
except Exception as e:
    print("Erro")
    print(e)

print("Finalizado")
