## NOde Class ##
class Node(object):
	"""Representing a singly linked node."""
	def __init__(self, data, next = None):
		"""Instantiates a Node with a default next of None."""
		self.data = data
		self.next = next
# Just an empty link
node1 = None
node2 = Node("A", None)
node3 = Node("B", node2)

class TwoWayNode(Node):
	"""class for TwoWayNode"""
	def __init__(self, data, previous = None, next = None):
		"""Instantiates a two way node."""
		Node.__init__(self, data, next)
		self.previous = previous