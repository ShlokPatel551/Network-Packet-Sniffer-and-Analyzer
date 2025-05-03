#include <pcap.h>
#include <stdio.h>

void callback(u_char *args, const struct pcap_pkthdr *header, const u_char *packet) {
    printf("Packet captured: Length: %d\n", header->len);
}

int main() {
    char errbuf[PCAP_ERRBUF_SIZE];
    pcap_t *handle = pcap_open_live("eth0", BUFSIZ, 1, 1000, errbuf);

    if (handle == NULL) {
        fprintf(stderr, "Could not open device: %s\n", errbuf);
        return 1;
    }

    pcap_loop(handle, 10, callback, NULL);
    pcap_close(handle);
    return 0;
}
