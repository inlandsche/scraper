import subprocess

def run_commands_and_save_output(commands, output_file):
    results = {}
    with open(output_file, 'w') as file:
        for command in commands:
            print(f"Running command:\n{command}")
            result = subprocess.run(command, shell=True, capture_output=True, text=True)
            output = result.stdout.strip()
            results[command] = output
            file.write(f"Command: {command}\nOutput:\n{output}\n\n")
    return results

commands = open('command.txt', 'r').readlines()
commands = [c.rstrip() for c in commands]

output_file = 'command_outputs.txt'
outputs = run_commands_and_save_output(commands, output_file)

