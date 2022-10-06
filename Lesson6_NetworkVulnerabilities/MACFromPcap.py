# Within the following codeboard we prepared a pcap file for you -
# that is, a traffic capture file collected by wireshark.
# Your task is to process this file,and extract the source MAC address of the 3rd captured packet.
#
# To do this, you should use the scapy python package, which can process pcap files (among many other things it can do).


from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment


def show_mac_address():
    packets = rdpcap(recording_path)
    third_packet = packets[2]
    eth_layer = third_packet[Ether]
    print(eth_layer.src)

show_mac_address()
