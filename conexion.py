import time
import pyRofex as pr

def env(environment):
    if(str(environment).upper()=='LIVE'):
        return pr.Environment.LIVE
    else:
        return pr.Environment.REMARKET

def iniciar(user, password, account, environment):
    try:
        pr.initialize(
            user=user,
            password=password,
            account=account,
            environment=env(environment),
        )
        print('Conexión establecida.')
        time.sleep(1)
    except Exception as error:
        print('Fallo de autenticación.')
        print(error)
        exit()
