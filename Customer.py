#Este módulo permitirá a los usuarios administrar la información de los clientes registrados 
#en la tienda en línea. Para ello, se deberá desarrollar lo siguiente:
#
#Registrar nuevos clientes con la siguiente información:
#Nombre y Apellido o Razón Social
#Tipo de cliente (Natural o Jurídico)
#Cédula o RIF
#Correo electrónico
#Dirección de envío
#Teléfono
#Modificar la información de los clientes existentes
#Eliminar clientes de la tienda
#Buscar clientes en función de los siguientes filtros:
#Cédula o RIF
#Correo electrónico

class Customer:
    def __init__(self, name, kind_customer, dni, correo, direction, phone):
        self.name = name
        self.kind_customer = kind_customer
        self.dni = dni
        self.correo = correo
        self.direction = direction
        self.phone = phone

    def show_customer(self):
       return f"""
       Nombre: {self.name}
       Tipo Cliente: {self.kind_customer}
       Dni: {self.dni}
       Correo: {self.correo}
       Direccion: {self.direction}
       Telefono: {self.phone}
       """
    

