#Este módulo permitirá a los usuarios administrar los productos que se venden en la tienda en línea. 
#Para eso tendrás que tener en cuenta, que la información será dada a través de una API, (ver observaciones). 
#Con esta información deberán desarrollar lo siguiente:
#
#Agregar nuevos productos a la tienda con la siguiente información:
#Nombre del producto
#Descripción
#Precio
#Categoría (por ejemplo: alimentos, suplementos, cuidado personal, etc.)
#Inventario disponible
#Buscar productos en función de los siguientes filtros:
#Categoría
#Precio
#Nombre
#Disponibilidad en inventario
#Modificar la información de los productos existentes
#Eliminar productos de la tienda


class Product:
    def __init__(self, name, description, cost, category, inventary):
        self.name = name
        self.description = description
        self.cost = cost
        self.category = category
        self.inventary = inventary

    def show_product(self):
        return f"""
        Nombre: {self.name}
        Descripcion: {self.description}
        Costo: {self.cost}
        Categoria: {self.category}
        Inventario: {self.inventary}
        """
    

        
        
        