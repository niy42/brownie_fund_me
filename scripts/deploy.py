from brownie import MockV3Aggregator, fundMe, network, config
from scripts.helpful import get_account, LBEnv, deploy_mocks
from brownie.network.gas.strategies import ExponentialScalingStrategy

gas_strategy = ExponentialScalingStrategy("10 gwei", "50 gwei")


def deploy_fundMe():
    account = get_account()
    if network.show_active() not in LBEnv:
        pricefeed = config["networks"][network.show_active()]["eth_usd_price"]
    else:
        deploy_mocks()
        pricefeed = MockV3Aggregator[-1].address
    _fundMe = fundMe.deploy(
        pricefeed,
        {"from": account, "gas_price": gas_strategy},
        publish_source=config["networks"][network.show_active()].get("verify"),
    )
    print(f"contract deployed at {_fundMe.address}")
    print(f"Current Mock price is {_fundMe.getPrice()}")
    return _fundMe


def main():
    deploy_fundMe()
