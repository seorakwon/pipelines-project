import cleaning
import scraping
import merging
import extra
import argparse

def parse_arguments():
    parser = argparse.ArgumentParser(description='Get crash information')
    parser.add_argument('--operator', help='get the 10 airlines with the most accidents')
    parser.add_argument('--year',  help='get the 10 years with the most airplane crashes')
    args = parser.parse_args()


    return args



def main():
    args = parse_arguments()
    print(args)
    
if __name__ == '__main__':
    main()
