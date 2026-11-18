# Criptografía cuántica

Plenaria de **Mecánica Cuántica 2026-II** · Universidad Distrital Francisco José de Caldas
**Camila Pérez y Sergio Carrasquilla** · Profesor: John Díaz · Noviembre de 2026

De la escítala espartana a la distribución cuántica de claves. La charla recorre la historia de los cifrados (César, Al-Kindi, Vigenère, Vernam, Enigma, clave pública), muestra por qué la mecánica cuántica permite repartir una clave y detectar a quien la espía (teorema de no clonación, protocolo BB84, umbral del 11 %), lo comprueba con simulaciones propias y termina con el entrelazamiento (E91, desigualdad de Bell) y los equipos reales: satélites, ataques a detectores y criptografía poscuántica.

Aquí está todo el material: la presentación, las figuras interactivas como herramientas sueltas, el código de las simulaciones, los documentos de apoyo y la bibliografía.

---

## Ver en línea

| Material | Enlace |
|---|---|
| Presentación | [plenaria-criptografia-cuantica.html](https://sacarrasquillah042.github.io/Quantum-Cryptography/presentacion/plenaria-criptografia-cuantica.html) |
| Cifrado César | [cesar.html](https://sacarrasquillah042.github.io/Quantum-Cryptography/herramientas/cesar.html) |
| Máquina Enigma | [enigma.html](https://sacarrasquillah042.github.io/Quantum-Cryptography/herramientas/enigma.html) |
| Protocolo BB84 | [bb84.html](https://sacarrasquillah042.github.io/Quantum-Cryptography/herramientas/bb84.html) |
| BB84 con una espía | [bb84-espia.html](https://sacarrasquillah042.github.io/Quantum-Cryptography/herramientas/bb84-espia.html) |
| E91 y la prueba de Bell | [e91-bell.html](https://sacarrasquillah042.github.io/Quantum-Cryptography/herramientas/e91-bell.html) |

También se pueden descargar y abrir con doble clic: cada HTML es un solo archivo que funciona sin internet.

---

## Contenido

```
Quantum-Cryptography/
├── presentacion/
│   └── plenaria-criptografia-cuantica.html   presentación completa (39 diapositivas)
├── herramientas/
│   ├── cesar.html          cifrar y descifrar con César; romperlo con χ²
│   ├── enigma.html         cifrar con una Enigma I (rotores I-II-III, reflector B)
│   ├── bb84.html           banco óptico de BB84
│   ├── bb84-espia.html     BB84 con ataque intercepta y reenvía
│   └── e91-bell.html       pares entrelazados y desigualdad CHSH
├── simulaciones/
│   ├── simulaciones.py     frecuencias, Monte Carlo de BB84, tasa de clave
│   ├── idiomas.py          frecuencias y χ² en cinco idiomas
│   ├── datos_*.json        resultados que generan los dos programas
│   └── fig_*.png           gráficas de los resultados
├── documentos/
│   ├── teoria_criptografia_cuantica.pdf   la teoría explicada desde cero (y su .tex)
│   └── guion_plenaria.pdf                 guion por diapositiva (y su .tex)
├── BIBLIOGRAFIA.md            42 referencias con enlaces
└── descargar_bibliografia.py  descarga los PDF de libre acceso
```

---

## La presentación

Abrir `presentacion/plenaria-criptografia-cuantica.html` en Chrome, Edge o Firefox. Todo va dentro del archivo (fórmulas, figuras, código QR); solo el video de la diapositiva 32 necesita internet.

| Tecla | Acción |
|---|---|
| `→` `Espacio` `Enter` | siguiente diapositiva |
| `←` `Retroceso` | diapositiva anterior |
| `Inicio` `Fin` | primera y última |
| `F` | pantalla completa |

Para ensayar, abrir el archivo con `?ensayo` al final de la dirección: `N` muestra u oculta las notas del orador y `T` reinicia el cronómetro.

Las figuras se manejan con el ratón o, después de hacer clic en ellas, con el teclado (cada figura indica sus teclas abajo). Las flechas siguen pasando diapositivas aunque el foco esté en una figura.

| Parte | Diapositivas | Minutos |
|---|---|---|
| Gancho e historia I: de la escítala a Kerckhoffs | 1–8 | 0–9 |
| Historia II: de Vernam a la clave pública | 9–17 | 9–14 |
| Formalismo: qubit, regla de Born, no clonación, BB84 | 18–24 | 14–27 |
| La espía y el umbral del 11 % | 25–28 | 27–37 |
| Simulación | 29–30 | 37–44 |
| Entrelazamiento, video y mundo real | 31–36 | 44–55 |
| Cierre y preguntas | 37–39 | 55–60 |

---

## Herramientas interactivas

Cada una tiene la figura de la presentación y un panel para escribir y controlarla. Sirven también en el celular.

- **César.** Se escribe cualquier texto, se elige la clave `k` y gira el disco. Abajo, el ataque por análisis de frecuencias: prueba las 26 claves, calcula χ² contra cinco idiomas y adivina la clave y el idioma.
- **Enigma.** Se elige la posición inicial de los rotores y se escribe el mensaje, en el panel o con el teclado de la máquina; se ilumina el camino de la corriente. Con la misma posición inicial, el texto cifrado devuelve el original.
- **BB84.** Se lanzan fotones uno a uno o en ráfagas; se ve la regla de Born, el cribado y la clave que van formando Alice y Bob. Con esa clave se cifra un mensaje propio (Vernam).
- **BB84 con una espía.** Igual, con Eve en la fibra: el QBER sube a cerca del 25 % y Bob lee el mensaje con caracteres equivocados.
- **E91 y Bell.** Cuatro perillas fijan los ángulos; las ráfagas de pares miden `S` de CHSH. Con los ángulos óptimos, `S` pasa de la cota clásica 2 y se acerca a 2√2.

---

## Simulaciones

Requieren Python 3 con `numpy` y `matplotlib`.

```bash
pip install numpy matplotlib
cd simulaciones
python3 simulaciones.py
python3 idiomas.py
```

`simulaciones.py` lee `quijote.txt` y, si no está, lo descarga una vez. `idiomas.py` descarga los diez libros que usa a la carpeta `corpus/`. Ningún resultado está escrito a mano: todo sale de los textos o del sorteo con semilla fija.

**Resultados**

| Simulación | Resultado |
|---|---|
| Frecuencias del español | Don Quijote, 1 640 824 letras. Más frecuentes: E 14,0 %, A 12,2 %, O 9,9 %, S 7,7 % |
| Romper César con χ² | mensaje de 409 letras cifrado con k = 3: el mínimo de χ² está en s = 3 |
| BB84, intercepta y reenvía | 11 valores de la fracción interceptada f, 200 000 fotones cada uno: el QBER sigue Q = f/4; con f = 1, Q = 24,92 % ± 0,11 % (teoría 25 %) |
| Umbral de seguridad | la tasa r = 1 − 2h(Q) se anula en Q = 11,003 % (bisección) |
| Cinco idiomas | letra más frecuente: E en español, inglés, francés y alemán; A en portugués. Con 400 letras, el par (idioma, clave) con menor χ² acierta el idioma entre el 96 y el 100 % de las veces y la clave entre el 99 y el 100 % |

---

## Bibliografía

[`BIBLIOGRAFIA.md`](BIBLIOGRAFIA.md) tiene 42 referencias ordenadas como la presentación, con su DOI y, cuando existe, un enlace de descarga libre (arXiv, NIST, repositorios universitarios).

Para descargar de una vez los 24 PDF de libre acceso:

```bash
python3 descargar_bibliografia.py
```

Quedan en la carpeta `pdf/`, numerados como en la bibliografía. Esa carpeta no se sube al repositorio, porque cada artículo tiene su propia licencia.

---

## Créditos

- Textos para las frecuencias: [Proyecto Gutenberg](https://www.gutenberg.org), dominio público.
- Video de la diapositiva 32: [Centre for Quantum Technologies, Singapur](https://www.youtube.com/watch?v=LaLzshIosDk).
- Fórmulas con [KaTeX](https://katex.org) y código QR con [qrcode-generator](https://github.com/kazuhikoarase/qrcode-generator), ambos con licencia MIT e incluidos dentro del HTML.
- Las figuras, las herramientas y las simulaciones son propias.
