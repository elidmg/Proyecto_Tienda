#Este módulo permitirá a los usuarios administrar las ventas realizadas en la tienda en línea.
#Para ello, se deberá desarrollar lo siguiente:
#
#Registrar las ventas con la siguiente información:
#Cliente que realizó la compra
#Productos comprados
#Cantidad de cada producto
#Método de pago
#Método de envío
#El desglose del total de compra
#Subtotal 
#Descuentos
#5% de descuento si el cliente es jurídico y paga de contado 
#IVA (16%)
#IGTF (3%) en caso de que pague en divisas
#Total
#Generar facturas para cada compra
#Si el cliente es jurídico se podrá realizar compras a crédito (pago en 15 o 30 días)
#Buscar ventas en función de los siguientes filtros:
#Cliente
#Fecha de la venta	
#Monto total de la venta

class Sale:
    def __init__(self, customer, product, quantity, method_pay, method_shipping, total, subtotal, discount, date):
        self.customer= customer
        self.product = product
        self.quantity = quantity
        self.method_pay = method_pay
        self.method_shipping = method_shipping
        self.total = total
        self.subtotal = subtotal
        self.discount = discount
        self.date = date

    def show_sale(self):
        return f"""
        Cliente: {self.customer}
        Producto: {self.product}
        Cantidad: {self.quantity}
        Metodo de pago: {self.method_pay}
        Metodo de envio: {self.method_shipping}
        Total: {self.total}
        Subtotal: {self.subtotal}
        Descuento: {self.discount}
        Fecha: {self.date}
        """
    