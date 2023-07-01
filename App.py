import requests 
from Product import Product
from Customer import Customer
from datetime import datetime
from Sale import Sale
from Pay import Pay
from Shipping import Shipping

class App:
    def __init__(self):
      self.lista_productos = []
      self.lista_clientes = [] 
      self.lista_envios = []
      self.lista_pagos = []
      self.lista_ventas = []
      self.lista_fecha = []

    def see_product(self):
      link = "https://raw.githubusercontent.com/Algoritmos-y-Programacion-2223-3/api-proyecto/main/products.json"
      response = requests.get(link)
      datos = response.json()
      return datos

    def change_objet(self, product):
      for i in product: 
        product = Product(i['name'], i['description'], i['price'], i['category'], 30)
        product.append(self.lista_productos)
      return product      
    
#------------------------------------------------------------------------------------------------------------#

    def register_produts(self):
      name = input("Por favor ingrese nombre del producto: ")
      description = input("Descripción del producto: ")
      cost = input("Ingrese el costo del producto: ")
      while cost.isnumeric() == False:  
        cost = input("¡Error! Ingrese numeros unicamente: ")   
      cost = int(cost)
      category = input("Ingrese tipo de producto: ")
      inventary = input("¿Cuantos hay disponible?: ")
      product = Product(name, description, cost, category, inventary)
      self.lista_productos.append(product)
      print(product)
      return product
    
    def modify_product(self):
      count = 1
      for i in self.lista_productos:
        print(f"{count}. {i.name}")
      modify = input("Ingrese el numero de producto que dea modificar: ")
      while modify.isnumeric() == False and int(modify) < len(self.lista_productos):  
        modify = input("¡Error! Ingrese numeros unicamente: ")   
      modify = int(modify) 
      modificar = input("""¿Que desea modificar?: 
        1. Nombre
        2. Description
        3. Cost
        4. Categoria
        5. Inventario
        """)
      if modificar == "1":
          name = input("Ingrese el nuevo nombre: ")
          self.lista_productos[modify] = name

      elif modificar == "2":
        description = input("Ingrese la nueva descripción: ")
        self.lista_productos[modify] = description

      elif modificar == "3":
        cost = input("Ingrese el nuevo precio: ")
        while cost.isnumeric() == False:  
          cost = input("¡Error! Ingrese numeros unicamente: ")   
        cost = int(cost) 
        self.lista_productos[modify] = cost  

      elif modificar == "4":
        category = input("Ingrese la nueva categoria: ")
        self.lista_productos[modify] = category
      
      elif modificar == "5":
        inventary = input("Ingrese el nuevo inventario: ")
        while inventary.isnumeric() == False:   
          inventary = input("¡Error! Ingrese numeros unicamente: ")   
        inventary = int(inventary)
        self.lista_productos[modify] = inventary
      
      else:
        print("Error!!! producto no encontrado")
      print("Modificado correctamente <3")

    def delete_product(self):
      count = 1
      for i in self.lista_productos:
        print(f"{count}. {i.name}")
      delete = input("Ingrese el numero de producto que desea eliminar: ")
      while delete.isnumeric() == False:
        delete = input("¡Error! Ingrese numeros unicamente: ")   
      delete = int(delete) 
      self.lista_productos.pop(delete)
      print("Se ha borrado exitosamente <3")
   
    def seach_category(self):
      self.lista_categoria = []
      for i in self.lista_productos: 
        if i.category not in self.lista_categoria:
          self.lista_categoria.append(i.category)
      count = 1
      for i in self.lista_categoria:
        print(f"{count} {i}")
        seach = input("Ingrese el numero de la categoria: ")
        while seach.isnumeric() == False and int(seach) > len(self.lista_categoria):
          seach = input("¡Error! Ingrese numeros unicamente: ")   
        seach = int(seach)
        found = self.lista_categoria[seach]-1
        for i in self.lista_productos:
          if i.category == found:
            print(i.show())
            
    def seach_name(self):
      self.lista_nombre = []
      for i in self.lista_productos:
        if i.name not in self.lista_nombre:
          self.lista_nombre.append(i.name)
      count = 1
      for i in self.lista_nombre:
        print(f"{count} {i}")
        seach = input("Ingrese el nombre del producto: ")
        found = self.lista_nombre[seach]-1
        for i in self.lista_productos:
          if i.name == found:
            print(i.show()) 
    
    def seach_precio(self):
      maxi = input("Diga su maximo de precio que desea buscar: ")
      while maxi.isnumeric == False:
        maxi = input("¡Error! Ingrese numeros unicamente: ")   
        maxi = int(maxi)
      mini = input("Diga su minimo de precio: ")
      while mini.isnumeric == False:
        mini = input("¡Error! Ingrese numeros unicamente: ")   
        mini = int(mini) 
      for i in self.lista_productos:
          if i.cost > mini and i.cost < maxi:
            print(i.show()) 

    def seach_inventary(self):
      for i in self.lista_productos:
        if i.inventary > 0:
          print(i.show())

