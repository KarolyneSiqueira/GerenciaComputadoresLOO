from datetime import datetime
import locale

def dataHoraAtual():
    locale.setlocale(locale.LC_ALL, '')
    hoje = datetime.today()
    return str(hoje.strftime("%c"))  
