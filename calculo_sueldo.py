# Constantes oficiales para 2024 en RD
PORC_TSS = 0.0591           # 5.91% de seguridad social
PORC_BONIFICACION = 0.0083  # 0.83% de bonificación

# Tramos de ISR anual según DGII (2024)
TRAMO_1 = 0
TRAMO_2 = 416220.00
TRAMO_3 = 624329.00
TRAMO_4 = 867123.00

# Tasa y deducción fija por tramo
TASA_2 = 0.15
TASA_3 = 0.20
TASA_4 = 0.25

DEDUCCION_3 = 31216.00
DEDUCCION_4 = 79792.00

# Entrada de datos
try:
    sueldo_bruto_mensual = float(input("Ingrese el sueldo bruto mensual del empleado (RD$): "))
    otros_descuentos = float(input("Ingrese otros descuentos (RD$): "))

    # Validación
    if sueldo_bruto_mensual <= 0:
        print("Error: El sueldo bruto debe ser mayor a 0.")
    elif otros_descuentos < 0:
        print("Error: Los otros descuentos no pueden ser negativos.")
    else:
        # 1. Calcular TSS mensual
        descuento_tss = sueldo_bruto_mensual * PORC_TSS

        # 2. Calcular ISR anual
        sueldo_anual = sueldo_bruto_mensual * 12

        if sueldo_anual <= TRAMO_2:
            isr_anual = 0
        elif sueldo_anual <= TRAMO_3:
            exceso = sueldo_anual - TRAMO_2
            isr_anual = exceso * TASA_2
        elif sueldo_anual <= TRAMO_4:
            exceso = sueldo_anual - TRAMO_3
            isr_anual = (exceso * TASA_3) + DEDUCCION_3
        else:
            exceso = sueldo_anual - TRAMO_4
            isr_anual = (exceso * TASA_4) + DEDUCCION_4

        # 3. ISR mensual
        retencion_isr_mensual = isr_anual / 12

        # 4. Bonificación
        bonificacion = sueldo_bruto_mensual * PORC_BONIFICACION

        # 5. Sueldo neto
        sueldo_neto = sueldo_bruto_mensual - descuento_tss - retencion_isr_mensual - otros_descuentos + bonificacion

        # Resultados
        print("\n=== DETALLE DE CÁLCULO ===")
        print(f"Sueldo Bruto: RD${sueldo_bruto_mensual:,.2f}")
        print(f"Descuento TSS (5.91%): RD${descuento_tss:,.2f}")
        print(f"Retención ISR mensual (cálculo anual / 12): RD${retencion_isr_mensual:,.2f}")
        print(f"Otros Descuentos: RD${otros_descuentos:,.2f}")
        print(f"Bonificación (0.83%): RD${bonificacion:,.2f}")
        print(f"Sueldo Neto: RD${sueldo_neto:,.2f}")

except ValueError:
    print("Error: Ingrese un valor numérico válido.")
