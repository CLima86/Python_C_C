"""
File: linkedstack.py
"""

from node import Node
from abstractstack import AbstractStack

class LinkedStack(AbstractStack):
	"""Link-based stack implementation."""
	def __init__(self, sourceCollection):
		self._items = None
		AbstractStack.__init__(self, sourceCollection)

	# Accessors
	def __iter__(self):
		"""Supports iteration over a view of self.
		Visits items from bottom to top of stack."""
		def visitNodes(node):
			if not node is None:
				visitNodes(node.next)
				tempList.append(node.data)
		tempList = list()
		visitNodes(self._items)
		return iter(tempList)

	def peek(self):
		"""Returns item at top of stack.
		Precondition: the stack is not empty."""
		if self.isEmpty():
			raise KeyError("The stack is empty.")
		return self._items.data

	# Mutators
	def clear(self):
		"""Makes self become empty."""
		self._size = 0
		self._items = None

	def push(self, item):
		"""Inserts items at top of the stack."""
		self._items = Node(item, self._items)
		self._size += 1

	def pop(slef):
		"""Removes and returns he item at top of the stack.
		Precondition: the stack is not empty."""
		if self.isEmpty():
			raise KeyError("The stack is empty.")
		oldItem = self._items.data
		self._items = self._items.next
		self._size -= 1
		return oldItem