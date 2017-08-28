from sales_tax_input_parser import SalesTaxInputParser
from sales_tax_calculate import SalesTaxCalculate

def main():
    deatils_input = list(multiline_input())
    items_data = SalesTaxInputParser(deatils_input).get_items_details()
    SalesTaxCalculate(items_data)

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