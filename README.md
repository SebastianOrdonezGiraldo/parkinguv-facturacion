# ParkingUV Facturacion

Modulo sencillo de facturacion para parqueaderos ParkingUV S.A.S.

## Reglas implementadas

- Los primeros 30 minutos son gratis.
- Desde el minuto 31 se cobra $500 por cada hora o fraccion.
- El maximo por cada bloque de 24 horas es $12.000.
- Clientes VIP reciben 20% de descuento sobre el total calculado.
- Duraciones negativas se rechazan como entrada invalida.

## Instalacion local

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

En Linux o macOS:

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Ejecutar pruebas

Unitarias:

```bash
pytest
```

BDD con Gherkin:

```bash
behave
```

Seguridad basica:

```bash
bandit -r parkinguv
```

API local:

```bash
uvicorn parkinguv.api:app --reload
```

Ejemplo:

```bash
curl "http://127.0.0.1:8000/calculate?minutes=91&vip=true"
```

Rendimiento con Locust:

```bash
uvicorn parkinguv.api:app --host 127.0.0.1 --port 8000
locust --headless --users 20 --spawn-rate 10 --run-time 15s --host http://127.0.0.1:8000
```

El script falla si el P95 supera 300 ms.

## Evidencia TDD y calidad

El historial contiene commits separados para tests rojos, implementaciones verdes, refactor, BDD, tabla de casos, Locust y pipeline.

La tabla de particion de equivalencia y valores limite esta en `docs/test-cases.md`.

GitHub Actions ejecuta unitarias, BDD y Bandit en cada push y pull request. La prueba de rendimiento se ejecuta solo en la rama `main`.
