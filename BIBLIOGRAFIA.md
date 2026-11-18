# Bibliografía: Criptografía cuántica

Plenaria de Mecánica Cuántica 2026-II, Universidad Distrital Francisco José de Caldas.
Camila Pérez y Sergio Carrasquilla. Profesor: John Díaz.

Cada entrada tiene el enlace oficial (DOI) y, cuando existe, una versión de descarga libre (arXiv, NIST, repositorios de las universidades). Entre paréntesis van las diapositivas donde se usa.

Los PDF libres se descargan todos juntos con `descargar_bibliografia.py`.

---

## 1. Historia de la criptografía (diapositivas 3 a 17)

1. **S. Singh** (2000). *Los códigos secretos*. Debate, Madrid. Original: *The Code Book*, 1999. Libro. (3 a 13: César, Al-Kindi, María Estuardo, Vigenère, Zimmermann, Enigma)
2. **D. Kahn** (1996). *The Codebreakers: The Story of Secret Writing*, edición revisada. Scribner, Nueva York. Libro. (3 a 13)
3. **I. A. Al-Kadit** (1992). Origins of cryptology: The Arab contributions. *Cryptologia* 16(2), 97-126. DOI: [10.1080/0161-119291866801](https://doi.org/10.1080/0161-119291866801). (5)
4. **B. Ycart** (2013). Letter counting: a stem cell for Cryptology, Quantitative Linguistics, and Statistics. *Historiographia Linguistica* 40(3). [Revista](https://benjamins.com/online/hl/articles/hl.40.3.01yca) · Libre: [arXiv:1211.6847](https://arxiv.org/abs/1211.6847). (5: el tratado de Al-Kindi y el conteo de letras)
5. **A. Kerckhoffs** (1883). La cryptographie militaire. *Journal des sciences militaires* 9, 5-38 y 161-191. Libre: [petitcolas.net/kerckhoffs](https://www.petitcolas.net/kerckhoffs/). (8)
6. **G. S. Vernam** (1926). Cipher printing telegraph systems for secret wire and radio telegraphic communications. *Journal of the American Institute of Electrical Engineers* 45, 109-115. (10)
7. **C. E. Shannon** (1949). Communication theory of secrecy systems. *Bell System Technical Journal* 28(4), 656-715. DOI: [10.1002/j.1538-7305.1949.tb00928.x](https://doi.org/10.1002/j.1538-7305.1949.tb00928.x) · [Nokia Bell Labs](https://nokia.com/bell-labs/publications-and-media/publications/communication-theory-of-secrecy-systems). (11)
8. **R. L. Benson** (2001). *The Venona Story*. Center for Cryptologic History, National Security Agency. Libre: [PDF, reimpresión de 2019](https://media.defense.gov/2021/Jul/13/2002761786/-1/-1/0/Venona%20Story_2019%20reprint%20version.PDF). (14: claves de un solo uso reutilizadas por los soviéticos)
9. **W. Diffie y M. E. Hellman** (1976). New directions in cryptography. *IEEE Transactions on Information Theory* 22(6), 644-654. DOI: [10.1109/TIT.1976.1055638](https://doi.org/10.1109/TIT.1976.1055638) · Libre: [Stanford](https://ee.stanford.edu/~hellman/publications/24.pdf). (15)
10. **R. L. Rivest, A. Shamir y L. Adleman** (1978). A method for obtaining digital signatures and public-key cryptosystems. *Communications of the ACM* 21(2), 120-126. DOI: [10.1145/359340.359342](https://doi.org/10.1145/359340.359342) · Libre: [MIT DSpace](https://dspace.mit.edu/handle/1721.1/148910). (15)
11. **P. W. Shor** (1997). Polynomial-time algorithms for prime factorization and discrete logarithms on a quantum computer. *SIAM Journal on Computing* 26(5), 1484-1509. DOI: [10.1137/S0097539795293172](https://doi.org/10.1137/S0097539795293172) · Libre: [arXiv:quant-ph/9508027](https://arxiv.org/abs/quant-ph/9508027). (15)

## 2. Fundamentos cuánticos (diapositivas 18 a 21 y 33)

12. **M. A. Nielsen e I. L. Chuang** (2010). *Quantum Computation and Quantum Information*, edición del décimo aniversario. Cambridge University Press. Libro; sección 12.6 sobre criptografía cuántica. (18 a 24)
13. **W. K. Wootters y W. H. Zurek** (1982). A single quantum cannot be cloned. *Nature* 299, 802-803. DOI: [10.1038/299802a0](https://doi.org/10.1038/299802a0). (20, 21)
14. **D. Dieks** (1982). Communication by EPR devices. *Physics Letters A* 92(6), 271-272. DOI: [10.1016/0375-9601(82)90084-6](https://doi.org/10.1016/0375-9601(82)90084-6). (20, 21)
15. **V. Bužek y M. Hillery** (1996). Quantum copying: Beyond the no-cloning theorem. *Physical Review A* 54, 1844. DOI: [10.1103/PhysRevA.54.1844](https://doi.org/10.1103/PhysRevA.54.1844) · Libre: [arXiv:quant-ph/9607018](https://arxiv.org/abs/quant-ph/9607018). (21: copias imperfectas)
16. **J. S. Bell** (1964). On the Einstein Podolsky Rosen paradox. *Physics Physique Fizika* 1, 195-200. DOI: [10.1103/PhysicsPhysiqueFizika.1.195](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195). (33)
17. **J. F. Clauser, M. A. Horne, A. Shimony y R. A. Holt** (1969). Proposed experiment to test local hidden-variable theories. *Physical Review Letters* 23, 880. DOI: [10.1103/PhysRevLett.23.880](https://doi.org/10.1103/PhysRevLett.23.880). (33: desigualdad CHSH)

## 3. Protocolos y pruebas de seguridad (diapositivas 22 a 28 y 31 a 33)

18. **S. Wiesner** (1983). Conjugate coding. *ACM SIGACT News* 15(1), 78-88. DOI: [10.1145/1008908.1008920](https://doi.org/10.1145/1008908.1008920). Escrito hacia 1970; es la idea de las dos bases que usa BB84. (22)
19. **C. H. Bennett y G. Brassard** (1984). Quantum cryptography: Public key distribution and coin tossing. *Proceedings of the IEEE International Conference on Computers, Systems and Signal Processing*, Bangalore, 175-179. Reimpreso en *Theoretical Computer Science* 560, 7-11 (2014), DOI: [10.1016/j.tcs.2014.05.025](https://doi.org/10.1016/j.tcs.2014.05.025) · Libre: [arXiv:2003.06557](https://arxiv.org/abs/2003.06557). (22 a 24: BB84)
20. **A. K. Ekert** (1991). Quantum cryptography based on Bell's theorem. *Physical Review Letters* 67, 661. DOI: [10.1103/PhysRevLett.67.661](https://doi.org/10.1103/PhysRevLett.67.661). (31 a 33: E91)
21. **P. W. Shor y J. Preskill** (2000). Simple proof of security of the BB84 quantum key distribution protocol. *Physical Review Letters* 85, 441. DOI: [10.1103/PhysRevLett.85.441](https://doi.org/10.1103/PhysRevLett.85.441) · Libre: [arXiv:quant-ph/0003004](https://arxiv.org/abs/quant-ph/0003004). (27, 28: tasa 1 - 2h(Q) y umbral del 11 %)
22. **G. Brassard** (2005). Brief history of quantum cryptography: A personal perspective. Libre: [arXiv:quant-ph/0604072](https://arxiv.org/abs/quant-ph/0604072). (22, 31: historia contada por uno de los autores de BB84)

## 4. Equipos reales y experimentos (diapositivas 34 a 36)

23. **W.-Y. Hwang** (2003). Quantum key distribution with high loss: Toward global secure communication. *Physical Review Letters* 91, 057901. DOI: [10.1103/PhysRevLett.91.057901](https://doi.org/10.1103/PhysRevLett.91.057901) · Libre: [arXiv:quant-ph/0211153](https://arxiv.org/abs/quant-ph/0211153). (34: estados señuelo)
24. **H.-K. Lo, X. Ma y K. Chen** (2005). Decoy state quantum key distribution. *Physical Review Letters* 94, 230504. DOI: [10.1103/PhysRevLett.94.230504](https://doi.org/10.1103/PhysRevLett.94.230504) · Libre: [arXiv:quant-ph/0411004](https://arxiv.org/abs/quant-ph/0411004). (34)
25. **L. Lydersen, C. Wiechers, C. Wittmann, D. Elser, J. Skaar y V. Makarov** (2010). Hacking commercial quantum cryptography systems by tailored bright illumination. *Nature Photonics* 4, 686-689. DOI: [10.1038/nphoton.2010.214](https://doi.org/10.1038/nphoton.2010.214) · Libre: [arXiv:1008.4593](https://arxiv.org/abs/1008.4593). (35: detectores cegados)
26. **H.-K. Lo, M. Curty y B. Qi** (2012). Measurement-device-independent quantum key distribution. *Physical Review Letters* 108, 130503. DOI: [10.1103/PhysRevLett.108.130503](https://doi.org/10.1103/PhysRevLett.108.130503) · Libre: [arXiv:1109.1473](https://arxiv.org/abs/1109.1473). (35: MDI-QKD)
27. **S. Pirandola, R. Laurenza, C. Ottaviani y L. Banchi** (2017). Fundamental limits of repeaterless quantum communications. *Nature Communications* 8, 15043. DOI: [10.1038/ncomms15043](https://doi.org/10.1038/ncomms15043) · Libre: [PMC5414096](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5414096/) · [arXiv:1510.08863](https://arxiv.org/abs/1510.08863). (36: límite de la fibra sin repetidores)
28. **S.-K. Liao et al.** (2017). Satellite-to-ground quantum key distribution. *Nature* 549, 43-47. DOI: [10.1038/nature23655](https://doi.org/10.1038/nature23655) · Libre: [arXiv:1707.00542](https://arxiv.org/abs/1707.00542). (36: Micius, BB84 desde el satélite)
29. **J. Yin et al.** (2017). Satellite-based entanglement distribution over 1200 kilometers. *Science* 356, 1140-1144. DOI: [10.1126/science.aan3211](https://doi.org/10.1126/science.aan3211) · Libre: [arXiv:1707.01339](https://arxiv.org/abs/1707.01339). (36)
30. **M. Lucamarini, Z. L. Yuan, J. F. Dynes y A. J. Shields** (2018). Overcoming the rate-distance limit of quantum key distribution without quantum repeaters. *Nature* 557, 400-403. DOI: [10.1038/s41586-018-0066-6](https://doi.org/10.1038/s41586-018-0066-6) · Libre: [arXiv:1811.06826](https://arxiv.org/abs/1811.06826). (36: twin-field QKD)
31. **J. Yin et al.** (2020). Entanglement-based secure quantum cryptography over 1,120 kilometres. *Nature* 582, 501-505. DOI: [10.1038/s41586-020-2401-y](https://doi.org/10.1038/s41586-020-2401-y). (36: Micius con entrelazamiento)
32. **Y.-A. Chen et al.** (2021). An integrated space-to-ground quantum communication network over 4,600 kilometres. *Nature* 589, 214-219. DOI: [10.1038/s41586-020-03093-8](https://doi.org/10.1038/s41586-020-03093-8). (36: red Pekín-Shanghái con nodos de confianza)
33. **D. P. Nadlinger et al.** (2022). Experimental quantum key distribution certified by Bell's theorem. *Nature* 607, 682-686. DOI: [10.1038/s41586-022-04941-5](https://doi.org/10.1038/s41586-022-04941-5) · Libre: [arXiv:2109.14600](https://arxiv.org/abs/2109.14600). (35: DI-QKD)
34. **W. Zhang et al.** (2022). A device-independent quantum key distribution system for distant users. *Nature* 607, 687-691. DOI: [10.1038/s41586-022-04891-y](https://doi.org/10.1038/s41586-022-04891-y) · Libre: [PMC9329124](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9329124/). (35: DI-QKD)
35. **Y. Liu et al.** (2023). Experimental twin-field quantum key distribution over 1000 km fiber distance. *Physical Review Letters* 130, 210801. DOI: [10.1103/PhysRevLett.130.210801](https://doi.org/10.1103/PhysRevLett.130.210801) · Libre: [arXiv:2303.15795](https://arxiv.org/abs/2303.15795). (36)

## 5. Revisiones (para estudiar todo el tema)

36. **N. Gisin, G. Ribordy, W. Tittel y H. Zbinden** (2002). Quantum cryptography. *Reviews of Modern Physics* 74, 145. DOI: [10.1103/RevModPhys.74.145](https://doi.org/10.1103/RevModPhys.74.145) · Libre: [arXiv:quant-ph/0101098](https://arxiv.org/abs/quant-ph/0101098).
37. **F. Xu, X. Ma, Q. Zhang, H.-K. Lo y J.-W. Pan** (2020). Secure quantum key distribution with realistic devices. *Reviews of Modern Physics* 92, 025002. DOI: [10.1103/RevModPhys.92.025002](https://doi.org/10.1103/RevModPhys.92.025002) · Libre: [arXiv:1903.09051](https://arxiv.org/abs/1903.09051).
38. **S. Pirandola et al.** (2020). Advances in quantum cryptography. *Advances in Optics and Photonics* 12(4), 1012-1236. DOI: [10.1364/AOP.361502](https://doi.org/10.1364/AOP.361502) · Libre: [arXiv:1906.01645](https://arxiv.org/abs/1906.01645).

## 6. Criptografía poscuántica (diapositivas 15 y 38)

39. **NIST** (2024). FIPS 203: Module-Lattice-Based Key-Encapsulation Mechanism Standard (ML-KEM). [Página](https://csrc.nist.gov/pubs/fips/203/final) · [PDF](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.203.pdf).
40. **NIST** (2024). FIPS 204: Module-Lattice-Based Digital Signature Standard (ML-DSA). [Página](https://csrc.nist.gov/pubs/fips/204/final) · [PDF](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.204.pdf).
41. **NIST** (2024). FIPS 205: Stateless Hash-Based Digital Signature Standard (SLH-DSA). [Página](https://csrc.nist.gov/pubs/fips/205/final) · [PDF](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.205.pdf).

## 7. Video (diapositiva 32)

42. **Centre for Quantum Technologies, Singapur.** Animación sobre la distribución de clave con pares entrelazados. [YouTube](https://www.youtube.com/watch?v=LaLzshIosDk).

## 8. Datos y código propios (diapositivas 5 y 29 a 30)

- `simulaciones.py`: análisis de frecuencias (diapositiva 5), Monte Carlo de BB84 con espía parcial, tasa de clave y umbral del 11 % (diapositivas 27 a 30).
- `idiomas.py`: frecuencias de letras y detección de idioma y clave con χ² en español, inglés, francés, alemán y portugués.
- Textos de dominio público del [Proyecto Gutenberg](https://www.gutenberg.org): Don Quijote ([2000](https://www.gutenberg.org/ebooks/2000)), Marianela ([17340](https://www.gutenberg.org/ebooks/17340)), Moby Dick ([2701](https://www.gutenberg.org/ebooks/2701)), Pride and Prejudice ([1342](https://www.gutenberg.org/ebooks/1342)), Les Misérables I ([17489](https://www.gutenberg.org/ebooks/17489)), Madame Bovary ([14155](https://www.gutenberg.org/ebooks/14155)), Buddenbrooks ([34811](https://www.gutenberg.org/ebooks/34811)), Effi Briest ([5323](https://www.gutenberg.org/ebooks/5323)), Os Maias ([40409](https://www.gutenberg.org/ebooks/40409)), Dom Casmurro ([55752](https://www.gutenberg.org/ebooks/55752)).
