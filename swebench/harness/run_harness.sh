set -x

dataset_name="outputs/tasks/transformers-task-instances.jsonl"
#outputs/tasks/openai-python-task-instances.jsonl
max_instances=5
ids=$(python swebench/collect/get_instance_id.py --task=$dataset_name --max_instances=$max_instances)
run_id=5
python -m swebench.harness.run_evaluation --dataset_name=$dataset_name --instance_ids $ids --predictions_path=gold --report_dir=outputs/reports --run_id=$run_id --namespace="" --cache_level="base" --force_rebuild=true

