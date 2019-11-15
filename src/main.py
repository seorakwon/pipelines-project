import cleaning
import scraping
import merging
import extra
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Get crash information')
    parser.add_argument('--operator', action='store_true', help='get the 10 airlines with the most accidents')
    parser.add_argument('--year', action='store_true', help='get the 10 years with the most airplane crashes')
    args = parser.parse_args()
    check_arguments(args)

    return args

def main():
    args = parse_arguments()
    if args.operator:
        get_operator()
    if args.year:
        get_year()
    
if __name__ == '__main__':
    main()
