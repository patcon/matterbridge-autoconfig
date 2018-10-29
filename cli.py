from collections import defaultdict
from copy import copy, deepcopy
import os

from iso639 import languages
from slackclient import SlackClient
import toml

def language_codes():
    return [lang.alpha2 for lang in languages]

def is_lang_chan(channel_name):
    chan_lang = channel_name.split("-")[-1]
    return chan_lang in language_codes()

def translation_chan_tree(channels):
    tree = defaultdict(list)

    channel_names = [ch["name"] for ch in channels]
    for name in channel_names:
        if is_lang_chan(name):
            base_name = name[:-3]
            if base_name in channel_names:
                lang_code = name.split("-")[-1]
                tree[base_name].append(lang_code)

    return tree

def translation_channels(channels):
    translation_channels = []
    tree = translation_chan_tree(channels)
    for base, langs in tree.items():
        translation_channels.append(base)
        for lang_code in langs:
            translation_channels.append(base+"-"+lang_code)

    return translation_channels


def generate_toml():
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    res = sc.api_call(
        "channels.list",
        exclude_archived=True,
    )

    gateways = defaultdict(list)

    if res["ok"] == True:
        print(translation_channels(res["channels"]))
        gateways = translation_chan_tree(res["channels"])

    config = {}
    config["gateway"] = []
    default_gw = {
        "enable": True,
        "inout": [],
        "name": "",
    }
    default_bridge = {
        "account": "",
        "channel": "",
        "options": {
            "locale": "",
        },
    }
    account = "slack.g0v-tw"
    for name, locales in gateways.items():
        gw = deepcopy(default_gw)
        gw["name"] = name
        base_bridge = copy(default_bridge)
        base_bridge["account"] = account
        base_bridge["channel"] = name
        base_bridge.pop("options")
        gw["inout"].append(base_bridge)
        for lang in locales:
            lang_bridge = deepcopy(default_bridge)
            lang_bridge["account"] = account
            lang_bridge["channel"] = name + "-" + lang
            lang_bridge["options"]["locale"] = lang
            gw["inout"].append(lang_bridge)
        config["gateway"].append(gw)

    toml_string = toml.dumps(config)

    return toml_string

# Print to terminal if running directly
if __name__ == "__main__":
    mytoml = generate_toml()
    print(mytoml)
