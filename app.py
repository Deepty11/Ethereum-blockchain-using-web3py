from web3 import Web3

ganache_url="http://127.0.0.1:7545"
web3=Web3(Web3.HTTPProvider(ganache_url))

account_1="0x94cCd09067fF8C50df53aaf190f6da75b9a6aAF1"
account_2="0xf7b544dEB47838a524ab03eE38D9660b13ac00C4"
private_key="ee17fd30e98f59c45f5cf9005512c2eaeb80cf6bce10519cf304f0b61a1b8a9e"

nonce=web3.eth.getTransactionCount(account_1)

tx={
    'nonce': nonce,
    'to':account_2,
    'value':web3.toWei(1,'ether'),
    'gas':2000000,
    'gasPrice':web3.toWei('50','gwei')

}

signed_tx=web3.eth.account.signTransaction(tx,private_key)
txHash=web3.eth.sendRawTransaction(signed_tx.rawTransaction)
print(web3.toHex(txHash))
