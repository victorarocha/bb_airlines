// Copyright (c) 2024, Victor and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {



	},
	update_total_amount(frm) {
		let total_amount = 0;
		for (let add_on of frm.doc.add_ons) {
			total_amount += add_on.amount;
		}
		total_amount += frm.doc.flight_price;

		frm.set_value('total_amount', total_amount);
    },
	flight_price(frm) {
		frm.trigger('update_total_amount');
	}}
);

frappe.ui.form.on("Airplane Ticket Add-on Item", {
	refresh(frm) {

	},
	amount(frm) {
		frm.trigger('update_total_amount');
	},
	add_ons_remove(frm) {
		frm.trigger('update_total_amount');
	}
})
