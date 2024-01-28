#!/usr/bin/env python

import scapy.all as scapy

def scan(ip):
    arp_request=scapy.ARP(pdst=ip)
    broadcast=scapy.Ether(dst="FF:FF:FF:FF:FF:FF")
    broadcast_arp_request=broadcast/arp_request
    answered_list=scapy.srp(broadcast_arp_request,timeout=1, verbose=False)[0]

    print("IP \t\t\t\t\t MAC ADDRESS\n-----------------------------------------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t\t\t" + element[1].hwsrc)



scan("192.168.228.1/24")