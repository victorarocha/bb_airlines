# Copyright (c) 2024, Victor and contributors
# For license information, please see license.txt

import frappe
from random import randrange
from frappe.model.document import Document


class AirplaneTicket(Document):
	def validate(self):
		self.check_add_ons_duplicates()
		frappe.throw(f"Capacity: {self.flight.airplane.capacity}")

	def before_submit(self):
		if self.status != "Boarded":
			frappe.throw("You can only submit a ticket that has been boarded")

	def before_save(self):
		if self.seat is None:
			self.assign_a_seat()

	def check_add_ons_duplicates(self):
		items = []
		duplicates = set()

		for item in self.add_ons:
			items.append(item.item)

		for add_on in self.add_ons:
			if items.count(add_on.item) > 1:
				duplicates.add(add_on.item)

		if len(duplicates) > 0:
			frappe.throw(f"Add-on {duplicates} duplicated")

	def assign_a_seat(self):
		# generate a random seat row between 1 and 25
		seat_row = randrange(1, 26)
		# generate a random row letter between A (chr 65) and E (chr 69)
		seat_letter = chr(randrange(65, 70))
		self.seat = f"{seat_row}{seat_letter}"
		self.total_amount = sum([add_on.amount for add_on in self.add_ons]) + self.flight_price

