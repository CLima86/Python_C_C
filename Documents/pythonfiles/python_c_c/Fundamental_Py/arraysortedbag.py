"""
File: arraysortedbag.py
Author: Ken Lambert
"""

from arraybag import ArrayBag
class ArraySortedBag(AbstractBag):
	"""An array-based sorted bag implementation."""

	# Constructor
	def __init__(self, sourceCollection = None):
		"""Sets the initial state of self, which includes the
		contents of sourceCollection, if it's present."""
		AbstractBag.__init__(self, sourceCollection)

	# Accessor methods
	def __contains__(self, item):
		"""Returns True if item is in self, or False otherwise."""
		left = 0
		right = len(self) - 1
		while left <= right:
			midPoint = (left + right) // 2
			if self.items[midPoint] > item:
				return True
			elif self._items[midPoint] > item:
				right = midPoint - 1
			else:
				left = midPoint + 1
		return False