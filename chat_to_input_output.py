import json
from typing import Generator

def main(args):
    input_file = args.input
    output_file = args.output
    print(f'Reading chatlog at {input_file}')

    # Read logs line by line

    def get_chat(input_file) -> Generator[dict, None, None]:
        with open(input_file, 'r', encoding='utf-8') as f:
            for line_number, line in enumerate(f, start=1):
                try:
                    if input_file.endswith('.jsonl'):
                        yield json.loads(line)
                except json.JSONDecodeError as e:
                    print(f'Error reading this line: {line_number} in file {input_file}')
                    print(f'Error message: {str(e)}')
    log = list(get_chat(input_file))

    output = []
    current_input = ''
    current_output = ''

    for i in range(len(log)):
        mes: str = log[i].get('mes', '') # String
        if mes == '': # Skip empty messages
            continue
        if log[i].get('is_user'):
            if current_input != '':
                output.append({'input': current_input.strip(), 'output': current_output.strip()})
                current_output = ''
            current_input = mes + '\n'
        else:
            current_output += mes + '\n'
    
    # Append the last conversation if it exists after loop
    if current_input != '' and current_output != '':
        output.append({'input': current_input.strip(), 'output': current_output.strip()})
    print(f'Writing {output_file}...')

    with open(output_file, 'a', encoding='utf-8') as f:
        for pair in output:
            f.write(json.dumps(pair) + '\n')
        print(f'{output_file} has been written')