import argparse, os, gzip
import re

file_name_pattern = r'pagecounts-\d{8}-\d{6}.gz'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("input_folder", help="The folder containing the input files")
    parser.add_argument("target_file", help="The file where the result will be written. "
                                            "If the files exists, contents will be appended")
    args = parser.parse_args()

    # open target file for write or append
    if not os.path.exists(args.target_file):
        target_f = open(args.target_file, 'w')
    else:
        target_f = open(args.target_file, 'a')

    # here we scan every file, appending the timestamp part of the filename to the new lines in the target
    for a_file in sorted(os.listdir(args.input_folder)):
        if re.match(file_name_pattern,a_file):
            print "Merging file ", a_file, "..."
            # we have our file
            f = gzip.open(os.path.join(args.input_folder, a_file), 'rb')
            file_content = f.readlines()
            for line in file_content:
                new_line = a_file[11:-3] + ' ' + line
                target_f.write(new_line)

    target_f.close()

if __name__ == '__main__':
    main()
