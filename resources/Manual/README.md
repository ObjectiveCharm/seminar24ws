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

Or you can also create conda environment by yourself

```shell
conda create -n Seminar python=3.9.0
```
Then activate the environment
```shell
conda activate Seminar
```

Then in the environment, install dependencies with `pip install` or `conda install`. 

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

if you want to get split figures for each protocol, run

```shell
python -O main.py -s
```
The `-s` is equivalent to `--split-output-figure`, which will generate figures for each protocol respectively.
That may be helpful when the amalgamated figure is too big to embed in a standard ieee 2 column format paper. 

Only in release profile (by add python parameter `-O`), the code will save the generated figures to directory  Results/<Corresponding Name>.png.
And the Data which used to generate Figures located in Data/Pcap/<Corresponding Name>.pcap.
If you want to give your data, please modify functions in `main.py` and put your data in Data/Pcap.
Please note that the formate of pcap data (with .pcap extension) is like `<name>dump.pcap`, please refer to `utils.py`. 




