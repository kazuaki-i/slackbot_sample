# -*- coding: utf-8 -*-

import random
from slackbot.bot import respond_to
import re

# When respond_to, reply a message for a timeline
Refrect = re.compile("(.+)")
@respond_to(Refrect)
def meshi_refrect(message, received):
    message.reply("やられっぱなしってのは性に合わねえんだ・・・\n \
        喰らえ！ :black_gorilla:< {}".format(received))
