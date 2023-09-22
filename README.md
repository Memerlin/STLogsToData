# STChatToData
 No one has made something like this and I literally don't know why.
## What is this?
I've been working really hard on [V.I.K.T.O.R](https://github.com/Memerlin/Virtual-Intelligence-Knowledge-Text-based-Opensource-Roleplay) and copying and pasting my logs manually was getting tiresome. This script as it is can convert the SillyTavern chatlogs to JSONL files that can be used as training data instead. It puts the messages sent by the user in the "input" column and messages sent by the bot in an "output" column. Then it'll convert it to a JSONL file and save it. The file should look like ``{"input": "...", "output": "..."}``
A friend asked me about making this for Alpaca formatting (which uses ``{"instruction": "...", "input": "...", "output": "..."}`` according to [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl#dataset) so that's on my mind too.
## How do I use this?
1. Open the script in your favorite IDE.
2. Move the log you want to convert to the same folder as the script.
3. Replace 'jayce_logs.jsonl' with the name of the log you want to convert.
4. Replace 'training-data2.jsonl' with the name you want for your file.
5. Done.
