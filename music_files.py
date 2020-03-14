import sys

def system_example():
	flac_cmd = 'flac ...'
	r = system(flac_cmd)
	if r:
		failure(r, "error encoding %s" % outname)
		system("touch '%s/FAILURE'" % mp3_dir)
	return 0

def main():
	print("hey %s" % sys.argv[0])

if __name__ == "__main__":
	main()


