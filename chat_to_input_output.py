import pandas as pd
# you can just rename all instances of df_jayce with whatever variable name you want. Just make sure is consistent
df_jayce = pd.read_json('jayce_logs.jsonl', lines=True) # Replace 'jayce_logs.jsonl' with the name of your chatlog. Make sure this is the same name as the log you wanna use and that it is on the same folder
df_jayce.drop(columns=['create_date', 'send_date', 'is_name', 'swipe_id', 'swipes', 'gen_started', 'gen_finished'], inplace=True) # I don't think we need those for now
# In SillyTavern, is_user is used to determine wether the message was sent by the user or not. Pandas recognizes False and True as 0.0 and 1.0 respectively
# The very first row (row 0, the first message in chat) has NaN as is_user. I'll drop it for now. Reminder to work with that later.
df_jayce = df_jayce.drop(0)
df_jayce.reset_index(drop=True, inplace=True)
# Convert 'is_user' to boolean. This will recognize 0.0 and 1.0 as True or False now.
df_jayce['is_user'] = df_jayce['is_user'].astype(bool)
input_data = df_jayce.loc[df_jayce['is_user'], 'mes'].reset_index(drop=True) # This will check if the data is from a user and put it in a new "input" column
output_data = df_jayce.loc[~df_jayce['is_user'], 'mes'].reset_index(drop=True) # This will check if the data is from the bot and put it in a new "output" column
# Create new column and a new dataframe with that information
ndf = pd.DataFrame({"input": input_data, "output": output_data})
# A field had {{ }} as input and I can't tell why. Another one has "NaN". Maybe because I swiped?
ndf['input'] = ndf['input'].fillna('').astype(str) # Convert NaN to an empty string
ndf['input'] = ndf['input'].str.replace(r'(\{\{\s*\}\}|NaN)', '', regex=True)
print(ndf)
# Append this new data to the previous training data
with open('training-data2.jsonl', 'a') as f:
    ndf.to_json(f, orient='records', lines=True)
