import os, sys, json
from jsonmerge import merge

def concatCommands(command_files, target_file):
    target_commands=''
    with open(target_file, 'w') as ft:
        for command_file in command_files:
            with open(command_file) as f:
                commands=f.read()
                target_commands+=commands[2:len(commands)-2]
                target_commands+=',\n'
        
        target_commands='[\n'+target_commands[:len(target_commands)-2]+'\n]'
        ft.write(target_commands)
        ft.close()


def findAllCommandFiles(ws_dir):
    command_files=[]
    path=ws_dir
    while True:
        if os.path.exists(os.path.join(path, 'build')):
            build_dir=os.path.join(path, 'build')
            packages=next(os.walk(build_dir))[1]
            print(packages)
            for package in packages:
                command_file=os.path.join(build_dir, package, 'compile_commands.json')
                if os.path.exists(command_file):
                    command_files.append(command_file)

            break

        path=os.path.join(path, os.path.pardir)

    return command_files

if __name__ == "__main__":
    target_file=os.path.join(os.getcwd(), 'compile_commands.json')
    concatCommands(findAllCommandFiles(os.getcwd()), target_file)
