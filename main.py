def define_env(env):

    # Defines variables which can be used in all pages

    # Defines a Markdown note that provides all the useful links for the addon's page.
    env.variables['addon_useful_links'] = f"""!!! info "Useful links"
    - [GitHub repository](https://github.com/BentoBoxWorld/{env.page.title})
    ([Releases](https://github.com/BentoBoxWorld/{env.page.title}/releases))
    - [Issue tracker](https://github.com/BentoBoxWorld/{env.page.title}/issues)
    - [Development builds](https://ci.codemc.org/job/BentoBoxWorld/job/{env.page.title})
    ([Latest stable build](https://ci.codemc.io/job/BentoBoxWorld/job/{env.page.title}/lastStableBuild/))
    """

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
    Each BentoBox addon can be translated.
    However, we rely on third-party contributions.

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
