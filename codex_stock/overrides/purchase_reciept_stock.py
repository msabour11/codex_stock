import frappe


# def on_submit_purchase_receipt(doc, method):
#     # Define the 12 components for "ديك"
#     components = [
#         "قطع لحم ديك",
#         "قنصة ديك",
#         "كبدة ديك",
#         "هيكل ديك",
#         "زلموكة ديك",
#         "شيش ديك",
#         "صدور ديك",
#         "وراك ديك",
#         "دبوس ورك ديك",
#         "دبوس صدر ديك",
#         "جناح ديك",
#         "رقبة ديك",
#     ]

#     # Loop through items in the Purchase Receipt
#     for item in doc.items:
#         if item.item_code == "ديك":  # Check if the received item is "ديك"
#             stock_entry = frappe.new_doc("Stock Entry")
#             stock_entry.stock_entry_type = "Material Receipt"
#             stock_entry.to_warehouse = (
#                 item.warehouse
#             )  # Use the warehouse from the Purchase Receipt

#             # Add each component with the same quantity as the "ديك" item
#             for component in components:
#                 stock_entry.append(
#                     "items",
#                     {
#                         "item_code": component,
#                         "qty": item.qty,  # Each "ديك" equals one of each component
#                         "t_warehouse": item.warehouse,
#                     },
#                 )

#             # Submit the Stock Entry to update stock
#             stock_entry.insert()
#             stock_entry.submit()


import frappe


def on_submit_purchase_receipt(doc, method):
    # Define parts and their quantities per "ديك"
    parts = {
        "قنصة ديك": 1,
        "كبدة ديك": 1,
        "هيكل ديك": 1,
        "زلموكة ديك": 1,
        "شيش ديك": 2,
        "صدور ديك": 2,
        "وراك ديك": 2,
        "دبوس ورك ديك": 2,
        "دبوس صدر ديك": 2,
        "جناح ديك": 2,
        "رقبة ديك": 1,
    }

    # Loop through each item in the Purchase Receipt
    for item in doc.items:
        if item.item_code == "ديك":  # Check if the item is "ديك"
            print("items is correctly")
            stock_entry = frappe.new_doc("Stock Entry")

            stock_entry.stock_entry_type = "Material Receipt"
            stock_entry.to_warehouse = (
                item.warehouse
            )  # Use the warehouse from the Purchase Receipt

            # Add each part with the appropriate quantity multiplied by the "ديك" quantity
            for part, qty_per_deek in parts.items():
                stock_entry.append(
                    "items",
                    {
                        "item_code": part,
                        "qty": qty_per_deek
                        * item.qty,  # Calculate total quantity for the received "ديك"
                        "t_warehouse": item.warehouse,
                    },
                )

            # Submit the Stock Entry to update stock
            stock_entry.insert()
            stock_entry.submit()
