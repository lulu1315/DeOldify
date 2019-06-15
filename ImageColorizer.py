import os
os.environ['CUDA_VISIBLE_DEVICES']='0'
from os import path
import torch
    
import fastai
from fasterai.visualize import *
plt.style.use('dark_background')

from pathlib import Path
torch.backends.cudnn.benchmark=True

#model_path='/shared/foss/DeOldify/'
#model path is hardcoded in fasterai/visualize.py
model_flag = int(sys.argv[1])
#0:video 1:artistic 2:stable
render_factor = int(sys.argv[2])
colorizer = get_image_colorizer(model_flag=model_flag, render_factor=render_factor)

source_path = sys.argv[3]
result_path = sys.argv[4]

result_path = colorizer.plot_transformed_image(path=source_path, out_path=result_path, render_factor=render_factor, compare=True)
