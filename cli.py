import json
from argparse import ArgumentParser

from abuse_finder import domain_abuse, email_abuse, ip_abuse


def cli(parser: ArgumentParser):
    parser.add_argument("target", help="Target for abuse finder.")
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-e", "--email", action="store_true", help="Email target type.")
    group.add_argument("-i", "--ip", action="store_true", help="Ip target type.")
    group.add_argument("-d", "--domain", action="store_true", help="Domain target type.")
    parser.add_argument("-o", "--output", default="output.json")
    return parser.parse_args()



def main():
    try:
        parser = ArgumentParser()
        args = cli(parser)
        result = {}
        if args.email:
            result = email_abuse(args.target)
        elif args.domain:
            result = domain_abuse(args.target)
        elif args.ip:
            result = ip_abuse(args.target)

        with open(args.output, "w") as f:
            json.dump(result, f, indent=2)
    except Exception as e:
        print(e)

    print("Done!")


if __name__ == '__main__':
    main()
