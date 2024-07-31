# 🎬 Formação Acelerada em Programação - Backend Python

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)

Este projeto faz parte do curso **Formação Acelerada em Programação - Backend Python**. Ele implementa um sistema de CRUD (Create, Read, Update, Delete) unificado para gerenciar a relação entre diretores e filmes, utilizando Python.

## 📖 Descrição do Projeto

O sistema permite criar, ler, atualizar e deletar informações sobre diretores e filmes. Cada diretor pode dirigir vários filmes, mas cada filme é dirigido por um único diretor. A estrutura do projeto garante que a integridade dessa relação seja mantida durante todas as operações CRUD.

## ✨ Funcionalidades

- **Diretores:**
  - ➕ Criar Diretor
  - 🔍 Ler Diretor
  - ✏️ Atualizar Diretor
  - ❌ Deletar Diretor
  - 📜 Listar todos os Diretores

- **Filmes:**
  - ➕ Criar Filme
  - 🔍 Ler Filme
  - ✏️ Atualizar Filme
  - ❌ Deletar Filme
  - 📜 Listar todos os Filmes

## 🗂️ Estrutura de Dados

Os dados são armazenados em listas de dicionários:
- `diretores`: armazena informações sobre diretores (ID e nome).
- `filmes`: armazena informações sobre filmes (ID, título e ID do diretor).

## 🚀 Uso

1. Clone este repositório:
   ```sh
   git clone https://github.com/thaiana-silva/filme_crud_python.git
   cd formacao_backend_python_crud
