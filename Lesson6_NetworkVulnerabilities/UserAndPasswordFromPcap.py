# In the following hackxercise, use scapy to read the pcap file,
# which is a recording of some network traffic captured with a sniffer (namely, Wireshark),
# and figure out what is the username and the password.

from scapy.all import *
from scapy.layers.http import *
import sys # ignore
sys.path.insert(0,'.') # ignore
from create_recording import recording_path # the path to the pcap file of this assignment


def show_username_password():
    bind_layers(TCP, HTTP, dport=8000)
    bind_layers(TCP, HTTP, sport=8000)
    packets = rdpcap(recording_path)
    for packet in packets:
        app_layer = packet[Http]


show_username_password()