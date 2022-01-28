#    Copyright (C) 2022  Seven, Trading-Tigers.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.


from web3 import Web3
import json, sys


# BSC most used ERC20 
WBNB = Web3.toChecksumAddress("0xbb4cdb9cbd36b01bd1cbaebf2de08d9173bc095c")
BUSD = Web3.toChecksumAddress("0xe9e7cea3dedca5984780bafc599bd69add087d56")
USDT = Web3.toChecksumAddress("0x55d398326f99059ff775485246999027b3197955")



UnicodeQR ="""
If you are fucking rich, donate something, so i can take more time for more tools.

ALL CHAINS DEV:
 0x3a0E4Fc1Ff11b86F9ba6308446B6B278772fB95b
   ▄▄▄▄▄▄▄ ▄ ▄ ▄ ▄    ▄  ▄▄▄▄▄▄▄  
   █ ▄▄▄ █ ▄██▀▀█▀▄▀ ▄ █ █ ▄▄▄ █  
   █ ███ █ █▀▀▄█▀██▀██▄█ █ ███ █  
   █▄▄▄▄▄█ ▄ █▀▄ █ ▄ ▄▀█ █▄▄▄▄▄█  
   ▄▄▄▄  ▄ ▄ █▄█▄█▀▀█ ▄▀▄  ▄▄▄ ▄  
   ▄▀█▀▄█▄██▄█▄█▄▄  █ ▀█ ▀▄█▄▄█▀  
   ▄█▀▀██▄█▀██ ▄█  █▄▄  █▀▀ █▄█   
   ▀  ▀▄▄▄▄▀█ █▀█ ▀ ▀██▄▀█ ▄▄▀▀█  
   ▄  █ ▄▄█▀▄ ▀▄▄█ █ ▀▄ ▄ █▀▀▄▀▄  
   ▄ ██▀ ▄▀█ ▀  ▀██▀ ▀  ▄ █▄▄ ▀   
    ▄▀▀▀ ▄▄█▀▄▀  ▄▀ █ █▄▄██▄ █ ▄  
   ▄▄▄▄▄▄▄ ▀█▀  ▄▄   ▄ █ ▄ █▀▄ ▀  
   █ ▄▄▄ █  ▄██▀▀ █▀   █▄▄▄█  ▄▄  
   █ ███ █ ██▀▀▄▀█ ██   ▄  ▀██ █  
   █▄▄▄▄▄█ █▀█▄▀▀  █ ▀▀█▀▀█ ▀ █   
                                  
"""

ascii = """

___________                 .__.__               
\__    _______________    __| _|__| ____   ____  
  |    |  \_  __ \__  \  / __ ||  |/    \ / ___\ 
  |    |   |  | \// __ \/ /_/ ||  |   |  / /_/  >
__________.___|  (____  \____ ||__|___|  \___  / 
\__    ___|__| ____   ___________ ______/_____/  
  |    |  |  |/ ___\_/ __ \_  __ /  ___/         
  |    |  |  / /_/  \  ___/|  | \\___ \          
  |____|  |__\___  / \___  |__| /____  >         
            /_____/      \/          \/          

"""

