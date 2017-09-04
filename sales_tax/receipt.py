from sales_tax_calculator import SalesTaxCalculator


class Receipt:
    def __init__(self, line_items):
        self.line_items = line_items
        self.sales_tax_calculator = SalesTaxCalculator()

    def print_bill(self):
        sales_tax = 0
        total = 0

        for line_item in self.line_items:
                line_item_tax = self.sales_tax_calculator.calculate_sales_tax(line_item)
                line_item.set_tax(line_item_tax)
                line_item.print_line_item()
                sales_tax = line_item.tax + sales_tax
                line_item_cost = line_item.get_line_item_cost()
                total = line_item_cost + total

        print "Sales Taxes: %s" %(self.sales_tax_calculator.round_to_05(sales_tax))
        print "Total: %s" %(self.sales_tax_calculator.round_to_05(total))