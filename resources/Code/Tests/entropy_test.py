import unittest
from Analyse import pcap_entropy_analyse
from Analyse import pcap_analyse
import utils
import io

class TestEntropy(unittest.TestCase):
    general_entropy_standard_result = 7.977084
    def test_general_entropy(self):
        analyse = pcap_analyse.PcapAnalyse(utils.get_pcap_file_path('https'), 'https')
        result = pcap_entropy_analyse.calculate_general_entropy(analyse)
        delta = abs(self.general_entropy_standard_result - result)
        self.assertLessEqual(delta, 0.2, f'[Test failed]: {result} has error {delta} > 0.1')
if __name__ == '__main__':
    unittest.main()