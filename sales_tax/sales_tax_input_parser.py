from line_item import LineItems

class SalesTaxInputParser:
    def __init__(self, items_detail):
        self.items_details = items_detail

        if len(items_detail) < 1:
            raise IOError("Invalid input")

    def get_line_items_details(self):
        item_data = []

        for item_deatils in self.items_details:
            if "Input" in item_deatils:
                continue
            list_item_details = item_deatils.split()
            item_data.append(LineItems(list_item_details))
        return item_data