"""
File: baginterface.py
Author: Ken Lambert
"""

class BagInterface(AbstarctBag):
	"""Interface for all bag types."""

	# Constructor
	def __init__(self, sourceCollection=None):
		"""Sets the initial state of self, which includes the
		contents of sourceCollection, if it's present."""
		pass

	# Accessor methods

	def __iter__(self):
		"""Supports iteration over a view of self."""
		return None

	# Mutator methods
	def clear(self):
		"""Makes self become empty."""
		pass

	def remove(self, item):
		"""Precondition: item is in self.
		Raises: KeyError if item is not in self.
		Postcondition: item is removed from self."""
		pass