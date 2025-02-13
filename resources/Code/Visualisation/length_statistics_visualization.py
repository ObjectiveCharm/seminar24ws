
from Analyse.pcap_analyse import PcapAnalyse
import numpy as np
import matplotlib.pyplot as plt
import os

from Analyse.pcap_length_analyse import occurrence_histogram, temporal_length_array

def plot_occurrence_of_length(save_path: PcapAnalyse, **kwargs: os.path):
    fig = plt.figure(figsize=(15, 20))
    fig.tight_layout()
    plt.subplots_adjust(hspace=0.2, wspace=0.3)
    for index, (protocol_name, analyse) in enumerate(kwargs.items()):
        ax = fig.add_subplot(2, 3, index + 1)
        hist, bins = occurrence_histogram(analyse, 5)
        # ax.set_xlim([0, max(bins)])
        # ax.set_xticks(np.arange(0, max(bins), 500))
        ax.hist(hist,
                bins=bins,
                color='skyblue',
                alpha=0.7)
        ax.set_title(f'{protocol_name}')
        ax.set_xlabel('Length')
        ax.set_ylabel('Occurrence')
    if not __debug__:
        plt.savefig(save_path, format='png')
    plt.show()

def plot_single_occurrence_of_length(save_path: os.path, analyse: PcapAnalyse):
    fig, ax = plt.subplots()
    hist, bins = occurrence_histogram(analyse, 5)
    ax.hist(hist,
            bins=bins,
            color='skyblue',
            alpha=0.7)
    ax.set_title(f'{analyse.protocol_name}')
    ax.set_xlabel('Length')
    ax.set_ylabel('Occurrence')
    if not __debug__:
        plt.savefig(save_path, format='png')
    plt.show()

# The temporal statistics of length for every packet for a single protocol
# We should combine it to a plot in order to compare between different protocols
def plot_length_statistic_of_protocol_in_temporal_domain(analyse: PcapAnalyse, fig, ax):
    ts, data = temporal_length_array(analyse)
    ax.plot(ts, data, label=analyse.protocol_name)

# The combination of all the protocols' graphs
def plot_length_statistic_in_temporal_domain(save_path: os.path, **kwargs: PcapAnalyse):
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
        ax.set_ylim(0, 3000)
        ax.set_xticks(np.arange(0, 120, 10))
        # ax.set_yticks(np.arange(0, 600, 100))
        ts, data = temporal_length_array(analyse)
        line = ax.plot(ts, data, label=analyse.protocol_name)
        # labels.append(label)
        # lines.append(line)
        ax.set_title(f'{protocol_name}')
        ax.set_xlabel('Time')
        ax.set_ylabel('Length')
    # p = fig.add_subplot(2, 3, len(kwargs) + 1)
    # p.legend(handles=lines, labels=labels)
    if not __debug__:
        plt.savefig(save_path, format='png')
    plt.show()
def plot_single_length_statistic_in_temporal_domain(save_path: os.path, analyse: PcapAnalyse):
    fig, ax = plt.subplots()
    ax.set_xlim(0, 120)
    ax.set_ylim(0, 3000)
    ax.set_xticks(np.arange(0, 120, 10))
    # ax.set_yticks(np.arange(0, 600, 100))
    ts, data = temporal_length_array(analyse)
    line = ax.plot(ts, data, label=analyse.protocol_name)
    ax.set_title(f'{analyse.protocol_name}')
    ax.set_xlabel('Time')
    ax.set_ylabel('Length')
    if not __debug__:
        plt.savefig(save_path, format='png')
    plt.show()

