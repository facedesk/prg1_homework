
#we all know bitcoin 
# "Bitcoin Bitcoin":6535.71,
coins = {"Ethereum Ethereum":206.14,"XRP XRP":0.46,"Bitcoin Cash Bitcoin Cash":446.20,"EOS EOS":5.40,"Stellar Stellar":0.24,"Litecoin Litecoin":53.01,"Tether Tether":0.97,"Cardano Cardano":0.08,"Monero Monero":105.28,"TRON TRON":0.02,"IOTA IOTA":0.51,"Dash Dash":158.90,"Binance Coin Binance Coin":9.89,"NEO NEO":17.27,"Ethereum Classic Ethereum Classic":9.71,"NEM NEM":0.10,"Tezos Tezos":1.37,"VeChain VeChain":0.01,"Zcash Zcash":121.65,"Dogecoin Dogecoin":0.00,"0x 0x":0.87,"Maker Maker":647.30,"OmiseGO OmiseGO":3.29,"Bitcoin Gold Bitcoin Gold":26.19,"Ontology Ontology":1.87,"Qtum Qtum":3.97,"Decred Decred":39.10,"Lisk Lisk":2.92,"Aeternity Aeternity":1.27,"ICON ICON":0.71,"Nano Nano":2.05,"BitShares BitShares":0.10,"Zilliqa Zilliqa":0.03,"Bitcoin Diamond Bitcoin Diamond":1.72,"DigiByte DigiByte":0.02,"Bytecoin Bytecoin":0.00,"Siacoin Siacoin":0.01,"Steem Steem":0.83,"Verge Verge":0.01,"Basic Attention Token Basic Attenti...":0.21,"Waves Waves":2.00,"Pundi X Pundi X":0.00,"Bytom Bytom":0.18,"Metaverse ETP Metaverse ETP":3.08,"TrueUSD TrueUSD":1.01,"Electroneum Electroneum":0.02,"Golem Golem":0.16,"Holo Holo":0.00,"Komodo Komodo":1.31,"Stratis Stratis":1.43,"Augur Augur":12.60,"Chainlink Chainlink":0.38,"Status Status":0.04,"Populous Populous":3.37,"Waltonchain Waltonchain":2.95,"Cryptonex Cryptonex":2.10,"Ardor Ardor":0.12,"Wanchain Wanchain":1.02,"Aion Aion":0.44,"IOST IOST":0.01,"Mithril Mithril":0.26,"KuCoin Shares KuCoin Shares":1.07,"Aurora Aurora":0.03,"CyberMiles CyberMiles":0.12,"ReddCoin ReddCoin":0.00,"ETERNAL TOKEN ETERNAL TOKEN":1.47,"Loopring Loopring":0.11,"Digitex Futures Digitex Futures":0.12,"MaidSafeCoin MaidSafeCoin":0.19,"GXChain GXChain":1.40,"DigixDAO DigixDAO":42.09,"Ark Ark":0.78,"HyperCash HyperCash":1.88,"aelf aelf":0.33,"Huobi Token Huobi Token":1.59,"FunFair FunFair":0.01,"Dentacoin Dentacoin":0.00,"PIVX PIVX":1.35,"QASH QASH":0.22,"Dropil Dropil":0.00,"MonaCoin MonaCoin":1.18,"Nebulas Nebulas":1.63,"Elastos Elastos":9.62,"Loom Network Loom Network":0.12,"Decentraland Decentraland":0.07,"MOAC MOAC":1.19,"Bancor Bancor":1.28,"Crypto.com Crypto.com":4.53,"Polymath Polymath":0.24,"Power Ledger Power Ledger":0.18,"Horizen Horizen":13.72,"Ravencoin Ravencoin":0.03,"Odyssey Odyssey":0.01,"RChain RChain":0.16,"Theta Token Theta Token":0.09,"WAX WAX":0.07,"TenX TenX":0.57,"Dai Dai":0.98,"Nxt Nxt":0.06}
'''
for altcoin in coins:
    #which alt coins hold a value greater than 50?
   
    if(coins[altcoin] > 50):
        print(altcoin, coins[altcoin])
    pass
'''

for altcoin in coins:
    #which alt coins have the word coin in them?
    if("coin" in altcoin.lower()):
        print(altcoin)
    pass



numbers_of_coins = len(coins)
sum = 0
for altcoin in coins:
    #what is the average cost of an alt coin?
    sum += coins[altcoin]
    pass
print(sum/numbers_of_coins)