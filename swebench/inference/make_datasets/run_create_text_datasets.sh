#!/bin/bash

set -x

output_dir=outputs/text_datasets_oracle
file_source=oracle

for repo_name in langchain openai-python transformers pydantic-ai
do
python swebench/inference/make_datasets/create_text_dataset.py --dataset_name_or_path=outputs/tasks/${repo_name}-task-instances_cleaned.jsonl --split=train --output_dir=$output_dir --validation_ratio=0 --file_source=$file_source --copy_repo_from_host_path=repos/$repo_name
done