### [![Python](https://img.shields.io/badge/Python-3.9%2B-blue)](https://www.python.org/downloads/)  [![Aiogram](https://img.shields.io/badge/aiogram-2.15-blue)](https://pypi.org/project/aiogram/) 

### About
A template for creating bots as quickly as possible. Written on [aiogram](https://github.com/aiogram/aiogram).

### Setting up

#### Preparations
- Update package lists `sudo apt-get update`;
- Make sure Git and docker-compose are installed `apt-get install git docker-compose -y`;
- Clone this repo via `git clone https://github.com/rdfsx/bot_template`;
- Move to the directory `cd bot_template`.

#### Deployment
- Rename `.env.sample` to `.env` and replace a token placeholder and owner id with your own one;
- Start the bot: `sudo docker-compose up --build`.