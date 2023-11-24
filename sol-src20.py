import solana
from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.publickey import PublicKey
from solana.system_program import TransferParams, transfer
from solana.transaction import Transaction
from solana.transaction import AccountMeta, TransactionInstruction
from base58 import b58encode, b58decode

client = Client("https://solana-mainnet.phantom.app/YBPpkkN4g91xDiAnTE9r0RcMkjg0sKUIWvAfoFVJ/")
secret = "3fxwYQXDnedkddt9MHTRo9KLGCeFCQGAacdjPH3UGagfSxve1YRh2w3YgvKtTzJUdXVMWf3YhBWGHom71HhaCEur"
keypair = Keypair.from_secret_key(b58decode(secret))
toAddr = "MemoSq4gqABAXKb96qnH8TysNcWxMyWCqXgDLGmfcHr"

def logMemo(message):
    transfer_parameters = TransactionInstruction(
    keys=[AccountMeta(pubkey=keypair.public_key, is_signer=True, is_writable=True)],
    data=bytes.fromhex(message.encode('utf-8').hex()),
    program_id=PublicKey(toAddr)
    )
    transaction = Transaction().add(transfer_parameters)
    transaction_result = client.send_transaction(transaction, Keypair.from_secret_key(b58decode(secret)))
    #print("发送结果 :" ,transaction_result)
    resultOfTxhash = transaction_result['result']
    print(f"发送完成 : hash地址为 https://solscan.io/tx/{resultOfTxhash}")

data = {"p":"src-20","op":"mint","tick":"lamp","amt":"1000"}

num = 10
for count in range(num):
    logMemo(str(data))

    

