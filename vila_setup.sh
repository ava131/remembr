#!/usr/bin/env bash


eval "$(conda shell.bash hook)"
conda activate remembr


python -m pip install --upgrade pip
apt-get update && apt-get install ninja-build -y


pip install flash-attn --no-build-isolation


cd deps/VILA


python -m pip install -e .


python -m pip install git+https://github.com/huggingface/transformers@v4.37.2


echo "VILA 推理环境配置完成！"