#------------------------------------------------------------------------------------------------------------#

    
    def register_sale(self):
      name = input("Ingrese el dni del cliente que realizó la compra: ")
      while name.isnumeric == False:
        name = input("¡Error! Ingrese numeros unicamente: ")   
      name = int(name)
      encontrado = False
      for i in self.lista_clientes:
        if i.dni == name:
          customer = i
          encontrado = True
          break
        if encontrado == True:
          count = 1
          for product in self.lista_productos:
            print(f"{count}.{product.show()}") 
            count =+ 1
        sale = [] 
        while True:
          buy = input("Ingrese el numero de producto que desea: ")
          while buy.isnumeric == False:
            buy = input("¡Error! Ingrese numeros unicamente: ")   
          buy = int(buy)
          product = self.lista_productos[buy]-1
          amount = input("¿Que cantidad desea?: ")
          while amount.isnumeric == False:
            amount = input("¡Error! Ingrese numeros unicamente: ")   
          amount = int(amount)
          sale.append(product)
          sale.append(amount)
          option = input("""¿Desea seguir comparando? 
          1. Sí
          2. No
          """)
          while option.isnumeric == False != "1" or "2":
            option = input("¡Error! Ingrese los numeros unicamente 1 o 2: ")   
          option = int(option)
          if option == "1":
            pass
          else:
            break
          pay = self.register_pay(customer, date, amount)
          envio = self.register_shipping(customer, date, self.lista_envios)
          subtotal = 0
          count = 0
          for i in sale:
            if isinstance(i,int) == False:
              print(i.show())
              subtotal += i.cost * sale[count + 1]
            count += 1
          print(f"El total es: {subtotal}")
          total, discount = self.discount(subtotal, customer) 
          date = datetime.date()
          date= str(date)
          sale = Sale(self, customer, sale, pay.kind_pay, envio.shipping_service, total, subtotal, discount, date)
          self.lista_envios.append(envio)
          self.lista_pagos.append(pay)
          self.lista_ventas.append(sale)

    def discount(self, subtotal, customer):
      discount = 0
      if customer.kind_customer == "J":
        discount = subtotal*0.05
        subtotal -= subtotal*0.05
      subtotal += subtotal*0.16
      if "$" == "$":
        subtotal += subtotal*0.03
      return subtotal, discount

    def seach_customer_sale(self):
      self.lista_sale =[]
      seach = input("Ingrese el dni del cliente que desea buscar: ")
      while seach.isnumeric() == False:
        seach = input("Error!!! Ingrese solo numeros ")
      seach = int(seach)
      for i in self.lista_ventas:
        if i.dni == seach:
          self.lista_sale.append(i)
      for i in self.lista_sale:
        print(i.show())

    def seach_date(self):
      self.lista_date = []
      date = input("Ingrese la fecha que quiere buscar: ")
      for i in self.lista_ventas:
        if i.date == date:
          self.lista_date.append(i)
      for i in self.lista_date:
        print(i.show())
    
    def seach_total(self):
      self.lista_total = []
      mini = input("Ingrese el minimo de costo: ")
      maxi = input("Ingrese el maximo de costo: ")
      while mini.isnumeric() == False:
        mini = input("Error!!! Ingrese solo numeros ")
      mini = int(mini)
      while maxi.isnumeric() == False:
        maxi = input("Error!!! Ingrese solo numeros ")
      maxi = int(maxi)
      for i in self.lista_ventas:
        if i.total > mini and i.total < maxi:
          self.lista_total.append(i)
      for i in self.lista_total:
        print(i.show())  
    
