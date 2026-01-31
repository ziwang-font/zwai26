
cls
title zwai26

setlocal

set HF_TOKEN=

set HF_HUB_ENABLE_HF_TRANSFER=1
set TORCH_COMPILE_DISABLE=1

set HF_ENDPOINT=https://hf-mirror.com
set GH_PROXY=https://ghproxy.com


rem https://mirrors.tuna.tsinghua.edu.cn/pypi/web/simple
rem https://pypi.tuna.tsinghua.edu.cn/simple
rem https://mirrors.aliyun.com/pypi/simple
rem https://pypi.mirrors.ustc.edu.cn/simple
rem https://pypi.doubanio.com/simple
rem https://repo.huaweicloud.com/repository/pypi/simple



set HF_HUB_CACHE=%~dp0\.cache
set PYTHONPYCACHEPREFIX=%~dp0\.cache\pycache
set TRITON_CACHE_DIR= %~dp0\.cache\triton_cache

set PATH=%PATH%;%~dp0\python_embeded\Scripts

set PIP_INDEX_URL=https://mirrors.aliyun.com/pypi/simple



rem .\python_embeded\python.exe -s launcher.py
rem .\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build --fast fp16_accumulation  --torch_dtype=float16
rem .\python_embeded\python.exe -s ComfyUI\main.py --windows-standalone-build 

.\python_embeded\python.exe -s ComfyUI\main.py --disable-xformers  --windows-standalone-build --fast fp16_accumulation


endlocal
