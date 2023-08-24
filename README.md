# CocoTb Installation on Linux

## Install MiniConda 
MiniConda is used to create virtual python environments. It is a small bootstrap version of Anaconda that includes only conda, Python, the packages they both depend on, and a small number of other useful packages (like pip, zlib, and a few others).
Go to [MiniConda](https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh) and get the shell script
```shell
bash Miniconda3-latest-Linux-x86_64.sh
```
Go through with the setup process until conda has been installed.
Restart terminal

## Initialize conda with python 

1. Create a new python environment in python3.8
```shell
conda create --name cocotb python3.8
```
2. Activate the new environment
```shell
conda activate cocotb
```

3. Install cocotb module inside this environment
```shell
pip install cocotb
pip install pytest
```
## Install iverilog and GTKWave
[Icarus Verilog](http://iverilog.icarus.com/.) is intended to compile ALL of the Verilog HDL as described in the IEEE-1364 standard. Of course, it's not quite there yet. It does currently handle a mix of structural and behavioural constructs. 

[GTKWave](https://gtkwave.sourceforge.net/) is a fully featured GTK+ based wave viewer for Unix, Win32, and Mac OSX which reads LXT, LXT2, VZT, FST, and GHW files as well as standard Verilog VCD/EVCD files and allows their viewing. 

```shell
sudo apt install iverilog -y
sudo apt isntall gtkwave -y
```

## Initialize Makefile to intergrate Verilog source with CocoTb python TestBench 
create a  `module.mak` file which contins the information about the project
```
# Makefile

# defaults
SIM ?= icarus
TOPLEVEL_LANG ?= verilog

VERILOG_SOURCES += $(PWD)/my_design.sv
# use VHDL_SOURCES for VHDL files

# TOPLEVEL is the name of the toplevel module in your Verilog or VHDL file
TOPLEVEL = my_design

# MODULE is the basename of the Python test file
MODULE = test_my_design

# include cocotb's make rules to take care of the simulator setup
include $(shell cocotb-config --makefiles)/Makefile.sim
```
Replace the `my_design` with verilog source file and `test_my_design` with Python TestBench

## Run CocoTB with make
```
make -f module.mak
```
