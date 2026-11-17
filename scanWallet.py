from mnemonic import Mnemonic
from eth_account import Account
from web3 import Web3
import time

Account.enable_unaudited_hdwallet_features()

ERC20_ABI = [
    {
        "constant": True,
        "inputs": [{"name": "_owner", "type": "address"}],
        "name": "balanceOf",
        "outputs": [{"name": "balance", "type": "uint256"}],
        "type": "function"
    }
]

# 链基础配置
CHAIN_RPC = [
    {
        "name": "Ethereum主网",
        "rpc": "https://ethereum-rpc.publicnode.com",
        "native_symbol": "ETH",
        "native_decimals": 18,
        "tokens": [
            {"symbol":"USDT","contract":"0xdAC17F958D2ee523a2206206994597C13D831ec7","decimals":6},
            {"symbol":"USDC","contract":"0xA0b86991c6218b36c1d19D4a2e9Eb0cE3606eB48","decimals":6},
            {"symbol":"DAI","contract":"0x6B175474E89094C44Da98b954EedeAC495271d0F","decimals":18},
            {"symbol":"WBTC","contract":"0x2260FAC5E5542a773Aa44fBCfeDf7C193bc2C599","decimals":8},
            {"symbol":"UNI","contract":"0x1f9840a85d5aF5bf1D1762F925BDADdC4201F984","decimals":18},
            {"symbol":"LINK","contract":"0x514910771AF9Ca656af840dff83E8264EcF986CA","decimals":18},
            {"symbol":"AAVE","contract":"0x7Fc66500c84A76Ad7e9c93437bFc5Ac33E2DDaE9","decimals":18},
            {"symbol":"SHIB","contract":"0x95aD61b0a150d79219dCF64E1E6Cc01f0B64C4cE","decimals":18},
            {"symbol":"WETH","contract":"0xC02aaA39b223FE8D0A0e5C4F27eAD9083C756Cc2","decimals":18},
            {"symbol":"COMP","contract":"0xc00e94cb662c3520282e6f5717214004a7f26888","decimals":18},
            {"symbol":"ARB","contract": "0xb50721bcf8d664c30412cfbc6cf7a15145234ad1","decimals": 18},
            {"symbol":"CRV","contract":"0xD533a949740bb3306d119CC777fa900bA034cd52","decimals":18},
        ]
    },
    {
        "name": "BSC币安智能链",
        "rpc": "https://bsc-rpc.publicnode.com",
        "native_symbol": "BNB",
        "native_decimals": 18,
        "tokens": [
            {"symbol":"USDT","contract":"0x55d398326f99059fF775485246999027B3197955","decimals":18},
            {"symbol":"USDC","contract":"0x8AC76a51cc950d9822D68b83fE1Ad97B32Cd580d","decimals":18},
            {"symbol":"DAI","contract":"0x1AF3F329e8BE154074D8769D1FFa4eE058B1DBc3","decimals":18},
            {"symbol":"WBTC","contract":"0x0555e30da8f98308edb960aa94c0db47230d2b9c","decimals":8},
            {"symbol":"LINK","contract":"0xf8a0bf9cf54bb92f17374d9e9a321e6a111a51bd","decimals":18},
            {"symbol":"COMP","contract":"0x52ce071bd9b1c4b00a0b92d298c512478cad67e8","decimals":18},
            {"symbol":"WETH","contract":"0x4db5a66e937a9f4473fa95b1caf1d1e1d62e29ea","decimals":18},
        ]
    },
    {
        "name": "Polygon",
        "rpc": "https://public.blazingnode.com",
        "native_symbol": "MATIC",
        "native_decimals": 18,
        "tokens": [
            {"symbol":"USDT","contract":"0xc2132D05D31c914a87C6611C10748AEb04B58e8F","decimals":6},
            {"symbol":"USDC","contract":"0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359","decimals":6},
            {"symbol":"DAI","contract":"0x8f3cf7ad23cd3cadbd9735aff958023239c6a063","decimals":18},
            {"symbol":"WBTC","contract":"0x1bfd67037b42cf73acf2047067bd4f2c47d9bfd6","decimals":8},
            {"symbol":"LINK","contract":"0x53E0bca35eC356BD5ddDFebbD1Fc0fD03FaBad39","decimals":18},
            {"symbol":"COMP","contract":"0x8505b9d2254a7ae468c0e9dd10ccea3a837aef5c","decimals":18},
            {"symbol":"WETH","contract":"0x7ceb23fd6bc0add59e62ac25578270cff1b9f619","decimals":18},
        ]
    },
    {
        "name": "Arbitrum One",
        "rpc": "https://arb1.arbitrum.io/rpc",
        "native_symbol": "ETH",
        "native_decimals": 18,
        "tokens": [
            {"symbol":"USDT","contract":"0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9","decimals":6},
            {"symbol":"USDC","contract":"0xaf88d065e77c8cC2239327C5EDb3A432268e5831","decimals":6},
            {"symbol":"DAI","contract":"0xDA10009cBd5D07dd0CeCc66161FC93D7c9000da1","decimals":18},
            {"symbol":"WBTC","contract":"0x2f2a2543b76a4166549f7aab2e75bef0aefc5b0f","decimals":8},
            {"symbol":"UNI","contract":"0xfa7f8980b0f1e64a2062791cc3b0871572f1f7f0","decimals":18},
            {"symbol":"LNNK","contract":"0xf97f4df75117a78c1a5a0dbb814af92458539fb4","decimals":18},
            {"symbol":"ARB","contract":"0x912ce59144191c1204e64559fe8253a0e49e6548","decimals":18},
            {"symbol":"COMP","contract":"0x354a6da3fcde098f8389cad84b0182725c6c91de","decimals":18},
            {"symbol":"WETH","contract":"0x82af49447d8a07e3bd95bd0d56f35241523fbab1","decimals":18},
        ]
    },
    {
        "name": "Base",
        "rpc": "https://mainnet.base.org",
        "native_symbol": "ETH",
        "native_decimals": 18,
        "tokens": [
            {"symbol":"USDT","contract":"0xfde4C96c8593536E31F229EA8f37b2ADa2699bb2","decimals":6},
            {"symbol":"USDC","contract":"0x833589fCD6eDb6E08f4c7C32D4f71b54bdA02913","decimals":6},
            {"symbol":"DAI","contract":"0x50c5725949a6f0c72e6c4a641f24049a917db0cb","decimals":18},
            {"symbol":"LINK","contract": "0x88fb150bdc53a65fe94dea0c9ba0a6daf8c6e196","decimals": 18},
            {"symbol":"COMP","contract":"0x9e1028f5f1d5ede59748ffcee5532509976840e0","decimals":18},
            {"symbol":"WETH","contract":"0x4200000000000000000000000000000000000006","decimals":18},
            {"symbol":"WBTC","contract": "0x0555e30da8f98308edb960aa94c0db47230d2b9c","decimals": 18},
        ]
    },
    {
        "name": "Avalanche",
        "rpc": "https://avalanche-rpc.blockreq.com/v1/rpc/public",
        "native_symbol": "ETH",
        "native_decimals": 18,
        "tokens": [
            {"symbol":"USDT","contract":"0x9702230a8ea53601f5cd2dc00fdbc13d4df4a8c7","decimals":6},
            {"symbol":"USDC","contract":"0xb97ef9ef8734c71904d8002f8b6bc66dd9c48a6e","decimals":6},
            {"symbol":"DAI","contract":"0xd586e7f844cea2f87f50152665bcbc2c279d8d70","decimals":18},
            {"symbol":"WBTC","contract":"0x50b7545627a5162f82a992c33b87adc75187b218","decimals":8},
            {"symbol":"UNI","contract":"0x8ebaf22b6f053dffeaf46f4dd9efa95d89ba8580","decimals":18},
            {"symbol":"LNNK","contract":"0x5947bb275c521040051d82396192181b413227a3","decimals":18},
            {"symbol":"COMP","contract":"0xc3048e19e76cb9a3aa9d77d8c03c29fc906e2437","decimals":18},
        ]
    },
    {
        "name": "OP",
        "rpc": "https://rpc-optimism.blockmachine.io",
        "native_symbol": "ETH",
        "native_decimals": 18,
        "tokens": [
            {"symbol":"USDT","contract":"0x94b008aa00579c1307b0ef2c499ad98a8ce58e58","decimals":6},
            {"symbol":"USDC","contract":"0x0b2c639c533813f4aa9d7837caf62653d097ff85","decimals":6},
            {"symbol":"DAI","contract":"0xda10009cbd5d07dd0cecc66161fc93d7c9000da1","decimals":18},
            {"symbol":"WBTC","contract":"0x68f180fcce6836688e9084f035309e29bf0a2095","decimals":8},
            {"symbol":"UNI","contract":"0x6fd9d7ad17242c41f7131d257212c54a0e816691","decimals":18},
            {"symbol":"LNNK","contract":"0x350a791bfc2c21f9ed5d10980dad2e2638ffa7f6","decimals":18},
            {"symbol":"COMP","contract":"0x7e7d4467112689329f7e06571ed0e8cbad4910ee","decimals":18},
            {"symbol":"WETH","contract":"0x82af49447d8a07e3bd95bd0d56f35241523fbab1","decimals":18},
        ]
    },

]

