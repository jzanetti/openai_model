import argparse
from process.se import se, write_output
from os.path import exists
from os import makedirs

# export PYTHONPATH=/Users/zhans/Github/openai_model:$PYTHONPATH

def get_example_usage():
    example_text = """example:
        * se
            --txt mine name is test123
            --workdir /tmp/openai
        """
    return example_text


def setup_parser():
    parser = argparse.ArgumentParser(
        description="Standard English correction system",
        epilog=get_example_usage(),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--txt",
        required=True,
        help="Text to be corrected")

    parser.add_argument(
        "--workdir",
        type=str,
        required=True,
        help="Working directory")


    return parser.parse_args(
        # [
        #    "--workdir", "/tmp/openai_model",
        #    "--txt", "mine name is test",
        # ]
    )


def main():
    """Standard English correction system
    """
    args = setup_parser()

    if not exists(args.workdir):
        makedirs(args.workdir)

    output = se(args.txt)

    write_output(args.workdir, output)

    print("done")



if __name__ == "__main__":
    main()