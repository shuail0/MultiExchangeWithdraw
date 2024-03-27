# gate_withdraw.py
"""
多交易所批量提币程序
author: shuai
twitter: @ShuaiL0
"""

def gate_withdraw(exchange, wallet_address, tag=None, currency=None, amount=None, chain=None):
    """
   在 bitget 交易所上执行提币操作。
   :param exchange: ccxt.Exchange 对象，已初始化的 OKX 交易所实例
   :param wallet_address: str, 提币目标钱包地址
   :param currency: str, optional, 提币的货币，如 'ETH'。默认为 None，需在调用时设置
   :param amount: float, optional, 提币的数量。默认为 None，需在调用时设置
   :param chain: str, optional, 提币所使用的链，如 'ETH-Arbitrum one'。默认为 None，需在调用时设置
   :param tag: str, optional, 提币地址标签（对于部分链可能需要）。默认为 None
   :return: None
   """
    # 获取链信息
    # params = {'currency': currency}
    # currencies = exchange.public_wallet_get_currency_chains(params)
    # print(currencies)
    # exit()
    # 检查资金账户余额
    free_balances = exchange.fetch_free_balance()
    if currency in free_balances:
        free_balance = float(free_balances[currency])
    else:
        free_balance = 0
    print(f"可用 {currency} 余额：{free_balance}")

    if free_balance >= amount:
        # 提现
        print(f"正在将 {amount} {currency} 提现到钱包地址 {wallet_address} 提币链 {chain}")
        params = {'currency': currency, 'chain': chain, 'address': wallet_address, 'amount': amount}
        if tag is not None:
            params['memo'] = tag
        withdrawal = exchange.privateWithdrawalsPostWithdrawals(params)
        print("提现结果：", withdrawal)
    else:
        print("余额不足，无法提现")

