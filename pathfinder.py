import os, glob, re

def main():
	script_dir = os.path.dirname(os.path.abspath(__file__))
	path1 = os.path.join(script_dir, 'check')
	currentFile = glob.glob( os.path.join(path, '*.txt.'))
	

	print path1
	print currentFile

if __name__ == '__main__': main()