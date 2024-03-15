# exchange_utils.py
"""
多交易所批量提币程序
author: shuai
twitter: @ShuaiL0
"""
import json
import ccxt
import os

# 获取当前代码文件所在的路径
current_file_path = os.path.abspath(__file__)

# 获取当前代码文件所在的目录路径
current_directory = os.path.dirname(current_file_path)


def load_api_keys(exchange_name: str) -> dict:
    """
    加载指定交易所的 API 密钥。
    :param exchange_name: 交易所名称，如 'okx'、'binance' 等
    :return: 包含 API 密钥的字典
    """
    file_path = os.path.join(current_directory, 'api_keys.json')

    with open(file_path, 'r') as f:
        api_keys = json.load(f)

    if exchange_name.lower() not in api_keys:
        raise ValueError(f"API keys for {exchange_name} not found in {file_path}")

    return api_keys[exchange_name.lower()]


def init_exchange(exchange_name: str, api_key: str, api_secret: str, password: str = None,
                  enable_rate_limit: bool = True) -> ccxt.Exchange:
    """
    初始化指定交易所的实例。

    :param exchange_name: 交易所名称，如 'okx'、'binance' 等
    :param api_key: 交易所的 API 密钥
    :param api_secret: 交易所的 API 密钥对
    :param password: 交易所的 API 密码（如果需要的话）
    :param enable_rate_limit: 是否启用速率限制
    :return: 初始化的交易所实例
    """
    exchange_class = getattr(ccxt, exchange_name.lower(), None)
    if not exchange_class:
        raise ValueError(f"Unsupported exchange: {exchange_name}")

    exchange_params = {
        'apiKey': api_key,
        'secret': api_secret,
        'enableRateLimit': enable_rate_limit,
        'timeout': 3000,
        'rateLimit': 10,
        'enableRateLimit': False,
        # 'httpsProxy': 'http://127.0.0.1:7890'
    }

    if password:
        exchange_params['password'] = password

    return exchange_class(exchange_params)
