from database.init_db import create_table
from cli.product_cli import ProductCLI


def main():
    create_table()
    product_cli = ProductCLI()
    product_cli.start()


if __name__ == "__main__":
    main()
