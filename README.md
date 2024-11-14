# Sistema de Grafos Simples

Este projeto implementa um sistema para criar, manipular e visualizar grafos simples. O usuário pode definir grafos direcionados/não-direcionados, valorados/não-valorados, e acessar funcionalidades de visualização, cálculo de caminho mínimo, grau dos vértices, e outras informações do grafo.

## Instalação e Execução

Para rodar o projeto, você precisa do Python 3 e das bibliotecas `matplotlib` e `networkx`.

Clone o repositório, crie um ambiente virtual, ative-o, instale as dependências, e inicie o sistema com os comandos abaixo:

```bash
    git clone https://github.com/felipesergiob/gerador-grafo-simples

    python3 -m venv myenv
```
MAC/LINUX:
```bash
    source myenv/bin/activate
```
WINDOWS
```bash
    Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
     .\myenv\Scripts\Activate
```

```bash
    python3 -m pip install -r requirements.txt
    python3 main.py
```

Para desativar a venv criada:

```bash
    deactivate
```