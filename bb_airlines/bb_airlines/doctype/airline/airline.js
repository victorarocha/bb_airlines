// Copyright (c) 2024, Victor and contributors
// For license information, please see license.txt

frappe.ui.form.on("Airline", {
	refresh(frm) {
        const web_url = frm.doc.website;
        if (web_url) {
            frm.add_web_link(web_url, "Visit Website");
        }
	},
});
