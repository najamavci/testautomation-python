from src.payments.payment_gateway import PaymentGateway


class Order:
    def __init__(self, products, amount, payment_gateway=None):
        self.products = products
        self.amount = amount
        self.status = "unpaid"
        self.payment_gateway = payment_gateway if payment_gateway else PaymentGateway()

    def make_payment(self):
        success = self.payment_gateway.execute_payment(self.amount)
        if success:
            self.status = "paid"
        else:
            self.status = "error"
        return success