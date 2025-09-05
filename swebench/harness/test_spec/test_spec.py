import json
from dataclasses import dataclass
from typing import Any, Union, cast

from swebench.constants import (
    SWEbenchInstance,
)
from swebench.harness.test_spec.create_scripts import (
    make_eval_script_list,
)
from swebench.data_specs import get_data_spec


@dataclass
class TestSpec:
    """
    A dataclass that represents a test specification for evaluation of a single instance of SWE-bench.
    Assumes images are already built and available.
    """

    instance_id: str
    image: str
    eval_script_list: list[str]
    repo: str
    version: str
    FAIL_TO_PASS: list[str]
    PASS_TO_PASS: list[str]

    @property
    def eval_script(self):
        return (
            "\n".join(["#!/bin/bash", "set -uxo pipefail"] + self.eval_script_list)
            + "\n"
        )
        # Don't exit early because we need to revert tests at the end


def get_test_specs_from_dataset(
    dataset: Union[list[SWEbenchInstance], list[TestSpec]],
) -> list[TestSpec]:
    """
    Idempotent function that converts a list of SWEbenchInstance objects to a list of TestSpec objects.
    """
    if isinstance(dataset[0], TestSpec):
        return cast(list[TestSpec], dataset)
    return list(
        map(
            lambda x: make_test_spec(x),
            cast(list[SWEbenchInstance], dataset),
        )
    )


def make_test_spec(
    instance: SWEbenchInstance,
) -> TestSpec:
    """
    Create a TestSpec from a SWEbenchInstance for evaluation purposes.
    Expects the instance to have an 'image' field pointing to a pre-built Docker image.
    """
    if isinstance(instance, TestSpec):
        return instance
    
    instance_id = instance["instance_id"]
    repo = instance["repo"]
    version = instance.get("version")
    base_commit = instance["base_commit"]
    problem_statement = instance.get("problem_statement")
    test_patch = instance["test_patch"]
    
    if "image" not in instance:
        raise ValueError(f"Instance {instance_id} missing required 'image' field")
    image = instance["image"]

    def _from_json_or_obj(key: str) -> Any:
        """If key points to string, load with json"""
        if key not in instance:
            # If P2P, F2P keys not found, it's a validation instance
            return []
        if isinstance(instance[key], str):
            return json.loads(instance[key])
        return instance[key]

    pass_to_pass = _from_json_or_obj("PASS_TO_PASS")
    fail_to_pass = _from_json_or_obj("FAIL_TO_PASS")

    env_name = "testbed"
    repo_directory = f"/{env_name}"
    specs = get_data_spec(repo, version)

    eval_script_list = make_eval_script_list(
        instance, specs, env_name, repo_directory, base_commit, test_patch
    )

    return TestSpec(
        instance_id=instance_id,
        image=image,
        eval_script_list=eval_script_list,
        repo=repo,
        version=version,
        FAIL_TO_PASS=fail_to_pass,
        PASS_TO_PASS=pass_to_pass,
    )