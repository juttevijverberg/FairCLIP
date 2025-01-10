#!/bin/bash
#SBATCH --partition=gpu_mig
#SBATCH --gpus=1
#SBATCH --job-name=evaluate_CLIP
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=9
#SBATCH --time=04:00:00
#SBATCH --output=slurm_output_%A.out

DATASET_DIR=/home/aeichholtz/FairCLIP-project/FairCLIP/FairVLMed
RESULT_DIR=.
MODEL_ARCH=vit-b16  # Options: vit-b16 | vit-l14
MODALITY_TYPE='slo_fundus'
LR=1e-5
BATCH_SIZE=32

PERF_FILE=${MODEL_ARCH}_${MODALITY_TYPE}.csv

source activate fairclip

python ./evaluate_CLIP.py \
		--dataset_dir ${DATASET_DIR} \
		--result_dir ${RESULT_DIR}/results/glaucoma_CLIP_${MODEL_ARCH} \
		--lr ${LR} \
		--perf_file ${PERF_FILE} \
		--model_arch ${MODEL_ARCH} \
		--pretrained_weights 'path-to-checkpoint/clip_ep002.pth'
