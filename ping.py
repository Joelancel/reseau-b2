from scapy.all import *
from scapy.layers.inet import ICMP, IP
from scapy.layers.l2 import Ether


ping = ICMP(type=8)
packet = IP(src="10.33.76.181", dst="10.0.0.1")
frame = Ether(src="F8-89-D2-E7-0B-5F", dst="0A-00-27-00-00-12")

final_frame = frame/packet/ping
answers, unanswered_packets = srp(final_frame, timeout=10)
print(f"Pong reçu : {answers[0]}")
