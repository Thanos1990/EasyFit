import os
import logging
import account

# Create a logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Create a file handler that logs into a file into the current folder
logfile = os.path.join(os.path.dirname(os.path.realpath(__file__)),'account.log')
handler = logging.FileHandler(logfile)
handler.setLevel(logging.INFO)

# Create a logging format
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
handler.setFormatter(formatter)

# Attach the handler to the logger
logger.addHandler(handler)

ccy = input('Please insert ccy: ')
acc=account.Account(ccy, logger)

while True:
    _action = input("Please insert deposit, withdraw or enter for quit: ")
    if _action.lower() == 'deposit':
        _deposit = float(input('How much you wish to deposit? '))
        acc.deposit(_deposit)
    elif _action.lower() == 'withdraw':
        _withdraw = float(input('How much you wish to withdraw? '))
        acc.withdraw(_withdraw)
    else:
        break

logger.warning('Final amount is: {}{}'.format(ccy ,acc.balance))