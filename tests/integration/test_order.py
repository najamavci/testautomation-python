import pytest
from src.payments.order import Order
from src.payments.payment_gateway import PaymentGateway


@pytest.mark.unit
def test_make_payment_sets_order_to_paid_when_gateway_returns_true(mocker):
    gateway = PaymentGateway()
    mocker.patch.object(gateway, "execute_payment", return_value=True)
    spy = mocker.spy(gateway, "execute_payment")

    order = Order(products=["Book", "Pen"], amount=150, payment_gateway=gateway)

    result = order.make_payment()

    assert result is True
    spy.assert_called_once_with(150)
    assert order.status == "paid"


@pytest.mark.unit
def test_make_payment_sets_order_to_error_when_gateway_returns_false(mocker):
    gateway = PaymentGateway()
    mocker.patch.object(gateway, "execute_payment", return_value=False)
    spy = mocker.spy(gateway, "execute_payment")

    order = Order(products=["Book", "Pen"], amount=150, payment_gateway=gateway)

    result = order.make_payment()

    assert result is False
    spy.assert_called_once_with(150)
    assert order.status == "error"