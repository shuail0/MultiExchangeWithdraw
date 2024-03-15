# okx_withdraw.py
"""
多交易所批量提币程序
author: shuai
twitter: @ShuaiL0
"""
import ccxt
import json
import pandas as pd
import time


def okx_withdraw(exchange, wallet_address, tag=None, currency=None, amount=None, chain=None):
    """
   在 OKX 交易所上执行提币操作。
   :param exchange: ccxt.Exchange 对象，已初始化的 OKX 交易所实例
   :param wallet_address: str, 提币目标钱包地址
   :param currency: str, optional, 提币的货币，如 'ETH'。默认为 None，需在调用时设置
   :param amount: float, optional, 提币的数量。默认为 None，需在调用时设置
   :param chain: str, optional, 提币所使用的链，如 'ETH-Arbitrum one'。默认为 None，需在调用时设置
   :param tag: str, optional, 提币地址标签（对于部分链可能需要）。默认为 None
   :return: None
   """
    # 获取所有币种列表
    currencies = exchange.fetchCurrencies()
    # 获取提币费用数据
    withdrawal_fee = None
    for key, value in currencies[currency]['networks'].items():
        if 'id' in value and value['info']['chain'] == chain:
            withdrawal_fee = value['fee']
            break
    if not withdrawal_fee:
        print('无法获取', chain, '网络的提币费用信息，程序退出')
        exit()

    # 检查资金账户余额
    balance = pd.DataFrame(exchange.privateGetAssetBalances()['data'])  # 获取资金账户余额
    balance.set_index('ccy', inplace=True, drop=True)
    balance = balance.to_dict('index')
    # 获取可用余额
    free_balance = float(balance[currency]['availBal'])
    print(f"可用 {currency} 余额：{free_balance}")

    if free_balance >= (amount + withdrawal_fee):
        # 提现
        print(f"正在将 {amount} {currency} 提现到钱包地址 {wallet_address} 提币链 {chain}")
        params = {'ccy': currency, 'amt': amount, 'dest': 4, 'toAddr': wallet_address, 'fee': withdrawal_fee,
                  'chain': chain}
        if tag is not None:
            params['toAddr'] = f'{wallet_address}:{tag}'
        withdrawal = exchange.privatePostAssetWithdrawal(params)
        print("提现结果：", withdrawal['data'])
        # 检查提现状态
        time.sleep(5)  # 等待 5 秒以获取更新状态
        status = exchange.privateGetAssetDepositWithdrawStatus(params={'wdId': withdrawal['data'][0]['wdId']})
        print("提现状态：", status)
    else:
        print("余额不足，无法提现")
