max_instances=20
python swebench/collect/remove_instance_ids.py --task outputs/tasks/openai-python-task-instances.jsonl --instance_ids openai__openai-python-1655,openai__openai-python-2025 --max_instances $max_instances
python swebench/collect/remove_instance_ids.py --task outputs/tasks/langchain-task-instances.jsonl --instance_ids langchain-ai__langchain-30448 --max_instances $max_instances
python swebench/collect/remove_instance_ids.py --task outputs/tasks/pydantic-ai-task-instances.jsonl --max_instances $max_instances
python swebench/collect/remove_instance_ids.py --task outputs/tasks/transformers-task-instances.jsonl --instance_ids huggingface__transformers-35858,huggingface__transformers-35802,huggingface__transformers-35835 --max_instances $max_instances
