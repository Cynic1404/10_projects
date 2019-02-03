from time import sleep
from datetime import datetime as dt
host_path = "C:\Windows\System32\drivers\etc\hosts"
temp_path = "hosts"
redirect = "127.0.0.1"
website_list = ["www.facebook.com", "www.4pda.ru", "www.vk.com"]


with open(host_path, "r+") as file:
    content = file.readlines()
    file.seek(0)
    for line in content:
        if not any(website in line for website in website_list):
            file.write(line)
    file.truncate()
quit()
