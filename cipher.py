import argparse
from functools import partial


def encrypt_text(plain_text: bytes, key: bytes) -> bytes:
    encrypted_text = b''
    byte_endian = 'big'
    for char_index in range(len(plain_text)):
        plain_char = plain_text[char_index]
        key_char = key[char_index]
        encrypted_text += (plain_char ^ key_char).to_bytes(1, byte_endian)
    return encrypted_text


def create_argument_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description='One time pad encoder/decoder'
    )
    parser.add_argument(
        'key',
        type=str,
        help='Encryption key file path'
    )
    parser.add_argument(
        'source',
        type=str,
        help='Source file path'
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
    source_file_path = args.source
    output_file_path = args.output
    key_file_path = args.key

    read_mode = 'rb'
    write_mode = 'wb'
    block_size = 8192
    with open(key_file_path, read_mode) as key_file, \
            open(source_file_path, read_mode) as source_file,\
            open(output_file_path, write_mode) as output_file:
        for source_block in iter(partial(source_file.read, block_size), b''):
            key_block: bytes = key_file.read(len(source_block))
            output_block = encrypt_text(source_block, key_block)
            output_file.write(output_block)
    print('Done')
