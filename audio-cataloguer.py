#!/usr/bin/python3
import sys
import getopt
from tagger import Tagger
from cataloguer import Cataloguer

def usage():
	print("USAGE")
	print("	python3 audio-cataloguer.py -p <path_to_files> [-q]")
	print
	print("OPTIONS")
	print("	-p		Select path to file to be cataloged")
	print("	-q		Quite mode, do not print step-by-step logs")

def main(argv):
	try:
		opts, args = getopt.getopt(argv, "hp:q", ["help"])
	except getopt.GetoptError:
		usage()
		sys.exit(2)
	path = ""
	quiet = False
	for opt, arg in opts:
		if opt in ('-h', '--help'):
			usage()
			sys.exit(0)
		if opt == '-q':
			quiet = True
		elif opt == '-p':
			path = arg
		else:
			usage()
			sys.exit(0)
	if not path:
		usage()
		sys.exit(0)

	print("Starting tag scanning...")
	tagger = Tagger(path, quiet)
	tagger.scan_audio_files()
	print("...Done!")
	print

	print("Starting file cataloguing...")
	dic = tagger.get_scanned_dic()
	cataloguer = Cataloguer(path, dic, quiet)
	cataloguer.create_catalogue()
	print("...Done!")
	print


if __name__ == '__main__':
	main(sys.argv[1:])
	sys.exit(0)
