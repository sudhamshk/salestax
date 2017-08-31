from sales_tax_input_parser import SalesTaxInputParser
from sales_tax_calculator import SalesTaxCalculator
from receipt import Receipt

def main():
    deatils_input = list(multiline_input())
    line_items = SalesTaxInputParser(deatils_input).get_line_items_details()
    receipt = Receipt(line_items)
    receipt.print_bill()

def multiline_input():
    try:
        while True:
            data = raw_input()
            if not data: break
            yield data
    except KeyboardInterrupt:
        return

if __name__ == '__main__':
    main()