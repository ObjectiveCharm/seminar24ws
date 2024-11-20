from Visualisation.entropy_statistics_visualization import plot_entropy_statistic_in_temporal_domain, \
    plot_single_temporal_entropy_statistic_of_protocol_in_temporal_domain
from utils import get_pcap_file_path, get_result_file_path
from Analyse.pcap_analyse import PcapAnalyse
from Analyse.pcap_entropy_analyse import calculate_entropy_of_data, calculate_general_entropy
from Visualisation.length_statistics_visualization import plot_occurrence_of_length, \
    plot_length_statistic_in_temporal_domain, plot_single_occurrence_of_length, \
    plot_single_length_statistic_in_temporal_domain
import sys
protocols = ['naiveproxy', 'trojan', 'shadowsocks', 'obfs4', 'https']

analyses = [PcapAnalyse(get_pcap_file_path(protocol), protocol) for protocol in protocols]



def main():
    s = split()
    entropy_occurrence_statistic_and_analyse(s)

    length_statistic_in_temporal_domain(s)

    entropy_statistic_in_temporal_domain(s)

    get_general_entropy()

def split():
    s = False
    if len(sys.argv) > 1:
        argument = sys.argv[1]
        s = argument == '--split-output-figure' or argument == '-s'
    return s

def entropy_occurrence_statistic_and_analyse(split: bool):
    print('Start [entropy occurrence statistic and analyse]')
    d = get_kwargs()
    if split:
        for protocol_name, analyse in d.items():
            result_path = get_result_file_path(f'occurrence_of_length_{protocol_name}')
            plot_single_occurrence_of_length(result_path, analyse)
            print(f'Plot saved at {result_path}')
    else:
        result_path = get_result_file_path('occurrence_of_length')
        plot_occurrence_of_length(result_path, **d)
        print(f'Plot saved at {result_path}')
    print('End [entropy occurrence statistic and analyse]')

def length_statistic_in_temporal_domain(split: bool):
    print('Start [length statistic in temporal domain]')
    d = get_kwargs()
    if split:
        for protocol_name, analyse in d.items():
            result_path = get_result_file_path(f'temporal_statistic_of_length_{protocol_name}')
            plot_single_length_statistic_in_temporal_domain(result_path, analyse)
            print(f'Plot saved at {result_path}')
    else:
        result_path = get_result_file_path('temporal_statistic_of_length')
        plot_length_statistic_in_temporal_domain(result_path, **d)
        print(f'Plot saved at {result_path}')
    print('End [length statistic in temporal domain]')

def entropy_statistic_in_temporal_domain(split: bool):
    print('Start [entropy statistic in temporal domain]')
    d = get_kwargs()
    if split:
        for protocol_name, analyse in d.items():
            result_path = get_result_file_path(f'temporal_statistic_of_entropy_{protocol_name}')
            plot_single_temporal_entropy_statistic_of_protocol_in_temporal_domain(result_path, analyse)
            print(f'Plot saved at {result_path}')
    else:
        result_path = get_result_file_path('temporal_statistic_of_length')
        plot_entropy_statistic_in_temporal_domain(result_path, **d)
        print(f'plot saved at {result_path}')
    print('End [entropy statistic in temporal domain]')

def get_general_entropy():
    print('Start [get general entropy]')
    for a in analyses:
        entropy = calculate_general_entropy(a)
        print(f'{a.protocol_name} general entropy: {entropy}')
    print('End [get general entropy]')

def get_kwargs():
    d = dict(zip(protocols, analyses))
    return d

if __name__ == '__main__':
    main()