#!/bin/bash

# for i in {0..9}; do
#     rm -rf checkpoint/
#     python3 src/train.py
#     python3 src/evaluate.py
# done

# rm checkpoint/Exp2 -rf
# ROBERTA_LEVEL=sentence python3 src/train.py

# rm checkpoint/Exp2 -rf
# ROBERTA_LEVEL=word python3 src/train.py

MODEL_NAME=NRMS
python run.py --top preprocess
#python run.py --top training
#python run.py --top evaluation