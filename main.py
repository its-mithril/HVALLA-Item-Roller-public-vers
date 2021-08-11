from discord.ext import commands
import roll_healing as healing
import roll_activity_db as activity
# import secrets

bot = commands.Bot(command_prefix='$')
on_error = 'Something went wrong! Please check your arguments '


@bot.event
async def on_ready():
    print('Logged in as {}'.format(bot.user))


@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("Unknown Command, please use `$help` to view all commands available."
                       "\nOr view the readme here:"
                       " <https://github.com/its-mithril/HVALLA-Item-Roller-public-vers#readme>")


@bot.command(help='rolls scavenging for wargrun, takes 2 arguments at most. Example: $scavenge [NAME] '
                  '[fg | optional]\nUse Quotes " to surround arguments with spaces. Example: $scavenge '
                  '"W46 Selby" [fg |optional]')
async def scavenge(ctx, id_name='', fg=''):  # $scavenge "W46 Selby" fg
    print('scavenge command received')
    if id_name.strip() == '':
        raise commands.BadArgument
    else:
        if fg.lower().strip() == 'fg':
            text = activity.scavenging_exploring(id_name.strip(), True, 'scavenging')
        else:
            text = activity.scavenging_exploring(id_name.strip(), activity='scavenging')

    await ctx.send(text)


@scavenge.error
async def scavenge_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(on_error + 'or use `$help scavenge` for details on the `scavenge` command')


@bot.command(help='rolls exploring for all regions, takes 2 arguments at most. Example: $explore [NAME] [fg | optional]'
                  '\nUse Quotes " to surround arguments with spaces. Example: $explore "W46 Selby" [fg | optional]')
async def explore(ctx, id_name='', fg=''):
    print('explore command received')
    if id_name.strip() == '':
        raise commands.BadArgument
    else:
        if fg.lower().strip() == 'fg':
            text = activity.scavenging_exploring(id_name.strip(), True, 'exploring')
        else:
            text = activity.scavenging_exploring(id_name.strip(), activity='exploring')

    await ctx.send(text)


@explore.error
async def explore_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(on_error + 'or use `$help explore` for details on the `explore` command')


@bot.command(help='rolls hunting for all prey items, takes 3 arguments at most. Example: $hunt [NAME] [prey] '
                  '[fg | optional]\n Use Quotes " to surround arguments with spaces. Example: $hunt "W46 Selby" [prey]'
                  '[fg | optional]\n Prey Options: [caribou, fox, grunox, arthro, clipperant, gryllo, goat, elk, deer]')
async def hunt(ctx, id_name='', prey='', fg=''):
    print('hunt command received, prey: ', prey.strip())
    if id_name.strip() == '' or prey.strip() == '':
        raise commands.BadArgument
    else:
        if fg.lower().strip() == 'fg':
            text = activity.hunting(id_name.strip(), prey.strip(), True)
        else:
            text = activity.hunting(id_name.strip(), prey.strip())

    await ctx.send(text)


@hunt.error
async def hunt_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(on_error + 'or use `$help hunt` for details on the `hunt` command')


@bot.command(help='rolls healing for all wargs, takes 2 arguments at most. Example: $heal [NAME] [debuff | optional]\n'
                  'Use Quotes " to surround arguments with spaces. Example: $heal "W46 Selby" [debuff | optional]')
async def heal(ctx, id_name='', debuff=''):
    print('heal command received')
    if id_name.strip() == '':
        raise commands.BadArgument
    else:
        if debuff.lower().strip() == 'debuff':
            text = healing.heal(id_name.strip(), True)
        else:
            text = healing.heal(id_name.strip())
    await ctx.send(text)


@heal.error
async def heal_error(ctx, error):
    if isinstance(error, commands.BadArgument):
        await ctx.send(on_error + 'or use `$help heal` for details on the `heal` command')


# bot.run(secrets.TOKEN)
