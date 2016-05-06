from nose.tools import assert_equal

class Node(object):

	def __init__(self, value):
		self.value = value
		self.nextnode = None

def chk_cycle(node):

	# set both points
	pos1 = node
	pos2 = node
	check = False

	# loop untl the end of the list
	while pos2 != None and pos2.nextnode != None:
		pos1 = pos1.nextnode
		# pos2 to traverse twice as fast to check for 
		# circular attribute of list
		pos2 = pos2.nextnode.nextnode

		if pos2 == pos1:
			check = True
			return check

	return check

class TestCycle(object):

	def test(self, sol):
		assert_equal(sol(a), True)
		print 'Test passed'

if __name__ == '__main__':
	a = Node(1)
	b = Node(2)
	c = Node(3)
	d = Node(4)

	# cycle list
	a.nextnode = b
	b.nextnode = c
	c.nextnode = d
	d.nextnode = a

	t = TestCycle()
	t.test(chk_cycle)
