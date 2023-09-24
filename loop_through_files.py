import argparse
import os
from chat_to_input_output import main


parser = argparse.ArgumentParser()

parser.add_argument('-p', '--path', type=str, help="Path to directory that contains the chatlogs", required=True)
parser.add_argument('-o', '--output', type=str, help="output file", required=True)

def process_files(args):
    for file in os.listdir(args.path):
        full_path = os.path.join(args.path, file)
        main(argparse.Namespace(input=full_path, output=args.output))

if __name__ == "__main__":

    args = parser.parse_args()

    files = []
    print('The following files have been found:')
    for file in os.listdir(args.path):
        files.append(file)

    print(files)
    print('Making it a total of ' + str(len(files)) + ' files')
    print('Converting files...')

    process_files(args)