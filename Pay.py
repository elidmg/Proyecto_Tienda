#Este módulo permitirá a los usuarios administrar los pagos realizados por los clientes 
#en la tienda en línea. Para ello, se deberá desarrollar lo siguiente:
#
#Registrar los pagos con la siguiente información:
#Cliente que realizó el pago
#Monto del pago
#Moneda del pago
#Tipo de pago (e.g. PdV, PM, Zelle, Cash)
#Fecha del pago
#Buscar pagos en función de los siguientes filtros:
#Cliente
#Fecha
#Tipo de pago
#Moneda de pago

class Pay:
    def __init__(self, customer, amount, currency, kind_pay, date):
        self.customer = customer
        self.amount = amount
        self.currency = currency
        self.kind_pay = kind_pay
        self.date = date
        
    def show_pay(self):
       return f"""
       Cliente: {self.customer}
       Monto : {self.amount}
       Moneda: {self.currency}
       Tipo Pago: {self.kind_pay}
       Date : {self.date}
       """
    
       

