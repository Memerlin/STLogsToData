import json
from typing import Generator

def main(args):
    input_file = args.input
    output_file = args.output
    print(f'Reading chatlog at {input_file}')
    print(f'Writing output to {output_file}')
    convert_to_input_and_output(input_file, output_file)
    
def get_chat(filename) -> Generator[dict, None, None]: 
    with open(filename, 'r', encoding='utf-8') as f:
        for line_number, line in enumerate(f, start=1):
            line = line.strip()
            if line:
                try:
                    yield {'mes': line}
                except json.JSONDecodeError as e:
                    print(f'Error reading line:  {line_number}: {line}')
                    print('Error message:', str(e))    
def convert_to_input_and_output(input_file, output_file):

    # Function to check if Pair exists in training_data
    def pair_exists(pair, training_data):
        return pair in training_data

    print('Reading chat log at ' + input_file)
    log = list(get_chat(input_file))

    output = []
    current_input = ''
    current_output = ''

    # Reading existing training data and store pairs in a set
    training_data_set = set()
    try:
        with open(output_file, 'r', encoding='utf-8') as f:
                for line in f:
                    pair = json.loads(line)
                    training_data_set.add((pair['input'], pair['output']))
    except FileNotFoundError:
        print(f"No {output} file found, creating new file...")

    for i in range(len(log)):
        mes: str = log[i].get('mes', '')  # string
        if mes == '':  # Skip empty messages
            continue

        if log[i].get('is_user'):
            if current_output != '':
                pair = {'input': current_input.strip(), 'output': current_output.strip()}
                if not pair_exists((pair['input'], pair['output']), training_data_set):
                    output.append(pair)
                else:
                    print(f'Warning: Pair already exists - {pair["input"]}, {pair["output"]}')
                current_output = ''
            current_input = mes + '\n'
        else:
            current_output += mes + '\n'

    # Append the last conversation if it exists after the loop
    if current_input != '' and current_output != '':
        pair = {'input': current_input.strip(), 'output': current_output.strip()}
        if not pair_exists((pair['input'], pair['output']), training_data_set):
            output.append(pair)
        else:
            print(f'Warning: Pair already exists - {pair["input"]}, {pair["output"]}')

    print('Writing output to ' + output_file)
    if output == []:
        print(f'The data between "{input_file}" and "{output_file}" is already present')
    else:
        with open(output_file, 'a') as f:
            for pair in output:
                f.write(json.dumps(pair) + '\n')
        print(f'Output appended to {output_file}')