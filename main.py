# okay command prompt version
# -roll [ID][name][city activity][prey - o][FG - o][addendum1 - o][addendum2 - o][addendum3 - o]
# i.e. 'W46 Selby --scavenging --FG' will roll scavenging (wargrun) for Selby with FG equipped
# i.e. 'W46 Selby --scavenging' will roll scavenging (wargrun) for Selby without FG equipped
# i.e. 'W46 Selby --healing --DEBUFF' will roll healing for Selby with attempt to heal debuff
# from discord.ext import commands

import roll_activity as act
import roll_healing as heal
# import discord as disc

"""
Wargrun Scavenging - 'scavenging'
Ljosa Exploring - 'ljosaexp'
Iringard Exploring - 'irinexp'
"""


def main():
    prompt = input(">>>")
    while prompt != "exit":
        # split prompt into a list
        args = prompt.strip().split(' --')
        # print(args)
        if args[1].lower() == "healing":  # this doesn't change
            if len(args) == 3 and args[2].lower() == "debuff":  # no forn gevir in healing, error proofing but okay
                heal.run_healing(args[0], True)
            else:
                heal.run_healing(args[0])

        if args[1].lower() == "scavenging":  # scavenging
            if len(args) == 3 and args[2].lower() == "fg":
                act.run_activity(args[0], "Scavenging", args[1], True)
            else:
                act.run_activity(args[0], "Scavenging", args[1])

        if args[1].lower() == "exploring":  # exploring
            if len(args) == 3 and args[2].lower() == "fg":
                act.run_activity(args[0], "Exploring", args[1], True)
            else:
                act.run_activity(args[0], "Exploring", args[1])
        else:
            print("Unknown Command, please enter again. ")
        prompt = input(">>>")


main()

client = disc.Client()
bot = commands.Bot(command_prefix='$')


@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$help'):
        await message.channel.send("Please view the readme here:" +
                                   " https://github.com/its-mithril/HVALLA-Item-Roller-public-vers")

    if message.content.startswith('$roll '):  # commands should be in the form $roll name --activity --FG
        string = message.content
        args = string.replace('$roll', '').strip().split(' --')
        if args[1].lower() == "healing":  # this doesn't change
            if len(args) == 3 and args[2].lower() == "debuff":  # no forn gevir in healing, error proofing but okay
                await message.channel.send(heal.run_healing(args[0], True))
            else:
                await message.channel.send(heal.run_healing(args[0]))
        elif args[1].lower() == "scavenging":  # scavenging
            if len(args) == 3 and args[2].lower() == "fg":
                await message.channel.send(act.run_activity(args[0], "Scavenging", args[1], True))
            else:
                await message.channel.send(act.run_activity(args[0], "Scavenging", args[1]))
        elif args[1].lower == "exploring":  # exploring: ljosa or iringard
            if len(args) == 3 and args[2].lower() == "fg":
                await message.channel.send(act.run_activity(args[0], "Exploring", args[1], True))
            else:
                await message.channel.send(act.run_activity(args[0], "Exploring", args[1]))
        elif args[1].lower == "hunting":  # command form: $roll [NAME] --hunting --[PREY] --FG (optional)
            if len(args) == 4 and args[3].lower() == "fg":
                await message.channel.send(act.run_hunting())
            else:
                await message.channel.send(act.run_hunting())
            pass
        else:
            await message.channel.send("unknown command, please try again")


client.run('TOKEN')
