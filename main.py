import discord
import asyncio
import requests
import threading
import sys
import os
from typing import Optional
from colorama import Fore
import time

def Clear():
  if sys.platform in ["linux", "linux2"]:
    os.system("clear")
  else:
    os.system("cls")

Clear()

def setTitle(title: Optional[any]=None):
  os.system(f"title {title}")

setTitle("Multiple Token Hoster - [KaramveerPlayZ#1337]")

session = requests.Session()
tokens = []
with open("tokens.txt", "r") as f:
  tokens_ = f.read().split("\n")

if len(tokens_) == 0:
  print("KaramveerPlayZ#1337 | They're Are No Tokens, Please Add Some Tokens To Host In tokens.txt File.")
  exit()

def Check_Token(Token):
  response = requests.get(f"https://discord.com/api/v9/users/@me", headers={"Authorization": Token})
  if response.status_code in [204, 200, 201]:
    print(f"KaramveerPlayZ#1337 | {Token} Is Vaild.")
    tokens.append(Token)
  if "need to verify" in response.text:
    print(f"KaramveerPlayZ#1337 | {Token} Is On Verification.")
  elif response.status_code in [404, 401, 400]:
    print(f"KaramveerPlayZ#1337 | {Token} Invaild Token Or Rate Limited.")

for tk in tokens_:
  Check_Token(tk)


if len(tokens) == 0:
  print("KaramveerPlayZ#1337 | All Tokens Were Invaild, Try Again Later With Working Tokens.")
  exit()

time.sleep(2)
Clear()
menu = f"""{Fore.RED}[-]{Fore.RESET} Created by KaramveerPlayZ#1337\n"""

print(menu)

st = input('KaramveerPlayZ#1337 | Accounts Status Idle, Dnd, Online, Mobile: ')
akks = []
stl = st.lower()
if stl == "dnd":
  status = discord.Status.dnd
elif stl == "idle":
  status = discord.Status.idle
elif stl == "online":
  status = discord.Status.online
ty = input("KaramveerPlayZ#1337 | Activity Type Playing, Streaming, Listening, Watching: ")
tyy = ty.lower()
if tyy == "streaming":
  name = input("KaramveerPlayZ#1337 | Streaming Name: ")
  acttt = discord.Streaming(name=name, url="https:/twitch/KaramveerPlayZ")
elif tyy == "playing":
  name = input("KaramveerPlayZ#1337 | Playing Name: ")
  acttt = discord.Game(name=name)
elif tyy == "listening":
  name = input("KaramveerPlayZ#1337 | Listening Name: ")
  acttt=discord.Activity(type=discord.ActivityType.listening, name=name)
elif tyy == "watching":
  name = input("KaramveerPlayZ#1337 | Watching Name: ")
  acttt=discord.Activity(type=discord.ActivityType.watching, name=name)
loop = asyncio.get_event_loop()
for tk in tokens:
  client = discord.Client(status=status, activity=acttt)
  loop.create_task(client.start(tk, bot=False))
  akks.append(client)
  print(" ")
  print("KaramveerPlayZ#1337 | {} Is Hosted.\n".format(tk))

threading.Thread(target=loop.run_forever).start()

while True:
  idk = 0
  idk += 1
