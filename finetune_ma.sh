#!/usr/bin/env bash

export model_path=$1
mkdir -p ${model_path}

python run_common_voice.py \
    --dataloader_num_workers="8" \
    --model_name_or_path="facebook/wav2vec2-large-xlsr-53" \
    --dataset_config_name="ar" \
    --output_dir=${model_path} \
    --num_train_epochs="50" \
    --per_device_train_batch_size="16" \
    --per_device_eval_batch_size="16" \
    --evaluation_strategy="steps" \
    --warmup_steps="500" \
    --fp16 \
    --freeze_feature_extractor \
    --save_steps="400" \
    --eval_steps="400" \
    --logging_steps="400" \
    --save_total_limit="1" \
    --group_by_length \
    --attention_dropout="0.094" \
    --activation_dropout="0.055" \
    --feat_proj_dropout="0.04" \
    --hidden_dropout="0.047" \
    --layerdrop="0.041" \
    --mask_time_prob="0.082" \
    --gradient_checkpointing \
    --learning_rate="3e-4" \
    --do_train --do_eval


    #--model_name_or_path="facebook/wav2vec2-large-xlsr-53" \
    #--overwrite_output_dir \
    #--model_name_or_path="/home/othrif/projects/wav2vec2/finetune-xlsr/models/ar/msa/wav2vec2-large-xlsr-arabic" \




