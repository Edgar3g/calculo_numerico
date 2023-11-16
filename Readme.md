# Método da Bisseção - Encontrar Raízes de Funções

## Descrição

Este projeto implementa o Método da Bisseção para encontrar raízes de funções matemáticas. O método é aplicado a uma função específica, neste caso, \(f(x) = x^3 - 9x + 3\). O programa solicita ao usuário um intervalo [A, B] e um limite de erro (E), e em seguida, utiliza o Método da Bisseção para encontrar uma raiz aproximada dentro desse intervalo.

## Como Usar

1. Execute o programa Python `bissecao.py`.
2. Insira o intervalo de busca [A, B].
3. Insira o limite de erro (E).
4. Aguarde o cálculo.

O programa imprimirá uma tabela mostrando as iterações do Método da Bisseção, exibindo os valores de \(a\), \(b\), \(X_k\), \(f(X_k)\) e \(|b - a|\). O processo continua até que a diferença entre \(b\) e \(a\) seja menor ou igual ao limite de erro especificado.

## Requisitos

Certifique-se de ter Python instalado. Você pode instalá-lo [aqui](https://www.python.org/downloads/).

## Exemplo

```python
Digite o intervalo de A: -2
Digite o intervalo de B: 2
Digite o limite de E: 0.01

by: Edgar3g; Alexandre Gaspar (math man) 