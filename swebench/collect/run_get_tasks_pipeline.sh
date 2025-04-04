#!/usr/bin/env bash

# If you'd like to parallelize, do the following:
# * Create a .env file in this folder
# * Declare GITHUB_TOKENS=token1,token2,token3...

python -m swebench.collect.get_tasks_pipeline \
    --repos 'langchain-ai/langchain' \
    --path_prs 'outputs/prs' \
    --path_tasks 'outputs/tasks' \
    --max_pulls 1000