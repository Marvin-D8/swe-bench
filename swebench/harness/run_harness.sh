set -x

dataset_dir="outputs/tasks"
max_instances=20
run_id=20

rm -r logs

for dataset_name in langchain-task-instances openai-python-task-instances pydantic-ai-task-instances transformers-task-instances
do
    
    echo "Running $dataset_name"
    dataset_path="$dataset_dir/${dataset_name}_cleaned.jsonl"
    ids=$(python swebench/collect/get_instance_id.py --task=$dataset_path --max_instances=$max_instances)
    
    python -m swebench.harness.run_evaluation --dataset_name=$dataset_path --instance_ids $ids --predictions_path=gold --report_dir=outputs/reports/$dataset_name --run_id=$run_id --namespace="" --cache_level="base" --force_rebuild=true

    run_id=$((run_id+1))
done

