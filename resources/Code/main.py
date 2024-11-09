from Visualisation.entropy_statistics_visualization import plot_entropy_statistic_in_temporal_domain
from utils import get_pcap_file_path, get_result_file_path
from Analyse.pcap_analyse import PcapAnalyse
from Analyse.pcap_entropy_analyse import calculate_entropy_of_data, calculate_general_entropy
from Visualisation.length_statistics_visualization import plot_occurrence_of_length, plot_length_statistic_in_temporal_domain

protocols = ['naiveproxy', 'trojan', 'shadowsocks', 'obfs4', 'https']

analyses = [PcapAnalyse(get_pcap_file_path(protocol), protocol) for protocol in protocols]

def main():
    entropy_occurrence_statistic_and_analyse()

    length_statistic_in_temporal_domain()

    entropy_statistic_in_temporal_domain()

    get_general_entropy()

def entropy_occurrence_statistic_and_analyse():
    print('Start [entropy occurrence statistic and analyse]')
    d, result_path = get_kwargs_and_result_path('occurrence_of_length')
    plot_occurrence_of_length(result_path, **d)
    print('End [entropy occurrence statistic and analyse]')

def length_statistic_in_temporal_domain():
    print('Start [length statistic in temporal domain]')
    d, result_path = get_kwargs_and_result_path('temporal_statistic_of_length')
    plot_length_statistic_in_temporal_domain(result_path, **d)
    print(f'Plot saved at {result_path}')
    print('End [length statistic in temporal domain]')

def entropy_statistic_in_temporal_domain():
    print('Start [entropy statistic in temporal domain]')
    d, result_path = get_kwargs_and_result_path('temporal_statistic_of_entropy')
    plot_entropy_statistic_in_temporal_domain(result_path, **d)
    print(f'plot saved at {result_path}')
    print('End [entropy statistic in temporal domain]')

def get_general_entropy():
    print('Start [get general entropy]')
    for a in analyses:
        entropy = calculate_general_entropy(a)
        print(f'{a.protocol_name} general entropy: {entropy}')
    print('End [get general entropy]')

def get_kwargs_and_result_path(item: str):
    d = dict(zip(protocols, analyses))
    result_path = get_result_file_path(item)
    return d, result_path

if __name__ == '__main__':
    main()