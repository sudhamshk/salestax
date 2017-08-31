class LineItems:
    def __init__(self, line_item_details):
        self.quantity = line_item_details[0]
        self.value = float(line_item_details[-1])
        self.imported = False
        self.tax = 0

        if "at" in line_item_details and "imported" not in line_item_details:
            self.name = " ".join(line_item_details[1:line_item_details.index("at")])

        if "imported" in line_item_details:
            line_item_details.remove("imported")
            self.name = " ".join(line_item_details[1:line_item_details.index("at")])
            self.imported = True

    def set_tax(self, tax):
        self.tax = tax

    def get_line_item_cost(self):
        return float(self.quantity)*(self.tax + self.value)

    def print_line_item_details(self):
        if self.imported:
            print "%s imported %s: %s" % (self.quantity, self.name, float(self.quantity)*(self.tax + self.value))
        else:
            print "%s %s: %s" % (self.quantity, self.name, float(self.quantity)*(self.tax + self.value))