# HotPepperGourmetDialogue
Restaurant Search System through Dialogue in Japanese.


## Installation
On the application root directory, execute following command to install required library.

```
pip install -r requirements.txt
```

## Setting
Set Hot Pepper and Docomo API key to environment variables.

```
export HOTPEPPER_API_KEY=xxxxxxxx
export DOCOMO_DIALOGUE_API_KEY=xxxxxxxx
```

## Execution
First, move to application directory. Then execute following command.

```
python app.py
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