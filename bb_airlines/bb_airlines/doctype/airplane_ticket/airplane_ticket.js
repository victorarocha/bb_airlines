// Copyright (c) 2024, Victor and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airplane Ticket", {
	refresh(frm) {
		frm.trigger("update_total_amount");
		frm.add_custom_button("Assign Seats", 
			() => { 
				frappe.prompt(
					[{'fieldname': 'seat', 'fieldtype': 'Data', 'label': 'Seat Number'}],
					(values) => {
						console.log(values);
						frm.set_value('seat', values.seat);
					},
					"Select Seat",
					"Assign");
				});
	},
	flight_price(frm) {
		frm.trigger("update_total_amount");
	},
	update_total_amount(frm) {
		let total_a = 0;
		for (let add_on of frm.doc.add_ons) {
			total_a += add_on.amount;
		}
		
		total_a = frm.doc.flight_price ? total_a + frm.doc.flight_price : total_a;

		frm.set_value('total_amount', total_a);
	},
	
});

frappe.ui.form.on("Airplane Ticket Add-on Item", {
	refresh(frm) {
		frm.trigger("update_total_amount");
	},
	amount(frm) {
		frm.trigger("update_total_amount");
	},
	add_ons_remove(frm) {
		frm.trigger("update_total_amount");
	},
	add_ons_add(frm) {
		frm.trigger("update_total_amount");
	}
});
