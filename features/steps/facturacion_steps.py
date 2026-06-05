from behave import then, when

from parkinguv.billing import calculate_fee


@when("calculo la tarifa para {minutes:d} minutos de un cliente {customer_type}")
def step_calculate_fee(context, minutes, customer_type):
    context.total = calculate_fee(minutes, vip=(customer_type.upper() == "VIP"))


@then("el total a pagar debe ser {expected:d} pesos")
def step_total_should_be(context, expected):
    assert context.total == expected
