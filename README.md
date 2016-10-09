# LaTeX Discord Bot
![Integral](http://i.imgur.com/34I0cSu.png)

Generate LaTeX images with white background, margin and given DPI.

It has been created for personal usage, so code is not perfect
and is not stress tested.
## Install
You must have Python 3.5 and install depedencies:
```
pip3.5 install discord.py
pip3.5 install Pillow
```
Make sure directory where bot is located is writeable for it. To run bot
you have to specify TOKEN env variable with Discord Bot token.
```
TOKEN="..." python3.5 bot.py
```
## Usage
With default DPI:
```
;latex;YOUR TEX HERE
```
With custom DPI:
```
;latex;DPI;YOUR TEX HERE
```
