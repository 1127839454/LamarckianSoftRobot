## Environment Setup

### Setting up evogym Environment for Windows

Download `evogym` and `LamarckianSoftRobot` folder.
Enter `LamarckianSoftRobot` using cd.
Install Python dependencies with conda:

```bash
conda env create -f environment.yml
conda activate evogym
```

### Setting up evogym Environment for Linux

Download `evogym` and `LamarckianSoftRobot` folder.
Enter `LamarckianSoftRobot` using cd.
Install Python dependencies with conda:

```bash
conda env create -f linux_environment.yml
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

## Trying it out

You can evolve robots with the following code (it takes a few minutes to run):

```bash
python ./example/run.py --max-iters 10 --population-size 5 --max-evaluations 10 --exp-dir ./result/experiment
```

## Robot Visualization

### For Windows:

You can also visualize the experiment results. The following code visualizes the movement of the best-performing robot in the experiments saved in the specified directory:

```bash
python visualize/best_robot.py -e ./result/experiment
```

### For Linux:

You can first evolve robots by running `run.py` on Linux server. As the result of the training is saved in folder `result`, you can download the result to your local Windows, and then conduct visulization on Windows.



## Experiment

### Experiment 1

Experiment on `BridgeWalker-v0` Task:

```bash
python ./example/run.py --env-name BridgeWalker-v0 --max-iters 1000 --population-size 25 --max-evaluations 250 --exp-dir ./result/experiment_bridge --crossover_rate 0.5 --mutation-rate 0.1 --elite-rate-high 0.6 --elite-rate-low 0.0 --lr 2.5e-4 --num-steps 128 --num-processes 4 --clip-param 0.1 --value-loss-coef 0.5 --entropy-coef 0.01 --num-evals 50 --use-linear-lr-decay --use-gae
```