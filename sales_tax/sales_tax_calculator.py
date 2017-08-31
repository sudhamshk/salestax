

class SalesTaxCalculator:
    tax_exemted = {"books" : ["book"],
                   "food" : ["chocolate bar", "box of chocolates"],
                   "Medical" : ["packet of headache pills"]}

    def __init__(self):
        self.sales_tax = 0
        self.total = 0
        self.line_item = 0

    def calculate_sales_tax(self, line_item):
        self.line_item = line_item
        products = []

        for values in self.tax_exemted.values():
            for value in values:
                products.append(value)

        if any(self.line_item.name in product for product in products):
            if self.line_item.imported:
                return self.round_to_05((5 * self.line_item.value) / 100)
            else:
                return 0
        else:
            if self.line_item.imported:
                return self.round_to_05(((5 * self.line_item.value) / 100) + ((self.line_item.value * 10) / 100))

            else:
                return self.round_to_05(((self.line_item.value * 10) / 100))

    def round_to_05(self, n, precision = 0.5):
        correction = 0.5 if n >= 0 else -0.5
        return float(n/precision+correction) * precision