# Copyright (c) 2024, Victor and contributors
# For license information, please see license.txt

# import frappe
from frappe.website.website_generator import WebsiteGenerator

class AirplaneFlight(WebsiteGenerator):
	def on_submit(self):
		self.status = "Completed"

# set the title of the page
def get_list_context(context):
	context.title = 'Airplane Flights'


