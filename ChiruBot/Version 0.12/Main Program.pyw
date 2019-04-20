import discord
import asyncio
import time
import random

from Bot_Functions import *
import Bot_Commands as bot_command

client = discord.Client()
prefix = '!'

async def bot_response( message ):
    await message.add_reaction( '\U0001F440' )
    input_message = message.content[1:].lower()

    for i in bot_command.help_info:
        if ( input_message.startswith( i ) ):
            function = getattr( bot_command, i )
            await function( message )
            return
    
    await incorrect_call( message.channel )

@client.event
async def on_ready():
    print( 'We have logged in as {0.user}'.format( client ) )
    await client.change_presence( activity =
                                  discord.Game( name = 'with YOUR LIFE'  ) )

    channel = client.get_channel( 567573421983268884 )
    await channel.send( 'Bot Active!' )

@client.event
async def on_message( message ):
    if ( message.author == client.user ):
        return

    if ( message.content.startswith( prefix ) ):
        await bot_response( message )
        return

client.run( SECRET )
