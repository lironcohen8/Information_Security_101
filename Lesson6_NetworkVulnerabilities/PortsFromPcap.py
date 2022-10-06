# In the following hackxercise, use scapy to read the pcap file, which is a recording of some network traffic
# captured with a sniffer (namely, Wireshark), and figure out what is the destination port of the third packet,
# and the source port address in the fourth packet.

from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment

#### Don't change the code until this line ####

def show_source_destination_ports():
    packets = rdpcap(recording_path)
    third_packet = packets[2]
    tcp_layer = third_packet[TCP]
    print(tcp_layer.dport)
    fourth_packet = packets[3]
    tcp_layer = fourth_packet[TCP]
    print(tcp_layer.sport)

show_source_destination_ports()