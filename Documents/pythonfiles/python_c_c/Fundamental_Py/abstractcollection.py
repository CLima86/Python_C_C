"""
File: abstractcollection.py
Author: Ken Lambert
"""

class AbstractCollection(object):
	"""An abstract collection implementation."""

	# Constructor
	def __init__(self, sourceCollection = None):
		"""Sets the initial state of self, which includes the
		contents of sourceCollection, if it's present."""
		self._size = 0
		if sourceCollection:
			for item in sourceCollection:
				self.add(item)