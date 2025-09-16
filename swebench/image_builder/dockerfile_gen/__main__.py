from . import main
from argparse import ArgumentParser
from swebench.image_builder.constants import IMAGE_BUILDER_LOG_DIR

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("dataset_name", type=str)
    parser.add_argument("split", type=str)
    parser.add_argument("output_dir", type=str, default=IMAGE_BUILDER_LOG_DIR)
    parser.add_argument("--instance_ids", type=list[str], default=None)
    args = parser.parse_args()
    main(**vars(args))
