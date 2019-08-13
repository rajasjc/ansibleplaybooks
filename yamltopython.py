#!/usr/bin/python 
import argparse,yaml,pprint
parser = argparse.ArgumentParser(description="JSON Parser")
parser.add_argument("-f",help="File Name")

args = parser.parse_args()

pprint.pprint(yaml.load(open(args.f).read()))
