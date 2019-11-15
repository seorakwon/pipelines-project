import argparse
import sys


def check_arguments(args: argparse.Namespace):
    
#Check if the user has not passed a flag pand abort
#execution if that happens, with a descriptive message

    found_arg = False
    for arg in [args.operator, args.year]:
        if arg:
            if found_arg:
                sys.exit('only one argument flag allowed')
            found_arg = True
    if not found_arg:
        sys.exit('at least an execution flag is needed')


def check_year(year: int):
#Check if the year is between the valid values accepted by the program and else abort execution
 
    if year < 1969 or year > 2019:
        sys.exit('only years between 1970 and 2019 are allowed')