import argparse

def frequency_to_hash(frequencies):
    byte_array = []
    for frequency in frequencies:
        byte = int(frequency/20) # mapping each frequency of RICK to a byte
        byte_array.append(byte)
    return bytes(byte_array).hex()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Convert a frequency array to a RICK portal')
    parser.add_argument('frequencies', nargs='+', type=int, help='The input frequency array')
    args = parser.parse_args()
    print(frequency_to_hash(args.frequencies))
