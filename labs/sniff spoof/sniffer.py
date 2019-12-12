#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *

print("--- sniffing packets ---")

def print_pkt(pkt):
	pkt.show()

#pkt = sniff(filter='icmp',prn=print_pkt)
#pkt = sniff(filter='tcp and (src host 10.0.2.9 and dst port 23)',prn=print_pkt)
pkt = sniff(filter='net 8.8.4.0/24',prn=print_pkt)