import argparse
import os
from functools import partial
import re
import pdb, traceback, sys

import xml.etree.ElementTree as ET

def content(tag):
    return tag.text + ''.join(ET.tostring(e).decode() for e in tag)

def generate_test_files(args,preposition_file):
    try:
        if preposition_file.startswith('.'):
            return preposition_file

        preposition_file_path = os.path.join(args.xml_folder_path,preposition_file)
        preposition = preposition_file.split('.')[0].split('-')[1]
        outfile_path = os.path.join(
            args.out_folder_path,
            preposition+'.out'
        )
        outfile = open(outfile_path,'w')

        key_file_path = os.path.join(args.key_folder_path, preposition + '.key')

        with open(key_file_path) as key_file:
            preposition_instance_to_sense = {
                x.split()[1] : x.split()[2] for x in key_file.readlines()
            }
        
        preposition_file_tree = ET.parse(preposition_file_path)
        lexlt = preposition_file_tree.getroot()

        for instance in lexlt:
            preposition_id = instance.attrib['id']
            sentence = re.sub('<[^<]+>', "",content(instance[0])).strip('` \n')

            if preposition_id in preposition_instance_to_sense:
                if args.mode == 'with_key':
                    outfile.write(
                        '{}|{}'.format(
                            sentence,
                            preposition_instance_to_sense[preposition_id]
                        ) + '\n'
                    )
                else:
                    outfile.write(
                        '{}'.format(
                            sentence,
                        ) + '\n'
                    )
        outfile.close()

        return preposition_file_path
    except:
        traceback.print_exc(file=sys.stdout)
        pdb.set_trace()





    


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='')

    parser.add_argument('--xml_folder_path',required=True)
    parser.add_argument('--key_folder_path',required=True)
    parser.add_argument('--out_folder_path',required=True)
    parser.add_argument('--mode',required=True,choices=['with_key', 'without_key'])

    args = parser.parse_args()

    _generate_test_files = partial(generate_test_files,args)
    print(
        list(map(_generate_test_files,os.listdir(args.xml_folder_path)))
    )

