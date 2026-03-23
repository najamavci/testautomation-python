import pytest
from src.bank.logger import Logger
from src.bank.bank_account import BankAccount
from src.bank.transaction import Transaction


@pytest.mark.integration
def test_deposit_logs_message(mocker):
    logger = Logger()
    spy = mocker.spy(logger, "log")
    account = BankAccount(balance=100, logger=logger)

    account.deposit(50)

    assert account.balance == 150
    spy.assert_called_once_with("deposit: 50 kr, saldo 150 kr")


@pytest.mark.integration
def test_withdraw_logs_message_when_successful(mocker):
    logger = Logger()
    spy = mocker.spy(logger, "log")
    account = BankAccount(balance=100, logger=logger)

    result = account.withdraw(40)

    assert result is True
    assert account.balance == 60
    spy.assert_called_once_with("withdraw: 40 kr, saldo 60 kr")


@pytest.mark.integration
def test_withdraw_logs_message_when_failing(mocker):
    logger = Logger()
    spy = mocker.spy(logger, "log")
    account = BankAccount(balance=30, logger=logger)

    result = account.withdraw(100)

    assert result is False
    assert account.balance == 30
    spy.assert_called_once_with("withdraw: kunde inte ta ut 100 kr från kontot")


@pytest.mark.integration
def test_transfer_moves_money_between_accounts(mocker):
    logger = Logger()
    spy = mocker.spy(logger, "log")

    from_account = BankAccount(balance=200, logger=logger)
    to_account = BankAccount(balance=50, logger=logger)
    transaction = Transaction()

    result = transaction.transfer(75, from_account, to_account)

    assert result is True
    assert from_account.balance == 125
    assert to_account.balance == 125

    assert spy.call_count == 2
    spy.assert_any_call("withdraw: 75 kr, saldo 125 kr")
    spy.assert_any_call("deposit: 75 kr, saldo 125 kr")


@pytest.mark.integration
def test_transfer_does_not_happen_when_balance_is_too_low(mocker):
    logger = Logger()
    spy = mocker.spy(logger, "log")

    from_account = BankAccount(balance=20, logger=logger)
    to_account = BankAccount(balance=100, logger=logger)
    transaction = Transaction()

    result = transaction.transfer(50, from_account, to_account)

    assert result is False
    assert from_account.balance == 20
    assert to_account.balance == 100

    spy.assert_called_once_with("withdraw: kunde inte ta ut 50 kr från kontot")