class Invoice:

    def __init__(self, bill_to, date):

        self.bill_to = bill_to
        self.date = date
        self.invoice_items = []
        self.invoice_total = 0

    def add_invoice_item(self, invoice_item):
        '''
        Write the code to append an invoice_item to the self.invoice_items list
        :param invoice_item:
        :return: void(nothing)
        '''
        self.invoice_items.append(invoice_item)
        return

    def get_invoice_total(self):
        '''
        Write code to iterate the self.invoice_items list and get the invoice self.invoice_total
        :return: the self.invoice_total
        '''
        for i in self.invoice_items:
            self.invoice_total += self.invoice_items[i]
        return self.invoice_total

    def print_invoice(self):
        '''
        Nothing to do here, I've written the code
        :return:
        '''

        extended_cost = 0
        print('Description', 'Quantity', '     Cost', 'Extended Cost')

        for invoice_item in self.invoice_items:
            extended_cost = invoice_item.quantity * invoice_item.cost
            print(invoice_item.description, format(invoice_item.quantity, '12d'), format(invoice_item.cost, '9,.2f'), \
                  format(extended_cost, '13,.2f'))

        print('Total: ', ' ' *29,format(extended_cost, '.2f'))
