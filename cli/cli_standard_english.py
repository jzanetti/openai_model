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
            [--model  text-curie-001]
            [--max_token 30]
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

    parser.add_argument(
        "--model",
        type=str,
        required=False,
        default="text-curie-001",
        help="choose OpenAI model from text-davinci-003, "
        "text-ada-001, text-curie-001")

    parser.add_argument(
        "--max_token",
        type=int,
        required=False,
        default=30,
        help="maximum token to be applied")

    return parser.parse_args(
        # [
        #    "--workdir", "/tmp/openai_model",
        #    "--txt", "mine name is test123",
        # ]
    )


def main():
    """Standard English correction system
    """
    args = setup_parser()

    if not exists(args.workdir):
        makedirs(args.workdir)

    output = se(args.txt, args.model, args.max_token)

    write_output(args.workdir, output)

    print("done")



if __name__ == "__main__":
    main()