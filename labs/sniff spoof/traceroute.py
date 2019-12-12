#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *
''' Usage: sudo ./traceroute.py "host name or ip address" '''

host = sys.argv[1]
print("Traceroute " + host)
ttl = 1
while 1:
	IPLayer = IP()
	IPLayer.dst = host
	IPLayer.ttl = ttl
	ICMPpkt = ICMP()
	pkt = IPLayer / ICMPpkt
	
	# sends packets and waits for first response
	replypkt = sr1(pkt, verbose=0)
	if replypkt is None:
		break
	elif replypkt[ICMP].type == 0:
		print(str(ttl)+" hops away: " + replypkt[IP].src)
		print("Done " + replypkt[IP].src)
		break
	else:
		print(str(ttl)+" hops away: " + replypkt[IP].src)
		ttl += 1