mnemo = Mnemonic("english")
LOG_FILE = "balance_hit.log"
RPC_MIN_INTERVAL = 0.3
last_rpc_ts = {}

def create_one_wallet():
    phrase = mnemo.generate(strength=128)
    acc = Account.from_mnemonic(phrase, account_path="m/44'/60'/0'/0/0")
    return phrase, acc.address

def rpc_cooling(rpc_url):
    now = time.time()
    prev = last_rpc_ts.get(rpc_url, 0)
    diff = now - prev
    if diff < RPC_MIN_INTERVAL:
        sleep_t = RPC_MIN_INTERVAL - diff
        time.sleep(sleep_t)
    last_rpc_ts[rpc_url] = time.time()

def build_token_group():
    token_group = {}
    for chain in CHAIN_RPC:
        c_name = chain["name"]
        rpc = chain["rpc"]
        for tk in chain["tokens"]:
            sym = tk["symbol"]
            item = {
                "chain_name": c_name,
                "rpc": rpc,
                "contract": tk["contract"],
                "decimals": tk["decimals"]
            }
            if sym not in token_group:
                token_group[sym] = []
            token_group[sym].append(item)
    return token_group

def query_multi_chain_balance(address):
    token_group = build_token_group()
    res = {}
    # 初始化结果结构
    for ch in CHAIN_RPC:
        res[ch["name"]] = {
            "native": None,
            "tokens": {},
            "error": None,
            "w3": None
        }

    # ========== 第一步：查询各链原生币，实时打印进展 ==========
    for chain in CHAIN_RPC:
        c_name = chain["name"]
        rpc = chain["rpc"]
        print(f"\n>>> 正在查询【{c_name}】原生币 {chain['native_symbol']}")
        try:
            rpc_cooling(rpc)
            w3 = Web3(Web3.HTTPProvider(rpc, request_kwargs={"timeout":12}))
            res[c_name]["w3"] = w3
            wei = w3.eth.get_balance(address)
            bal = round(wei / (10 ** chain["native_decimals"]),6)
            res[c_name]["native"] = bal
            print(f"✅ 【{c_name}】原生币结果：{bal}")
        except Exception as e:
            err_msg = str(e)[:80]
            res[c_name]["error"] = err_msg
            print(f"❌ 【{c_name}】原生币查询失败: {err_msg}")

    # ========== 第二步：按币种分组循环查询代币，每一个代币实时打印 ==========
    for symbol, chain_list in token_group.items():
        for tk_info in chain_list:
            c_name = tk_info["chain_name"]
            rpc = tk_info["rpc"]
            contract_addr = tk_info["contract"]
            decimals = tk_info["decimals"]
            chain_data = res[c_name]
            if chain_data["error"] is not None:
                print(f"⏭ 跳过 {symbol} @ {c_name}，该链之前查询异常")
                continue
            w3 = chain_data["w3"]
            print(f">>> 正在查询代币 {symbol} @【{c_name}】")
            try:
                rpc_cooling(rpc)
                c_addr = Web3.to_checksum_address(contract_addr)
                c = w3.eth.contract(address=c_addr, abi=ERC20_ABI)
                raw = c.functions.balanceOf(address).call()
                bal = round(raw / (10**decimals),6)
                res[c_name]["tokens"][symbol] = bal
                print(f"✅ {symbol} @ {c_name} = {bal}")
            except Exception as e:
                err = repr(e)
                print(f"❌ TOKEN_QUERY_ERR {symbol} @ {c_name} : {err[:120]}")
                continue
    return res

