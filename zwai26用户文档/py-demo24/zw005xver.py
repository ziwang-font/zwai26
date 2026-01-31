# -*- coding: utf-8 -*-
'''
TopQuant-简称TQ极宽智能量化回溯分析系统，培训课件-配套教学python程序

Top极宽量化(原zw量化)，Python量化第一品牌 
by Top极宽·量化开源团队 2017.10.1 首发;
   edit @2020.02.02  


网站： www.zwPython.com  www.TopQuant.vip      www.ziwang.com
QQ群: Top极宽量化总群，124134140

'''

import sys
#
#import numba as nb
#import numexpr as ne  

# py数值分析
import numpy as np
import scipy as sp
#import statsmodels as sm


# py量化：三大件:pd,,zp,py量化分析的三个核心模块库，
import pandas as pd
import polars as pl
#import zipline 
#import talib as ta
#
#   py量化框架
#import pyalgotrade as pat
#import backtrader as bt


#   py量化绩效分析
#import pyfolio
#import ffn
#import alphalens
#import empyrical 
#
#----金融数据抓取
#import tushare as ts
#import ccxt
#import pytdx
#


#
#---py 图像处理
import PIL
import cv2
#import skimage

#---py绘图
import matplotlib as mpl #mpl
import matplotlib.pyplot as plt
#import ggplot as gpl


#---py图表，可视化数据分析
import seaborn 
#import pyecharts
#import dash
#import plotly
#import plotly_express as px     


#--- ai，机器学习
import sklearn 
#import theano 
#

#import keras
#from tensorflow import keras
#

# NLK语意分析
#import nltk
#import pattern3
import spacy

#
#---神经网络，深度学习三大平台
#import tensorflow as tf
#tf.disable_v2_behavior()
import torch
import torchvision
#import mxnet

#
# --- 其他
#import pygame
#import PyQt5
#import pyopencl
#import gdal
#import pycuda





#=====================




print("\n @py量化：三大件:pd,btr,talib   @py量化分析的三个核心模块库");
print("pandas ver:",pd.__version__)
print("porlars ver:",pl.__version__)
#print("talib ver:",ta.__version__)
#print("backtrader ver:",bt.__version__)



#
print("\n py数值分析");
print("numpy ver:",np.__version__)
print("scipy ver:",sp.__version__)
#print("statsmodels ver:",sm.__version__)

#print("\n py量化工具");
#print("pyalgotrade ver:",pat.__version__)
#print("zipline ver:",zipline.__version__)
#print("talib ver:",ta.__version__)

#print("pyfolio ver:",pyfolio.__version__)
#print("ffn ver:",ffn.__version__)
#print("alphalens ver:",alphalens.__version__)  #0.34
#print("empyrical ver:",empyrical.__version__)


#
print('\n金融数据抓取')
#print("tushare ver:",ts.__version__)
#print("ccxt ver:",ccxt.__version__)
#print("pytdx通达信 ver:")

print("\n py图形处理")
print("PIL ver:",PIL.__version__)
print("cv2 ver:",cv2.__version__)
#print("skimage ver:",skimage.__version__)

print("matplotlib ver:",mpl.__version__)
#print("ggplot ver:",gpl.__version__)




print("\n py图表，可视化数据分析")
print("seaborn ver:",seaborn.__version__)
#print("dash ver:",dash.__version__)
#print("pyecharts ver:",pyecharts.__version__)
#print("plotly ver:",plotly.__version__)
#print("plotly-express ver:",px.__version__)



print("\n ai，机器学习");
print("sklearn ver:",sklearn.__version__)
#print("theano ver:",theano.__version__)
#print("keras ver:",keras.__version__)

print("\n NLK语意分析")
#print("nltk ver:",nltk.__version__)
#print("pattern3 ver:",pattern3.__version__)
print("spacy ver:",spacy.__version__)

print("\n 神经网络，深度学习三大平台");
#print("tensorflow ver:",tf.__version__)
print("torch ver:",torch.__version__)
print("torchvision ver:",torchvision.__version__)
#print("mxnet ver:",mxnet.__version__)

print("\n 其他");
#print("pygame ver:",pygame.__version__)
#print("PyQt5 ver:") #,PyQt5.__version__)
#print("gdal ver:") #,gdal.__version__)
#print("pyopencl ver:",pyopencl.__version__)
#print("pycuda ver:",pycuda.VERSION)



print("");
print("");
print("BLAS,Basic Linear Algebra Subprograms,基础线性代数子程序库")
print("检验numpy等库是否使用了blas加速")
print("zwPython采用的是intel-MKL版本numpy模块库，性能比BLAS更快。")
print("如果结果是：False，则表明实现了BLAS加速。")

fgBlas=(id(np.dot) == id(np.core.multiarray.dot))
print("fgBlas,",fgBlas)


print("");
print('Top极宽·量化开源组 网站：www.zwPython.com, www.TopQuant.vip，www.ziwang.com')

