# Network-Packet-Sniffer-and-Analyzer
Here's a simple and practical Packet Sniffer project using Python, with an optional C implementation idea afterward. This project demonstrates capturing and analyzing packets at a basic level — ideal for a cybersecurity/networking portfolio.

# 🕵️‍♂️ Packet Sniffer in Python

A basic network packet sniffer built with Python using raw sockets. It captures Ethernet frames and prints protocol headers such as IP, TCP, UDP, and ICMP.

## 📌 Features

- Captures raw Ethernet frames
- Parses and displays:
  - MAC addresses
  - IP header info (source, destination, TTL, protocol)
  - TCP/UDP/ICMP headers
- Supports protocol filtering and logging
- Terminal-based interface (optional GUI extension)

## 🛠️ Tech Stack

- **Language**: Python 3
- **Libraries**: `socket`, `struct`, `os`
- **Platform**: Linux/macOS (requires raw socket support)

## 🔒 Requirements

- Python 3.x
- Admin privileges (run with `sudo`)
- Linux or WSL (Windows raw sockets are limited)

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone https://github.com/yourusername/packet-sniffer.git
cd packet-sniffer
