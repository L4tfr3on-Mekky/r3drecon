import urllib.parse
import base64
import html
from termcolor import colored

# get the file name from the user
filename = input("Enter the file name: ")

# open the input file for reading
with open(filename, 'r') as f:
    lines = f.readlines()

# encoding options
encoding_options = {
    '1': {'name': 'URL-encoded', 'function': lambda line: urllib.parse.quote(line.strip()) + '\n', 'extension': 'url_encoded', 'color': 'green'},
    '2': {'name': 'Hex-encoded', 'function': lambda line: line.encode().hex() + '\n', 'extension': 'hex_encoded', 'color': 'yellow'},
    '3': {'name': 'Base64-encoded', 'function': lambda line: base64.b64encode(line.strip().encode()).decode() + '\n', 'extension': 'base64_encoded', 'color': 'blue'},
    '4': {'name': 'HTML-encoded', 'function': lambda line: html.escape(line.strip()) + '\n', 'extension': 'html_encoded', 'color': 'magenta'},
    '5': {'name': 'UTF-8-encoded', 'function': lambda line: line.encode('utf-8').decode() + '\n', 'extension': 'utf8_encoded', 'color': 'cyan'},
    '6': {'name': 'UTF-16-encoded', 'function': lambda line: line.encode('utf-16').decode('utf-16') + '\n', 'extension': 'utf16_encoded', 'color': 'yellow'},
    '7': {'name': 'UTF-32-encoded', 'function': lambda line: line.encode('utf-32').decode('utf-32') + '\n', 'extension': 'utf32_encoded', 'color': 'blue'},
    '8': {'name': 'ASCII-encoded', 'function': lambda line: line.encode('ascii', 'ignore').decode('ascii') + '\n', 'extension': 'ascii_encoded', 'color': 'cyan'},
    '9': {'name': 'Unicode-encoded', 'function': lambda line: line.encode('unicode_escape').decode() + '\n', 'extension': 'unicode_encoded', 'color': 'green'},
    '10': {'name': 'All-encoded', 'function': lambda line: '', 'extension': 'all_encoded', 'color': 'red'},
}

# display the encoding options
while True:
    print("Encoding options:")
    for option in encoding_options:
        print(f"{option}: {colored(encoding_options[option]['name'], encoding_options[option]['color'])}")
    print("x: Exit")
    choice = input("Choose an option: ")

    if choice == 'x':
        break

    # validate the choice
    if choice not in encoding_options and choice != '10':
        print(colored("Invalid choice. Please try again.", "red"))
        continue

    # encode the lines
    if choice == '10':
        for option in encoding_options:
            if option == '10':
                continue
            encoded_lines = [encoding_options[option]['function'](line) for line in lines]
            output_file = f"{filename.split('.')[0]}_{encoding_options[option]['extension']}.txt"
            with open(output_file, 'w') as f:
                f.writelines(encoded_lines)
            print(f"{colored(encoding_options[option]['name'], encoding_options[option]['color'])} text saved to {colored(output_file, 'yellow')}")
    else:
        encoded_lines = [encoding_options[choice]['function'](line) for line in lines]
    output_file = f"{filename.split('.')[0]}_{encoding_options[choice]['extension']}.txt"
    with open(output_file, 'w') as f:
        f.writelines(encoded_lines)
        print(f"{encoding_options[choice]['name']} text saved to {output_file}")
    print(f"All text saved to {filename.split('.')[0]}_all_encoded.txt")
