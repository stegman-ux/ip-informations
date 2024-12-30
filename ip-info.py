import requests
import colorama
import os
from colorama import Fore
import clear
def ip_info(ip_info):
  url = f"http://ip-api.com/json/{ip_address}" # u can use this ip-api for u py script (:
  response = requests.get(url)

  if response.status_code == 200:
    return response.json()
  else:
    return None
os.system("pip install colorama")
os.system("pip install clear")
os.system("pip install requests")
os.system("title ip-info made by intrable")
clear.clear()
art = Fore.RED+'''
██╗██████╗       ██╗███╗   ██╗███████╗ ██████╗ 
██║██╔══██╗      ██║████╗  ██║██╔════╝██╔═══██╗
██║██████╔╝█████╗██║██╔██╗ ██║█████╗  ██║   ██║
██║██╔═══╝ ╚════╝██║██║╚██╗██║██╔══╝  ██║   ██║
██║██║           ██║██║ ╚████║██║     ╚██████╔╝
╚═╝╚═╝           ╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝ 
'''
print(art)
ip_address = input(Fore.RED+"Enter the IP --> : ")
ip_info = ip_info(ip_info)

if ip_info:
  print(Fore.RED+"----------------------------------")
  print(Fore.RED+f"[*]Query --> {ip_address}:")
  print("----------------------------------")
  print(f"[*]Country : {ip_info['country']}")
  print(f"[*]countryCode : {ip_info['countryCode']}")
  print(f"[*]city : {ip_info['city']}")
  print(f"[*]zip code : {ip_info['zip']}")
  print(f"[*]timezone : {ip_info['timezone']}")
  print(f"[*]Org : {ip_info['org']}")
  print(f"[*]region : {ip_info['region']}")
  print(f"[*]RegionName : {ip_info['regionName']}")
  print(f"[*]As : {ip_info['as']}")
  print(f"[*]Latitude : {ip_info['lat']}")
  print(f"[*]Longitude : {ip_info['lon']}")
  print("----------------------------------")
  input("Press enter to return in the menu...")
  clear.clear()
  if os.name =='nt':
      os.system('python ip-info.py')
  else:
      os.system('python3 ip-info.py')
else:
  print(f"Invalid ip : {ip_address}.")
