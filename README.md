# 🚀 Honeypot Rescue 🚀
![TradingTigers](https://trading-tigers.com/assets/img/TradingTigers.png)  

Don't expect too much, the transfer function must work, if whitelisting is used there, it is still not possible to sell it.

Please do not deliberately buy Honeypot tokens, and do not rely on this script, it is currently in the testing phase.  

```python
* We are not responsible for lost money, not functioning sales,
* Thermonuclear war, or misuse of this tool.
```
  
So, let's annoy the F*** scammers! 

Please give feedback!
![](https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.pngfind.com%2Fmpng%2FThbTmT_join-the-conversation-telegram-logo-white-png-transparent%2F&psig=AOvVaw19UUoIXdbWlZ96wgzunSnJ&ust=1643477225680000&source=images&cd=vfe&ved=0CAgQjRxqFwoTCLiMi_n71PUCFQAAAAAdAAAAABAI)

# Infos
 This script is written in Solidity and Python3, it allows you to sell Honeypot tokens despite broken TransferFrom function.
 The main part of the HoneypotRescue.sol is a fork of the PancakeSwap router, I have rewritten the function so that no TransferFrom is used.  
 In addition, it may be possible to bypass FEES of tokens.
 Please do not forget the LICENSE!

# It works only if:
 - Your Honeypot Token don't use Whitelist for Transfer function.
 - Your Honeypot Token is Available for purchase and it works to buy this one.
 - Your Honeypot Token Owns Liquidity.
  

# To the Preparation:  
Clone Repository:
```shell
git clone https://github.com/Trading-Tiger/Honeypot_Rescue_Solidity_Python
```
---
# Deploy Contract:
 - This must be executed only once per address!
 - The easiest way is https://remix.ethereum.org/.
 - Upload the HoneypotRescue.sol to REMIX, connect to Metamask and select Solidity 6.6.
 - ATTENTION TO THE INITHASH & FEES in LINE 164/180/190 of the HoneypotRescue.sol and adjust them to your selected swap. Currently this is set to PancakeSwap.(You can find it in your block explorer in the contract code of the according router.)
 - Compile the contract, fill in the parameters, FACTORY & WRAPPED ADDRESS.
---
 - Copy the Created Contract addresse and insert it in the settings.json between the "" after "rescueContract":!

- [Install python3, pip.](https://www.python.org/)
- Go to the downloaded directory, open a terminal, make sure you are in the TRADINGTIGERS_HONEYPOTRESCUE folder.

# Install the Python3 dependencies with:
```shell
python3 -m pip install -r requirements.txt
```
If there are errors here, make sure you have the required C++ build tools for your system.
- [Windows](https://stackoverflow.com/questions/44951456/pip-error-microsoft-visual-c-14-0-is-required/44953739#44953739) 
- [Ubuntu/apt Based](https://linuxconfig.org/how-to-install-g-the-c-compiler-on-ubuntu-18-04-bionic-beaver-linux)

---
# Support Trading-Tigers.com by Buying [TradingTigers Token](https://bscscan.com/token/0x34faa80fec0233e045ed4737cc152a71e490e2e3)