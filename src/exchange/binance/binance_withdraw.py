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


def binance_withdraw(exchange, wallet_address, tag=None, currency=None, amount=None, chain=None):
    """
   在 币安 交易所上执行提币操作。
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
        # 检查提现状态
        time.sleep(5)  # 等待 5 秒以获取更新状态
        status = exchange.sapiGetCapitalWithdrawHistory(
            params={'withdrawOrderId': withdrawal['id'], 'timestamp': int(time.time()) * 1000})
        print("提现状态：", status)

    else:
        print("余额不足，无法提现")
