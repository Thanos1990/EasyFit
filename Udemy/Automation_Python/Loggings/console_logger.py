import account
import logging

# Create a logger with min level INFO
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

acc = account.Account('EUR', logger)
acc.deposit(100.0)
acc.deposit('20.0')
acc.withdraw(4000.0)
acc.withdraw(30.0)
logger.warning('Final amount is: {}'.format(acc.balance))