class TradingTigersRescue():

    def __init__(self):
        self.w3 = self.initWEB3()
        self.token_contract = False
        self.readSettings()
        self.checkSettings()
        self.menu()
    
    def readSettings(self):
        with open("settings.json", "r") as S:
            settings = json.load(S)
        self.address = settings["address"]
        self.SecretKey = settings["SecretKey"]
        self.gas_price = int(settings["GAS_GWEI"] * (10**9))
        self.rescueContract = settings["rescueContract"]


    def checkSettings(self):
        if len(self.address) != 42:
            print("Check Address in settings.json")
            sys.exit()
        if len(self.SecretKey) != 64:
            print("Check Secret Key in settings.json")
            sys.exit()
        if len(self.rescueContract) == 42:
            self.ContractDeployed = True
            try:
                self.initRescueContract()
                if self.CheckContractDEV() == True:
                    self.rescueInitSuccessfully = True
                else:
                    self.rescueInitSuccessfully = False
                    print("ITS NOT YOUR CONTRACT!")
            except Exception as e:
                print(e)
                self.rescueInitSuccessfully = False

        else:
            self.ContractDeployed = False



    def initWEB3(self):
        with open("./settings.json") as f:
            keys = json.load(f)
        if keys["Provider"][:2].lower() == "ws":
            w3 = Web3(Web3.WebsocketProvider(keys["Provider"]))
        else:
            w3 = Web3(Web3.HTTPProvider(keys["Provider"]))
        return w3


    def initRescueContract(self):
        with open("./Artifacts/TradingTigersRescueRouter.json") as f:
            Abi = json.load(f)
        self.TradingTigersRescueRouter = self.w3.eth.contract(address=Web3.toChecksumAddress(self.rescueContract), abi=Abi)    


    def initToken(self):
        print("Input your Honeypot Token Address")
        while True:
            try:
                self.token_address = Web3.toChecksumAddress(input("=> "))
                break
            except Exception as e:
                print("Wrong Address Format, Try Again!")
                if e == KeyboardInterrupt:
                    sys.exit()
        with open("./Artifacts/IERC20.json") as IERC20:
            contract_abi = json.load(IERC20)
        self.token_contract = self.w3.eth.contract(address=self.token_address, abi=contract_abi)
        self.TokenSymbol = self.token_contract.functions.symbol().call()
        print("OK, its Token Contract!")


    def estimateGas(self, txn):
        gas = self.w3.eth.estimateGas(txn)
        gas = gas + (gas / 10) # Adding 1/10 from gas to gas!
        maxGas = Web3.fromWei(gas * self.gas_price, "ether")
        print("\nMax Transaction cost " + str(maxGas))
        return gas


    def SendToken(self):
        if self.token_contract == False:
            self.initToken()
        self.TokenBalance = self.token_contract.functions.balanceOf(self.address).call()
        self.TokenDecimals = self.token_contract.functions.decimals().call()
        print("You want to send", self.TokenBalance / (10**self.TokenDecimals), self.TokenSymbol, "to", self.rescueContract, "?")
        print("------------------------------------")
        print("1. => YES")
        print("2. => No, Cancel")
        print("------------------------------------")
        ipt = int(input("=> "))
        try:
            if ipt == 1:
                try:

                    TXN = self.token_contract.functions.transfer(
                        self.rescueContract,
                        self.TokenBalance
                    ).buildTransaction({
                                'from': self.address, 
                                'gas': 480000,
                                'gasPrice': self.gas_price,
                                'nonce': self.w3.eth.getTransactionCount(self.address), 
                                })
                    TXN.update({ 'gas' : int(self.estimateGas(TXN))})
                    signed_txn = self.w3.eth.account.sign_transaction(TXN,self.SecretKey)
                    txn = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
                    txn_receipt = self.w3.eth.waitForTransactionReceipt(txn)
                    if txn_receipt["status"] == 1: "SEND Transaction Successfull, Looking Good!"
                    else: "Damn, SEND Transaction Faild, sorry no chance to sell!"

                except Exception as e:
                    print("Damn, some error, looks like token has Whitlist for Transfer function.")
                    print(e)
                    self.exit = True
                
        except Exception as e:
            print(e)

    def executeSell(self):
        print("Set you Pooled Liquidity Token:")
        print("1. => WBNB")
        print("2. => BUSD")
        print("3. => USDT")
        print("4. => Costum address")
        print("------------------------------------")
        ipt = int(input("=> "))
        try:
            if ipt == 1:
                self.path = [self.token_address, WBNB]
            elif ipt == 2:
                self.path = [self.token_address, BUSD]
            elif ipt == 3:
                self.path = [self.token_address, USDT]
            elif ipt == 4:
                print("4. => Costum address")
                while True:
                    try:
                        ct = Web3.toChecksumAddress(input("=> "))
                        self.path = [self.token_address, ct]
                        break
                    except Exception as e:
                        print(e)
            TXN = self.TradingTigersRescueRouter.functions.HoneypotBypass(
                        0,
                        self.path
                    ).buildTransaction({
                                'from': self.address, 
                                'gas': 480000,
                                'gasPrice': self.gas_price,
                                'nonce': self.w3.eth.getTransactionCount(self.address), 
                                })
            TXN.update({ 'gas' : int(self.estimateGas(TXN))})
            signed_txn = self.w3.eth.account.sign_transaction(TXN,self.SecretKey)
            txn = self.w3.eth.sendRawTransaction(signed_txn.rawTransaction)
            txn_receipt = self.w3.eth.waitForTransactionReceipt(txn)

            if txn_receipt["status"] == 1: "Bypass Transaction Successfull!"
            else: "Damn, Bypass Transaction Fails, sorry no chance to sell it!"
            
        except Exception as e:
            print("Wrong input!")
            print(e)


    def CheckContractDEV(self):
        DEV = self.TradingTigersRescueRouter.functions.DEV().call()
        if Web3.toChecksumAddress(DEV) == Web3.toChecksumAddress(self.address):
            return True
        return False


    def menu(self):
        print(ascii)
        print("------------------------------------")
        print("Current Address: ", self.address)
        if self.rescueInitSuccessfully == False:
            print("Please Deploy first your Contract with https://remix.ethereum.org/")
            sys.exit() 
        else:
            print("Contract Ready:", self.ContractDeployed)
        if self.token_contract != False:
            print("Current Token:", self.token_address, self.TokenSymbol)
        print("Options:")
        print("1. => Set Token Address")
        print("2. => Send Token to Contract")
        print("3. => Execute Sell")
        print("4. => exit")
        print("------------------------------------")
        self.exit = False
        ipt = int(input("=> "))
        try:
            if ipt == 1:
                self.initToken()
            elif ipt == 2:
                self.SendToken()
            elif ipt == 3:
                self.executeSell()
            elif ipt == 4:
                print("Ok, Bye!")
                self.exit = True
        except Exception as e:
            print("Wrong input!")
            print(e)

        if self.exit != True:
            self.menu()
        print(UnicodeQR)
        sys.exit()
        






TradingTigersRescue()