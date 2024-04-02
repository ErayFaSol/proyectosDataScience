# Datos proporcionados
ingresos_totales = 604000
coste_bienes_vendidos = 34500
gastos_operativos = 63201 + 32945
impuestos = 0.06
prestamos = 230550
inversion = 10000000

print(gastos_operativos)

# Cálculo del beneficio bruto
beneficio_bruto = ingresos_totales - coste_bienes_vendidos
print("Beneficio operativo: ", beneficio_bruto)

# Cálculo del margen de beneficio bruto
margen_beneficio_bruto = (beneficio_bruto / ingresos_totales) * 100
print("Margen de beneficio bruto: ", margen_beneficio_bruto)

# Cálculo del beneficio operativo
beneficio_operativo = beneficio_bruto - gastos_operativos
print("beneficio operativo: ", beneficio_operativo)

# Cálculo de margen de beneficio operativo
margen_beneficio_operativo = (beneficio_operativo / ingresos_totales) * 100
print("Margen beneficio operativo: ",margen_beneficio_operativo)

# Cálculo Beneficio neto
beneficio_neto = beneficio_operativo - (ingresos_totales * impuestos) - prestamos
print("Beneficio neto: ",beneficio_neto)

# Cálculo sobre la inversion
beneficio_neto = 25000000
roi = (beneficio_neto - inversion) / inversion

print(roi)