#   def show_product(self):
      #for product in self.lista_productos:
        #print(product.show()) 

#------------------------------------------------------------------------------------------------------------#

    def register_customer(self):
      
      name = input("Por favor ingrese su nombre y apellido: ")
      kind_customer = input("""
      Es usted: 
      1- persona juridica
      2- persona normal
      """)
      while kind_customer != '1' and kind_customer != '2':
        kind_customer = input("""
        Error! ingrese el numéro correcto:
        1- persona juridica
        2- persona normal
        """)
      dni = input("Ingrese su cédula: ")
      while dni.isnumeric() == False:  
        dni = input("¡Error! Ingrese numeros unicamente: ")   
      dni = int(dni)  
      correo = input("Ingrese su correo electronico: ")
      while not "@" in correo: 
          correo = input("¡Erro! Ingrese su correo nuevamente, asegure que tenga @: ")
      direction = input("Ingrese su dirección: ")
      phone = input("Ingrese su número de telefono: ")
      while phone.isnumeric() == False:   
        phone = input("¡Error! Ingrese numeros unicamente: ")   
      phone = int(phone)
      if kind_customer == "1":
        customer = Customer(name, "J", dni, correo, direction, phone) 
      else: 
        customer = Customer(name, "N", dni, correo, direction, phone)
      self.lista_clientes.append(customer)
      print(customer)
      return customer
    
    def modify_customer(self):

      usuario = input("Ingrese el dni del usuario que desea modifiar: ")
      while usuario.isnumeric() == False:  
        usuario = input("¡Error! Ingrese numeros unicamente: ")   
      usuario = int(usuario) 
      encontrado = False
      count = 0
      for i in self.lista_clientes:
        if i.dni == usuario:    
              encontrado = True
              break
        else:
              count += 1
      if encontrado == True:
        modificar = input("""¿Que desea modificar?: 
        1. Nombre
        2. Tipo de cliente
        3. Dni
        4. Correo 
        5. Telefono
        """)
        if modificar == "1":
          name = input("Ingrese el nuevo nombre: ")
          self.lista_clientes[count] = name

        elif modificar == "2":
          if self.lista_clientes[count].kind_customer == "J":
            self.lista_clientes[count].kind_customer == "N"
          else:
            self.lista_clientes[count].kind_customer == "J"

        elif modificar == "3":
          dni = input("Ingrese el nuevo dni: ")
          while dni.isnumeric() == False:  
            dni = input("¡Error! Ingrese numeros unicamente: ")   
          dni = int(dni) 
          self.lista_clientes[count] = dni  

        elif modificar == "4":
          correo = input("Ingrese el nuevo correo: ")
          while not "@" in correo: 
            correo = input("¡Erro! Ingrese el correo nuevamente, asegure que tenga @: ")
          self.lista_clientes[count] = correo
        
        elif modificar == "5":
          phone = input("Ingrese su número de telefono: ")
          while phone.isnumeric() == False:   
            phone = input("¡Error! Ingrese numeros unicamente: ")   
          phone = int(phone)
          self.lista_clientes[count] = phone
        
      else:
        print("Error!!! usuario no encontrado")
     
      print("Modificado correctamente <3")
    
    def delete_customer(self):
      
      delete = input("Indique el dni, del usuario que desea eliminar: ")  
      while delete.isnumeric() == False:   
        delete = input("¡Error! Ingrese numeros unicamente: ")   
      delete = int(delete)
      for i in range(len(self.lista_clientes["dni"])):
        if i.dni == delete:   #cedula #esto para acc a un atributo
            self.lista_clientes.pop(i)
            break
      print("Se ha borrado exitosamente <3")
        
    def seach_customer(self):

      seach = input("Ingrese el dni del usuario que desea buscar: ")
      while seach.isnumeric() == False:
        seach = input("Error!!! Ingrese solo numeros ")
      seach = int(seach)
      for bus in self.lista_clientes:
        if bus.dni == seach:
          cliente = bus
      print(cliente.show())
      
