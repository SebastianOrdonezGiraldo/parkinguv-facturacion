# Tabla de casos de prueba

Los casos combinan particion de equivalencia y analisis de valores limite sobre las reglas principales del cobro.

| ID | Regla | Tecnica | Entrada | Tipo cliente | Resultado esperado | Justificacion |
| --- | --- | --- | ---: | --- | ---: | --- |
| TC-01 | Primeros 30 minutos gratis | Valor limite inferior | 0 min | Normal | $0 | Inicio valido de una estadia |
| TC-02 | Primeros 30 minutos gratis | Valor limite superior | 30 min | Normal | $0 | Ultimo minuto gratuito |
| TC-03 | Cobro desde minuto 31 | Valor limite | 31 min | Normal | $500 | Primer minuto cobrado |
| TC-04 | Hora o fraccion | Particion valida | 90 min | Normal | $500 | Una hora exacta despues de la gracia |
| TC-05 | Hora o fraccion | Valor limite | 91 min | Normal | $1.000 | Primera fraccion de la segunda hora |
| TC-06 | Tope diario | Valor limite | 1440 min | Normal | $12.000 | Maximo de un bloque de 24 horas |
| TC-07 | Tope por dias | Particion valida | 1471 min | Normal | $12.500 | Un dia completo mas una fraccion adicional |
| TC-08 | Descuento VIP | Particion valida | 91 min | VIP | $800 | 20% sobre $1.000 |
| TC-09 | VIP antes del tope | Valor limite | 1440 min | VIP | $9.600 | 20% aplicado sobre el total diario |
| TC-10 | Entrada invalida | Particion invalida | -1 min | Normal | Error | No existen estadias negativas |
