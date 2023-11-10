from brownie import fundMe
from scripts.helpful import get_account
import time


def fund():
    _fundMe = fundMe[-2]  # gets address from fundMe collection to interact with
    account = get_account()  # making a state change
    entrance_fee = _fundMe.getEntranceFee()
    print(f"The current entry fee is {entrance_fee}")
    tx = _fundMe.fundme({"from": account, "value": entrance_fee})
    tx.wait(1)
    time.sleep(3)


def withdraw():
    _fundMe = fundMe[-2]
    account = get_account()
    tx = _fundMe.withdraw({"from": account})
    tx.wait(1)
    time.sleep(3)
    print(f"tx_hash: {tx}")


def main():
    fund()
    withdraw()


# 0.025000000000000000
