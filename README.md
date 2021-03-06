# slackbot_sample

## はじめに
このプログラムは、slackを介して複数の対話システムを動作させることを最終目的に据えて作成した、pythonによるシンプルなslackbotの実装です。

## 依存パッケージ
- python
  - slackbot (0.4.1)
    - 開発者のgithub: https://github.com/lins05/slackbot
    - pip等でインストールしておく(pip install slackbot)

## 動かし方
1. slackでbotのアカウントを作成する
    - botを作成したいteamにログインしている状態で、以下にアクセス
      - https://my.slack.com/services/new/bot
    - 名前を決定した画面後に表示される”API Token”をメモ
    
      <img src="https://github.com/kazuaki-i/slackbot_sample/blob/images/images/API_Token.png?raw=true" alt="API_Token" width="50%">
    - また、作成したbotを活動させたいチャンネルに招待しておく


2. pythonでの準備
    - slackbot_settings.py 内の”API_TOKEN”に（1）でメモった"API_Token"を書き入れる


3. 実行
    - "python run.py"
      - "ゴレイヌ"と入力すると、botが反応しだし、"3"や"黒"などのキーワードに反応して、応答を返す
      - 再度「ゴレイヌ」と入力すると、botの反応が止まる
      - また、↑の状況に関わらず "@bot名 任意の文字列" と入力すると、任意の文字列部分をオウム返しする
        - なお、生成される「:grilla:」等の文字列は、slackのカスタム絵文字です。（適当な画像を引っ張ってきて絵文字に登録すると幸せになれるかもしれません）

#### 実行例
- plugins/goreinu_listen.py や  plugins/goreinu_respond.py と一緒に見ると幸せになれるかもしれない


<img src="https://github.com/kazuaki-i/slackbot_sample/blob/images/images/result.png?raw=true" alt="API_Token" width="50%">




## 中身について
応答の生成に関する部分は plugins/ 以下に存在します。

1. goreinu_listen.py
    - 主に @listen_to と massage.send() を利用した応答生成
    - チャンネルに投稿された文字列を監視し「活動/休止の制御」および「特定のキーワードに対する応答」を行う。
      - botとしては、後者の実装だけで問題ないが、将来的に複数の対話システムの切り替えを行いたいと考えていたため、活動の制御も実装した
      - ~~あと、制御できないとゴリラゴリラしててうっとおしいので~~


2. goreinu_respond.py
    - 主に @respond_to と massage.reply() を利用した応答生成
    - 「@ボット名」を使用した問いかけに対して応答を行う
      - ユーザーの入力した文字列がreceivedに格納される
        - 対話生成モデルに投げ入れるなど、ご自由にどうぞ
        - なお、listenの方でも同様に記述すれば入力文字列をプログラム内で加工可能

## 余談
- 本プログラムの対話部分は、私の所属するslack teamの"meshi"というチャンネル内に出現している「ゴレイヌbot」の影響を受けて作成しており、対話応答の基本部分はS.K氏によって作成されたものです。

## 参考
- slackbot for python: https://github.com/lins05/slackbot
  - Special thanks to lins05!
