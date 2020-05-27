def define_env(env):

    languages = [
        {"id": "en-US", "name": "English (United States)"},
        {"id": "zh-CN", "name": "Chinese (China)"}
    ]

    @env.macro
    def translations(gitlocalize_id:int, available_translations:list):
        result = f"""!!! note "We need your help!"
    Each BentoBox addon can be translated.
    However, we rely on third-party contributions.
    
    * If your language is not available for this addon or if you would like to improve the existing translation,
    please read the [translation guidelines](../../BentoBox/Translate-BentoBox-and-addons) and [start translating](https://gitlocalize.com/repo/{gitlocalize_id})!
    * If your language is not listed below, please contact us on [Discord](https://discord.bentobox.world) and we will setup everything so that you can start translating!
    """
        return result
