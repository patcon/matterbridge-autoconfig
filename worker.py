import logging
import os
import sys
import time

from gunicorn.glogging import CONFIG_DEFAULTS
import requests
from slackclient import SlackClient


slack_token = os.environ["SLACK_API_TOKEN"]
sc = SlackClient(slack_token)

watched_types = [
    "channel_archive",
    "channel_created",
    "channel_deleted",
    # TODO: These become important if we want to fully support bot tokens.
    #"channel_joined",
    #"channel_left",
    "channel_rename",
    "channel_unarchive",
]

logging.basicConfig(
    format=CONFIG_DEFAULTS["formatters"]["generic"]["format"],
    datefmt=CONFIG_DEFAULTS["formatters"]["generic"]["datefmt"],
)
logger = logging.getLogger(__name__)

if os.environ.get("DEBUG"):
    logger.setLevel(logging.DEBUG)

if sc.rtm_connect(with_team_state=False):
    while True:
        fire_hook = False
        for ev in sc.rtm_read():
            etype = ev.get("type")
            channel = ev.get("channel")

            if etype == "hello":
                logger.info("Received hello message!")

            if etype in watched_types:
                fire_hook = True
                if type(channel) is dict:
                    channel = channel["id"]
                logger.info(etype + " - " + channel)

        webhook_url = os.environ.get("WEBHOOK_URL")
        webhook_token = os.environ.get("WEBHOOK_TOKEN")
        if fire_hook and webhook_url and webhook_token:
            r = requests.post(webhook_url, data={'token': webhook_token})
            if r.status_code != 200:
                logging.warning("POST to webhook failed...")

        time.sleep(5)
