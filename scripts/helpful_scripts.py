from brownie import (
    network,
    accounts,
    config,
    Contract,
    interface,
)

FORKED_LOCAL_ENRIVONMENTS = ["mainnet-fork", "mainnet-fork-dev"]
LOCAL_BLOCKCHAIN_ENVIRONMENTS = [
    "development",
    "ganache-local",
]  # this is a list of local networks so that we know when to deploy mocks


def get_account(index=None, id=None):
    # index will choose one of the addresses inside accounts array
    # id will use one of the accounts saved inside brownie -> $ brownie accounts list
    if index:
        return accounts[index]
    if id:
        return accounts.load(id)
    if (
        network.show_active() in LOCAL_BLOCKCHAIN_ENVIRONMENTS
        or network.show_active() in FORKED_LOCAL_ENRIVONMENTS
    ):
        return accounts[0]

    return accounts.add(config["wallets"]["from_key"])

