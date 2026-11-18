#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Simulaciones de la plenaria "Criptografia cuantica"
Mecanica Cuantica 2026-II, Universidad Distrital Francisco Jose de Caldas
Camila Perez y Sergio Carrasquilla

Genera tres resultados, todos calculados (ningun dato esta escrito a mano):

  1. Analisis de frecuencias (Al-Kindi): frecuencias de letras del espanol
     medidas sobre un corpus de dominio publico (Don Quijote, Proyecto
     Gutenberg), frecuencias de un texto cifrado con Cesar y recuperacion
     de la clave k minimizando chi^2.
  2. BB84 con ataque intercepta-reenvia (Monte Carlo): QBER de la clave
     cribada en funcion de la fraccion f de fotones interceptados,
     comparado con la prediccion Q = f/4.
  3. Tasa de clave asintotica r(Q) = 1 - 2 h(Q) (Shor-Preskill) y su
     umbral r = 0, hallado numericamente por biseccion.

Uso:
    python3 simulaciones.py

Salidas (en la misma carpeta):
    datos_simulaciones.json   datos que usa el deck HTML
    fig_frecuencias.png, fig_qber.png, fig_tasa.png

Requiere: numpy, matplotlib. El corpus se lee de quijote.txt; si no esta,
se descarga una vez.
"""
import json
import os
import unicodedata
import urllib.request

import numpy as np

AQUI = os.path.dirname(os.path.abspath(__file__))
SEMILLA = 20261112
ALFABETO = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# --------------------------------------------------------------------------
# 1. Analisis de frecuencias
# --------------------------------------------------------------------------
CORPUS = os.path.join(AQUI, "quijote.txt")
CORPUS_URLS = [
    "https://www.gutenberg.org/cache/epub/2000/pg2000.txt",
    "https://raw.githubusercontent.com/GITenberg/Don-Quijote_2000/master/2000-8.txt",
]

# Texto que se cifra. Es independiente del corpus de referencia, para que la
# comparacion de frecuencias no sea trivial.
MENSAJE = """
Durante siglos quien queria guardar un secreto cambiaba cada letra del
mensaje por otra, siempre la misma, y confiaba en que nadie adivinara la
regla. El metodo parece seguro porque hay muchisimas reglas posibles, pero
tiene una debilidad que no depende de la regla elegida: cada idioma usa unas
letras mucho mas que otras, y esa huella sobrevive al cifrado. Basta contar
cuantas veces aparece cada simbolo y comparar con las frecuencias del idioma
para reconstruir el mensaje sin conocer la clave.
"""
K_SECRETA = 3


def normalizar(texto):
    """Mayusculas A-Z: quita tildes y dieresis, convierte la enie en N."""
    sin_marcas = unicodedata.normalize("NFD", texto.upper())
    return "".join(c for c in sin_marcas if c in ALFABETO)


def leer_corpus():
    if not os.path.exists(CORPUS):
        for url in CORPUS_URLS:
            try:
                datos = urllib.request.urlopen(url, timeout=60).read()
                with open(CORPUS, "wb") as archivo:
                    archivo.write(datos)
                break
            except Exception as error:  # se prueba la siguiente direccion
                print("no se pudo descargar", url, error)
    with open(CORPUS, "rb") as archivo:
        crudo = archivo.read()
    try:
        texto = crudo.decode("utf-8")
    except UnicodeDecodeError:
        texto = crudo.decode("latin-1")
    # Se descartan el encabezado y la licencia de Gutenberg (en ingles).
    inicio = texto.find("*** START")
    fin = texto.find("*** END")
    if inicio >= 0:
        texto = texto[texto.find("\n", inicio):]
    if fin >= 0:
        texto = texto[: fin - inicio] if inicio >= 0 else texto[:fin]
    return texto


def frecuencias(letras):
    cuenta = np.array([letras.count(c) for c in ALFABETO], dtype=float)
    return cuenta / cuenta.sum(), cuenta


def cesar(letras, k):
    """E_k(x) = (x + k) mod 26."""
    return "".join(ALFABETO[(ALFABETO.index(c) + k) % 26] for c in letras)


def analisis_de_frecuencias():
    referencia = normalizar(leer_corpus())
    f_ref, _ = frecuencias(referencia)

    claro = normalizar(MENSAJE)
    cifrado = cesar(claro, K_SECRETA)
    f_cif, n_cif = frecuencias(cifrado)
    n = len(cifrado)

    # Para cada corrimiento s se descifra y se compara con el espanol:
    # chi^2(s) = sum_x (O_x - E_x)^2 / E_x, con E_x = n * f_ref(x).
    chi2 = []
    for s in range(26):
        observado = np.roll(n_cif, -s)  # letra x del claro = letra x+s del cifrado
        esperado = n * f_ref
        chi2.append(float(((observado - esperado) ** 2 / esperado).sum()))
    k_hallada = int(np.argmin(chi2))

    return {
        "alfabeto": list(ALFABETO),
        "corpus": "Don Quijote (Proyecto Gutenberg, libro 2000)",
        "letras_corpus": len(referencia),
        "letras_cifrado": n,
        "k_secreta": K_SECRETA,
        "k_hallada": k_hallada,
        "frec_espanol": [round(float(v), 5) for v in f_ref],
        "frec_cifrado": [round(float(v), 5) for v in f_cif],
        "chi2": [round(v, 2) for v in chi2],
        "muestra_cifrado": cifrado[:60],
    }


# --------------------------------------------------------------------------
# 2. BB84 con intercepta-reenvia
# --------------------------------------------------------------------------
def bb84(n_fotones, f, rng):
    """Devuelve (bits cribados, errores) para una fraccion f interceptada.

    Bases: 0 = Z {|0>, |1>}, 1 = X {|+>, |->}. Medir un estado en su propia
    base da el bit con certeza; en la otra base, |<b|psi>|^2 = 1/2 (Born).
    """
    bit_a = rng.integers(0, 2, n_fotones)
    base_a = rng.integers(0, 2, n_fotones)

    # Estado que viaja por el canal: (base, bit). Sin Eve, el de Alice.
    base_canal = base_a.copy()
    bit_canal = bit_a.copy()

    eve = rng.random(n_fotones) < f
    base_e = rng.integers(0, 2, n_fotones)
    azar_e = rng.integers(0, 2, n_fotones)
    # Eve mide: acierta si usa la base de Alice; si no, resultado al azar.
    bit_e = np.where(base_e == base_a, bit_a, azar_e)
    # Reenvia el estado que encontro, en la base en que midio.
    base_canal = np.where(eve, base_e, base_canal)
    bit_canal = np.where(eve, bit_e, bit_canal)

    base_b = rng.integers(0, 2, n_fotones)
    azar_b = rng.integers(0, 2, n_fotones)
    bit_b = np.where(base_b == base_canal, bit_canal, azar_b)

    cribado = base_a == base_b
    errores = int((bit_a[cribado] != bit_b[cribado]).sum())
    return int(cribado.sum()), errores


def h(x):
    """Entropia binaria h(x) = -x log2 x - (1 - x) log2 (1 - x)."""
    x = np.clip(np.asarray(x, dtype=float), 1e-15, 1 - 1e-15)
    return -x * np.log2(x) - (1 - x) * np.log2(1 - x)


def tasa(q):
    """Tasa de clave asintotica por bit cribado, r = 1 - 2 h(Q)."""
    return 1 - 2 * h(q)


def monte_carlo_bb84(n_fotones=10000, repeticiones=20):
    """Para cada f se repite el experimento y se reporta la media del QBER y
    su error estandar empirico (desviacion entre repeticiones / sqrt(R))."""
    rng = np.random.default_rng(SEMILLA)
    filas = []
    for f in np.linspace(0, 1, 11):
        corridas = [bb84(n_fotones, f, rng) for _ in range(repeticiones)]
        q_i = np.array([e / n for n, e in corridas])
        q = float(q_i.mean())
        filas.append({
            "f": round(float(f), 2),
            "fotones": n_fotones * repeticiones,
            "repeticiones": repeticiones,
            "cribados": int(sum(n for n, _ in corridas)),
            "errores": int(sum(e for _, e in corridas)),
            "qber": round(q, 5),
            "error_estandar": round(float(q_i.std(ddof=1) / np.sqrt(repeticiones)), 5),
            "teoria": round(float(f) / 4, 5),
            "tasa": round(float(tasa(q)), 5),
        })
    return filas


# --------------------------------------------------------------------------
# 3. Umbral de la tasa de clave
# --------------------------------------------------------------------------
def umbral():
    """Resuelve 1 - 2 h(Q) = 0 en (0, 1/2) por biseccion."""
    a, b = 1e-6, 0.5
    for _ in range(80):
        m = 0.5 * (a + b)
        if tasa(m) > 0:
            a = m
        else:
            b = m
    return 0.5 * (a + b)


def curva_tasa():
    q = np.linspace(0, 0.25, 126)
    return {
        "q": [round(float(v), 4) for v in q],
        "r": [round(float(v), 5) for v in tasa(q)],
        "h": [round(float(v), 5) for v in h(q)],
        "umbral": round(float(umbral()), 5),
    }


# --------------------------------------------------------------------------
def graficas(datos):
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    plt.rcParams.update({"font.family": "sans-serif", "font.size": 11, "axes.spines.top": False, "axes.spines.right": False})

    fr = datos["frecuencias"]
    x = np.arange(26)
    fig, ax = plt.subplots(1, 2, figsize=(11, 3.8), gridspec_kw={"width_ratios": [2.2, 1]})
    ax[0].bar(x - 0.2, 100 * np.array(fr["frec_espanol"]), 0.4, label="espanol (corpus)", color="#888")
    ax[0].bar(x + 0.2, 100 * np.array(fr["frec_cifrado"]), 0.4, label="texto cifrado", color="#1f5fd0")
    ax[0].set_xticks(x, fr["alfabeto"])
    ax[0].set_ylabel("frecuencia (%)")
    ax[0].legend(frameon=False)
    ax[1].plot(range(26), fr["chi2"], "o-", color="#1f5fd0", ms=4)
    ax[1].set_xlabel("corrimiento s")
    ax[1].set_ylabel(r"$\chi^2(s)$")
    ax[1].set_yscale("log")
    fig.tight_layout()
    fig.savefig(os.path.join(AQUI, "fig_frecuencias.png"), dpi=200)

    mc = datos["bb84"]
    f = np.array([fila["f"] for fila in mc])
    q = np.array([fila["qber"] for fila in mc])
    s = np.array([fila["error_estandar"] for fila in mc])
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot([0, 1], [0, 25], "-", color="#888", label="teoria: Q = f/4")
    ax.errorbar(f, 100 * q, yerr=100 * 2 * s, fmt="o", color="#1f5fd0", capsize=3, label="Monte Carlo (barras: 2 sigma)")
    ax.axhline(100 * datos["tasa"]["umbral"], ls="--", color="#c0392b", lw=1)
    ax.set_xlabel("fraccion interceptada f")
    ax.set_ylabel("QBER (%)")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(AQUI, "fig_qber.png"), dpi=200)

    t = datos["tasa"]
    fig, ax = plt.subplots(figsize=(6, 4))
    ax.plot(100 * np.array(t["q"]), t["r"], "-", color="#888", label="r = 1 - 2h(Q)")
    ax.plot(100 * q, [fila["tasa"] for fila in mc], "o", color="#1f5fd0", label="Monte Carlo")
    ax.axhline(0, color="k", lw=0.6)
    ax.axvline(100 * t["umbral"], ls="--", color="#c0392b", lw=1)
    ax.set_xlabel("QBER (%)")
    ax.set_ylabel("tasa de clave r")
    ax.legend(frameon=False)
    fig.tight_layout()
    fig.savefig(os.path.join(AQUI, "fig_tasa.png"), dpi=200)


if __name__ == "__main__":
    datos = {
        "semilla": SEMILLA,
        "frecuencias": analisis_de_frecuencias(),
        "bb84": monte_carlo_bb84(),
        "tasa": curva_tasa(),
    }
    with open(os.path.join(AQUI, "datos_simulaciones.json"), "w", encoding="utf-8") as salida:
        json.dump(datos, salida, ensure_ascii=False, indent=1)
    graficas(datos)

    fr = datos["frecuencias"]
    print("corpus: %d letras; cifrado: %d letras" % (fr["letras_corpus"], fr["letras_cifrado"]))
    orden = np.argsort(fr["frec_espanol"])[::-1][:6]
    print("mas frecuentes en espanol:", ", ".join("%s %.1f%%" % (ALFABETO[i], 100 * fr["frec_espanol"][i]) for i in orden))
    print("k secreta = %d, k hallada = %d" % (fr["k_secreta"], fr["k_hallada"]))
    for fila in datos["bb84"]:
        print("f = %.1f  cribados = %5d  QBER = %5.2f%% +- %.2f%%  (f/4 = %5.2f%%)  r = %+.3f" % (
            fila["f"], fila["cribados"], 100 * fila["qber"], 100 * fila["error_estandar"], 100 * fila["teoria"], fila["tasa"]))
    print("umbral r = 0 en Q = %.3f%%" % (100 * datos["tasa"]["umbral"]))
