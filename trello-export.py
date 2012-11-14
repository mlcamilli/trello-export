import os
import sys
import argparse
import json


def main():
	parser = argparse.ArgumentParser()
	parser.add_argument("inputfile", help="the json file containing trello board data")
	parser.add_argument("--outputfile", help="the json file containing trello board data")
	args = parser.parse_args()
	print args.inputfile





if __name__ == "__main__":
	main()