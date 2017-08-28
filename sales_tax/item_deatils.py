class ItemDetails:
    def __init__(self, item_details):
        self.quantity = item_details[0]
        self.value = float(item_details[-1])
        self.imported = False

        if "at" in item_details and "imported" not in item_details:
            self.name = " ".join(item_details[1:item_details.index("at")])

        if "imported" in item_details:
            item_details.remove("imported")
            self.name = " ".join(item_details[1:item_details.index("at")])
            self.imported = True