def has_any_balance(bal_data):
    for chain_data in bal_data.values():
        if chain_data.get("error"):
            continue
        if chain_data["native"] > 0:
            return True
        for token_bal in chain_data["tokens"].values():
            if token_bal > 0:
                return True
    return False

def write_log(idx, mnemonic, address, bal_data):
    lines = []
    lines.append(f"===== HIT NO.{idx} =====\n")
    lines.append(f"助记词: {mnemonic}\n")
    lines.append(f"地址: {address}\n")
    for c_name, info in bal_data.items():
        lines.append(f"【{c_name}】\n")
        if info.get("error"):
            lines.append(f"  查询异常: {info['error']}\n")
        else:
            lines.append(f"  原生: {info['native']}\n")
            for sym, b in info["tokens"].items():
                lines.append(f"  {sym}: {b}\n")
    lines.append("-"*80+"\n")
    with open(LOG_FILE, "a", encoding="utf-8") as f:
        f.writelines(lines)

if __name__ == "__main__":
    generate_count = 10000
    print(f"开始生成 {generate_count} 个钱包；按币种分组查询，内置RPC冷却防封禁")
    print(f"检测到余额会写入文件：{LOG_FILE}\n")

    for idx in range(generate_count):
        print(f"\n======== 开始扫描第 {idx+1} 号钱包 ========")
        mnemonic_phrase, addr = create_one_wallet()
        print(f"助记词：{mnemonic_phrase}")
        print(f"地址：{addr}")
        bal_data = query_multi_chain_balance(addr)

        # 检测余额并写入日志
        if has_any_balance(bal_data):
            print(f"🎉 !!!发现有余额的钱包，写入log文件!!!")
            write_log(idx+1, mnemonic_phrase, addr, bal_data)
        print("-"*70)
