# its350
course materials and references for its350

## Lab11: Packet Sniffing and Spoofing

### Description
**This lab is adapted from [SEED Packet Sniffing and Spoofing Lab](https://seedsecuritylabs.org/Labs\_16.04/Networking/Sniffing\_Spoofing/)**

Packet sniffing and spoofing are two important concepts in network security; they are two major threats
in network communication. Being able to understand these two threats is essential for understanding security
measures in networking. 

There are many packet sniffing and spoofing tools, such as [Wireshark](https://en.wikipedia.org/wiki/Wireshark), [Scapy](https://en.wikipedia.org/wiki/Scapy), [Tcpdump](https://en.wikipedia.org/wiki/Tcpdump), etc. Some of these tools are widely used by security experts, as well as by attackers. Being able to use these tools is important for students, but what is more important for students in a network security course is to understand how these tools work, i.e., how packet sniffing and spoofing are implemented in software.

The objective of this lab is two-fold: learning to use the tools and understanding the technologies underlying
these tools. For the second object, students will write simple sniffer and spoofing programs, and gain an in-depth understanding of the technical aspects of these programs. This lab exploits [Scapy](https://en.wikipedia.org/wiki/Scapy) for sniffing and spoofing.

**Preparation:** Use TWO  SEED VMs from the three VMs setup in Lab01,  and connect them to the same NAT network if you don't have. Their IPv4 settings can be static or dynamic. In the network setting, each VM's **'Promiscuous mode'** should be 'Allow All' so they can capture all packets passing their NAT network. Choose one VM as the attacker machine <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/>  and the other as the victim machine <!-- $ V\!M_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/nNZaRSbpGS.svg"/>.

#### Task1 (20%): Network information
In this task, find the network information and make sure your VMs can communicate with each other and can access Internet.
**Two VMs are needed:**

* use command below to find the IP settings for each VM, make sure all VMs can communicate (ping) with each other and access the Internet.

```bash
ifconfig -a
# or 
ip addr
```
* make a file whose file name can identify the VM at home folder, e.g. <!-- $ V\!M_{attack}:I\!P_{attack},V\!M_{victim}:I\!P_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/cScNVHRb09.svg"/>, replace these IPs with your real IP addresses through out this lab.


#### Task2 (20%): Use Scapy
To use Scapy in a Python3 program, execute this program using Python3. Use subl to create a simple program named as 'myscapy.py' as below.  We should run Python3 using the root privilege because the privilege is required for sniffing and spoofing packets.

```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-
from scapy.all import *

a = IP()
a.show()
```

* Run the program without root privilege in command line:
```bash
python3 myscapy.py
```
What do you observe?

* Run the program with root privilege in command line:
```bash
sudo python3 myscapy.py
```
What do you observe?


#### Task3 (60%) Packet sniffing and spoofing
With the Python source code files provided, complete the following tasks. Run all programs with root privilege.

##### Task 3.1: Sniffing Packets  (15%) 
Scapy can sniff only certain types of packets by setting filters in sniffing. Scapy’s filter use the BPF (Berkeley Packet Filter) syntax. 
Use subl open the provided Python3 program [sniffer.py](./sniffspoof/sniffer.py), set the BPF filter  as below respectively. In this task, edit and run sniffing programs in <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/> and carry out network activities in <!-- $ V\!M_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/nNZaRSbpGS.svg"/>.

1. Capture only the ICMP packets: filter = 'icmp'. 
In <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/>, open  'sniffer.py' in subl, uncomment line 11, comment line 12 and 13, then save it as 'sniff-icmp.py' and run it, don't stop it.
In <!-- $ V\!M_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/nNZaRSbpGS.svg"/>, open a new terminal window, run command 
```bash
ping -c 2 google.com 
```
Go back to <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/> and record your observation on the sniffing terminal.

2. Capture any TCP packet that come from a particular IP and with a destination port number 23: filter = 'tcp and (src host <!-- $ I\!P_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/ONuIgXJIoI.svg"/> and dst port 23)'

In <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/>, open 'sniffer.py' in subl, uncomment line 12 and replace <!-- $ I\!P_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/ONuIgXJIoI.svg"/> your <!-- $ V\!M_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/nNZaRSbpGS.svg"/>'s IP address, comment line 11 and 13, then save it as 'sniff-tcp.py' and run it, don't stop it.

In <!-- $ V\!M_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/nNZaRSbpGS.svg"/>, open a new terminal window, run command 

<div style="background-color:tomato;outline-style: solid;outline-color:red;outline-width:2px">
telnet <!-- $ I\!P_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/MQ9z0nuaXz.svg"/>
</div>

Go back to <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/> and 	record your observation on the sniffing terminal.

1. Capture packets come from or go to a particular subnet. You may pick any subnets, such as 8.8.4.0/24. But you should not pick the subnet that your VM attached: filter = 'net 8.8.4.0/24'.

In <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/>, open 'sniffer.py' in subl, uncomment line 13, comment line 11 and 12, then save it as 'sniff-subnet.py' and run it, don't stop it.

In <!-- $ V\!M_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/nNZaRSbpGS.svg"/>, open a new terminal window, run command 
```bash
ping -c 2 8.8.4.4
``` 
Go back to <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/> and 	record your observation on the sniffing terminal.


##### Task 3.2: Spoofing ICMP Packets  (15%)
As a packet spoofing tool, Scapy can set the fields of IP packets to arbitrary values.  The objective of this task is to spoof IP packets with an arbitrary source IP address.  We will spoof ICMP echo request packets, and send them to the Google domain name server with IP address '8.8.4.4' on be half of the spoofed or victim VM. Run  Wireshark on the victim VM to observe whether the spoofed request is accepted by the Google DNS. If it is accepted, an echo reply packet will be sent to the spoofed IP address, i.e. the victim machine, which will be captured in Wireshark.

* On <!-- $ V\!M_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/nNZaRSbpGS.svg"/>, run Wireshark and start capture
* On <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/>, open the provided Python3 program [spoof.py](./sniffspoof/spoof.py) in subl, in line 8, replace the IP address with <!-- $ I\!P_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/ONuIgXJIoI.svg"/>, save it as 'spoof-vm2.py' and run it
* Go back to <!-- $ V\!M_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/nNZaRSbpGS.svg"/>, observed the captured packets in Wireshark and identify the echo reply packets.


##### Task 3.3: Traceroute  (15%)
Scapy can be used to estimate the distance, in terms of number of routers, between your VM and a selected Internet server, which is similar to the 'traceroute' command.  The idea is quite straightforward: just send an packet (any type) to the destination, with its Time-To-Live (TTL) field set to 1 first. This packet will be dropped by the first router, which will back an ICMP error message, telling  that the time-to-live has exceeded. That is how to get the IP address of the first router.  Then increase the TTL field to 2, send out, and get the IP address of the second router. Repeat this procedure until the packet finally reach the destination. It should be noted that this experiment only gets an estimated result, because in theory, not all these packets take the same route.
the victim machine, which will be captured in Wireshark.

* On <!-- $ V\!M_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/nNZaRSbpGS.svg"/>, run Wireshark and start capture
* On <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/>, run command 
```bash
traceroute 8.8.4.4
```
and record the result.
* On <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/>, run the provided Python3 program 'traceroute.py' as 
```bash
sudo python3 traceroute.py 8.8.4.4 
```
and record the result.
* Go back to <!-- $ V\!M_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/nNZaRSbpGS.svg"/>, observed the captured packets in Wireshark and identify the echo reply packets for 'traceroute' and 'traceroute.py' respectively


##### Task 3.4: Sniffing and-then Spoofing  (15%)
Usually, a hacker pings a server to determine it is alive or dead.  If the server is alive, the ping program will receive and print an echo reply.
 
In this task, combine the sniffing and spoofing techniques to implement the following sniff-and-then-spoof program. 

The provided sniff-and-then-spoof program runs on <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/>, which monitors the LAN through packet sniffing.  Whenever it sees an ICMP echo request, regardless of what the target IP address is, your program should immediately send out an echo reply using the packet spoofing technique. Therefore, regardless of whether the server is alive or not, the ping program will always receive a reply, indicating that the server is alive.


* In <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/>, open the provided Python program 'sniffspoof.py', in line 31, replace the IP address with <!-- $ I\!P_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/ONuIgXJIoI.svg"/> and save the modified file as 'tease-vm2.py' then run it and keep it running
* In <!-- $ V\!M_{victim} $ --> <img style="transform: translateY(0.25em);" src="../../svg/nNZaRSbpGS.svg"/>, run command 
```bash
ping -c 2 8.8.4.4
``` 
and record your observation. Could you explain the result?
* Go back to <!-- $ V\!M_{attack} $ --> <img style="transform: translateY(0.25em);" src="../../svg/gGkN0bRu8i.svg"/>,  record your observation. Could you explain the result?

#### Help
For BPF(Berkeley Packet Filter) syntax, please refer to [CaptureFilters](https://wiki.wireshark.org/CaptureFilters), [Filtering while capturing](https://www.wireshark.org/docs/wsug\_html\_chunked/ChCapCaptureFilterSection.html), [WIRESHARK DISPLAY FILTERS](./papers/Wireshark\_Display\_Filters.pdf), [PCAP-FILTER](https://www.wireshark.org/docs/man-pages/pcap-filter.html).

For further information refer to the seed lab [SEED Packet Sniffing and Spoofing Lab](https://seedsecuritylabs.org/Labs\_16.04/Networking/Sniffing\_Spoofing/).	


### Report

Write a report about the process you complete the tasks in the description, key screen snapshots are needed as evidences.


### References
* [SEED Packet Sniffing and Spoofing Lab](https://seedsecuritylabs.org/Labs\_16.04/Networking/Sniffing\_Spoofing/)
* [Scapy](https://en.wikipedia.org/wiki/Scapy)
  * [Scapy](https://scapy.net/)
* [Wireshark](https://en.wikipedia.org/wiki/Wireshark)
  * [Wireshark](https://www.wireshark.org/) 
* [Tcpdump](https://en.wikipedia.org/wiki/Tcpdump)
  * [Tcpdump](https://www.tcpdump.org/)
* [CaptureFilters](https://wiki.wireshark.org/CaptureFilters)
* [Filtering while capturing](https://www.wireshark.org/docs/wsug\_html\_chunked/ChCapCaptureFilterSection.html)
* [WIRESHARK DISPLAY FILTERS](./papers/Wireshark\_Display\_Filters.pdf)
* [PCAP-FILTER](https://www.wireshark.org/docs/man-pages/pcap-filter.html)
* [pcap-filter](https://linux.die.net/man/7/pcap-filter)