#------------------------------------------------------------------------------------------------------------#

    def register_pay(self, customer, date, total):
      currency = input("""Ingrese la moneda con la que desea pagar:
      $ 
      Bs
      """)
      while currency != "$" and currency != "Bs":
        currency = input("Por favor solo ingrese los simbolos mostrados: ")
      kind_pay = input("""Ingrese el tipo de pago: 
      PdV 
      PM 
      Zelle 
      Cash
      """)
      while kind_pay != "PdV" and  kind_pay != "PM" and kind_pay != "Zelle" and kind_pay != "Cash":
        kind_pay = input("""Ingrese solo las opciones mostradas: 
        PdV 
        PM 
        Zelle 
        Cash
        """)
      pay = Pay(self, customer, total, currency, kind_pay, date)
      return pay 
      
    def seach_customer_pay(self):
      seach = input("Ingrese el dni del usuario que desea buscar: ")
      while seach.isnumeric() == False:
        seach = input("Error!!! Ingrese solo numeros ")
      seach = int(seach)
      for bus in self.lista_pagos:
        if bus.dni == seach:
          cliente = bus
      print(cliente.show())

    def seach_date_pay(self):
      self.lista_date = []
      date = input("Ingrese la fecha que quiere buscar: ")
      for i in self.lista_pagos:
        if i.date == date:
          self.lista_date.append(i)
      for i in self.lista_date:
        print(i.show())

    def seach_kind_pay(self):
      pass

    def seach_currency(self):
      pass
 
#------------------------------------------------------------------------------------------------------------#
                          #(self, customer, date, lista_envios)
    def register_shipping(self):
    
      order = len(self.lista_envios)
      shipping_service = input("""Ingrese la empresa de envios deseada:
      MRW 
      Zoom
      Delivery 
      """)
      while shipping_service != "MRW" and  kind_pay != "Zoom" and kind_pay != "Delivery":
        kind_pay = input("""Ingrese solo las opciones mostradas: 
        MRW 
        Zoom
        Delivery
        """)
      shipping = Shipping(self, order, shipping_service)
      return shipping                                     #data_delivery, cost
      
    def seach_customer_shipping(self):
      seach = input("Ingrese el dni del usuario que desea buscar: ")
      while seach.isnumeric() == False:
        seach = input("Error!!! Ingrese solo numeros ")
      seach = int(seach)
      for bus in self.lista_ventas:
        if bus.dni == seach:
          cliente = bus
      print(cliente.show())
    
    def seach_date_shipping(self):
      self.lista_date = []
      date = input("Ingrese la fecha que quiere buscar: ")
      for i in self.lista_ventas:
        if i.date == date:
          self.lista_date.append(i)
      for i in self.lista_date:
        print(i.show())

