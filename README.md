# MGQP - Multiplayer Game QUIC Protocol

## Author  
Jhitesh Guptha

## Course  
CS 544 - Network Protocol Design

## Overview  
This project implements a custom, lightweight multiplayer game protocol inspired by QUIC using Python sockets over UDP. It demonstrates a basic handshake mechanism between a client and a server with clearly defined states and message types.

## Files  
- `Server.py`: Server-side script to accept and validate client session requests  
- `Client.py`: Client-side script to initiate the session with the server  
- `README.md`: Project documentation and explanation of DFA usage in the protocol  

## How to Run  
1. Start the server in one terminal:  
   ```bash
   python3 Server.py
   ```  
2. Start the client in another terminal:  
   ```bash
   python3 Client.py
   ```  

## DFA Implementation  
This project includes a DFA-based state transition system for both client and server.  

### Client DFA States:  
1. **IDLE**: The client has not yet initiated communication  
2. **CONNECTING**: The client has sent a SESSION_REQUEST and is awaiting a response  
3. **ACTIVE**: The client has received a SESSION_RESPONSE and the session is active  

#### Transitions:  
- `IDLE → CONNECTING`: Upon sending SESSION_REQUEST  
- `CONNECTING → ACTIVE`: Upon receiving SESSION_RESPONSE  

### Server DFA States:  
1. **LISTENING**: The server is waiting for a client request  
2. **VALIDATING**: The server received SESSION_REQUEST and is validating  
3. **SESSION_ACTIVE**: Server has accepted and established the session  

#### Transitions:  
- `LISTENING → VALIDATING`: Upon receiving SESSION_REQUEST  
- `VALIDATING → SESSION_ACTIVE`: Upon sending SESSION_RESPONSE  

## Purpose of DFA  
Using a deterministic finite automaton (DFA) structure ensures that message processing on both ends adheres to a defined stateful protocol flow, avoiding undefined behaviors and enforcing protocol correctness.
