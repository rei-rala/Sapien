import logging

logger = logging

modo_debug = input('\nIngresar en modo debug? Ingrese "Si" o "Debug"\n==> ')

if modo_debug.lower() == 'si' or modo_debug.lower() == 'debug':
    logger.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                    datefmt='%I:%M:%S %p',
                    handlers=[
                        logging.FileHandler('manejo_de_errores.log'),
                        logging.StreamHandler()
                    ])
    print()
    logging.debug('MODO DEBUG ACTIVADO')
else:
    logger.basicConfig(level=logging.ERROR,
                    format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
                    datefmt='%I:%M:%S %p',
                    handlers=[
                        logging.FileHandler('manejo_de_errores.log'),
                        logging.StreamHandler()
                    ])
    print()
    print('Modo normal')


if __name__ == '__main__':
    logging.debug('mensaje debug')
    logging.info('mensaje info')
    logging.warning('mensaje warning')
    logging.error('mensaje error')
    logging.critical('mensaje critical')