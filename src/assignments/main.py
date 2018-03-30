from src.assignments.invoice_item import InvoiceItem
from src.assignments.invoice import Invoice
#Write import statements for classes invoice and invoice_item
'''
LOOK AT THE TEST CASES FOR HINTS
Create an invoice object
In the loop:
Create a new InvoiceItem
Create a user controlled loop to continue until y is not typed, in loop...
    Prompt user for description, quantity, and cost.
    Add values to the InvoiceItem.
    Add the InvoiceItem to the invoice object.
    Once user types a letter other than y display the Invoice to screen
'''


def main():
    invoice_obj = Invoice()
    keep_going = 'y'
    while keep_going == 'y':
        invoice_item = InvoiceItem()
        description = input("Enter description: ")
        quantity = input("Enter quantity: ")
        cost = input("Enter cost: ")

        invoice_obj.append(invoice_item)
        keep_going = input("Enter y to continue: ")
    print(invoice_obj)


main()