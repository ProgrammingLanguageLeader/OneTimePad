import argparse
import secrets
import re


def parse_key_length(length: str) -> int:
    size_dict = {
        'B': 1,
        'KB': 1024,
        'MB': 1024 ** 2,
        'GB': 1024 ** 3
    }
    pattern = re.compile('^(\d+)(B|KB|MB|GB)$')
    default_error_code = -1
    if length.isdecimal():
        return int(length)
    matched_string = pattern.match(length)
    if matched_string:
        size_in_units = matched_string[1]
        unit = matched_string[2]
        return int(size_in_units) * size_dict[unit]
    return default_error_code


def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='Random key generator'
    )
    parser.add_argument(
        'length',
        type=str,
        help='Key length'
    )
    parser.add_argument(
        'output',
        type=str,
        help='Output file path'
    )
    return parser


if __name__ == '__main__':
    parser = create_argument_parser()
    args = parser.parse_args()
    length = parse_key_length(args.length)
    output_file_path = args.output
    if length <= 0:
        exit('Invalid length')

    write_mode = 'wb'
    block_size = 8192
    with open(output_file_path, write_mode) as output_file:
        bytes_left = length
        while bytes_left > 0:
            token_length = block_size \
                if bytes_left >= block_size \
                else bytes_left
            output_block = secrets.token_bytes(block_size)
            output_file.write(output_block)
            bytes_left -= token_length
    print('Done')
