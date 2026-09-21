# Cierre de Unidad 2 — Ejercicio de laboratorio

**Ingeniería de Software · Grupo 1359 / 1359A · Ciclo 2027-1**
**Sesión:** Lunes 21 de septiembre · 18:00–19:30 · A9-923

## Cómo usar este repositorio

1. Hagan **fork** de este repositorio (a la organización de GitHub del curso o a la cuenta de su equipo).
2. Abran su fork en **GitHub Codespaces**.
3. Resuelvan las cuatro partes en orden — cada una trae las instrucciones completas, no necesitan nada más para avanzar.
4. Completen los espacios marcados `# COMPLETAR` en `prototipo_entorno.py` con información real de su sistema.
5. Completen `docs/cierre_unidad2.md` con datos reales de su sistema (nada genérico).
6. Hagan `git commit` y `git push` antes de que termine la sesión.

Todo lo que produzcan aquí lo usan directamente para redactar **E2** (documento de especificación funcional y entorno de desarrollo justificado) — nada de este ejercicio se tira.

---

## Parte A — Verificación del entorno (10 min)

En la terminal de su Codespace, corran:

```bash
python3 --version
python3 -c "import sqlite3; print(sqlite3.sqlite_version)"
```

Ambos comandos deben correr sin error. Si algo falla, avisen al profesor antes de seguir — no avancen a la Parte B con un entorno roto.

## Parte B — Prototipo mínimo con su propio caso (30 min)

Esto **no** es su modelo entidad/relación final (eso se formaliza en la Unidad 5). Es una prueba de que su entorno puede manejar el tipo de dato central de su sistema.

1. Elijan un solo objeto central de su sistema (el libro en una biblioteca, el objeto perdido en un sistema de objetos extraviados, el producto en un catálogo, etc.).
2. Abran `prototipo_entorno.py` y completen cada `# COMPLETAR` con información real de su sistema — no dejen texto de ejemplo.
3. Ejecuten:
   ```bash
   python3 prototipo_entorno.py
   ```
4. Confirmen que ambas consultas (todos los registros, y la consulta filtrada) muestran resultados coherentes con lo que escribieron.

## Parte C — Documentación (30 min)

Abran `docs/cierre_unidad2.md` y completen las tres secciones (2.4, 2.5 y 2.6) con datos reales de su sistema.

## Parte D — Revisión cruzada y cierre (10 min)

Intercambien `docs/cierre_unidad2.md` con otro equipo (por pantalla, no hace falta imprimir). Revisen:

- [ ] Las 5 funciones de 2.5 corresponden a algo real del sistema, no genérico.
- [ ] 2.6 cita el commit de la Parte A/B como evidencia, no solo lo afirma.

## Entrega

```bash
git add prototipo_entorno.py docs/cierre_unidad2.md
git commit -m "Cierre Unidad 2: entorno, prototipo y especificación funcional"
git push
```

Suban el enlace a su fork y las capturas pedidas al documento de evidencia en Classroom.

---

## Declaración de uso de IA

Pueden usar IA en este ejercicio, declarándolo en `docs/cierre_unidad2.md`. Son responsables de todo lo que entregan — si no pueden explicarlo, no lo entregaron ustedes.
