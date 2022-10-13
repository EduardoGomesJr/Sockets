# Classe: Sockets_Server_Win
# Descrição: Cria/sobe serviço no Windows
# Data: 12/10/2022
# Autor: Eduardo Gomes Júnior

import win32serviceutil
import servicemanager
import win32event
import win32service


class Sockets_Server_Win(win32serviceutil.ServiceFramework):

    _svc_name_ = 'pythonService'
    _svc_display_name_ = 'Python Service'
    _svc_description_ = 'Python Service Description'

    @classmethod
    # Rotina: ClassMethod para analisar a linha de comando
    # Descrição: Cria serviço Windows
    # Data: 12/10/2022
    def parse_command_line(cls):
        win32serviceutil.HandleCommandLine(cls)

    # Rotina: __init__
    # Descrição: Cria serviço Windows
    # Data: 12/10/2022
    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    # Rotina: SvcStop
    # Descrição: Chamado quando serviço é parado
    # Data: 12/10/2022
    def SvcStop(self):
        self.stop()
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    # Rotina: SvcDoRun
    # Descrição: Chamado quando serviço é inicializado
    # Data: 12/10/2022
    def SvcDoRun(self):
        self.start()
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE,
                              servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))
        self.main()

    # Rotina: start
    # Descrição: Inicia serviço
    # Data: 12/10/2022
    def start(self):
        pass

    # Rotina: stop
    # Descrição: Parar serviço
    # Data: 12/10/2022
    def stop(self):
        pass

    # Rotina: main
    # Descrição: Rotina principal.
    # Data: 12/10/2022
    def main(self):
        pass


# entry point of the module: copy and paste into the new module
# ensuring you are calling the "parse_command_line" of the new created class
if __name__ == '__main__':
    Sockets_Server_Win.parse_command_line()
