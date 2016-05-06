# some initial experiment with file date reading and writing

import os, glob, re, time

class File:
	def __init__(self, file_name):
		self.file_name = file_name

	def reading(self):
		read_list = []
		read_dict = []
		header = ['Date', 'Max', 'Min', 'Preci']
		
		# check if file exists
		try:
			fd = open(self.file_name, 'r')
			reads = fd.readlines()
			fd.close()
		except IOError:
			print 'File does not exist\n'
		else:
			for line in reads:
				read_list.extend(line.rstrip('\t\n').split('\t'))
 
		# suing the zip function to pair the data in the file with the headers
		# store each line in the file as a list of dictionaries
		read_dict = [
	 		dict(zip(header, items)) 
	 			for items in zip(read_list[::4], read_list[1::4], read_list[2::4], read_list[3::4])
		]
		
		return read_dict

	def delete(self, del_item, wFile):
		k = self.reading()
		temp = []
		hold = ''
		i = 0

		# all file data with '-9999' is incomplete
		# delete all lines of data which have '-9999'

		while i < len(k):
			if k[i]['Preci'] == del_item or k[i]['Min'] == del_item or k[i]['Max'] == del_item:
				del k[i]
			else:
				i += 1

		#print k
		for j in k:
			temp.append(j.values())

		newList = [newList[::] for newList in temp]

		# print newList
		
		for m in range(len(newList)):
		 	hold += '\t'.join(newList[m]) + '\n'
		
		# print hold
		writes = open(wFile, 'w')
		writes.write(hold)
		writes.truncate()
		writes.close()

def main():
	# travesing directory to script, input file data and output file
	script_dir = os.path.dirname(os.path.abspath(__file__))
	write_path = os.path.join(script_dir, 'sort/data.txt')
	read_path = os.path.join(script_dir, 'wx_data')

	currentFile = glob.glob(os.path.join(read_path, '*.txt'))
	for file in currentFile:
		x = File(file)
		x.delete('-9999', write_path)

if __name__ == '__main__':
	# timer to keep track of data reading and writing
	start_time = time.time()
	main()
	print '<< %s seconds >>' %(time.time() - start_time)