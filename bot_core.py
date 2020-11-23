import discord
import logging
import numexpr
import sys
import re
from discord.utils import get
from secrets import discord_bot_token

class Counter(object):
    last_number = 0

class NotUnderstoodError(Exception):
    "For some reason we didn't understand the input as a number"
    pass

class WrongError(Exception):
    "We understood the answer. It's wrong."
    pass

EMOJI_TICK = '\u2705'
EMOJI_CROSS = '\u274c'
EMOJI_INTERROBANG = '\u2049'
EMOJI_LADYBIRD = '\U0001f41e'

emoji = {
        69: '\u264B', # cancer
        420: '\U0001f525', # fire
        1: '1\uFE0F\u20E3', # 1 emoji keycap
        2: '2\uFE0F\u20E3', 
        3: '3\uFE0F\u20E3', 
        4: '4\uFE0F\u20E3', 
        5: '5\uFE0F\u20E3', 
        6: '6\uFE0F\u20E3', 
        7: '7\uFE0F\u20E3', 
        8: '8\uFE0F\u20E3', 
        9: '9\uFE0F\u20E3', 
        }

replacements = {
        '\u221e': '(1/0)', # infinity,
        '\u221a': 'sqrt',  # root,
        # '\u221b' # cuberoot
        # '\u221c' # fourthroot
        '\u2070': '**0', # super 0
        '\u00b0': '**0', # degree
        '\u00ba': '**0', # super o
        '\u00b9': '**1', # super 1
        '\u00b2': '**2', # super 2
        '\u00b3': '**3', # super 2
        '\u2074': '**4', # super 2
        '\u2075': '**5', # super 2
        '\u2076': '**6', # super 2
        '\u2077': '**7', # super 2
        '\u2078': '**8', # super 2
        '\u2079': '**9', # super 2
        '\u2071': '**i', # super 2
        '\U0001F967': '(pi)', # unicode pie
        'α': '(1/137.03599908)', # alpha, the fine structure constant
        'π': '(pi)', # pi
        '÷': '/', # division
        '×': '*',
        '¼': '(1/4)',
        '½': '(1/2)',
        '¾': '(3/4)',

        '\uFE0F': '', # emoji presentation
        '\u20E3': '', # combining keycap
}

memes = {
        '(?:^|\D)69(?:$|\D)': 69,
        '(?:^|\D)420(?:$|\D)': 420,
        '^1.*2.*3.*4.*5.*6.*7.*8.*9$': 9,
        '^1.*2.*3.*4.*5.*6.*7.*8$': 8,
        '^1.*2.*3.*4.*5.*6.*7$': 7,
        '^1.*2.*3.*4.*5.*6$': 6,
        '^1.*2.*3.*4.*5$': 5,
        '^1.*2.*3.*4$': 4,
        '^1.*2.*3$': 3,
        '^3.*2.*1$': 3,
        '^4.*3.*2.*1$': 4,
        '^5.*4.*3.*2.*1$': 5,
        '^6.*5.*4.*3.*2.*1$': 6,
        '^7.*6.*5.*4.*3.*2.*1$': 7,
        '^8.*7.*6.*5.*4.*3.*2.*1$': 8,
        '^9.*8.*7.*6.*5.*4.*3.*2.*1$': 9,
        }


e = 2.718281828459
pi = 3.14159265359
dozen = 12
gross = 144
score = 20
pair = 2
eleventy = 110
one = 1
two = 2
three = 3
four = 4
five = 5
six = 6
seven = 7
eight = 8
nine = 9
ten = 10
eleven = 11
twelve = 12
thirteen = 13
fourteen = 14
fifteen = 15
sixteen = 16
seventeen = 17
eighteen = 18
nineteen = 19
twenty = 20
thirty = 30
fourty = 40
fifty = 50
sixty = 60
seventy = 70
eighty = 80
ninety = 90
hundred = 100
thousand = 1000
million = 1e6
billion = 1e9
trillion = 1e12
brace = 2
myriad = 10e3
grand = 1000
googol = 1e100
i = 1j

"""
message:

id=#
channel.id=#, .name=$, .position=n, .nsfw=b, .news=b, .catgegory_id=?
author.id=#, .name=$, .discriminator=$, .bot=b, .nick=b
"""

def meme_search(text):
    for pattern, number in memes.items():
        if re.search(pattern, text):
            return number
    return False

def do_maths(text, integer=True):
    t = text
    for key, value in replacements.items():
        t=t.replace(key, value)
    print (t)
    try:
        if integer:
            return int(complex(numexpr.evaluate(t)).real)
        else:
            return float(complex(numexpr.evaluate(t)).real)
    except KeyError as e:
        raise NotUnderstoodError("I don't know a variable {}.".format(str(e)))
    except ZeroDivisionError:
        raise WrongError("Please don't divide by zero, it hurts my brain..")
    except OverflowError:
        raise WrongError("Wow, that's a big number. Too big.")
    except ValueError as e: # occurs if strings?
        raise NotUnderstoodError("... was that a string?".format(str(e)))
    except SyntaxError: 
        raise NotUnderstoodError("... did a cat just walk across your keyboard?")

def display_message(message):
    return(f"{message.author.name} on {message.channel.name}: {message.content}")

async def counting(message):
    print ("Counting Candidate seen:", display_message(message))
    try:
        message_number = do_maths(message.content)
    except NotUnderstoodError as e:
        await message.add_reaction(emoji=EMOJI_INTERROBANG)
        await message.channel.send(str(e))
        return
    except WrongError as e:
        await message.add_reaction(emoji=EMOJI_CROSS)
        await message.channel.send(str(e))
        Counter.last_number = 0
    except Exception as e:
        await message.add_reaction(emoji=EMOJI_LADYBIRD)
        await message.channel.send("{}: {}".format(type(e), str(e)))
        return


    if message_number == Counter.last_number + 1:
        Counter.last_number += 1
        await message.add_reaction(emoji=EMOJI_TICK)
        meme = meme_search(message.content)
        if meme:
            await message.add_reaction(emoji=emoji[meme])
    else:
        await message.add_reaction(emoji=EMOJI_CROSS)
        try:
            exact = do_maths(message.content)
        except Exception:
            pass
        await message.channel.send("I calculated that to be {} ({}), not {}".format(exact, message_number, Counter.last_number+1))
        Counter.last_number = 0



client = discord.Client()

channel_roles = {
                760564203667980349: [counting], # mewlip/secrets
                }

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id in channel_roles:
        for role_function in channel_roles[message.channel.id]:
            await role_function(message)

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

if 'console' in sys.argv:
    while True:
        x = input()
        try:
            print (do_maths(x))
        except Exception as e:
            print (e)
            print (type(e))
else:
    client.run(discord_bot_token)


