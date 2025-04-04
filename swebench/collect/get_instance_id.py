import json
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--task", type=str, help="jsonl file path with tasks", required=True)
    args = parser.parse_args()

    with open(f"{args.task}", "r") as f:
        for line in f:
            instance = json.loads(line)
            print(instance["instance_id"])

if __name__ == "__main__":
    main()