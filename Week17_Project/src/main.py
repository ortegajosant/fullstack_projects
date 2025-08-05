import argparse

from src.entities.FinanceHandler import FinanceHandler
from src.interface.main_view import run_gui


def define_args_parser():
    """Define the command line argument parser."""
    parser = argparse.ArgumentParser(description="Finance Manager Application")
    parser.add_argument(
        "--data-directory",
        type=str,
        help="Path to the directory containing finance data files",
    )
    args = parser.parse_args()
    return args


def initialize_finance_handler(args):
    data_directory = args.data_directory
    finance_handler = FinanceHandler(data_directory)
    return finance_handler


def main():
    args = define_args_parser()
    finance_handler = initialize_finance_handler(args)
    run_gui(finance_handler)


if __name__ == "__main__":
    main()
