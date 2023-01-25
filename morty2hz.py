import argparse



def hash_to_frequency(input_hash):
    byte_array = bytearray.fromhex(input_hash)
    frequencies = []
 

    for byte in byte_array:
        frequency = byte*20 # mapping each byte of RICK to a frequency
        frequencies.append(frequency)

    return ' '.join(map(str, frequencies))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert morty raw hex to a frequency')
    parser.add_argument('input_hash', type=str, help='inputhexheremorty')
    args = parser.parse_args()
    print(hash_to_frequency(args.input_hash))
