from argparse import ArgumentParser
from swebench.harness.utils import load_swebench_dataset
from swebench.image_builder.constants import IMAGE_BUILDER_LOG_DIR
from pathlib import Path

OG_SWE_BENCH_DATASETS = {
    "SWE-bench/SWE-bench",
    "SWE-bench/SWE-bench_Lite",
    "SWE-bench/SWE-bench_Verified",
    "SWE-bench/SWE-bench_Multimodal",
    "princeton-nlp/SWE-bench",
    "princeton-nlp/SWE-bench_Lite",
    "princeton-nlp/SWE-bench_Verified",
}

SWE_BENCH_MULTIMODAL_DATASETS = {
    "SWE-bench/SWE-bench_Multimodal",
    "princeton-nlp/SWE-bench_Multimodal",
}

def get_dockerfile(instance: dict, dataset_name: str) -> str:
    """
    The main dockerfile generator function.
    """
    if dataset_name in OG_SWE_BENCH_DATASETS:
        from swebench.image_builder.dockerfile_gen._swebench import _get_dockerfile
        return _get_dockerfile(instance)
    elif dataset_name in SWE_BENCH_MULTIMODAL_DATASETS:
        raise ValueError("Multimodal datasets are not supported yet")
        # from swebench.image_builder.dockerfile_gen._swebench_multimodal import _get_dockerfile
        # return _get_dockerfile(instance)
    elif dataset_name == "SWE-bench/SWE-bench_Multilingual":
        from swebench.image_builder.dockerfile_gen._swebench_multilingual import _get_dockerfile
        return _get_dockerfile(instance)
    else:
        raise ValueError(f"Invalid dataset name: {dataset_name}")


def main(dataset_name: str, split: str, output_dir: str, instance_ids: list[str] | None):
    dataset = load_swebench_dataset(dataset_name, split, instance_ids=instance_ids)
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    for instance in dataset:
        dockerfile = get_dockerfile(instance, dataset_name)
        instance_dir = output_dir / instance["instance_id"]
        instance_dir.mkdir(parents=True, exist_ok=True)
        (instance_dir / "Dockerfile").write_text(dockerfile)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("dataset_name", type=str)
    parser.add_argument("split", type=str)
    parser.add_argument("output_dir", type=str, default=IMAGE_BUILDER_LOG_DIR)
    parser.add_argument("--instance_ids", type=list[str], default=None)
    args = parser.parse_args()
    main(**vars(args))
