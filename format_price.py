import argparse
import re


def format_price(price):
    if not (isinstance(price, (int, float, str))):
        raise TypeError('Price have to be int, float or str')
    if isinstance(price, str):
        price_pattern = re.compile(r'-?\d+[\.,]?\d*$')
        if re.match(price_pattern, price):
            price = price.replace(',', r'.')
        else:
            raise ValueError('Incorrect value')
    price = float(price)
    price = round(price, 2)
    if price.is_integer():
        return format(price, ',.0f').replace(',', ' ')
    else:
        return format(price, ',.2f').replace(',', ' ')


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='returns price in easy-readable format')
    parser.add_argument('price', help='input price')
    args = parser.parse_args()
    print(format_price(args.price))
