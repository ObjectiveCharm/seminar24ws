from Analyse.pcap_analyse import PcapAnalyse
from Analyse.pcap_entropy_analyse import calculate_entropy_per_packet
import numpy as np
import matplotlib.pyplot as plt
import os

def plot_temporal_entropy_statistic_of_protocol_in_temporal_domain(analyse: PcapAnalyse, fig, ax):
    ts, data = calculate_entropy_per_packet(analyse)
    ax.plot(ts, data, label=analyse.protocol_name)

def plot_entropy_statistic_in_temporal_domain(save_path:os.path, **kwargs:PcapAnalyse):
    # fig, ax = plt.subplots()
    # ax.set_xlim(0, 120)
    # ax.set_ylim(0, 8)
    # ax.set_xticks(np.arange(0, 120, 10))
    # ax.set_yticks(np.arange(0, 8, 0.5))
    # ax.set_title('Statistic of Entropy of single packet')
    # for protocol_name, analyse in kwargs.items():
    #     plot_temporal_entropy_statistic_of_protocol_in_temporal_domain(analyse, fig, ax)
    # ax.legend()
    # ax.set_xlabel('Time')
    # ax.set_ylabel('Entropy')
    # if not __debug__:
    #     plt.savefig(save_path, format='png')
    # plt.show()
    fig = plt.figure(figsize=(15, 20))
    fig.tight_layout()
    plt.subplots_adjust(hspace=0.2, wspace=0.3)
    fig.suptitle('Payload Length in Temporal Domain')
    # lines = []
    # labels = []
    for index, (protocol_name, analyse) in enumerate(kwargs.items()):
        # label = analyse.protocol_name
        ax = fig.add_subplot(2, 3, index + 1)
        ax.set_xlim(0, 120)
        ax.set_ylim(0, 8)
        ax.set_xticks(np.arange(0, 120, 10))
        # ax.set_yticks(np.arange(0, 600, 100))
        ts, data = calculate_entropy_per_packet(analyse)
        line = ax.plot(ts, data, label=analyse.protocol_name)
        # labels.append(label)
        # lines.append(line)
        ax.set_title(f'{protocol_name}')
        ax.set_xlabel('Time')
        ax.set_ylabel('Entropy')
    if not __debug__:
        plt.savefig(save_path, format='png')
    plt.show()

