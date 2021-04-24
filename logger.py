import logging

logger = logging


def mode(modo):
    modo_fijado = ['DEBUG', 'ERROR' ]
    if modo.lower() in ('si', 's', 'debug', 'd', 'bug', 'dev'):
        logger.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
            datefmt='%I:%M:%S %p',
            handlers=[
                logging.FileHandler(f'manejo_de_errores.log'),
                logging.StreamHandler()
            ]
        )
        logging.debug('MODO DEBUG ACTIVADO')
    else:
        logger.basicConfig(
            level=logging.ERROR,
            format='%(asctime)s: %(levelname)s [%(filename)s:%(lineno)s] %(message)s',
            datefmt='%I:%M:%S %p',
            handlers=[
                logging.FileHandler(f'manejo_de_errores.log'),
                logging.StreamHandler()
            ]
        )
        print('Modo normal')


mode(input('\nIngresar en modo debug? Ingrese "Si" o "Debug"\n==> '))


if __name__ == '__main__':
    print('Prueba de log')
    logging.debug('mensaje debug')
    logging.info('mensaje info')
    logging.warning('mensaje warning')
    logging.error('mensaje error')
    logging.critical('mensaje critical')
