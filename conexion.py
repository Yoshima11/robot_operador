import time
import pyRofex as pr

class conexion:
    def __init__(self, user, password, account, environment):
        self.user = user
        self.password = password
        self.account = account
        self.environment = environment
    def env(environment):
        if(str(environment).upper()=='LIVE'):
            return pr.Environment.LIVE
        else:
            return pr.Environment.REMARKET
    def iniciar(user, password, account, environment):
        try:
            val = pr.initialize(
                user=user,
                password=password,
                account=account,
                environment=conexion.env(environment),
            )
            print('Conexión establecida.')
            print(val)
            time.sleep(1)
        except Exception as error:
            print('Fallo de autenticación.')
            print(error)
            exit()
