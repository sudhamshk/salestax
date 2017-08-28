from sales_tax_print import SalesTaxPrint

class SalesTaxCalculate:
    tax_exemted = {"books" : ["book"],
                   "food" : ["chocolate bar", "box of chocolates"],
                   "Medical" : ["packet of headache pills"]}

    def __init__(self, items_data):
        self.items_data = items_data
        self.sales_tax = 0
        self.total = 0

        for item_data in self.items_data:
            item_tax = self.calculate_sales_tax(item_data)
            item_total_cost = item_data.value + item_tax
            SalesTaxPrint(item_data, item_total_cost).print_bill()
            self.sales_tax = item_tax + self.sales_tax
            self.total = item_total_cost + self.total

        print "Sales Taxes: %s" %(self.round_to_05(self.sales_tax))
        print "Total: %s" %(self.round_to_05(self.total))

    def calculate_sales_tax(self, item_data):
        products = []

        for values in self.tax_exemted.values():
            for value in values:
                products.append(value)

        if any(item_data.name in product for product in products):
            if item_data.imported:
                return self.round_to_05((5*item_data.value)/100)
            else:
                return 0
        else:
            if item_data.imported:
                return self.round_to_05(((5*item_data.value)/100) + ((item_data.value*10)/100))

            else:
                return self.round_to_05(((item_data.value*10)/100))

    def round_to(self, n, precision):
        correction = 0.5 if n >= 0 else -0.5
        return int( n/precision+correction ) * precision

    def round_to_05(self, n):
        return self.round_to(n, 0.05)

    def print_bill(self,item_data, item_total_cost):
        if item_data.imported:
            print "%s imported %s: %s" % (item_data.quantity, item_data.name, item_total_cost)
        else:
            print "%s %s: %s" % (item_data.quantity, item_data.name, item_total_cost)