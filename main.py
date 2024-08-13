import sys
import subprocess
sys.path.append("ex")

from ex import extract_data, scrape_util

def run(commands, output_file):
    results = {}
    with open(output_file, 'w') as file:
        for command in commands:
            print(f"Running command:\n{command}")
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = result.stdout.strip()
            results[command] = output
            file.write(f"Command: {command}\nOutput:\n{output}\n\n")
    return results

def main():
    res = extract_data.do_request("http://103.127.135.93:8080/")
    scrape_util.save_url(res, 'data.txt', "--batch --level 3 --risk 3")

    f = open('command.txt', 'r').readlines()
    f = [i.rstrip() for i in f]
    
    commands = open('command.txt', 'r').readlines()
    commands = [c.rstrip() for c in commands]

    output_file = 'command_outputs.txt'
    outputs = run(commands, output_file)
    
if __name__ == "__main__":
    main()


