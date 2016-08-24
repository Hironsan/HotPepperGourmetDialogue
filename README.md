# HotPepperGourmetDialogue
Restaurant Search System through Dialogue in Japanese.


## Installation
On the application root directory, execute following command to install required library.

```
$ pip install -r requirements.txt
```

## Setting
Set HotPepper, Docomo and SLACK API Key to environment variables.

```
$ export HOTPEPPER_API_KEY=xxxxxxxx
$ export DOCOMO_DIALOGUE_API_KEY=xxxxxxxx
$ export SLACK_API_KEY=xxxxxxxx
```

Set PYTHONPATH to environment variables.

```
$ cd HotPepperGourmetDialogue
$ export PYTHONPATH=`pwd`
```

## Execution
First, move to application directory. 

```
$ cd application
```

If you want to start slack bot, Then execute following command.

```
$ python slack_bot.py
```

If you want to start websocket server, Then execute following command.

```
$ python server.py
```

## Dialogue Example

```
S: 料理のジャンルや場所をおっしゃってください。
U: イタリアンが食べたい
S: イタリアンですね。場所はどのあたりですか？
U: 西新宿のあたり
S: 場所は西新宿ですね。予算の上限はどのくらいですか？
U: 4000円以下
S: 予算は4000円ですね。ではこちらの場所はどうでしょうか？（HotPepper APIを叩いて場所を出す）
U: ありがとう
S: どういたしまして
```