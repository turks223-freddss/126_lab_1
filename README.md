# How to Run the OSI Model Simulation

## Steps to Run:
1. Open **two terminal windows**.
2. In the **first terminal**, start server using : python main.py server
3. in the **2nf terminal**, start client using: python main.py client



# 126_lab_1
Lab 1: Simulating the OSI Model from Scratch in Python
Objective
Students will recreate a simplified OSI model using Python. Each layer will be a separate Python module or class, and data must move through all seven layers to simulate real-world network communication.
Physical Layer: Simulated using Python sockets and bit-level operations.
Data Link Layer: Implements a MAC addressing system and frame transmission.
Network Layer: Simulates IP addressing and packet routing.
Transport Layer: Implements TCP-like packet sequencing and error handling.
Session Layer: Manages connection states and synchronization.
Presentation Layer: Handles encryption, compression, and encoding.
Application Layer: Implements HTTP-like request-response communication.

Constraints
No use of existing network libraries (no Flask, Django, FastAPI, or requests).
Must use only low-level Python features (e.g., socket, struct, pickle, json).
Must correctly simulate all seven OSI layers.

Implementation Plan

Each layer will be a separate Python class that takes data from the previous layer, processes it, and passes it down (for sending) or up (for receiving).

Submission
Please submit your Github link.

Rubric:
This will be graded manually and will be evaluated according to the following criteria: 
Program Correctness 50 % 
Clarity & Readability of Code 20 % 
Program Modularity 15 % 
Cost Effectiveness(Simplicity) 15 % 
TOTAL 100 %

Program Correctness:
The program meets all functional requirements.

Clarity & Readability of Code:
Code is well-structured and easy to understand.
Uses meaningful variable and function names that reflect their purpose.
Includes relevant comments where necessary to explain complex logic.

 Program modularity:
The program is divided into well-defined functions or modules instead of one long script.
Code avoids redundancy by implementing reusable components.

Cost Effectiveness (Simplicity):
The solution is efficient and avoids unnecessary complexity.
Uses optimal data structures and algorithms to improve performance.
