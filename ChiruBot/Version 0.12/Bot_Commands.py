from Bot_Functions import *
import discord

help_info = { 'help' : ( 'short-info', 'long-info' ),
              'say' : ( 'short-info', 'long-info' ) }

async def help_message( message ):
    embed = discord.Embed( title = '**LIST OF COMMANDS**',
                           description = 'type !help [command_name] for a more detailed description',
                           color=0xf7ff28 )

    for i in help_info:
            embed.add_field( name = i,
                            value = (help_info[i])[0],
                            inline = False )
    await message.channel.send( embed = embed )

async def help( message ):
    if ( len(message.content) == len( prefix ) + len( 'help' ) ):
         await help_message( message )
         return
    
    if ( not ( await verify_input ( message, 'help' ) ) ):
        return

    help_command = ( message.content[ len( prefix ) + len( 'help' ) : ] ).strip()

    try:
        await message.channel.send( (help_info[ help_command ])[1] )
    except:
        await incorrect_call( message.channel )
         
async def say( message ):
    if ( not ( await verify_input ( message, 'say' ) ) ):
        return

    message_to_say = message.content[4:]

    await message.delete()
    await message.channel.send( message_to_say )
