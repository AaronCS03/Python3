Cálculo de Sueldo Neto en República Dominicana (Python)

Este proyecto en Python permite calcular el sueldo neto mensual de un empleado en República Dominicana, aplicando los descuentos oficiales por Seguridad Social (TSS), Retención del Impuesto Sobre la Renta (ISR), Bonificación, y otros descuentos personalizados.



Objetivo

Aplicar los conceptos de programación en Python y conocimientos sobre el sistema tributario y de seguridad social dominicano para determinar el sueldo neto de un empleado.



Fórmulas y Normativa Aplicada

Seguridad Social (TSS)
- **Porcentaje:** 5.91% del sueldo bruto mensual.

ISR (Impuesto Sobre la Renta) — Tramos 2024 según la DGII
- **Sueldo anual ≤ RD$416,220:** Exento.
- **RD$416,220.01 – RD$624,329.00:** 15% del excedente.
- **RD$624,329.01 – RD$867,123.00:** 20% del excedente + RD$31,216.
- **Mayor a RD$867,123.00:** 25% del excedente + RD$79,792.
- **ISR mensual = ISR anual ÷ 12**

Bonificación
Porcentaje: 0.83% del sueldo bruto mensual.

Otros Descuentos
- Valor personalizado ingresado por el usuario.



🖥️ Uso del Programa

📥 Entradas:
- Sueldo bruto mensual.
- Otros descuentos (en RD$).

📤 Salidas:
- Sueldo Bruto.
- Descuento por TSS.
- Retención mensual de ISR.
- Bonificación.
- Otros descuentos.
- Sueldo Neto.

---

▶️ Ejecución

1. Asegúrate de tener Python 3 instalado.
2. Ejecuta el archivo `.py`:

```bash
