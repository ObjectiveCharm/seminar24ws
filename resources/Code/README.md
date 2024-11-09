# Seminar Support Code
This directory contains the code which generate result for my seminar paper.

# Install Dependencies
It uses Python version 3.9.0 and has direct dependency of dpkt, numpy and matplotlib, see requirements.txt.
To install dependencies, use

```shell
pip install -r requirements.txt
```

We use conda to manage environment, if you prefer it, run

```shell
conda env create -f Seminar.yml
```

The Seminar.yml file located at this directory.
Then activate the environment by in this directory.

```shell
conda activate Seminar
```

# Usage
To generate result, run

```shell
python -O main.py
```

Only in release profile (by add python parameter `-O`), the code will save the generated figures to directory  Results/<Corresponding Name>.png.
And the Data which used to generate Figures located in Data/Pcap/<Corresponding Name>.pcap.
If you want to give your data, please modify functions in `main.py` and put your data in Data/Pcap.
Please note that the formate of pcap data (with .pcap extension) is like `<name>dump.pcap`, please refer to `utils.py`. 




