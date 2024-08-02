import discord
from discord.ext import commands
from openai import OpenAI
from api_keys import disc_key, openai_key
from datetime import timedelta        

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = "/", intents= intents)
gpt = OpenAI(api_key= openai_key)

MAX_STRIKES = 5

MAX_TIMEOUT = 1000
#maximumm time for timeout in minutes

conversations = {}
strikes = {}

key = disc_key

@bot.event
async def on_ready():
    print("Bot logged into server")

    
    #when bot is activated send this intro message
    guild = bot.guilds[0]
    channel = guild.text_channels[0]

    message = (
            f"Hi there! I'm {bot.user.name}, your personal chat bot.\n"
            f"Here's a quick summary of available commands:\n"

            f" - `/chat <message>`: Ask me about anything new or continue talking where we left off here or on any other servers\n"
            f" - `/history`: See our conversation history throughout all servers\n"
            f" - `/clear: Start fresh with me and clear our conversation history\n"
        )
    if channel:
        await channel.send(message)



@bot.event
async def on_message(message):
    saftey= gpt.moderations.create(
        input= message.content
    )
    saftey_scores = saftey['results'][0]['category_scores']
    safe = True
    for num in saftey_scores.values():
        if num > 0.7:
            safe = False
    
    if safe:
        await bot.process_commands(message)
    
    else:
        await message.delete()
        await message.channel.send(f'Message from {message.author} deleted because it was deemed unsafe.')
        strikes[message.author.id] += 1
        if strikes[message.author.id] >= MAX_STRIKES:
            duration = timedelta(minutes = min(MAX_TIMEOUT,20 *strikes[message.author.id]))
            await message.author.timeout(duration, reason = "repeated unsafe content in chat")


@bot.command(name = 'chat')
async def chat(ctx,* ,message: str):

    client = ctx.author.id
    if client not in conversations:
        conversations[client] = []
    
    conversations[client].append({"role": "user", "content": message})

    response = gpt.chat.completions.create(
        model= "gpt-4",
        messages= conversations[client],
    )

    reply = response.choices[0].message['content']
    conversations[client].append({"role":"assistant","content": reply})
    await ctx.channel.send(reply)


@bot.command(name = 'history')
async def print_history(ctx):
    client = ctx.author.id

    if client not in conversations:
        await ctx.channel.send("You have not started a chat session yet")
    
    else:
        convo = "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversations[client]])
        await ctx.send(f"Here's our conversation so far:\n{convo}")


@bot.command(name = 'clear' or 'c')
async def clear_convo(ctx):
    client = ctx.author.id

    if client not in conversations:
        await ctx.channel.send("You have not started a chat session yet")
    else:
        del conversations[client]
        await ctx.channel.send("Your chat history has been deleted")
   



bot.run(key)
