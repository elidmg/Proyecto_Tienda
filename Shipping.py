#Este módulo permitirá a los usuarios administrar los envíos realizados por la tienda en línea. 
#Para ello, se deberá desarrollar lo siguiente:
#
#Registrar los envíos con la siguiente información:
#Orden de compra
#Servicio de envío (e.g. MRW, Zoom, Delivery)
#En caso de que sea delivery agregar los datos del motorizado
#Costo del servicio
#Buscar envíos en función de los siguientes filtros:
#Cliente
#Fecha

class Shipping:
    def __init__(self, order, shipping_service, data_delivery, cost):
        self.order = order
        self.shipping_service = shipping_service
        self.data_delivery = data_delivery
        self.cost = cost
        
    def show_shipping(self):
       return f"""
       Orden: {self.order}
       Servicio de Envío: {self.shipping_service}
       Datos de Delivery: {self.data_delivery}
       Cost: {self.cost}
       """
    