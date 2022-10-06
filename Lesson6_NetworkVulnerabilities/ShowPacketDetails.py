# In an imaginary protocol stack, the header structures are as follows:
#
# Layer 1 has the following structure:
# The first  4  bytes are the ID of the sender
# The next  4  bytes are the ID of the receiver
# The next  4  bytes are the size of the content (let's call it  n )
# The next  n  bytes are the content
# Layer 2 has the following header and footer:
# The first  4  bytes are the session ID
# The last  4  bytes are a checksum of the message
# The middle bytes are the content
# Layer 3 has the following structure:
# The first  4  bytes are the message ID
# The rest of the bytes are the message
# here is a message captured on the wire, that was sent using this protocol stack.
#
# Write a Python program to decode the captured message and print out the contents of the following fields:
# sender ID, message ID, message text, and the checksum.
#
# Note that all the IDs and numbers in the message are unsigned  4 -byte integers, encoded in little endian format.
# You need to print and submit them as normal (decimal) numbers.
import struct
from struct import *
packet = b'\x08\x00\x00\x00\xf6\x01\x00\x00\x24\x00\x00\x00\x03\x00\x00\x00\x0c\x00\x00\x00I think, therefore I am.\xca\xcd\x00\x00'


def show_details():
    sender_ID = packet[:4]
    reciever_ID = packet[4:8]
    n = hex_string_to_int(packet[8:12])
    layer_1_content = packet[12: 12+2*n]

    session_ID = layer_1_content[:4]
    checksum = layer_1_content[-4:]
    layer_2_content = layer_1_content[4:-4]

    message_ID = layer_2_content[:4]
    message_text = layer_2_content[4:]

    print(hex_string_to_int(sender_ID))
    print(hex_string_to_int(message_ID))
    print(str(message_text))
    print(hex_string_to_int(checksum))


def hex_string_to_int(hex_string):
    return struct.unpack("<i", hex_string)[0]


show_details()