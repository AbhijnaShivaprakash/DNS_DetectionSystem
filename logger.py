from datetime import datetime

def save_log(domain, fake_ip, action):
    time_now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    with open("logs.txt", "a") as file:
        file.write(f"{time_now} | {domain} | {fake_ip} | {action}\n")

def read_logs():
    with open("logs.txt", "r") as file:
        return file.readlines()
