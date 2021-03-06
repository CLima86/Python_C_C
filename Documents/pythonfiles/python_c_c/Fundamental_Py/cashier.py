"""
File: cashier.py
"""

from linkedqueue import LinkedQueue
class Cashier(object):
	def __init__(self):
		self._totalCustomerWaitTime = 0
		self._customersServed = 0
		self._currentCustomer = None
		self._queue = LinkedQueue

	def addCustomer(self, c):
		if self._currentCustomer is None:
			# No customers yet
			if self._queue.isEmpty():
				return
			else:
				# Pop first waiting customer
				# and tally results
				self._currentCustomer = self._queue.pop()
				self._totalCustomerWaitTime += currentTime - self._currentCustomer.arrivalTime()
				self._customersServed += 1

		# Give a unit of service
		self._currentCustomer.serve()

		# If current customer is finished, send it away
		if self._currentCustomer.amountOfServiceNeeded() == 0:
			self._currentCustomer = None

	def __str__(slef):
		result = "TOTALS FOR THE CASHIER\n" + "Number of customers served:     " + 
				 str(self._customersServed) + "\n"
		if self._customersServed != 0:
			aveWaitTime = self._totalCustomerWaitTime / self._customersServed
			result += "Number of customers left in queue: " + str(len(self._queue)) + "\n" +
					  "Average time customers spend\n" + "waiting to be served:       " + 
					  "%5.2f" % aveWaitTime

		return result
