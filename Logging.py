import logging
logging.basicConfig(filename='D:\\Personal Files\\Documents\\Python Projects\\log.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')
#Basic logging setup.
#There are five logging levels: DEBUG, INFO, WARNING, ERROR and CRITICAL. Critical is the highest level.

#logging.disable(logging.CRITICAL)
logging.debug('Start of program')

def factorial(n):
    logging.debug('Start of factorial (%s)' % (n))
    total = 1
    for i in range(1, n + 1): #First argument specifies a starting integer in range.
        total *= i
        logging.debug('i is %s, total is %s' % (i, total))
    logging.debug('Return value is %s' %(total))
    return total
print(factorial(5))

logging.debug('End of program')
