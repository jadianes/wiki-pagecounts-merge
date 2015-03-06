import argparse
import os
from urllib2 import urlopen, URLError, HTTPError
from urllib import urlretrieve

url_root = 'https://dumps.wikimedia.org/other/pagecounts-raw'

def download_file_by_read(url, target_folder):
    # Open the url
    try:
        f = urlopen(url)
        print "downloading " + url

        # Open our local file for writing
        with open(os.path.join(target_folder, os.path.basename(url)), "wb") as local_file:
            local_file.write(f.read())

        return local_file

    #handle errors
    except HTTPError, e:
        print "HTTP Error:", e.code, url
    except URLError, e:
        print "URL Error:", e.reason, url

# Example link: https://dumps.wikimedia.org/other/pagecounts-raw/2009/2009-05/pagecounts-20090501-000000.gz


def download_file_by_retrieve(url_to_download, target_path):
    print "downloading " + url_to_download
    urlretrieve(url_to_download, os.path.join(target_path, os.path.basename(url_to_download)))


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("target_path", help="A path to download all the files")
    parser.add_argument("year", help="The year to download page counts as a number", type=int)
    parser.add_argument("month", help="The month to download page counts as a number", type=int)
    parser.add_argument("from_day", help="The starting day to download page counts as a number", type=int)
    parser.add_argument("to_day", help="The ending day to download page counts as a number", type=int)
    args = parser.parse_args()

    # Iterate over image ranges
    for day in range(args.from_day, args.to_day+1):
        for hour in range(0,24):
            url_to_download = (url_root + "/%d/%d-%02d/pagecounts-%d%02d%02d-%02d0000.gz" %
                               (args.year, args.year, args.month, args.year, args.month, day, hour))
            # Create destination folder if needed
            if not os.path.exists(args.target_path):
                os.makedirs(args.target_path)
            elif not os.path.isdir(args.target_path):
                print("Target folder is not a directory")
                exit()
            # Finally download the file
            # download_file_by_retrieve(url_to_download, args.target_path)
            download_file_by_read(url_to_download, args.target_path)



if __name__ == '__main__':
    main()
