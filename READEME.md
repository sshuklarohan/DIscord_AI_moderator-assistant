# DIscord_AI_moderator-assistant


## Summary

This discord bot utilizes OpenAI's gpt 4 chat completion to assist users with their activities, whilst also using OpenAI's moderation feature to enforce server guidlines


### 1. Chat with bot

the `/chat` command allows users to interact with the bot using natural language. The bot utilizes gpt-4 to generate responses and is able to keep track of its conversation with individual users and reply with context 

### 2. Moderation

using discords on_message function the bot relays all chat messages to OpenAI's moderation detection system which relays back a score that indicates wether or not the message is appropriate. If it's deemed inapropriate it will be deleted and the nessecary bans/punishments will be placed on the user   


### 3. Greetings

- When the bot connects to the discord server, you are greated with a list of commands explaining how to use the bot.


