from scapy.all import sniff, DNSQR

def packet_callback(packet):
    if packet.haslayer(DNSQR):
        domain = packet[DNSQR].qname.decode(errors="ignore").rstrip(".")
        print("DNS Query Captured:", domain)

print("Listening on loopback...\n")
sniff(iface="lo", filter="udp port 53", prn=packet_callback, store=False)
