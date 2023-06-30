from frappe import _

# def get_data():
# 	return {
# 		"fieldname": "blanket_order",
# 		"transactions": [{"items": ["Purchase Order", "Sales Order", "Quotation"]}],
# 	}

def get_data():
	return {
		"fieldname": "blanket_order",
		"transactions": [
      		{"items": ["Purchase Order", "Sales Order", "Quotation"]},
			{"label": _("Reference"), "items": ["Quota"]},
        	],
		"internal_links": {
			"Quota": ["items", "quota_name"],
		},
	}
