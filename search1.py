def binarysearch(alist, item):
	first = 0
	last = len(alist) - 1
	found = False

	while first <= last and not found:
		mid = (first + last) // 2
		if alist[mid] == item:
			found = True
		else:
			if item < alist[mid]:
				last = mid - 1
			else:
				first = mid + 1

	return found



def main():
	chk_list = [0, 1, 2, 3, 25, 28, 31, 45, 49]
	print binarysearch(chk_list, 2)

if __name__ == '__main__': main()
