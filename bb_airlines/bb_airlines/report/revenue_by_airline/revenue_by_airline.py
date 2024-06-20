# Copyright (c) 2024, Victor and contributors
# For license information, please see license.txt

import frappe
from frappe.query_builder.functions import Sum

def execute(filters=None):
	columns, data, report_summary = [], [], []
	airplane = frappe.qb.DocType('Airplane')
	airline = frappe.qb.DocType('Airline')
	ticket = frappe.qb.DocType('Airplane Ticket')
	flight = frappe.qb.DocType('Airplane Flight')

	query = (
		frappe.qb
		.select(airline.name.as_('airline'), Sum(ticket.total_amount).as_('revenue'))
		.from_(airline)
		.left_join(airplane).on(airline.name == airplane.airline)
		.left_join(flight).on(airplane.name == flight.airplane)
		.left_join(ticket).on(flight.name == ticket.flight)
		.groupby(airline.name)
	)

	data = query.run(as_dict=True)

	for x in data:
		if x.revenue is None:
			x.revenue = 0

	total_revenue = sum([x.revenue for x in data])

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

	chart = {
		"data": {
			"labels": [x.airline for x in data],
			"datasets": [
				{
					"values": [x.revenue for x in data]
				}
			],
		},
		"type": "donut"
	}

	report_summary = [{
		"value": total_revenue,
		"label": "Total Revenue",
		"indicator": "Green",
		"datatype": "Currency",
		"currency": "USD"
	}]

	return columns, data, None, chart, report_summary
