from datetime import datetime

class Persona:
    def __init__(self, idPersona, nombre, email, telefono):
        self.idPersona=idPersona
        self.nombre=nombre
        self.email=email
        self.telefono=telefono

    def login(self):
        print(self.nombre, "Se inicio sesión")

    def logout(self):
        print(self.nombre, "Se cerró sesión")

    def actualizarDatos(self, email, telefono):
        self.email=email
        self.telefono=telefono

class Usuario(Persona):

    def __init__(self, idPersona, nombre, email, telefono):
        super().__init__(idPersona, nombre, email, telefono)
        self.puntosFidelidad=0
        self.historialReservas=[]

    def crearReserva(self, reserva):
        self.historialReservas.append(reserva)

    def Promociones(self):
        print("Promociones disponibles...")

    def cancelarReserva(self, reserva):
        reserva.estado = "CANCELADA"
        print("Reserva cancelada")

class Empleado(Persona):

    def __init__(self, idPersona, nombre, email, telefono, idEmpleado, rol, horario):
        super().__init__(idPersona, nombre, email, telefono)
        self.idEmpleado=idEmpleado
        self.rol=rol
        self.horario=horario

    def marcarEntrada(self):
        print(self.nombre, "marcó entrada")

    def gestionarFunciones(self):
        if self.rol=="ADMIN":
            print("Gestionando funciones...")
        else:
            print("No tienes permiso")

class Espacio:

    def __init__(self, idEspacio, nombre, ubicacion):
        self.idEspacio=idEspacio
        self.nombre=nombre
        self.ubicacion=ubicacion

    def Disponibilidad(self):
        print("Espacio disponible")

    def limpiarEspacio(self):
        print("Limpiando espacio...")

class Sala(Espacio):

    def __init__(self, idEspacio, nombre, ubicacion, tipo, capacidadTotal, esVip):
        super().__init__(idEspacio, nombre, ubicacion)
        self.tipo=tipo
        self.capacidadTotal=capacidadTotal
        self.esVip=esVip

    def ajustarAforo(self, nuevoAforo):
        self.capacidadTotal=nuevoAforo

    def obtenerTipoSala(self):
        return self.tipo

class ZonaComida(Espacio):

    def __init__(self, idEspacio, nombre, ubicacion):
        super().__init__(idEspacio, nombre, ubicacion)
        self.listaProductos=[]
        self.stockActual={}

    def venderProducto(self, producto):
        if producto in self.stockActual and self.stockActual[producto] > 0:
            self.stockActual[producto]-=1
            print("Producto vendido")
        else:
            print("No hay stock")

    def actualizarInventario(self, producto, cantidad):
        self.stockActual[producto]=cantidad

class Pelicula:

    def __init__(self, titulo, duracion, clasificacion, genero):
        self.titulo=titulo
        self.duracion=duracion
        self.clasificacion=clasificacion
        self.genero=genero

    def Sinopsis(self):
        print("Sinopsis de", self.titulo)

    def esAptaParaTodoPublico(self):
        return self.clasificacion=="A"

class Funcion:

    def __init__(self, idFuncion, pelicula, sala, horarioInicio, precioBase):
        self.idFuncion=idFuncion
        self.pelicula=pelicula
        self.sala=sala
        self.horarioInicio=horarioInicio
        self.precioBase=precioBase
        self.asientosOcupados=[]

    def AsientosLibres(self):
        return self.sala.capacidadTotal - len(self.asientosOcupados)

    def DetallesFuncion(self):
        print(self.pelicula.titulo, "-", self.horarioInicio)

class Promocion:

    def __init__(self, codigo, descripcion, porcentajeDescuento, fechaExpiracion):
        self.codigo=codigo
        self.descripcion=descripcion
        self.porcentajeDescuento=porcentajeDescuento
        self.fechaExpiracion=fechaExpiracion

    def esValida(self, usuario):
        hoy=datetime.now().date()
        return hoy <= self.fechaExpiracion

    def aplicarDescuento(self, monto):
        return monto - (monto * self.porcentajeDescuento) 
      
class Reserva:

    def __init__(self, idReserva, usuario, funcion, asientos):
        self.idReserva=idReserva
        self.usuario=usuario
        self.funcion=funcion
        self.asientos=asientos
        self.estado="PENDIENTE"
        self.montoTotal=len(asientos) * funcion.precioBase

    def confirmarPago(self):
        self.estado="PAGADA"
        print("Pago confirmado")

    def generarTicket(self):
        print("Ticket generado para", self.usuario.nombre)

    def aplicarPromocion(self, promo):
        if promo.esValida(self.usuario):
            self.montoTotal = promo.aplicarDescuento(self.montoTotal)