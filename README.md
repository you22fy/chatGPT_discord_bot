# chatGPT_discord_bot
## 概要
chatGPT APIをdiscord側から利用できるbotの実装です。
fly.ioでデプロイしていますが、非公開botとなっています。
pythonのバージョンは3.11.5で実装しました。

## 実行
- pythonのバージョンを確認する
```
python --version
>>> Python 3.11.5
```
- 必要なライブラリをインストールする
```
pip install requirements.txt
```

- 環境変数を設定する
    - `.env`を利用する場合
        ```
        TOKEN=YOUR_DISCORD_BOT_TOKEN
        CHAT_GPT_API_KEY = YOUR_CHAT_GPT_API_KEY
        ```
    - flyの環境変数を追加する
        ```
        flyctl secrets set TOKEN=YOUR_DISCORD_BOT_TOKEN CHAT_GPT_API_KEY=YOUR_CHAT_GPT_API_KEY
        ```
- 実行
```
python main.py
```
