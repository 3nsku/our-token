from brownie import network, OurToken
from scripts.helpful_scripts import get_account

TOKEN_SUPPLY = 300 * 10 ** 18


def deploy_token():
    account = get_account()
    our_token = OurToken.deploy(TOKEN_SUPPLY, {"from": account})
    print(f"Token Contract Address {our_token.address}")
    print(f"Initial Supply of Token {our_token.balanceOf(our_token.address)}")
    print(f"balance of contract creator {our_token.balanceOf(account.address)}")


def main():
    deploy_token()
