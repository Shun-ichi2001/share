import torch
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import Normalize
from matplotlib.colors import rgb2hex
import matplotlib.pyplot as plt

# 与えられたテンソルデータ
data = torch.tensor([
    [31.4688, 31.5000, 23.6875, 26.1406, 28.1250, 26.3438, 25.6562, 22.7031,
     17.7812, 20.1250, 26.7812, 27.1562, 24.7344, 25.8125, 12.7656, 24.0000,
     20.2812, 19.5938, 24.4531, 24.2031, 25.7031, 19.3906, 24.8125, 17.6094,
     20.0000, 26.4844, 22.1875, 24.2969, 19.4375, 21.4062, 19.5781, 19.7031,
     26.5156, 25.4844, 23.0938, 26.4688, 27.7656, 27.0000, 26.8281, 28.1250,
     24.8594, 27.2656, 25.8594, 25.5156, 27.2500, 28.2656, 24.0938, 28.5938,
     25.9219]
], dtype=torch.float16)

# テンソルを1次元配列に変換
x = data.flatten()

cm = "jet"
n_samples = 49

cmap = plt.get_cmap("jet")

for k, x in enumerate(np.linspace(0.0, 1.0, n_samples)):
    colorcode = rgb2hex(cmap(x))
    print(f"{k:02d}/{n_samples}\t{x:0.3f}\t{colorcode}")
