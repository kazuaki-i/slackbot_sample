# -*- coding: utf-8 -*-

import random
from slackbot.bot import listen_to
from slackbot.bot import respond_to
import re

# global variable
IsGoreinu = False

# control bot's IN/OUT
@listen_to("ゴレイヌ")
def swither(message):
    global IsGoreinu
    if IsGoreinu == 1:
        pass
    elif IsGoreinu:
        IsGoreinu = False
        text = "*** ゴレイヌさんがログアウトしました ***"
    else:
        IsGoreinu = True
        text = "*** ゴレイヌさんがログインしました ***"
    message.send(text)

# When listen_to some keywords, send a message for a timeline
Three = re.compile("[3３三]")
@listen_to(Three)
def meshi_three(massage):
    global IsGoreinu
    if IsGoreinu:
        massage.send("オレが3人分 :gorilla: :white_gorilla: :black_gorilla: になる・・・ ")

Black = re.compile("黒|ブラック")
@listen_to(Black)
def meshi_black(massage):
    global IsGoreinu
    if IsGoreinu:
        massage.send(":black_gorilla: 黒の賢人（ブラックゴレイヌ）")

White = re.compile("白|ホワイト")
@listen_to(White)
def meshi_white(massage):
    global IsGoreinu
    if IsGoreinu:
        massage.send(":white_gorilla: 白の賢人（ホワイトゴレイヌ）")

Meshi = re.compile("[飯食]")
@listen_to(Meshi)
def meshi_other(massage):
    global IsGoreinu
    if IsGoreinu:
        tl = ["ゴハンヌ", "ゴレイヌ", "ごはんヌ", "ごはん",
                "えげつねェな・・・",
                "くそが・・・このまま終われるかよ！！",
                 "強・・・・！\n速・・・！\n避・・・・・無理！\n否 死！",
                 "飯・・・・！\n速・・・！\n避・・・・・食事！\n否 死！",
                 "オレが３人分になる・・・"]
        m = random.choice(tl)
        massage.send(m)
