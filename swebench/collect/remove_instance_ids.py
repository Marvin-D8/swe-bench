'''
getting instance ids list as cli argument and dataset jsonl path
removing instances from dataset jsonl file
and svaes the reuslting dataset into new file

python swebench/collect/remove_instance_ids.py --task outputs/tasks/openai-python-task-instances.jsonl --instance_ids openai__openai-python-1655,openai__openai-python-2025
python swebench/collect/remove_instance_ids.py --task outputs/tasks/langchain-task-instances.jsonl --instance_ids langchain-ai__langchain-30448
'''
import json
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, help="jsonl file path with tasks", required=True)
    parser.add_argument("--instance_ids", default="", type=str, help="instance ids to remove", required=False)
    parser.add_argument("--max_instances", default=None, type=int, help="max instances to remove", required=False)
    args = parser.parse_args()

    instance_ids = args.instance_ids.split(",")
    new_dataset = []
    with open(f"{args.task}", "r") as f:
        for line in f:
            instance = json.loads(line)
            if instance["instance_id"] in instance_ids:
                continue
            else:
                new_dataset.append(instance)
    if args.max_instances is not None:
        new_dataset = new_dataset[:args.max_instances]
    with open(f"{args.task.replace('.jsonl', '_cleaned.jsonl')}", "w") as f:
        for instance in new_dataset:
            f.write(json.dumps(instance) + "\n")

if __name__ == "__main__":
    main()