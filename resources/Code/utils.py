from enum import Enum
import os

class WorkDirectory(Enum):
    Data = 0
    Analyse = 1
    Visualisation = 2
    Results = 3

def get_dir_path(dir: WorkDirectory):
    current_path = os.path.dirname(__file__)
    dir_path = os.path.join(current_path, dir.name)
    # if __debug__:
        # print(f"Directory path: {dir_path}")
    return dir_path

def get_pcap_file_path(name):
    pcap_file_name = f'{name}dump.pcap'
    return os.path.join(get_dir_path(WorkDirectory.Data), 'Pcap', pcap_file_name)

def get_result_file_path(name, extension: str='png'):
    return os.path.join(get_dir_path(WorkDirectory.Results), f'{name}.{extension}')

# def get_tcp_bin_file_path(name):
#     return os.path.join(get_dir_path(WorkDirectory.Data), 'Binary',f'{name}tcpdump')