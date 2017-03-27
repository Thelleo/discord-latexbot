import discord
import asyncio
import urllib.request
import urllib.parse
import random
import os
from PIL import Image
import io

client = discord.Client()

# Using 3rdparty site to render TeX is not
# the best solution, however CodeCogs site
# is pretty stable and this method does not
# require installing LaTeX on local machine.
async def generate_file(dpi, tex):
    MARGIN = 20
    URL = 'https://latex.codecogs.com/gif.latex?{0}'
    TEMPLATE = '\\dpi{{{}}} \\bg_white {}'
    filename = '{}.png'.format(random.randint(1, 1000))
    query = TEMPLATE.format(dpi, tex)
    url = URL.format(urllib.parse.quote(query))
    bytes = urllib.request.urlopen(url).read()
    img = Image.open(io.BytesIO(bytes))
    old_size = img.size
    new_size = (old_size[0] + MARGIN, old_size[1] + MARGIN)
    new_img = Image.new("RGB", new_size, (255, 255, 255))
    new_img.paste(img, (int(MARGIN / 2), int(MARGIN / 2)))
    img_bytes = io.BytesIO()
    new_img.save(img_bytes, 'PNG')
    img_bytes.seek(0)
    return img_bytes

@client.event
async def on_ready():
    print('Ready')

@client.event
async def on_message(message):
    if message.content.startswith(';latex'):
        await client.send_typing(message.channel)
        parts = message.content.split(';')
        dpi = 200
        tex = ''
        if len(parts) == 3:
            tex = ';'.join(parts[2:])
        else:
            dpi = int(parts[2])
            tex = ';'.join(parts[3:])
        print('{}: dpi={} tex={}'.format(message.author.name, dpi, tex))
        bytes = await generate_file(dpi, tex)
        filename = '{}.png'.format(random.randint(1, 1000))
        await client.send_file(message.channel, bytes, filename=filename)


client.run(os.environ['TOKEN'])
