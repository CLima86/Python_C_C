"""
File: linkedbag.py
Author: Ken Lambert
"""
from node import Node
from abstractbag import AbstractBag
class LinkedBag(AbstractBag):
 	"""A link-based bag inplementation."""
 	def add(self, other):
 		"""Returns a new bag containing the contents
 		of self and other."""
 		result = type(self)(self)
 		for item in other:
 			result.add(item)
 		return result

 	# Constructor
 	def __init__(self, sourceCollection = None):
 		"""Sets the initial state of self, which includes the
 		contents of sourceCollection, if it's present."""
 		self._items = None
 		AbstractBag.__init__(self, sourceCollection)


 	def __iter__(self):
 		"""Supports iteration over a view of self."""
 		cursor = self._items
 		while not cursor is None:
 			yield cursor.data
 			cursor = cursor.next

 	def remove(self, item):
 		"""Precondition: item is in self.
 		Raises: KeyError if item is not in self.
 		postcondition: item is removed from self."""
 		# Check precondition and raise if necessary
 		if not item in self:
 			raise KeyError(str(item) + "not in bag")
 		# Search for the node containing thetarget item
 		# probe will point to the target node, and trailer
 		# will point to the one before it, if it exists
 		probe = self._items
 		trailer = None
 		for targetItem in self:
 			if targetItem == item:
 				break
 			trailer = probe
 		# Unhook the node to be deleted, either the first one or the
 		# one thereafter
 		if probe == self._items:
 			self._items = self._items.next
 		else:
 			trailer.next = probe.next
 		# Decrement logical size
 		self._size -= 1
 		
