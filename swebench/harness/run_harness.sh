set -x

for id in langchain-ai__langchain-29426 langchain-ai__langchain-30448 langchain-ai__langchain-29942 langchain-ai__langchain-29761
do
    echo "Running $id"
    python -m swebench.harness.run_evaluation --dataset_name=outputs/tasks/langchain-task-instances.jsonl --split=dev --instance_ids $id --predictions_path=gold --report_dir=outputs/reports --run_id=$id --namespace="" --cache_level="base" --force_rebuild=true
done

