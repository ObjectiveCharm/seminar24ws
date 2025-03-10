
import dpkt
import io
import os
from typing import List, Tuple, Union
from enum import Enum

class Choice(Enum):
    TIME_STAMP = 0
    PAYLOAD = 1

class PcapAnalyse:
    pcap_file_name: str = None
    pcap_file_path: os.path = None
    pcap_file_data = None
    # MARK: Decoded TCP Payload with Timestamp
    tcp_payload_with_timestamp: List[Tuple[float, bytearray]] = None
    start_ts: float = None
    end_ts: float = None
    protocol_name: str = None

    def __init__(self, path:os.path, protocol_name:str):
        self.pcap_file_path = path
        self.pcap_file_name = os.path.basename(path)
        pkts = read_pkts(path)
        self.protocol_name = protocol_name
        self.pcap_file_data = pkts
        self.tcp_payload_with_timestamp = retrieve_tcp_payload_with_timestamp(pkts, self.pcap_file_name)
        self.start_ts = float(pkts[0][0])
        self.end_ts = float(pkts[-1][0])


    def retrieve_tcp_payload_or_timestamp(self, choice: Choice) -> List[
        Union[float, bytearray]]:
        if choice == Choice.TIME_STAMP:
            return [x[Choice.TIME_STAMP.value] for x in self.tcp_payload_with_timestamp]
        else:
            return [x[Choice.PAYLOAD.value] for x in self.tcp_payload_with_timestamp]

def read_pkts(pcap_file_path: os.path):
    with io.open(pcap_file_path, 'rb') as f:
        pkts = dpkt.pcap.Reader(f).readpkts()
    return pkts

def retrieve_tcp_payload_with_timestamp(pcapfile, pcap_file_name) -> List[Tuple[float, bytearray]]:
    l: List[Tuple[float, bytearray]] = []
    for ts, buff in pcapfile:
        # Initialize ETH Packet from pcap_buff
        eth = dpkt.ethernet.Ethernet(buff)
        # First retrieve IP Packet from Ethernet Packet
        if len(eth.data) == 0:
            continue
        ip = eth.data
        assert isinstance(ip, dpkt.ip.IP), f'Unknown non IP datatype {eth.data.__class__} in {pcap_file_name}'

        payload_bytes = None
        # Then retrieve TCP Packet from IP Packet
        # Check for TCP in the transport layer
        if len(ip.data) == 0:
            continue
        if isinstance(ip.data, dpkt.tcp.TCP):
            tcp = ip.data
            payload_bytes = tcp.data
        assert payload_bytes is not None, f'Unknown non TCP datatype {ip.data.__class__} in {pcap_file_name}'
        l.append((float(ts), bytearray(payload_bytes)))
    return l

