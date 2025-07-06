
#!/usr/bin/env python3
"""
MGQP (Multiplayer Game QUIC Protocol) - Server
CS 544 - Computer Networks
Author: Jhitesh Guptha
"""

import socket
import threading
import struct
import logging
from enum import IntEnum
from dataclasses import dataclass

# Setup logging
logging.basicConfig(level=logging.INFO, format='[SERVER] %(asctime)s - %(message)s')
logger = logging.getLogger(__name__)

# Message types for protocol
class MessageType(IntEnum):
    SESSION_REQUEST = 0x01
    SESSION_RESPONSE = 0x02
    ERROR = 0x0B

# DFA-like server states
class ServerState(IntEnum):
    LISTENING = 1
    VALIDATING = 2
    SESSION_ACTIVE = 3
    TERMINATING = 4

@dataclass
class ClientSession:
    address: tuple
    state: ServerState

# Store sessions
sessions = {}

def handle_client(sock):
    while True:
        try:
            data, addr = sock.recvfrom(1024)
            if addr not in sessions:
                sessions[addr] = ClientSession(address=addr, state=ServerState.LISTENING)
            session = sessions[addr]

            if not data:
                continue

            msg_type = data[0]
            logger.info(f"Received msg type {msg_type} from {addr}")

            if msg_type == MessageType.SESSION_REQUEST:
                if session.state == ServerState.LISTENING:
                    session.state = ServerState.VALIDATING
                    logger.info(f"Validating client {addr}")

                    response = struct.pack('B', MessageType.SESSION_RESPONSE)
                    sock.sendto(response, addr)
                    session.state = ServerState.SESSION_ACTIVE
                    logger.info(f"Session established with {addr}")

            else:
                logger.warning(f"Unhandled message type {msg_type} from {addr}")

        except Exception as e:
            logger.error(f"Error: {e}")

def main():
    host = "localhost"
    port = 12345
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind((host, port))
    logger.info(f"Server listening on {host}:{port}")

    handle_client(sock)

if __name__ == "__main__":
    main()
