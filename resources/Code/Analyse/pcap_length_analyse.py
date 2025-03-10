from array import array
from math import trunc

from numpy import dtype

from Analyse.pcap_analyse import PcapAnalyse, Choice
import numpy as np
# class PcapLengthAnalyse(PcapAnalyse):
#     def __init__(self, pcap_file_name):
#         super().__init__(pcap_file_name)
#
#     def occurrence_of_length(self):
#         occurrences = list[int]()
#         for _, payload in self.tcp_payload_with_timestamp:
#             occurrences.append(len(payload))
#         return Counter(occurrences)
#
#     def temporal_statistic_of_length(self):
#         records: list[Tuple[float, int]] = []
#         for ts, payload in self.tcp_payload_with_timestamp:
#             records.append((ts, len(payload)))
#         return records


# Generate a histgram of the occurrence of the length of the TCP payload
# The x-axis is the lengths of the TCP payload (in ranges: bins which has a width of delta)
# The y-axis is the occurrences of the length
def occurrence_histogram(analyse: PcapAnalyse, delta: int):
    occurrences = []
    for _, payload in analyse.tcp_payload_with_timestamp:
        l = len(payload)
        # Filter the zero sized packets
        if l > 0:
            occurrences.append(len(payload))
    assert len(occurrences) > 0, f'Unexpected empty TCP payload in {analyse.pcap_file_name}'
    max_l = max(occurrences)
    min_l = min(occurrences)
    # Prepare np array for plotting

    bins = np.linspace(0, max_l, 60)
    return occurrences, bins

def temporal_length_array(analysis: PcapAnalyse):
    t = analysis.retrieve_tcp_payload_or_timestamp(Choice.TIME_STAMP)
    l = analysis.retrieve_tcp_payload_or_timestamp(Choice.PAYLOAD)
    p = np.array([int(x - analysis.start_ts) for x in t])
    q = np.array([int(len(y)) for y in l])
    # ts = np.asarray(p)
    # length = np.asarray(q)
    # max_l = max(len(ts), len(length))
    # ts.reshape(-1, max_l)
    # length.reshape(-1, max_l)
    return p, q