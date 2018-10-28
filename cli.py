from collections import defaultdict
from copy import copy, deepcopy
import os

from iso639 import languages
from slackclient import SlackClient
import toml

def generate_toml():
    slack_token = os.environ["SLACK_API_TOKEN"]
    sc = SlackClient(slack_token)

    res = sc.api_call(
        "channels.list",
        exclude_archived=True,
    )

    gateways = defaultdict(list)

    if res["ok"] == True:
        channel_names = [ch["name"] for ch in res["channels"]]
        for ch in res["channels"]:
            lang_code = ch["name"].split("-")[-1]
            if lang_code in [lang.alpha2 for lang in languages]:
                base_name = ch["name"][:-3]
                if base_name in channel_names:
                    gateways[base_name].append(lang_code)

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
