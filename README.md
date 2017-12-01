# trans
Translate sentences in clipboard contents immediately.

# Example
Copy these lines and run trans.py:
```
This program reads and concatenates lines which are arbitrarily
splitted by'\n' to make lines of sentences. Then it translates
them into Japanese sentences.
```
then you get such lines in the clipboard:
```
This program reads and concatenates lines which are arbitrarily splitted by'\n' to make lines of sentences.
Then it translates them into Japanese sentences.

このプログラムは、文の行を作るために '\ n'で任意に分割された行を読み込んで連結します。
そして、それを日本語の文に翻訳します。
```

## Requirements
Install pyperclip in your current environment:
https://github.com/asweigart/pyperclip

You may also install clip board utility on Ubuntu:
"sudo apt-get install xclip" or "sudo apt-get install xsel"

## TODO
Add an ML model to decide wheather '.' is end of sentence or not.
