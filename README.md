# STChatToData
 No one has made something like this and I literally don't know why.
## What is this?
I've been working really hard on [V.I.K.T.O.R](https://github.com/Memerlin/Virtual-Intelligence-Knowledge-Text-based-Opensource-Roleplay) and copying and pasting my logs manually was getting tiresome. This script as it is can convert the SillyTavern chatlogs to JSONL files that can be used as training data instead. It puts the messages sent by the user in the "input" column and messages sent by the bot in an "output" column. Then it'll convert it to a JSONL file and save it. The file should look like ``{"input": "...", "output": "..."}``
A friend asked me about making this for Alpaca formatting (which uses ``{"instruction": "...", "input": "...", "output": "..."}`` according to [Axolotl](https://github.com/OpenAccess-AI-Collective/axolotl#dataset) so that's on my mind too.
## How do I use this?
1. Run run_through_files.py like this:
```
python loop_through_files.py -p path/to/your/chatlogs -o name_of_your_training_data.jsonl
```
2. Wait
3. Done
