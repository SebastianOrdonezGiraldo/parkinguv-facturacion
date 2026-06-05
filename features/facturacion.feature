# language: es
Característica: Facturacion de parqueadero ParkingUV
  Como gerente de ParkingUV
  Quiero calcular el valor de una estadia
  Para cobrar de forma consistente a clientes normales y VIP

  Escenario: Primeros 30 minutos gratis
    Cuando calculo la tarifa para 30 minutos de un cliente normal
    Entonces el total a pagar debe ser 0 pesos

  Escenario: Cobro por hora o fraccion desde el minuto 31
    Cuando calculo la tarifa para 91 minutos de un cliente normal
    Entonces el total a pagar debe ser 1000 pesos

  Escenario: Descuento VIP antes del tope diario
    Cuando calculo la tarifa para 1440 minutos de un cliente VIP
    Entonces el total a pagar debe ser 9600 pesos
