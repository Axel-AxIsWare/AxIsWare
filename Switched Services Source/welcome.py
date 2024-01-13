import discord
from discord.ext import commands
from datetime import datetime, timezone

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    channel_id = urchannelid

    try:
        channel = bot.get_channel(channel_id)

        if channel is None:
            raise ValueError(f"Channel with ID {channel_id} not found.")

        account_age = datetime.now(timezone.utc) - member.created_at
        account_age_days = account_age.days

        embed = discord.Embed(
            title=f' Welcome ',
            description=f'Thank you for joining our server!',
            color=0x42f56c
        )

        embed.add_field(name='User', value=f'{member.mention}', inline=True)
        embed.add_field(name='Account Age', value=f'{account_age_days} days', inline=True)

        await channel.send(embed=embed)

    except Exception as e:
        print(f"An error occurred: {e}")

bot.run('ur bot token')