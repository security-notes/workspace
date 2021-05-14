import os
from scapy.all import rdpcap

pcap = rdpcap(os.path.dirname(__file__)+'/icmp.pcap')

data = [p.load for p in pcap]

with open(os.path.dirname(__file__)+'/flag.jpg','wb') as f:
    for d in data:
        f.write(d)
