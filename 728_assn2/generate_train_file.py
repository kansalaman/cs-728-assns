import argparse
import random
import pdb

def has_label(datum):
    return len(datum.split(','))>3

def clean_datum(datum):
    dsplit = datum.split(',')
    return ','.join(
        [
            dsplit[0],
            dsplit[1],
            dsplit[3]
        ]

    ) + '\n'

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--input_file_path',required=True)
    parser.add_argument('--output_file_path',required=True)
    parser.add_argument('--test_ratio',required=True,type=float)

    args = parser.parse_args()

    random.seed(42)

    with open(args.input_file_path) as input_file:
        input_file_lines = input_file.readlines()
        data = list(
            filter(
                has_label,
                input_file_lines
            )
        )

        # pdb.set_trace()

        train_data = list(
            map(
                clean_datum,
                random.sample(
                    data,
                    int(len(data)*(1-args.test_ratio))
                )
            )
        )

        with open(args.output_file_path,'w') as output_file:
            output_file.writelines(train_data)
    