#------------------------------------------------------------------------------------------------------------#
    def menu(self): 

      while True:
        dato = self.see_product()
        self.change_objet(dato)
        print(self.lista_productos)

        print("""
        ------ BIENVENIDO A ORANGE STORE -----
        TIENDA EN LÍNEA DE PRODUCTOS NATURALEZ
        
        ¿A que modulo quieres ingresar?
        """)
        option = input("""
        1. Modulo productos:
        2. Modulo venta:
        3. Modulo cliente: 
        4. Modulo pagos:
        5. Modulo envios:
        6. Modulo estadisticas: 
        7. Salir
        """)

        if option == "1":
          option = input("""
          1. Registrar producto: 
          2. Modifiar producto:
          3. ELiminar producto:
          4. Busar producto:
          """)

          if option == '1':
            self.register_produts()

          elif option == "2":
            self.modify_product()
          
          elif option == "3":
            self.delete_product()

          elif option == "4":
            option = input("""
            1. Buscar por categoria
            2. Buscar por nombre
            3. Buscar por precio
            4. Buscar por disponibilidad
            """)

            if option == "1":
              self.seach_category()
            
            elif option == "2":
              self.seach_name()
            
            elif option == "3":
              self.seach_precio()

            elif option == "4":
              self.seach_inventary()
        
        elif option == "2":
          option = input("""
          1. Registrar venta: 
          2. Descuentos:
          3. Buscar venta:
          """)

          if option == "1":
            self.register_sale
          
          elif option == "2":
            self.discount()
          
          elif option == "3":
            option = input("""
            1. Buscar por cliente
            2. Buscar por fecha
            3. Buscar por total
            """)

            if option == "1":
              self.seach_customer()
            
            elif option == "2":
              self.seach_date()
            
            elif option == "3":
              self.seach_total()

        elif option == '3':
          option = input("""
          1. Registrar cliente: 
          2. Modifiar cliente:
          3. ELiminar cliente:
          4. Busar cliente:
          """)
          if option == '1':
            self.register_customer()

          elif option == "2":
            self.modify_customer()
          
          elif option == "3":
            self.delete_customer()

          elif option == "4":
            self.seach_customer()
        
        elif option == "4":
          option = input("""
          1. Registrar pago: 
          2. Buscar por:
          """)
          if option == "1":
             self.register_pay()
          
          elif option == "2":
            option = input("""
            1. Buscar por cliente
            2. Buscar por fecha
            3. Buscar por tipo de pago
            4. buscar por moneda
            """)
            if option == "1":
               self.seach_customer_pay()

            elif option == "2":
               self.seach_date_pay()
            
            elif option == "3":
               self.seach_kind_pay()

            elif option == "4":
               self.seach_currency()

        elif option == "5":
          option = input("""
          1. Registrar envio: 
          2. Buscar por:
          """)
          if option == "1":
             self.register_shipping()
          
          elif option == "2":
            option = input("""
            1. Buscar por cliente
            2. Buscar por fecha
            """)
            if option == "1":
               self.seach_customer_shipping()

            elif option == "2":
               self.seach_date_shipping()

        elif option == '6':
            option = input("""
            1. Generar informe de venta
            2. Generar informe de pagos 
            3. Generar informe de envios
            Pulse cualquier otra tecla para retroceder
            Elija el numero de la accion que desea realizar: """)
            if option == '1':
                option = input("""
                1. Buscar ventas totales por fechas
                2. Buscar por producto mas vendidos
                Cualquier otra tecla para buscar clientes mas frecuentes
                Pulse el numero de la accion que desea realizar: """)
                if option == '1':
                    option = input("""
                    1. Ventas totales de un dia
                    2. Ventas totales de un mes
                    Cualquier otra tecla. Ventas totales de un anio
                    Ingrese el numero del proceso que desea realizar: """)
                    if option == '1':
                        fechaD = input('Ingrese la fecha completa (AAAA-MM-DD): ')
                        for i in self.lista_ventas:
                            if i.date == fechaD:
                                self.lista_fecha.append(i)
                        if len(self.lista_fecha)>0:
                            print('Se han encontrado las siguientes ventas: ')
                            for i in self.lista_fecha:
                                print(f'El cliente {i.customer} pago: ')
                                for j in i.order:
                                    print(f'- {j[0]}: {j[2]} unidades')
                                print(f'Y su total fue: {i.total}')
                        else:       
                            print('No se encontraron pagos registrados en la fecha')
               
                    elif option == '2':
                        fechaM = input('Ingrese la fecha completa (AAAA-MM): ')
                        while len(fechaM)<7:
                            fechaM = input('Ingrese correctamente la fecha completa (AAAA-MM): ')
                        fechaM = fechaM[0:8]
                        self.lista_fecha = []

                        for i in self.lista_ventas:
                            if i.date == fechaM:
                                self.lista_fecha.append(i)
                        if len(self.lista_fecha)>0:
                            print('Se han encontrado las siguientes ventas: ')
                            for i in self.lista_fecha:
                                print(f'El cliente {i.customer} pago: ')
                                for j in i.order:
                                    print(f'- {j[0]}: {j[2]} unidades')
                                print(f'Y su total fue: {i.total}')
                        else:       
                            print('No se encontraron pagos registrados en la fecha')
               
                    else:
                        fechaA = input('Ingrese la fecha completa (AAAA): ')
                        while len(fechaA)<4:
                            fechaA = input('Ingrese correctamente la fecha completa (AAAA-MM): ')
                        fechaA = fechaA[0:4]
                        self.lista_fecha = []

                        for i in self.lista_ventas:
                            if i.date == fechaA:
                                self.lista_fecha.append(i)
                        if len(self.lista_fecha)>0:
                            print('Se han encontrado las siguientes ventas: ')
                            for i in self.lista_fecha:
                                print(f'El cliente {i.customer} pago: ')
                                for j in i.order:
                                    print(f'- {j[0]}: {j[2]} unidades')
                                print(f'Y su total fue: {i.total}')
                        else:       
                            print('No se encontraron pagos registrados en la fecha')
               

                elif option == '2':
                    self.esta_productos = []
                    self.esta_productos_cantidad = []
                    for i in self.lista_ventas: 
                        for j in i.order:
                            if j[0] in self.esta_productos:
                                for k in self.esta_productos_cantidad:  
                                    if k[0] == j[0]:
                                        k[1] = int(j[2]) + int(k[1])
                                        k[1] = str(k[1])
                            else:
                                self.esta_productos.append(j[0])
                                self.esta_productos_cantidad.append([j[0],j[2]])
                    #hacer top
                    top1 = ['',0]
                    top2 = ['',0]
                    top3 = ['',0]
                    for i in self.esta_productos_cantidad:
                        if int(i[1])>top1[1]:
                            top1[0]=i[0]
                            top1[1]=int(i[1])
                    top1[1]=str(top1[1])
                    self.esta_productos_cantidad.remove(top1)
                    for i in self.esta_productos_cantidad:
                        if int(i[1])>top2[1]:
                            top2[0]=i[0]
                            top2[1]=int(i[1])
                    top2[1]=str(top2[1])
                    self.esta_productos_cantidad.remove(top2)
                    for i in self.esta_productos_cantidad:
                        if int(i[1])>top3[1]:
                            top3[0]=i[0]
                            top3[1]=int(i[1])
                    top3[1]=str(top3[1])
                    self.esta_productos_cantidad.remove(top3)
                    print(f'El producto mas vendido es: {top1[0]} con {top1[1]} unidades')
                    print(f'El producto mas vendido es: {top2[0]} con {top2[1]} unidades')
                    print(f'El producto mas vendido es: {top3[0]} con {top3[1]} unidades')
                else:
                    self.esta_clientes = []
                    for i in self.lista_ventas:
                        self.esta_clientes.append(i.customer)
                    print(self.esta_clientes)
                    top1 = ["", 0]
                    for i in self.esta_clientes:
                        if self.esta_clientes.count(i) > top1[1]:
                            top1[0]= i
                            top1[1]=self.esta_clientes.count(i)
                    
                    while top1[0] in self.esta_clientes:
                        self.esta_clientes.remove(top1[0])
                    
                    top2 = ["", 0]
                    for i in self.esta_clientes:
                        if self.esta_clientes.count(i) > top2[1]:
                            top2[0]= i
                            top2[1]= self.esta_clientes.count(i)
                    while top2[0] in self.esta_clientes:
                        self.esta_clientes.remove(top2[0])
                    top3 = ["", 0]
                    for i in self.esta_clientes:
                        if self.esta_clientes.count(i) > top3[1]:
                            top3[0]= i
                            top3[1]= self.esta_clientes.count(i)
                    while top3[0] in self.esta_clientes:
                        self.esta_clientes.remove(top3[0])

                    print(f'el cliente que mas compras tiene es {top1}')
                    print(f'el cliente que mas compras tiene es {top2}')
                    print(f'el cliente que mas compras tiene es {top3}')

            elif option == '2':
                option = input("""
                1. Pagos totales de un dia
                2. Pagos totales de un mes
                Cualquier otra tecla. Pagos totales de un anio
                Ingrese el numero del proceso que desea realizar: """)
                if option == '1':
                    fechaD = input('Ingrese la fecha completa (AAAA-MM-DD): ')
                    self.lista_fecha = []
                    for i in self.lista_pagos:
                        if i.date == fechaD:
                            self.lista_fecha.append(i)
                    if len(self.lista_fecha)>0:
                        print('Se han encontrado las siguientes ventas: ')
                        for i in self.lista_fecha:
                            print(f'El cliente {i.customer} pago {i.total} en {i.currency} a traves de {i.kind_pay}: ')
                    else:       
                        print('No se encontraron pagos registrados en la fecha')

                elif option == '2':
                    fechaM = input('Ingrese la fecha completa (AAAA-MM): ')
                    while len(fechaM)<7:
                        fechaM = input('Ingrese correctamente la fecha completa (AAAA-MM): ')
                    fechaM = fechaM[0:8]
                    self.lista_fecha = []

                    for i in self.lista_pagos:
                        if i.date == fechaM:
                            self.lista_fecha.append(i)
                    if len(self.lista_fecha)>0:
                        print('Se han encontrado las siguientes ventas: ')
                        for i in self.lista_fecha:
                            print(f'El cliente {i.customer} pago {i.total} en {i.currrency} a traves de {i.kind_pay}: ')
                    else:       
                        print('No se encontraron pagos registrados en la fecha')
                else:
                    fechaA = input('Ingrese la fecha completa (AAAA): ')
                    while len(fechaA)<4:
                        fechaA = input('Ingrese correctamente la fecha completa (AAAA-MM): ')
                    fechaA = fechaA[0:4]
                    self.lista_fecha = []

                    for i in self.lista_pagos:
                        if i.date == fechaA:
                            self.lista_fecha.append(i)
                    if len(self.lista_fecha)>0:
                        print('Se han encontrado las siguientes pagos: ')
                        for i in self.lista_fecha:
                            print(f'El cliente {i.customer} pago {i.total} en {i.currency} a traves de {i.kind_pay}: ')
                    else:       
                        print('No se encontraron pagos registrados en la fecha')
               
            else:
                option = input("""
                1. Buscar envio por fechas
                Cualquier otra tecla para buscar por producto enviado
                Pulse el numero de la accion que desea realizar: """)
                
                if option == '1':
                    option = input("""
                    1. Envios totales de un dia
                    2. Envios totales de un mes
                    Cualquier otra tecla. Envios totales de un anio
                    Ingrese el numero del proceso que desea realizar: """)
                    if option == '1':
                        fechaD = input('Ingrese la fecha completa (AAAA-MM-DD): ')
                        self.lista_fecha = []
                        for i in self.lista_envios:
                            if i.fecha == fechaD:
                                self.lista_fecha.append(i)
                        if len(self.lista_fecha)>0:
                            print('Se han encontrado las siguientes ventas: ')
                            for i in self.lista_fecha:
                                print(f'El cliente {i.customer} recibio la orden {i.order}, con {i.shipping_service} con un costo de {i.cost}: ')
                               
                        else:       
                            print('No se encontraron pagos registrados en la fecha')
               
                    elif option == '2':
                        fechaM = input('Ingrese la fecha completa (AAAA-MM): ')
                        while len(fechaM)<7:
                            fechaM = input('Ingrese correctamente la fecha completa (AAAA-MM): ')
                        fechaM = fechaM[0:8]
                        print(fechaM)
                        self.lista_fecha = []

                        for i in self.lista_envios:
                            print(i.date[0:8])
                            if i.date[0:7] == fechaM:
                                self.lista_fecha.append(i)
                        if len(self.lista_fecha)>0:
                            print('Se han encontrado las siguientes ventas: ')
                            for i in self.lista_fecha:
                                  print(f'El cliente {i.customer} recibio la orden {i.order}, con {i.shipping_service} con un costo de {i.cost}: ')
                        else:       
                            print('No se encontraron pagos registrados en la fecha')
               
                    else:
                        fechaA = input('Ingrese la fecha completa (AAAA): ')
                        while len(fechaA)<4:
                            fechaA = input('Ingrese correctamente la fecha completa (AAAA-MM): ')
                        fechaA = fechaA[0:4]
                        print(fechaA)
                        self.lista_fecha = []

                        for i in self.lista_envios:
                            if i.fecha[0:4] == fechaA:
                                self.lista_fecha.append(i)
                        if len(self.lista_fecha)>0:
                            print('Se han encontrado las siguientes ventas: ')
                            for i in self.lista_fecha:
                                  print(f'El cliente {i.customer} recibio la orden {i.order}, con {i.shipping_service} con un costo de {i.cost}: ')
                        else:       
                            print('No se encontraron pagos registrados en la fecha')
          
                else:
                    self.esta_productos = []
                    self.esta_productos_cantidad = []
                    for i in self.lista_ventas: 
                        for j in i.order:
                            if j[0] in self.esta_productos:
                                for k in self.esta_productos_cantidad:  
                                    if k[0] == j[0]:
                                        k[1] = int(j[2]) + int(k[1])
                                        k[1] = str(k[1])
                            else:
                                self.esta_productos.append(j[0])
                                self.esta_productos_cantidad.append([j[0],j[2]])
                    #hacer top
                    top1 = ['',0]
                    top2 = ['',0]
                    top3 = ['',0]
                    for i in self.esta_productos_cantidad:
                        if int(i[1])>top1[1]:
                            top1[0]=i[0]
                            top1[1]=int(i[1])
                    top1[1]=str(top1[1])
                    self.esta_productos_cantidad.remove(top1)
                    for i in self.esta_productos_cantidad:
                        if int(i[1])>top2[1]:
                            top2[0]=i[0]
                            top2[1]=int(i[1])
                    top2[1]=str(top2[1])
                    self.esta_productos_cantidad.remove(top2)
                    for i in self.esta_productos_cantidad:
                        if int(i[1])>top3[1]:
                            top3[0]=i[0]
                            top3[1]=int(i[1])
                    top3[1]=str(top3[1])
                    self.esta_productos_cantidad.remove(top3)
                    print(f'El producto mas enviado es: {top1[0]} con {top1[1]} unidades')
                    print(f'El producto mas enviado es: {top2[0]} con {top2[1]} unidades')
                    print(f'El producto mas enviado es: {top3[0]} con {top3[1]} unidades')
        else:
          print("Gracias por visitarnos, nos vemos pronto <3")
          break
            
    
