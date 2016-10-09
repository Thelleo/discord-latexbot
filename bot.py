import discord
import asyncio
import urllib.request
import urllib.parse
import random
import os
from PIL import Image

client = discord.Client()

# Using 3rdparty site to render TeX is not
# the best solution, howerer CodeCogs site
# is pretty stable and this method does not
# require installing LaTeX on local machine.
async def generate_file(dpi, tex):
    MARGIN = 20
    URL = 'https://latex.codecogs.com/gif.latex?{0}'
    TEMPLATE = '\\dpi{{{0}}} \\bg_white {1}'
    filename = '{0}.png'.format(random.randint(1, 1000))
    query = TEMPLATE.format(dpi, tex)
    url = URL.format(urllib.parse.quote(query))
    urllib.request.urlretrieve(url, filename)
    img = Image.open(filename)
    old_size = img.size
    new_size = (old_size[0] + MARGIN, old_size[1] + MARGIN)
    new_img = Image.new("RGB", new_size, (255, 255, 255))
    new_img.paste(img, (int(MARGIN / 2), int(MARGIN / 2)))
    new_img.save(filename)
    return filename

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
        print('{0}: dpi={1} tex={2}'.format(message.author.name, dpi, tex))
        name = await generate_file(dpi, tex)
        await client.send_file(message.channel, name)
        os.remove(name)


client.run(os.environ['TOKEN'])
