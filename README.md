# DIscord_AI_moderator-assistant


## Summary

This discord bot utilizes OpenAI's gpt 4 chat completion to assist users with their activities, whilst also using OpenAI's moderation feature to enforce server guidelines


### 1. Chat with bot

the `/chat` command allows users to interact with the bot using natural language. The bot utilizes gpt-4 to generate responses and is able to keep track of its conversation with individual users and reply with context


### 2. Text history

the `/history` command allows users to see their conversation history with the bot. This will display texts from user and bot from all sessions across different channels and servers

### 3. Clear history

the `/clear` command allows users to erease their conversation history with the bot, allowing users to start fresh.


### 4. Moderation

using discords on_message function the bot relays all chat messages to OpenAI's moderation detection system which relays back a score that indicates wether or not the message is appropriate. If it's deemed inapropriate it will be deleted and the nessecary bans/punishments will be placed on the user   


### 5. Greetings

- When the bot connects to the discord server, you are greated with a list of commands explaining how to use the bot.


### Prerequisites

- Python 3.6 or higher
- Discord.py library
- OpenAI library
- OpenAI gpt-4 API key




