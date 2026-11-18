#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Analisis de frecuencias en cinco idiomas (complemento de la diapositiva 5).

Para cada idioma se usan dos libros de dominio publico (Proyecto Gutenberg):
uno de referencia, para medir las frecuencias del idioma, y otro distinto, de
donde se toman los textos de prueba que se cifran con Cesar.

Calcula:
  1. Las letras mas frecuentes de cada idioma.
  2. chi^2(s) para un texto cifrado con k = 3, comparado con su idioma.
  3. Si el idioma y la clave se pueden detectar a la vez: para cada idioma de
     referencia y cada corrimiento s se calcula chi^2, y se elige el par
     (idioma, s) con el chi^2 minimo. Se repite con muchos textos de prueba.
  4. El indice de coincidencia, que no cambia con ninguna sustitucion.

Uso:  python3 idiomas.py [CARPETA]   (por defecto "corpus"; los libros que falten se descargan)
"""
import json
import os
import random
import re
import sys
import unicodedata

import numpy as np

ABC = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
LIBROS = {
    "español":   ("quijote.txt", "Don Quijote", "17340.txt", "Marianela"),
    "inglés":    ("2701.txt", "Moby Dick", "1342.txt", "Pride and Prejudice"),
    "francés":   ("17489.txt", "Les Misérables I", "14155.txt", "Madame Bovary"),
    "alemán":    ("34811.txt", "Buddenbrooks", "5323.txt", "Effi Briest"),
    "portugués": ("40409.txt", "Os Maias", "55752.txt", "Dom Casmurro"),
}
K = 3
N_CORTO, N_LARGO = 100, 400
PRUEBAS = 300
SEMILLA = 20261117


URLS = {
    "quijote.txt": "https://raw.githubusercontent.com/GITenberg/Don-Quijote_2000/master/2000-8.txt",
    "17340.txt": "https://raw.githubusercontent.com/GITenberg/Marianela_17340/master/17340-8.txt",
    "2701.txt": "https://raw.githubusercontent.com/GITenberg/Moby-Dick--Or-The-Whale_2701/master/2701-0.txt",
    "1342.txt": "https://raw.githubusercontent.com/GITenberg/Pride-and-Prejudice_1342/master/1342-0.txt",
    "17489.txt": "https://raw.githubusercontent.com/GITenberg/Les-mis-rables-Tome-I--13-Fantine_17489/master/17489-8.txt",
    "14155.txt": "https://raw.githubusercontent.com/GITenberg/Madame-Bovary_14155/master/14155-8.txt",
    "34811.txt": "https://raw.githubusercontent.com/GITenberg/BuddenbrooksVerfall-einer-Familie_34811/master/34811-8.txt",
    "5323.txt": "https://raw.githubusercontent.com/GITenberg/Effi-Briest_5323/master/5323-8.txt",
    "40409.txt": "https://raw.githubusercontent.com/GITenberg/Os-Maiasepisodios-da-vida-romantica_40409/master/40409-8.txt",
    "55752.txt": "https://raw.githubusercontent.com/GITenberg/Dom-Casmurro_55752/master/55752-8.txt",
}


def leer(ruta):
    if not os.path.exists(ruta):
        import urllib.request
        os.makedirs(os.path.dirname(ruta) or ".", exist_ok=True)
        with open(ruta, "wb") as f:
            f.write(urllib.request.urlopen(URLS[os.path.basename(ruta)], timeout=120).read())
    crudo = open(ruta, "rb").read()
    try:
        texto = crudo.decode("utf-8")
    except UnicodeDecodeError:
        texto = crudo.decode("latin-1")
    # Quita el encabezado y la licencia de Gutenberg (en ingles).
    ini = re.search(r"\*\*\*\s*START OF[^\n]*", texto)
    fin = re.search(r"\*\*\*\s*END OF", texto)
    if ini:
        texto = texto[ini.end():fin.start() if fin and fin.start() > ini.end() else None]
    return texto


def normalizar(texto):
    """A-Z: quita tildes, dieresis y cedillas; ß -> SS, Æ -> AE, Œ -> OE."""
    texto = texto.upper().replace("ß", "SS").replace("Æ", "AE").replace("Œ", "OE")
    sin_marcas = unicodedata.normalize("NFD", texto)
    return "".join(c for c in sin_marcas if c in ABC)


def cuentas(letras):
    return np.array([letras.count(c) for c in ABC], dtype=float)


def cesar(letras, k):
    return "".join(ABC[(ABC.index(c) + k) % 26] for c in letras)


def chi2_todos(cifrado, p_ref):
    """chi^2(s) para s = 0..25: se descifra con s y se compara con p_ref."""
    o = cuentas(cifrado)
    n = o.sum()
    return np.array([(((np.roll(o, -s) - n * p_ref) ** 2) / (n * p_ref)).sum() for s in range(26)])


def indice_coincidencia(letras):
    o = cuentas(letras)
    n = o.sum()
    return float((o * (o - 1)).sum() / (n * (n - 1)))


def main(carpeta):
    rng = random.Random(SEMILLA)
    ref, prueba = {}, {}
    for idioma, (r, _, t, _) in LIBROS.items():
        ref[idioma] = normalizar(leer(os.path.join(carpeta, r)))
        prueba[idioma] = normalizar(leer(os.path.join(carpeta, t)))
    # Medio conteo extra por letra, para que ninguna tenga probabilidad cero
    # (en el Quijote no aparece ninguna K).
    p = {i: (cuentas(ref[i]) + 0.5) / (len(ref[i]) + 13) for i in LIBROS}
    idiomas = list(LIBROS)
    salida = {"k": K, "libros": LIBROS}

    # 1. Letras mas frecuentes
    print("1. LETRAS MAS FRECUENTES (libro de referencia)")
    salida["frecuencias"] = {}
    for i in idiomas:
        orden = np.argsort(p[i])[::-1]
        top = [(ABC[j], round(100 * p[i][j], 1)) for j in orden[:8]]
        salida["frecuencias"][i] = {"letras": len(ref[i]), "top": top, "p": [round(float(v), 5) for v in p[i]]}
        print(f"  {i:10s} ({len(ref[i]):>9,} letras): " + "  ".join(f"{c} {v:.1f}" for c, v in top))

    # 2. chi^2(s) para un texto de 400 letras de cada idioma, cifrado con k = 3
    print(f"\n2. CHI^2(s) PARA UN TEXTO DE {N_LARGO} LETRAS CIFRADO CON k = {K}")
    salida["ejemplo"] = {}
    for i in idiomas:
        inicio = len(prueba[i]) // 2
        claro = prueba[i][inicio:inicio + N_LARGO]
        c2 = chi2_todos(cesar(claro, K), p[i])
        orden = np.argsort(c2)
        salida["ejemplo"][i] = {"claro": claro[:40], "chi2": [round(float(v), 1) for v in c2]}
        print(f"  {i:10s} min en s = {orden[0]:2d}: chi2 = {c2[orden[0]]:7.1f} | segundo s = {orden[1]:2d}: {c2[orden[1]]:7.1f} | s=0: {c2[0]:7.1f}")

    # 3. Detectar idioma y clave a la vez
    for n in (N_LARGO, N_CORTO):
        print(f"\n3. IDIOMA Y CLAVE A LA VEZ, {PRUEBAS} TEXTOS DE {n} LETRAS POR IDIOMA (k al azar)")
        matriz = {i: {j: 0 for j in idiomas} for i in idiomas}
        clave_ok = {i: 0 for i in idiomas}
        for i in idiomas:
            for _ in range(PRUEBAS):
                a = rng.randrange(0, len(prueba[i]) - n)
                k = rng.randrange(26)
                cif = cesar(prueba[i][a:a + n], k)
                mejor = min(((float(chi2_todos(cif, p[j]).min()), j, int(np.argmin(chi2_todos(cif, p[j])))) for j in idiomas))
                matriz[i][mejor[1]] += 1
                # clave con la referencia de su propio idioma
                clave_ok[i] += int(np.argmin(chi2_todos(cif, p[i])) == k)
        salida[f"matriz_{n}"] = matriz
        salida[f"clave_{n}"] = clave_ok
        print("  real \\ detectado " + " ".join(f"{j[:5]:>6s}" for j in idiomas) + "   clave correcta")
        for i in idiomas:
            print(f"  {i:16s} " + " ".join(f"{100 * matriz[i][j] / PRUEBAS:5.0f}%" for j in idiomas) + f"   {100 * clave_ok[i] / PRUEBAS:5.1f}%")

    # 4. Indice de coincidencia
    print("\n4. INDICE DE COINCIDENCIA (no cambia con ninguna sustitucion)")
    salida["ic"] = {}
    for i in idiomas:
        ic = indice_coincidencia(ref[i])
        salida["ic"][i] = round(ic, 4)
        print(f"  {i:10s} {ic:.4f}")
    print(f"  al azar    {1 / 26:.4f}")
    claro = prueba["español"][len(prueba["español"]) // 2:][:2000]
    clave = "CLAVE"
    vig = "".join(ABC[(ABC.index(c) + ABC.index(clave[i % len(clave)])) % 26] for i, c in enumerate(claro))
    rnd = random.Random(1)
    otp = "".join(ABC[(ABC.index(c) + rnd.randrange(26)) % 26] for c in claro)
    salida["ic_cifrados"] = {
        "claro": round(indice_coincidencia(claro), 4),
        "cesar": round(indice_coincidencia(cesar(claro, K)), 4),
        "vigenere_CLAVE": round(indice_coincidencia(vig), 4),
        "un_solo_uso": round(indice_coincidencia(otp), 4),
    }
    print("  texto en español de 2000 letras:", salida["ic_cifrados"])

    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "datos_idiomas.json"), "w", encoding="utf-8") as f:
        json.dump(salida, f, ensure_ascii=False, indent=1)


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "corpus")
