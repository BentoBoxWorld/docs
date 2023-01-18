import csv
import json

def define_env(env):

    languages = [
        {"id": "zh-CN", "name": "Chinese (China)"},
        {"id": "zh-HK", "name": "Chinese (Hong Kong)"},
        {"id": "zh-TW", "name": "Chinese (Taiwan)"},
        {"id": "hr", "name": "Croatian"},
        {"id": "cs", "name": "Czech"},
        {"id": "fr", "name": "French"},
        {"id": "de", "name": "German"},
        {"id": "hu", "name": "Hungarian"},
        {"id": "id", "name": "Indonesian"},
        {"id": "it", "name": "Italian"},
        {"id": "ja", "name": "Japanese"},
        {"id": "ko", "name": "Korean"},
        {"id": "lv", "name": "Latvian"},
        {"id": "pl", "name": "Polish"},
        {"id": "pt", "name": "Portuguese"},
        {"id": "ro", "name": "Romanian"},
        {"id": "ru", "name": "Russian"},
        {"id": "es", "name": "Spanish"},
        {"id": "tr", "name": "Turkish"},
        {"id": "vi", "name": "Vietnamese"}
    ]

    @env.macro
    def translations(gitlocalize_id:int, available_translations:list):
        yes = "✅"
        no = "❌"

        # We are adding the intro + header of the language table
        result = f"""!!! note "We need your help!"
    A vast majority of strings in BentoBox and its addons can be translated into virtually any language.
    However, most of the translations that are provided with BentoBox or said addons are made by the community, on which we heavily rely.
    We cannot review all the content of these translations nor guarantee its quality, hence why we highly appreciate any contributions.

    * If your language is not available for this addon or if you would like to improve the existing translation,
    please read the [translation guidelines](../../BentoBox/Translate-BentoBox-and-addons)
    and [start translating](https://gitlocalize.com/repo/{gitlocalize_id})!
    * If your language is not listed below, please contact us on [Discord](https://discord.bentobox.world)
    and we will setup everything so that you can start translating!

| Available | Language | Language code | Progress |
| --- | ---------- | --- | ----------- |
| ✅ | English (United States) | `en-US` | 100% (Default) |
"""

        for language in languages:
            available = no
            if language["id"] in available_translations:
                available = yes
            link = f"https://gitlocalize.com/repo/{gitlocalize_id}/{language['id']}/src/main/resources/locales"
            badge = f"https://gitlocalize.com/repo/{gitlocalize_id}/{language['id']}/badge.svg"
            result += f"| {available} | [{language['name']}]({link}) | `{language['id']}` | ![progress]({badge}) |\n"

        return result

    @env.macro
    def addon_description(addon_name:str, beta:bool=False):
        result = ""

        if beta:
            result += f"""!!! warning
    **{addon_name}** is currently in **Beta**.\n
    Keep in mind that **you are more likely to encounter bugs** and **some features might not be stable**.\n\n"""

        result += f"""!!! info "Useful links"
    - [GitHub repository](https://github.com/BentoBoxWorld/{addon_name})
    ([Releases](https://github.com/BentoBoxWorld/{addon_name}/releases))
    - [Issue tracker](https://github.com/BentoBoxWorld/{addon_name}/issues)
    - [Development builds](https://ci.codemc.org/job/BentoBoxWorld/job/{addon_name})
    ([Latest stable build](https://ci.codemc.io/job/BentoBoxWorld/job/{addon_name}/lastStableBuild/))"""

        return result

    @env.macro
    def placeholders_bundle(gamemode_name:str):
        result = ""
        source = ""

        # Let's read the csv file
        with open('data/placeholders.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Analyze the source
                if (row['source'] != source):
                    # We are in a new "source" so we have to put the header
                    source = row['source']
                    result += f"""\n## {source} placeholders

| Placeholder | Description | {source} version
| ---------- | ---------- | ---------- |
"""

                result += f"| %{row['placeholder'].replace('[gamemode]',gamemode_name)}% | {row['desc']} | {row['version']} |\n"

        return result

    # Adds placeholder table to the addon pages.
    @env.macro
    def placeholders_source(source:str):
        result = f"""!!! tip "Tip"\n
    `[gamemode]` is a prefix that differs depending on the gamemode you are running.\n
    The prefix is the lowercased name of the gamemode, i.e. if you are using BSkyBlock, the prefix is `bskyblock`.\n\n
    Properly translated placeholders for each gamemode can be found:\n
    - [AcidIsland](/en/latest/gamemodes/AcidIsland/Placeholders)
    - [AOneBlock](/en/latest/gamemodes/AOneBlock/Placeholders)
    - [Boxed](/en/latest/gamemodes/Boxed/Placeholders)
    - [BSkyBlock](/en/latest/gamemodes/BSkyBlock/Placeholders)
    - [CaveBlock](/en/latest/gamemodes/CaveBlock/Placeholders)
    - [SkyGrid](/en/latest/gamemodes/SkyGrid/Placeholders).\n
    Please read the main [Placeholders page](/en/latest/BentoBox/Placeholders).\n\n"""

        result += f"""\n

| Placeholder | Description | {source} version
| ---------- | ---------- | ---------- |
"""

        # Let's read the csv file
        with open('data/placeholders.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Analyze the source
                if (row['source'] == source):
                    # We are in our plugin, populate rows
                    result += f"| %{row['placeholder']}% | {row['desc']} | {row['version']} |\n"

        return result


    # Creates a table of requested flags type.
    @env.macro
    def flags_bundle(type:str):
        result = ""
        source = ""

        # Let's read the csv file
        with open('data/flags.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Analyze the source
                if (row['source'] != source):
                    # We are in a new "source" so we have to put the header
                    source = row['source']

                    if (row['type'] == type) or (type == "WORLD_DEFAULT_PROTECTION" and row['type'] == "PROTECTION"):
                        if (type == "PROTECTION"):
                            result += f"""\n## {source} {type.replace("_", " ").capitalize()} flags
    
| | Flag ID | Flag | Description | Default | Min Rank | Max Rank |
| - | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
"""

                            result += f"| <i class='icon-minecraft {icon_css(row['icon'])}'></i> | {row['flag']} | {row['name']} | {row['description']} | {row['default']} | {row['min']} | {row['max']} |\n"
                        else:
                            result += f"""\n## {source} {type.replace("_", " ").capitalize()} flags
    
| | Flag ID | Flag | Description | Default |
| - | ---------- | ---------- | ---------- | ---------- |
"""
                            result += f"| <i class='icon-minecraft {icon_css(row['icon'])}'></i> | {row['flag']} | {row['name']} | {row['description']} | {row['default']} |\n"

        return result


    # Creates a table of requested flags type.
    @env.macro
    def flags_source(source:str, type:str):
        result = ""

        # Let's read the csv file
        with open('data/flags.csv', newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                # Analyze the source
                if (row['source'] == source):
                    # We are in a new "source" so we have to put the header

                    if (row['type'] == type) or (type == "WORLD_DEFAULT_PROTECTION" and row['type'] == "PROTECTION"):
                        if (type == "PROTECTION"):
                            result += f"""\n## {source} {type.replace("_", " ").capitalize()} flags
    
| | Flag ID | Flag | Description | Default | Min Rank | Max Rank |
| - | ---------- | ---------- | ---------- | ---------- | ---------- | ---------- |
"""

                            result += f"| <i class='icon-minecraft {icon_css(row['icon'])}'></i> | {row['flag']} | {row['name']} | {row['description']} | {row['default']} | {row['min']} | {row['max']} |\n"
                        else:
                            result += f"""\n## {source} {type.replace("_", " ").capitalize()} flags
    
| | Flag ID | Flag | Description | Default |
| - | ---------- | ---------- | ---------- | ---------- |
"""
                            result += f"| <i class='icon-minecraft {icon_css(row['icon'])}'></i> | {row['flag']} | {row['name']} | {row['description']} | {row['default']} |\n"

        return result

    # Creates a table of requested flags type.
    @env.macro
    def icon_css(icon:str):
        with open("data/minecraft-block-and-entity.json", 'r') as j:
            contents = json.loads(j.read())

            for entry in contents:
                if icon.lower() == entry['name']:
                    return entry['css']

        return ""