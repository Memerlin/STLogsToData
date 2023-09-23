import json
import argparse
from typing import Generator

parser = argparse.ArgumentParser(description='Convert chat logs to input/output format')

parser.add_argument('-i', '--input', type=str, help='The chatlog to convert', required=True)
parser.add_argument('-o', '--output', type=str, help='The output file', required=True)

args = parser.parse_args()

# Read logs line by line
def get_chat(filename) -> Generator[dict, None, None]: 
    with open(filename, 'r', encoding='utf-8') as f:
        for line in f:
            try:
                yield json.loads(line)
            except:
                print('Error reading line: ' + line)

print('Reading chat log at ' + args.input)
log = list(get_chat(args.input))

output = []
current_input = ''
current_output = ''

for i in range(len(log)):
    mes: str = log[i].get('mes', '')  # string
    if mes == '':  # Skip empty messages
        continue

    if log[i].get('is_user'):
        if current_output != '':
            output.append({'input': current_input.strip(), 'output': current_output.strip()})
            current_output = ''
        current_input = mes + '\n'
    else:
        current_output += mes + '\n'

# Append the last conversation if it exists after the loop
if current_input != '' and current_output != '':
    output.append({'input': current_input.strip(), 'output': current_output.strip()})

print('Writing output to ' + args.output)
print(output)

with open(args.output, 'a') as f:
    for pair in output:
        f.write(json.dumps(pair) + '\n')
