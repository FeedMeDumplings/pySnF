def checks(strr):
	chk = strr[::-1]
	found = False

	if chk == strr:
		found = True
	else:
		pass
	
	return found


def main():
	u_input = raw_input(str('Enter string: '))
	print checks(u_input)


if __name__ == '__main__': main()