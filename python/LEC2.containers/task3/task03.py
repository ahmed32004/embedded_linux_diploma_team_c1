#!/usr/bin/python3

import requests

# def get_public_ip():
#     url = "https://api.ipify.org?format=json"
#     response = requests.get(url)
#     if response.status_code == 200:
#         ip_data = response.json()
#         public_ip = ip_data["ip"]
#         return public_ip
#     else:
#         return None

# # Get the public IP address
# public_ip = get_public_ip()
# if public_ip:
#     print("Your public IP address is:", public_ip)
# else:
#     print("Failed to retrieve public IP address.")
    
    
ip_url = requests.get("https://api.ipify.org/?format=json")
print(f"My IP is:: {ip_url.json()['ip']}")
    
    
    