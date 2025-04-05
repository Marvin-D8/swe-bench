#!/bin/bash

set -x

for repo_name in langchain openai-python transformers pydantic-ai
do
python swebench/inference/make_datasets/create_text_dataset.py --dataset_name_or_path=outputs/tasks/${repo_name}-task-instances_cleaned.jsonl --split=train --output_dir=outputs/text_datasets/ --validation_ratio=0 --copy_repo_from_host_path=repos/$repo_name
done