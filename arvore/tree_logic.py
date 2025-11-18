
# tree_logic.py — você edita APENAS este arquivo nesta atividade.

class Node:
    def __init__(self, question, yes=None, no=None):
        """
        Se 'yes' e 'no' forem None, este nó é uma FOLHA e 'question' guarda a decisão final (string).
        Caso contrário, 'question' é o texto da pergunta e 'yes'/'no' são seus filhos.
        """
        self.question = question
        self.yes = yes
        self.no = no

def is_leaf(node):
    return node is not None and node.yes is None and node.no is None

def navigate_tree(node, answers):
    """
    Percorre a árvore a partir de 'node' seguindo a sequência de respostas (lista de strings).
    Retorna a decisão final (string) quando alcançar uma folha.
    """
    # Cria uma cópia das respostas para não modificar a original
    respostas_pendentes = answers.copy()
    
    # Enquanto o nó atual não for folha:
    while not node.is_leaf():
        if not respostas_pendentes:
            raise ValueError("Faltam respostas para concluir a decisão.")
        
        # Pega a próxima resposta e normaliza
        proxima_resposta = respostas_pendentes.pop(0).lower().strip()
        
        # Trata 'nao' como 'não'
        if proxima_resposta == 'nao':
            proxima_resposta = 'não'
            
        # Navega com base na resposta
        if proxima_resposta == 'sim':
            node = node.yes
        elif proxima_resposta == 'não':
            node = node.no
        else:
            # Resposta inválida
            raise ValueError(f"Resposta inválida: '{proxima_resposta}'. Esperado 'sim' ou 'não'.")("Implemente a função navigate_tree.")
