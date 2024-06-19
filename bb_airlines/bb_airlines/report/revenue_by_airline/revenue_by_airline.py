# Copyright (c) 2024, Victor and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder.functions import Count
from frappe.query_builder.functions import Sum

def execute(filters=None):
	columns, data = [], []
	airplane = frappe.qb.DocType('Airplane')
	ticket = frappe.qb.DocType('Airplane Ticket')
	flight = frappe.qb.DocType('Airplane Flight')
	revenue = Sum(ticket.total_amount).as_('revenue')

	query = frappe.qb.select(airplane.airline, revenue).from_(ticket).join(flight).on(ticket.flight == flight.name).join(airplane).on(airplane.name == flight.airplane).groupby(airplane.airline)

	data = query.run()

	columns = [
		{
			'fieldname': 'airline',
			'label': 'Airline',
			'fieldtype': 'Link',
			'options': 'Airline',
			'width': 300
		},
		{
			'fieldname': 'revenue',
			'label': 'Revenue',
			'fieldtype': 'Currency',
			'options': 'USD',
			'width': 200


		}]

	return columns, data
