
# graph_logic.py — você edita APENAS este arquivo nesta atividade.
# Dica: use apenas LISTAS para a fila/estrutura de dados (nada de deque).
# Você pode fazer BFS com:
#   fila = [a]; visitados = [a]
#   while fila:
#       u = fila.pop(0)          # remove o primeiro
#       if u == b: return True
#       for v in graph.get(u, []):
#           if v not in visitados:
#               visitados.append(v)
#               fila.append(v)
#   return False
#
# Alternativamente, pode usar DFS com uma lista como "pilha":
#   pilha = [a]; visitados = []
#   while pilha:
#       u = pilha.pop()          # remove o último
#       ...
#   return False

def connected(graph, a, b):
   """
    Retorna True se existe um caminho (qualquer) entre 'a' e 'b' no grafo não direcionado.
    Implementa uma busca simples (BFS com listas), e trata erros de entrada de dados.
    """
    
    # Normalização dos nomes (Pessoa A e Pessoa B) para maiúscula inicial,
    # consistente com a estrutura do grafo em app_graph.py.
    start = a.strip().capitalize()
    end = b.strip().capitalize()
    
    # 1. TRATAMENTO DE ENTRADA DE DADOS
    if not start or not end:
        raise ValueError("Pessoa A e Pessoa B não podem ser nomes vazios.")
    if start not in graph:
        raise ValueError(f"Pessoa '{a}' não existe no grafo (nó inicial).")
    if end not in graph:
        raise ValueError(f"Pessoa '{b}' não existe no grafo (nó final).")

    # 2. Caso Trivial
    if start == end:
        return True

    # 3. Implementação do BFS (com lista)
    fila = [start]
    visitados = [start] 

    while fila:
        u = fila.pop(0)
        
        for v in graph.get(u, []):
            if v not in visitados:
                if v == end:
                    return True
                
                visitados.append(v)
                fila.append(v)
    
    # 4. Se a fila esvaziar
    return False
