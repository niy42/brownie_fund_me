from scripts.helpful import get_account, LBEnv
from scripts.deploy import deploy_fundMe
from brownie import network, accounts, exceptions
import pytest
import time


def test_can_fund_and_withdraw():
    account = get_account()
    _fundMe = deploy_fundMe()
    entrance_fee = _fundMe.getEntranceFee() + 100
    tx = _fundMe.fundme({"from": account, "value": entrance_fee})
    tx.wait(1)
    time.sleep(1)
    assert _fundMe.addresstoamountFunded(account.address) == entrance_fee
    tx2 = _fundMe.withdraw({"from": account})
    tx2.wait(1)
    time.sleep(1)
    assert _fundMe.addresstoamountFunded(account.address) == 0


def test_only_owner_can_withdraw():
    if network.show_active() not in LBEnv:
        pytest.skip("Only for Local Testing...")
    _fundMe = deploy_fundMe()
    bad_actor = accounts.add()
    with pytest.raises(exceptions.VirtualMachineError):
        _fundMe.withdraw({"from": bad_actor})
