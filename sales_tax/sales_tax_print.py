class SalesTaxPrint:
    def __init__(self, item_data, item_total_cost):
        self.item_data = item_data
        self.item_total_cost = item_total_cost

    def print_bill(self,):
        if self.item_data.imported:
            print "%s imported %s: %s" % (self.item_data.quantity, self.item_data.name, self.item_total_cost)
        else:
            print "%s %s: %s" % (self.item_data.quantity, self.item_data.name, self.item_total_cost)