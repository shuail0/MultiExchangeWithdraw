# 更新

2023/6/20： 新增BitGet交易所


# 序

这是一个交易所批量向钱包提币的程序， 目前支持okx和binance这两个交易所，后续可能会在增加新的交易所。


# 注意事项

1. **提币需要申请API，并开通提币权限。提币权限比较敏感！提币结束后记得及时删除相关API。**

2. **子账户没有提币权限，需要用主账户执行。**

3. **binance开通提币权限需要绑定IP，如果你用的是梯子，绑定的是梯子的IP。**

4. **okx的提币费用需要另外支付，提币时需要注意留有足够的手续费。**

5. **binance提币费用从提币金额中扣除，要自己注意计算提币的数量。**

6. **okx只能向地址簿中的白名单提币，提币前需要在提币页面点击地址簿添加地址（一次可以添加20个）。**


# 运行前的配置

## API配置

1. 所有的API 配置都在src目录下的`api_keys.json`文件中，打开文件将对应参数改成自己的即可。
2. okx在创建API时会要求你设置一个密码，这个密码就是填入`password`字段的密码。
## 提币地址配置

1. 提币地址在data目录下的`deposit_address.csv` 文件中配置（你也可以选择自行配置）。
2. **`deposit_address.csv` 文件中有我的示例地址，记得删掉。**
3. 提币地址的字段解释：
   - **wallet_address**: 提币的钱包地址。
   - **tag**: 提某些币种（如Atom、EOS）需要的memo或tag参数，如果没有则留空。
   - **currency**：提币的币种，如ETH。
   - **amount**：提币数量。
   - **chain**：提币的链，可以在交易所提币页面看到（如okx提ETH到以太坊链时为chain为：ETH-ERC20，binance则为: ETH)。
   - **exchange_name**：交易所名字，需要和ccxt调用的交易所名字相同。

## 程序运行配置

- 运行主程序是`src`目录下的multi_exchange_withdraw.py 文件。
- 代码中的 `address_file_path = '../data/deposit_address.csv'` 是配置提币文件的路径地址，有需要可以改成自己的文件路径。
- 配置完成后直接运行`multi_exchange_withdraw.py`文件即可。
- `sleep_time`是设置两次提币的间隔，如果是binance提币，建议这个值30以上（binance提币消耗600权重，binance每个账户每分钟最多1200权重）。


# 交易所设置

## 币安
无需设置，直接提币
## OKX地址配置（将地址添加至地址簿）
操作步骤：
1. 打开资金帐户点击提币：
![image-20230422225003791](https://s2.loli.net/2023/06/20/bU5u3KwkEIgRYpH.png)

2. 选择相应的币种：
![image-20230422225031380](https://s2.loli.net/2023/06/20/8MwEZ5QVRIgieSA.png)

3. 点击地址旁边的这个按钮进入地址簿：
![image-20230422225121515](https://s2.loli.net/2023/06/20/pMxCLl1czIyKfoW.png)
4. 点击新增提现地址：
![image-20230422225203275](https://s2.loli.net/2023/06/20/ZWGTukvLXHhJUl1.png)
5. 输入地址添加，可以把“保存为通用地址钩上，这样下次提同网络的其它币种就不需要再次添加地址了。
![image-20230422225334525](https://s2.loli.net/2023/06/20/g9lNHbtFQ32IXeB.png)
6. OKX若是地址较多，可以点击继续添加地址填入更多地址，OKX一次最多可添加20个地址。

## BitGet
### 将地址添加至地址簿
1. 打开提币地址管理页面：https://www.bitget.site/zh-CN/asset/address
2. 选择添加提币地址（单个添加1个地址）或 批量添加（一次添加多个地址，最多50个）。
3.  ETH、BSC、MATIC、ARBITRUMONE、OPTIMISM等EVM兼容链推荐直接添加EVM地址，后续提这些链的币是不需要再添加。
###  提币链chain参数获取
BitGet提币链的配置与网站提币页面展示的数据有些不同，这个参数最好是从特定的网站获取，否则可能回导致提币失败。具体的获取步骤如下：
1. 浏览器打开这个网站，获取提币信息：https://api.bitget.com/api/spot/v1/public/currencies
2. 根据自己的币种和网络，查找对应的Chain参数，下图是BTC 提币至BSC链的信息：
![image-20230620145757857](https://s2.loli.net/2023/06/20/WVjuknNvS31QRyC.png)
3. 将这个参数填入至地址表格中：
![image-20230620150017465](https://s2.loli.net/2023/06/20/PZ61zK5MUnD4jda.png)
