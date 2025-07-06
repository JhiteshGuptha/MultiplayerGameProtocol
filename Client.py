
#!/usr/bin/env python3
"""
MGQP (Multiplayer Game QUIC Protocol) - Client
CS 544 - Computer Networks
Author: Jhitesh Guptha
"""

import socket
import struct
import logging
from enum import IntEnum

# Setup logging
logging.basicConfig(level=logging.INFO, format='[CLIENT] %(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# Message types for protocol
class MessageType(IntEnum):
    SESSION_REQUEST = 0x01
    SESSION_RESPONSE = 0x02

# DFA-like client states
class ClientState(IntEnum):
    IDLE = 1
    CONNECTING = 2
    ACTIVE = 3

def main():
    server_address = ("localhost", 12345)
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    state = ClientState.IDLE

    try:
        logger.info("Sending SESSION_REQUEST...")
        session_request = struct.pack('B', MessageType.SESSION_REQUEST)
        sock.sendto(session_request, server_address)
        state = ClientState.CONNECTING

        data, _ = sock.recvfrom(1024)
        msg_type = data[0]

        if msg_type == MessageType.SESSION_RESPONSE:
            logger.info("Received SESSION_RESPONSE from server.")
            state = ClientState.ACTIVE

        logger.info(f"Client state: {state.name}")

    except Exception as e:
        logger.error(f"Error: {e}")
    finally:
        sock.close()

if __name__ == "__main__":
    main()
