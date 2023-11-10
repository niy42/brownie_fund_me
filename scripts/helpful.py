from brownie import accounts, network, MockV3Aggregator, config

FORKED_LEnv = ["mainnet-fork", "mainnet-fork-dev"]
LBEnv = ["development", "ganache-local"]
DECIMALS = 8
STARTING_PRICE = 200000000000


def get_account():
    if network.show_active() in LBEnv or network.show_active() in FORKED_LEnv:
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def deploy_mocks():
    print(f"The active network is {network.show_active()}")
    print("Deploying mocks....")
    if len(MockV3Aggregator) <= 0:
        MockV3Aggregator.deploy(DECIMALS, STARTING_PRICE, {"from": get_account()})
    print("Mocks Deployed!")
    print(f"Mock recently at {MockV3Aggregator[-1].address}")
