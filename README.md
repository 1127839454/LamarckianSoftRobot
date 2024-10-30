## Environment Setup
### Setting up evogym Environment
Download `evogym` and `LamarckianSoftRobot` folder.
Enter `LamarckianSoftRobot` using cd.
Install Python dependencies with conda:
```bash
conda env create -f environment.yml
conda activate evogym
```
### Build and Install Package
Enter `evogym` using cd.
To build the C++ simulation, build all the submodules, and install `evogym` run the following command:
```bash
python setup.py install
```
### Test Installation
cd to the `examples` folder and run the following script:
```shell
python gym_test.py
```

