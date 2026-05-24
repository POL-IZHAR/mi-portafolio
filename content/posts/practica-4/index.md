---
title: "Práctica 4: Paradigma Lógico - Aplicaciones con Prolog"
date: 2026-05-23T12:00:00-07:00
draft: false
tags: ["Prolog", "Paradigma Lógico"]
description: "Implementación del puzzle clásico Torres de Hanoi y el problema de planificación del Mono y la Banana."
---

**Nombre:** JARETH IZHAR APARICIO LOPEZ  
**Matrícula:** 376619  
**Materia:** PARADIGMAS DE LA PROGRAMACION  
**Practica:** Torres de Hanoi | Mono y la Banana  
**Lenguaje:** Prolog (SWI-Prolog)

---

## 1. Introduccion al Paradigma Logico

El paradigma logico es un estilo de programacion declarativa basado en logica formal de primer orden.
En lugar de especificar **como** resolver un problema, el programador declara **que** es verdadero:
hechos, reglas y relaciones. El motor de inferencia busca soluciones mediante unificacion y backtracking.

### Caracteristicas principales
- **Hechos:** Verdades absolutas. Ej: `parent(tom, bob).`
- **Reglas:** Implicaciones logicas. Ej: `father(X,Y) :- parent(X,Y), male(X).`
- **Consultas:** Preguntas al motor. Ej: `?- father(tom, bob).`
- **Unificacion:** Matching entre terminos.
- **Backtracking:** Exploracion automatica de alternativas.

---

## 2. Archivos de la Practica Anterior

| Archivo | Contenido |
|---------|-----------|
| `kb1.pl` | Base de conocimiento: girl/can_cook |
| `kb2.pl` | Hechos y reglas: happy/plays_guitar |
| `kb3.pl` | Reglas con condiciones: like |
| `kb4.pl` | Relacion hermanos con parent/male |
| `family.pl` | Familia basica: mother/father/sister/brother |
| `family_ext.pl` | Familia extendida: grandparent/uncle/aunt |
| `family_rec.pl` | Recursion: predecessor |
| `conj_disj.pl` | Conjuncion y disyuncion |
| `var_anon.pl` | Variables anonimas |
| `option.pl` | If-Then-Else en Prolog |
| `loop.pl` | Iteracion: count_to_10/count_down/count_up |
| `operadores.pl` | Operadores aritmeticos |
| `list_basics.pl` | Listas basicas |
| `list_repos.pl` | Listas avanzadas: perm/rev/subset/union |
| `list_misc.pl` | Miscelanea: max_elem/sum/divide |
| `likes.pl` | Demo backtracking con comida |

---

## 3. Torres de Hanoi

### Descripcion
Puzzle clasico con N discos y 3 postes. Mover todos los discos del poste izquierdo al derecho:
- Solo un disco a la vez.
- No poner disco grande sobre uno pequeno.
- Minimo de movimientos: 2^N - 1.

### Codigo (`hanoi.pl`)
```prolog
hanoi(1, Origen, Destino, _) :-
    format("Mover disco 1 de ~w a ~w~n", [Origen, Destino]).

hanoi(N, Origen, Destino, Auxiliar) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, Origen, Auxiliar, Destino),
    format("Mover disco ~w de ~w a ~w~n", [N, Origen, Destino]),
    hanoi(N1, Auxiliar, Destino, Origen).

hanoi(N) :- hanoi(N, izquierda, derecha, centro).
```

### Ejecucion con 3 discos
```
?- hanoi(3).
Mover disco 1 de izquierda a derecha
Mover disco 2 de izquierda a centro
Mover disco 1 de derecha a centro
Mover disco 3 de izquierda a derecha
Mover disco 1 de centro a izquierda
Mover disco 2 de centro a derecha
Mover disco 1 de izquierda a derecha
```

---

## 4. El Mono y la Banana

### Descripcion
Problema de planificacion de IA. Un mono quiere una banana del techo:
- Estado: `estado(PosicionMono, PosicionCaja, MonoEnCaja, TieneBanana)`
- Acciones: caminar, empujar_caja, subir_caja, tomar_banana
- Busqueda: BFS para encontrar la secuencia optima.

### Codigo (`mono_banana.pl`)
```prolog
mover(estado(_, CajaPos, en_suelo, Banana),
      caminar(NuevaPos),
      estado(NuevaPos, CajaPos, en_suelo, Banana)) :-
    member(NuevaPos, [puerta, centro, ventana]).

mover(estado(Pos, Pos, en_suelo, Banana),
      empujar_caja(NuevaPosicion),
      estado(NuevaPosicion, NuevaPosicion, en_suelo, Banana)) :-
    member(NuevaPosicion, [puerta, centro, ventana]),
    Pos \= NuevaPosicion.

mover(estado(Pos, Pos, en_suelo, Banana),
      subir_caja,
      estado(Pos, Pos, en_caja, Banana)).

mover(estado(centro, centro, en_caja, no),
      tomar_banana,
      estado(centro, centro, en_caja, si)).

objetivo(estado(_, _, _, si)).
```

### Ejecucion
```
?- demo.
Estado inicial: mono en puerta, caja en ventana
Objetivo: que el mono tome la banana del techo

Secuencia de acciones encontrada:
  Paso 1: caminar(ventana)
  Paso 2: empujar_caja(centro)
  Paso 3: subir_caja
  Paso 4: tomar_banana
```

---

## 5. Conceptos Prolog Aplicados

- **Recursion:** Fundamental; refleja directamente la definicion matematica.
- **Unificacion:** Los patrones en clausulas imponen restricciones implicitas.
- **findall/3:** Recolecta todas las soluciones de un objetivo.
- **Operador \+:** Negacion por fallo para evitar estados repetidos.
- **format/2:** Salida formateada.

---

## 6. Conclusiones

1. Prolog permite expresar soluciones de forma declarativa, muy cercana a la descripcion matematica.
2. La recursion es natural; el motor maneja automaticamente el stack.
3. Para busqueda, la representacion explicita del estado es clave.
4. La unificacion actua como filtro de patrones sin codigo adicional.
5. El paradigma logico es adecuado para IA y satisfaccion de restricciones.

---

## 7. Referencias

- Bratko, I. (2011). *Prolog Programming for Artificial Intelligence* (4a ed.). Addison-Wesley.
- Clocksin, W. & Mellish, C. (2003). *Programming in Prolog* (5a ed.). Springer.
- SWI-Prolog. (2024). Reference Manual. https://www.swi-prolog.org/pldoc/
- Russell, S. & Norvig, P. (2020). *Artificial Intelligence: A Modern Approach* (4a ed.). Pearson.
