% =============================================
% Torres de Hanoi
% Uso: hanoi(N) donde N es el número de discos
% Ejemplo: ?- hanoi(3).
% =============================================

% Caso base: mover 1 disco directamente
hanoi(1, Origen, Destino, _) :-
    format("Mover disco 1 de ~w a ~w~n", [Origen, Destino]).

% Caso recursivo: mover N discos
hanoi(N, Origen, Destino, Auxiliar) :-
    N > 1,
    N1 is N - 1,
    hanoi(N1, Origen, Auxiliar, Destino),
    format("Mover disco ~w de ~w a ~w~n", [N, Origen, Destino]),
    hanoi(N1, Auxiliar, Destino, Origen).

% Predicado principal: llama con torres nombradas
hanoi(N) :-
    hanoi(N, izquierda, derecha, centro).
