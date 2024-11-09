
from collections import Counter
import math
import numpy as np
import functools
import io
import utils

from Analyse.pcap_analyse import PcapAnalyse, Choice
# class PcapEntropyAnalyse(pcap_analyse.PcapAnalyse):
#     def __init__(self, pcap_file_name):
#         super().__init__(pcap_file_name)
#
#     temporal_record_per_packet: List[Tuple[float, float]] = []
#     temporal_record_with_time: List[Tuple[float, float]] = []
#     general_entropy: float = 0
#     highest_entropy: float = 0
#     lowest_entropy: float = 0
#
#     @staticmethod
#     def _calculate_entropy(data) -> float:
#         total = len(data)
#         occurrences = Counter(data)
#         accum = 0
#         for count in occurrences.values():
#             probability = count / total
#             accum -= probability * math.log2(probability)
#         return accum
#
#     """
#         I amalgamate the methods which calculate the general entropy, temporal entropy and high/lowest entropy of the file,
#         so all these calculation can be finished in one run
#         Call it after initialisation this class, and it will store all the results in the class
#     """
#     def calculate_properties(self):
#         record_per_packet: List[tuple[float, float]] = []
#         record_with_time: List[tuple[float, float]] = []
#         accum_payload = bytearray()
#         highest_entropy = 0
#         lowest_entropy = 0
#         for i in range(0, len(self.tcp_payload_with_timestamp)):
#             current_payload = self.tcp_payload_with_timestamp[i][1]
#             current_timestamp = self.tcp_payload_with_timestamp[i][0]
#             accum_payload += current_payload
#             record_per_packet.append((current_timestamp, PcapEntropyAnalyse._calculate_entropy(current_payload)))
#             record_with_time.append((current_timestamp, PcapEntropyAnalyse._calculate_entropy(accum_payload)))
#         self.general_entropy = PcapEntropyAnalyse._calculate_entropy(accum_payload)
#         self.highest_entropy = highest_entropy
#         self.lowest_entropy = lowest_entropy
#         self.temporal_record_with_time = record_with_time
#         self.temporal_record_per_packet = record_per_packet

def calculate_entropy_of_data(data: bytearray) -> float:
    total = len(data)
    occurrences = Counter(data)
    accum = 0
    for count in occurrences.values():
        probability = float(count / total)
        accum -= probability * math.log2(probability)
    return accum

def calculate_entropy_per_packet(analyse: PcapAnalyse):
    ts = analyse.retrieve_tcp_payload_or_timestamp(Choice.TIME_STAMP)
    # x-axis: time
    # Because the duration of recording is 120 seconds, so we should set tick to divide x-axis into 120 parts
    array_ts = np.array([float(i - ts[0]) for i in ts])
    # y-axis: entropy
    data = analyse.retrieve_tcp_payload_or_timestamp(Choice.PAYLOAD)
    array_data = np.array([calculate_entropy_of_data(i) for i in data])
    return array_ts, array_data

def calculate_general_entropy(analyse: PcapAnalyse) -> float:
    amalgamated_payload = bytearray()
    for _, buff in analyse.tcp_payload_with_timestamp:
        amalgamated_payload += buff
    # if __debug__:
    #     with io.open(utils.get_result_file_path('httpspayload',extension='bin'), mode='wb') as f:
    #         f.write(amalgamated_payload)
    return calculate_entropy_of_data(amalgamated_payload)
