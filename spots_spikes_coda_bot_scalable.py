import os
import discord
from discord.ext import commands
import openai

# Load tokens from environment variables
DISCORD_TOKEN = os.environ.get("DISCORD_TOKEN")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

if not DISCORD_TOKEN or not OPENAI_API_KEY:
    raise ValueError("DISCORD_TOKEN and OPENAI_API_KEY must be set in environment variables")

# Initialize OpenAI
openai.api_key = OPENAI_API_KEY

# Set up Discord bot
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

# Commands
@bot.command(name="coda")
async def coda(ctx, *, message: str):
    await ctx.send(f"Hello! You said: {message}")

@bot.command(name="story")
async def story(ctx, *, prompt: str):
    try:
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=f"Write a short story about: {prompt}",
            max_tokens=150
        )
        await ctx.send(response.choices[0].text.strip())
    except Exception as e:
        await ctx.send(f"Error: {e}")

@bot.command(name="character")
async def character(ctx, *, name: str):
    await ctx.send(f"Character received: {name}")

# On ready
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}!")

# Run bot
bot.run(DISCORD_TOKEN)
