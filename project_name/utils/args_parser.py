import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Description of the project')
    parser.add_argument('--example', default=True, help='Argument example')

    args = parser.parse_args()

    return args
