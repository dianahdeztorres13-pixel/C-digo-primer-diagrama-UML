from models import *
from datetime import datetime

usu1=Usuario(1,"Guadalupe","lupe@mail.com","2849802")
usu2=Usuario(2,"Luis","luis@mail.com","8339913")
usu3=Usuario(3,"Carla","carla@mail.com","1837492")
usu4=Usuario(4,"Diego","diego@mail.com","0237851")
usu5=Usuario(5,"Leonel","leonel@mail.com","8734108")
usu6=Usuario(6,"Ian","Ian@mail.com","6129456")
usu7=Usuario(7,"Laura","laura@mail.com","8875150")
usu8=Usuario(8,"Pedro","pedro@mail.com","1930987")
usu9=Usuario(9,"Angel","angel@mail.com","8862723")
usu10=Usuario(10,"Carlos","carlos@mail.com","2827228")

print("Usuarios creados:")
print(usu1.nombre)
print(usu2.nombre)
print(usu3.nombre)
print(usu4.nombre)
print(usu5.nombre)
print(usu6.nombre)
print(usu7.nombre)
print(usu8.nombre)
print(usu9.nombre)
print(usu10.nombre)

peli1=Pelicula("Matrix",130,"B","Accion")
peli2=Pelicula("Titanic",195,"B","Drama")
peli3=Pelicula("Avengers",140,"B","Accion")
peli4=Pelicula("Mario Bros",100,"A","Animacion")
peli5=Pelicula("Batman",120,"B","Accion")
peli6=Pelicula("Joker",122,"C","Drama")
peli7=Pelicula("Coco",105,"A","Animacion")
peli8=Pelicula("Spiderman",115,"B","Accion")
peli9=Pelicula("Interstellar",169,"B","Ciencia Ficcion")
peli10=Pelicula("Avatar",160,"B","Fantasia")

print("Peliculas creadas:")
print(peli1.titulo)
print(peli2.titulo)
print(peli3.titulo)
print(peli4.titulo)
print(peli5.titulo)
print(peli6.titulo)
print(peli7.titulo)
print(peli8.titulo)
print(peli9.titulo)
print(peli10.titulo)

sa1=Sala(1,"Sala 1","Planta baja","2D",50,False)
sa2=Sala(2,"Sala 2","Planta baja","3D",50,False)
sa3=Sala(3,"Sala 3","Primer piso","IMAX",60,True)
sa4=Sala(4,"Sala 4","Primer piso","2D",50,False)
sa5=Sala(5,"Sala 5","Primer piso","3D",50,False)
sa6=Sala(6,"Sala 6","Segundo piso","2D",40,False)
sa7=Sala(7,"Sala 7","Segundo piso","IMAX",60,True)
sa8=Sala(8,"Sala 8","Segundo piso","2D",40,False)
sa9=Sala(9,"Sala 9","Segundo piso","3D",40,False)
sa10=Sala(10,"Sala 10","VIP","IMAX",30,True)

print("Salas creadas:")
print(sa1.nombre)
print(sa2.nombre)
print(sa3.nombre)
print(sa4.nombre)
print(sa5.nombre)
print(sa6.nombre)
print(sa7.nombre)
print(sa8.nombre)
print(sa9.nombre)
print(sa10.nombre)

funcion1 = Funcion(1,peli1,sa1,"18:00",80)

print("Funcion creada:")
funcion1.DetallesFuncion()

asientos = ["A1","A2","A3"]

reserva1 = Reserva(1,usu1,funcion1,asientos)

print("Reserva creada")
print("Usuario:",reserva1.usuario.nombre)
print("Asientos:",reserva1.asientos)
print("Monto:",reserva1.montoTotal)

promo1 = Promocion("DESC20","20% descuento",0.20,datetime(2026,12,31).date())

print("Aplicando promocion...")
reserva1.aplicarPromocion(promo1)

print("Nuevo monto:",reserva1.montoTotal)

reserva1.confirmarPago()
reserva1.generarTicket()

print("Probando limpieza de sala")
sa1.limpiarEspacio()