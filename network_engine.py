import time
import random
import config
from logger import save_log
from detector import detect_suspicious_activity

def start_system():
    config.SYSTEM_STATUS = True
    print("Advanced DNS Monitoring System Started...\n")

    domain_list = list(config.TARGET_DOMAINS.keys())

    while config.SYSTEM_STATUS:
        time.sleep(3)

        config.PACKETS_CAPTURED += 1

        domain = random.choice(domain_list)
        fake_ip = config.TARGET_DOMAINS[domain]

        print(f"Captured DNS request for: {domain}")

        config.SPOOF_COUNT += 1
        print(f"Spoofed {domain} to {fake_ip}")

        save_log(domain, fake_ip, "Redirected")

        alert = detect_suspicious_activity(domain, config.PACKETS_CAPTURED)
        print(alert)

        print(f"Packets Captured: {config.PACKETS_CAPTURED}")
        print(f"Total Spoofed: {config.SPOOF_COUNT}")
        print("-" * 40)

def stop_system():
    config.SYSTEM_STATUS = False
