# -*- coding: utf-8 -*-
'''
TopQuant-简称TQ极宽智能量化回溯分析系统，培训课件-配套教学python程序

Top极宽量化(原zw量化)，Python量化第一品牌 
by Top极宽·量化开源团队 2017.10.1 首发;
   edit @2020.02.02  


网站： www.zwPython.com  www.TopQuant.vip      www.ziwang.com
QQ群: Top极宽量化总群，124134140

#pip install nvidia-ml-py3
# from pynvml import *
'''

#
import sys,numpy
from icecream import ic as cpp
#from pynvml import *
#import tensorflow as tf
#tf.disable_v2_behavior()
import torch,torchvision 
import pytorch_lightning as pl
#
#import peft #,bitsandbytes #,xformers
import diffusers,transformers,huggingface_hub

#import flash
#
import pynvml
#
#        
pynvml.nvmlInit()
#
#--------------------------

#--2026.01
def st_env4ai():
    #
    #
    print(f"Python版本: {sys.version.split()[0]}")
    print(f"PyTorch 版本: {torch.__version__}")
    print(f"CUDA 可用: {torch.cuda.is_available()}")
    print(f"CUDA 版本: {torch.version.cuda}")
    print(f"GPU 型号: {torch.cuda.get_device_name(0)}")
    #
    cpp(diffusers.__version__,transformers.__version__,huggingface_hub.__version__)
    #
    kfg_cuda=torch.cuda.is_available()
    cpp(kfg_cuda)
    #
    #model = YourModel().half()
    print(f"已分配: {torch.cuda.memory_allocated()/1024**3:.2f} GB")
    print(f"已缓存: {torch.cuda.memory_reserved()/1024**3:.2f} GB")
    #
    


    #import nunchaku 
    #import lightx2v,flash_attn,triton,sageattention
    #import sageattention flash_attn,triton
    cpp(numpy.__version__)
    #cpp(sageattention.__version__)
    #cpp(dir(sageattention))
    #cpp(nunchaku.__version__)
    #cpp(nunchaku.version)
    
    
    
    
    #
    try:
        cpp(triton.__version__)
        cpp(flash_attn.__version__)
        cpp(lightx2v.__version__)
        #
        print(f"xFormers版本: {xformers.__version__}")
        print(f"xFormers CUDA支持: {xformers._is_cuda_available()}")
    except:
        print("❌ 请安装 xFormers")
        #exit(1)  
    #
    try:
        subprocess.run(["ffmpeg", "-version"], check=True, capture_output=True)
        print("✅ FFmpeg 已安装")
    except:
        print("❌ 请安装 FFmpeg 并添加到系统 PATH")
        #exit(1)
    #
    # 简单模型测试
    model = torch.nn.Linear(10, 10).cuda()
    model = torch.compile(model)  # 启用编译
    x = torch.randn(32, 10).cuda()
    try:
        output = model(x)
        print("✅ 编译成功！")
    except Exception as e:
        print(f"❌ 错误: {e}")
        
#--------------

#

#print("tensorflow ver:",tf.__version__)
print("torch ver:",torch.__version__)
print("torchvision ver:",torchvision.__version__)
print("torch CUDA:",torch.version.cuda)
print("torch cuDNN:",torch.backends.cudnn.version())
#print("xformers:",xformers.__version__)
#
#print('fastai',fastai.version())
#print('fastai',fastai.__version__)
#print('fastcore',fastcore.__version__)
#print('fastcore',fastcore.version())
#print('pl',pl.version())
#print('flash',flash.version())
print('pl',pl.__version__)
#print('flash',flash.__version__)
#
#print('peft',peft.__version__)
#print('bitsandbytes',bitsandbytes.version())
#print('peft',bitsandbytes.__version__)
#xxxx

#nvml_lib = CDLL(r"C:\Windows\System32\nvml.dll")
handle = pynvml.nvmlDeviceGetHandleByIndex(0)
info = pynvml.nvmlDeviceGetMemoryInfo(handle)
k=1024*1024*1024
print(f"\nTotal memory: {info.total/k:0.2f} G")
print(f"Free memory: {info.free/k:0.2f} G")
print(f"Used memory: {info.used/k:0.2f} G")

#
device=torch.cuda.current_device()
x1=torch.cuda.get_device_properties(device)
x2=torch.cuda.get_device_capability
#
gcnt=torch.cuda.get_device_properties(0).multi_processor_count
print(x1,x2,device,gcnt)

#--2026.01
st_env4ai()
#