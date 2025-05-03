import socket
import struct

def ethernet_frame(data):
    dest_mac, src_mac, proto = struct.unpack('!6s6sH', data[:14])
    return {
        'dest_mac': get_mac_addr(dest_mac),
        'src_mac': get_mac_addr(src_mac),
        'protocol': socket.htons(proto),
        'data': data[14:]
    }

def get_mac_addr(bytes_addr):
    return ':'.join(format(b, '02x') for b in bytes_addr)

def main():
    conn = socket.socket(socket.AF_PACKET, socket.SOCK_RAW, socket.ntohs(3))
    print("Listening for packets...")
    
    while True:
        raw_data, addr = conn.recvfrom(65535)
        eth = ethernet_frame(raw_data)
        print(f"\nEthernet Frame:\n  Source: {eth['src_mac']}  Destination: {eth['dest_mac']}  Protocol: {eth['protocol']}")

if __name__ == "__main__":
    main()
