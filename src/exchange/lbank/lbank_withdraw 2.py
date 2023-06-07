# binance_withdraw.py
"""
多交易所批量提币程序
author: shuai
twitter: @ShuaiL0
"""
import ccxt
import json
import pandas as pd
import time
import random


# 设置最大行和列的显示限制为无穷大
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('expand_frame_repr', False)


def lbank_withdraw(exchange, wallet_address, tag=None, currency=None, amount=None, chain=None):
    """
   在 Lbank 交易所上执行提币操作。
   :param exchange: ccxt.Exchange 对象，已初始化的 OKX 交易所实例
   :param wallet_address: str, 提币目标钱包地址
   :param currency: str, optional, 提币的货币，如 'ETH'。默认为 None，需在调用时设置
   :param amount: float, optional, 提币的数量。默认为 None，需在调用时设置
   :param chain: str, optional, 提币所使用的链，如 'ETH-Arbitrum one'。默认为 None，需在调用时设置
   :param tag: str, optional, 提币地址标签（对于部分链可能需要）。默认为 None
   :return: None
   """

    # 检查资金账户余额
    balance = pd.DataFrame(exchange.sapiV3PostAssetGetUserAsset())  # 获取资金账户余额
    balance.set_index('asset', inplace=True, drop=True)
    balance = balance.to_dict('index')
    # 获取可用余额
    free_balance = float(balance[currency]['free'])
    print(f"可用 {currency} 余额：{free_balance}")

    if free_balance >= (amount):
        # 提现
        print(f"正在将 {amount} {currency} 提现到钱包地址 {wallet_address} 提币链 {chain}")
        timestamp = int(time.time()) * 1000
        params = {'coin': currency, 'network': chain, 'address': wallet_address, 'amount': amount,
                  'timestamp': timestamp}
        if tag is not None:
            params['addressTag'] = tag
        withdrawal = exchange.sapiPostCapitalWithdrawApply(params)
        print("提现结果：", withdrawal)
        exit()

        # 检查提现状态
        time.sleep(5)  # 等待 5 秒以获取更新状态
        status = exchange.sapiGetCapitalWithdrawHistory(
            params={'withdrawOrderId': withdrawal['id'], 'timestamp': int(time.time()) * 1000})
        print("提现状态：", status)

    else:
        print("余额不足，无法提现")


params = {
    "apiKey": "1a0c0d8c-aa79-4d87-ab38-6f54e32bb131",
    "secret": "MIICdgIBADANBgkqhkiG9w0BAQEFAASCAmAwggJcAgEAAoGBAKRAaHvmfoGJdbQ3Q+NObIAYuv+j1ITlowOYkOm6n9HBJBOPtNWJnEQ18cr/sQ68T2JYrLZeRTOtNke/3bwrGxyv3r7t8SHG6VzUvq45WLzmD9jnGUddhYvqLRCSdPmj2PbSDNrCqIk7mqmUomCMxCGbC1ZWuJnvM+nQ2ONtWETvAgMBAAECgYBjs2j41Hez36Gf6+/8eS0pMFnKNUMaDF5AH4rPJWY/p3JjoVaOTAKb8Pa9Vym9nRa+xr7H0D9HV/vb354Ty0Kf0n03B8cISWquq2QOkWa0sMnWCcQ97rl8Jvc2kVh7BbQYTsrgcrRlvfkqwtjwz3m0urQ06MkRUwfgYb/tQEHsMQJBAO3agIcUe4gEvDnsKEZFEMswZjLqWIy+nHu1au2gwxz11ylpAUWUeTrcavxOuYaOk89nB6bNky0KW30bYo7Z2qkCQQCwyGSLIWcryyMImk4o12mENTE1ZqhRWbEJ/eHwOvL5nsZld8eQDo65Hp0kMSlrMAMHqD+LjX77F/JOqtQOYjnXAkB+7XRbIV4OpuA/VLvlS+P7WlefYhlg+jMNfTGTn4+fe72XNpbcJ7BN7eQVwnkUyi8spcGajOe2SGmsKJn+u1kJAkEAgWvDx+PFb1dBJ6wn6liBxCtZAjpMoXnjVWhLv564gSzPHDvLmtg9fqM98eAX7YPxw+pV0yncu6C1YQhJRNp+cwJAeLYj8Kn8eIvIM2jMsytPpJVY8MFAIUgafig55hhZXoREFiTSQ7zx0+K5y8Y619fDWPjIlsBdl/ROE6YEi/frDg==",
    'verbose': True,  # 启用调试功能

}
exchange = ccxt.lbank2(params)


exchange.privateKey()
print(exchange.signHash())
exit()

def update_custom_header(exchange):
    random_number = random.randint(1, 100)
    exchange.headers['Custom-Header'] = f'Custom header value {random_number}'


def fetch_balance_with_updated_header(exchange):

    balance = exchange.load_markets()
    print("Balance 1:", exchange.headers)
    exit()
    return balance


# 请求1

update_custom_header(exchange)
balance1 = fetch_balance_with_updated_header(exchange)


# 请求2
update_custom_header(exchange)
balance2 = fetch_balance_with_updated_header(exchange)
print("Balance 2:", exchange.headers)
exit()



balance = exchange.publicGetTimestamp()
print(balance)
exit()
market = pd.DataFrame(exchange.load_markets()).T
print(market['symbol'])
exit()

r = exchange.withdraw('GETH', 5, '0x32Ec95fF39425Bd7F2C98D078A0b4AfB03641521', params={'fee': 4})
print(r)
