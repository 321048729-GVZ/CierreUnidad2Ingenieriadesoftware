# Cierre de Unidad 2 — Proyecto Kiro Market

**Sistema:** Sistema de registro de ventas para negocios minoristas.
**Integrantes:** González Vargas Alfredo Zenif
**Fecha:** 21 de septiembre de 2026

## 2.4 Propuesta de desarrollo

- **Alcance (qué incluye):** Un módulo de registro de ventas y compras diarias, un módulo de gestión del inventario y la generación de informes ejecutivos automatizados por intervalos de tiempo. Todo operado mediante una web sencilla, intuitiva y clara, respaldada por una API REST y arquitectura monolítica modular para el servidor.
- **Fuera de alcance (qué NO incluye):** La capacidad para gestionar o sincronizar múltiples empresas y/o sucursales en esta versión. Tampoco incluye módulo de facturación electrónica, registro fiscal avanzado, ni infraestructura de servidores propios de la empresa.
- **Restricciones (tiempo, tecnología, tamaño del equipo):** El desarrollo está restringido al calendario del semestre actual (Unidad 2). El equipo consta de un único desarrollador asumiendo los roles de diseño, construcción y mantenimiento. La tecnología está limitada a herramientas de software libre (como SQLite y JavaScript/Python) para el entorno local.
- **Viabilidad en una frase:** Es un proyecto altamente viable dado que el alcance técnico está acotado a las operaciones esenciales de una sola sucursal y será desarrollado por un ingeniero con conocimiento directo de las necesidades operativas del negocio.

## 2.5 Especificación funcional (mínimo 5 funciones)

| # | Función | Qué hace |
|---|---|---|
| 1 | **Registro rápido de ventas** | Permite escanear códigos de barras (ej. "457190") o buscar artículos manualmente para agregarlos a un ticket en pantalla y calcular el total a cobrar de forma instantánea. |
| 2 | **Actualización de inventario en tiempo real** | Descuenta automáticamente las unidades vendidas del stock disponible tras confirmar una venta, y suma unidades al registrar compras a los proveedores. |
| 3 | **Cálculo de márgenes de ganancia** | Compara el costo de adquisición de cada producto contra su precio de venta al público para proyectar la utilidad neta de cada transacción. |
| 4 | **Generación de informes ejecutivos** | Consolida las transacciones en un periodo definido para mostrar los indicadores clave del negocio (ingresos, productos más vendidos) a los dueños, facilitando la toma de decisiones. |
| 5 | **Emisión de comprobantes** | Genera un recibo o ticket final con el desglose exacto de los artículos adquiridos, precios individuales y el total pagado por el cliente. |

## 2.6 Entorno de desarrollo justificado

- **Evidencia técnica:** enlace al commit [Link al commit](https://github.com/321048729-GVZ/CierreUnidad2Ingenieriadesoftware/blob/main/prototipo_entorno.py)
- **Costo:** Nulo durante la fase de desarrollo. Se utilizan bases de datos locales (SQLite) y lenguajes de programación de código abierto sin requerir licenciamiento comercial.
- **Curva de aprendizaje:** Moderada. Requiere la integración estructurada de bases de datos relacionales, lógica de servidor (API) y diseño de interfaz frontend, conceptos que se dominan progresivamente durante el ciclo escolar.
- **Soporte / documentación disponible:** Extensa y de alta calidad. Al utilizar arquitecturas estándar (API REST) y bases de datos consolidadas, existe una vasta cantidad de foros técnicos, documentación oficial y herramientas de depuración.

## Declaración de uso de IA

| Herramienta | Para qué la usaron | Qué verificaron |
|---|---|---|
| Gemini | Asistente ejecutivo de redacción para estructurar el formato Markdown del documento de Cierre de Unidad 2. | Se verificó que la propuesta de desarrollo y el alcance coincidan estrictamente con el documento de Visión del sistema (Plantilla E1) previamente definido. |
|Gemini | Revisar un problema al momento de ejecución del python  | Faltaba escribir una letra para corregir el problema