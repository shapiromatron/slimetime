from gooey import Gooey, GooeyParser


@Gooey()
def main():
    # borrowed from https://github.com/chriskiehl/GooeyExamples/blob/master/examples/simple_demo.py
    parser = GooeyParser(description="Process some integers.")

    parser.add_argument("required_field", metavar="Some Field", help="Enter some text!")

    parser.add_argument(
        "-f",
        "--foo",
        metavar="Some Flag",
        action="store_true",
        help="I turn things on and off",
    )

    parser.parse_args()
    print("Hooray!")


def app():
    main()
