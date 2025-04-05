import json
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, help="jsonl file path with tasks", required=True)
    parser.add_argument("--max_instances", type=int, help="max instances to run", required=False, default=None)
    args = parser.parse_args()

    instance_ids = []
    with open(f"{args.task}", "r") as f:
        for line in f:
            instance = json.loads(line)
            if args.max_instances is not None and len(instance_ids) >= args.max_instances:
                break
            instance_ids.append(instance["instance_id"])
    print(" ".join(instance_ids))
if __name__ == "__main__":
    main()