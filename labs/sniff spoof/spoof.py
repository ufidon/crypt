#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *

print("--- sending spoofing ICMP packets ---")
IPLayer = IP()
IPLayer.src = '10.0.2.8'
IPLayer.dst = '8.8.4.4'
ICMPpkt = ICMP()
pkt = IPLayer / ICMPpkt
pkt.show()
send(pkt,verbose=0)

