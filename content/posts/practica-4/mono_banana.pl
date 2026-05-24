% =============================================
% Problema del Mono y la Banana
% Estado: estado(PosicionMono, PosicionCaja, MonoEnCaja, TieneBanana)
%   - PosicionMono: puerta | centro | ventana
%   - PosicionCaja: puerta | centro | ventana
%   - MonoEnCaja:   en_caja | en_suelo
%   - TieneBanana:  si | no
%
% Uso: ?- puede_tomar_banana(estado(puerta, ventana, en_suelo, no), Pasos).
% =============================================

% 1. El mono camina a una nueva posicion (solo si esta en el suelo)
mover(
    estado(_, CajaPos, en_suelo, Banana),
    caminar(NuevaPos),
    estado(NuevaPos, CajaPos, en_suelo, Banana)
) :-
    member(NuevaPos, [puerta, centro, ventana]).

% 2. El mono empuja la caja (debe estar en la misma posicion que la caja)
mover(
    estado(Pos, Pos, en_suelo, Banana),
    empujar_caja(NuevaPosicion),
    estado(NuevaPosicion, NuevaPosicion, en_suelo, Banana)
) :-
    member(NuevaPosicion, [puerta, centro, ventana]),
    Pos \= NuevaPosicion.

% 3. El mono sube a la caja (cuando esta en la misma posicion)
mover(
    estado(Pos, Pos, en_suelo, Banana),
    subir_caja,
    estado(Pos, Pos, en_caja, Banana)
).

% 4. El mono toma la banana (cuando esta sobre la caja en el centro)
mover(
    estado(centro, centro, en_caja, no),
    tomar_banana,
    estado(centro, centro, en_caja, si)
).

% Objetivo: el mono tiene la banana
objetivo(estado(_, _, _, si)).

% Busqueda en amplitud (BFS)
puede_tomar_banana(EstadoInicial, Pasos) :-
    buscar([[EstadoInicial, []]], [], Pasos).

buscar([[Estado, Pasos] | _], _, PasosOrden) :-
    objetivo(Estado),
    reverse(Pasos, PasosOrden).

buscar([[Estado, Pasos] | Cola], Visitados, Solucion) :-
    \+ objetivo(Estado),
    \+ member(Estado, Visitados),
    findall(
        [NuevoEstado, [Accion | Pasos]],
        (mover(Estado, Accion, NuevoEstado), \+ member(NuevoEstado, Visitados)),
        Sucesores
    ),
    append(Cola, Sucesores, NuevaCola),
    buscar(NuevaCola, [Estado | Visitados], Solucion).

buscar([[Estado, _] | Cola], Visitados, Solucion) :-
    member(Estado, Visitados),
    buscar(Cola, Visitados, Solucion).

% Predicado de demostracion
demo :-
    EstadoInicial = estado(puerta, ventana, en_suelo, no),
    write('Estado inicial: mono en puerta, caja en ventana'), nl,
    write('Objetivo: que el mono tome la banana del techo'), nl, nl,
    ( puede_tomar_banana(EstadoInicial, Pasos) ->
        write('Secuencia de acciones encontrada:'), nl,
        imprimir_pasos(Pasos, 1)
    ;
        write('No se encontro solucion.')
    ).

imprimir_pasos([], _).
imprimir_pasos([Paso|Resto], N) :-
    format("  Paso ~w: ~w~n", [N, Paso]),
    N1 is N + 1,
    imprimir_pasos(Resto, N1).
