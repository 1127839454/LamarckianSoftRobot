import argparse
import csv
import sys
from pathlib import Path
from typing import Optional

import numpy as np

sys.path.append(".")
from specify_robot import SpecifyRobotVisualizer

from alg.globals import POP_CSV_FILE_NAME


# class BestRobotVisualizer(SpecifyRobotVisualizer):
#     def __init__(
#         self,
#         exp_dir: Path,
#         movie_path: Optional[str],
#         num_episodes: int = 1,
#     ):

#         with (exp_dir / POP_CSV_FILE_NAME).open() as fd:
#             reader = csv.reader(fd)
#             next(reader)

#             last_row = next(reader)

#             for row in reader:
#                 semi_last_row = last_row
#                 last_row = row

#         generation = int(last_row[0])
#         fitness_list = []
#         for semi_fitness, fitness in zip(semi_last_row[1:], last_row[1:]):
#             if fitness == "":
#                 fitness_list.append(float(semi_fitness))
#             else:
#                 fitness_list.append(float(fitness))

#         id_ = int(np.argmax(fitness_list))

#         super().__init__(exp_dir, generation, id_, movie_path, num_episodes)

class BestRobotVisualizer(SpecifyRobotVisualizer):
    def __init__(
        self,
        exp_dir: Path,
        movie_path: Optional[str],
        num_episodes: int = 1,
    ):
        # 打开CSV文件并读取
        with (exp_dir / POP_CSV_FILE_NAME).open() as fd:
            reader = csv.reader(fd)
            next(reader)  # 跳过头部

            last_row = None
            for row in reader:
                if row:  # 跳过空行
                    semi_last_row = last_row
                    last_row = row
                    print(f"Last row: {last_row}, Semi last row: {semi_last_row}")

        # 检查是否有足够的行数据
        if last_row is None or semi_last_row is None:
            raise ValueError("The CSV file does not包含足够的数据。")

        # 获取最后一代的编号
        generation = int(last_row[0])
        fitness_list = []
        for semi_fitness, fitness in zip(semi_last_row[1:], last_row[1:]):
            if fitness == "":
                fitness_list.append(float(semi_fitness))
            else:
                fitness_list.append(float(fitness))

        # 获取最佳适应度个体的id
        id_ = int(np.argmax(fitness_list))

        # 调用父类的初始化
        super().__init__(exp_dir, generation, id_, movie_path, num_episodes)



if __name__ == "__main__":
    """
    Visualize the movement of the robot that performed the best during the experiments.
    """

    parser = argparse.ArgumentParser()
    parser.add_argument("-e", "--exp-dir", type=str)
    parser.add_argument("-m", "--movie-path", type=str, default=None)
    parser.add_argument("-n", "--num-episodes", type=int, default=1)

    args = parser.parse_args()

    visualizer = BestRobotVisualizer(
        exp_dir=Path(args.exp_dir),
        movie_path=args.movie_path,
        num_episodes=args.num_episodes,
    )

    visualizer.run()
