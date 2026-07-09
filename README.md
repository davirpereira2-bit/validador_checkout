

# Validador de Checkout

Programa em Python que simula a etapa de validação de um checkout (e-mail e valor do ingresso), utilizando exceções customizadas, expressões regulares e tratamento de erros completo com `try/except/else/finally`.

## 📋 Funcionalidades

- Validação do formato de e-mail digitado, usando expressão regular
- Validação do valor do ingresso, garantindo que seja maior que zero
- Exibição de mensagens de erro específicas para cada tipo de problema (e-mail inválido ou valor inválido)
- Exibição de mensagem de sucesso somente quando todos os dados são válidos
- Execução garantida de uma mensagem final, independentemente do resultado da validação

## 🛠️ Tecnologias utilizadas

- Python 3
- Módulo `re` (expressões regulares) para validação de padrão de e-mail
- Exceções customizadas (`class EmailInvalidoError(Exception)`)
- Estrutura completa de tratamento de erros: `try / except / else / finally`
- Docstrings para documentação da exceção customizada

## 💻 Conceitos praticados

- Criação de exceções personalizadas, herdando de `Exception`, para representar erros específicos da regra de negócio
- Uso de expressões regulares (`re.match`) para validar formato de dado (e-mail)
- Uso de múltiplos blocos `except` para tratar diferentes tipos de erro de forma independente
- Uso do bloco `else`, executado apenas quando nenhuma exceção ocorre no `try`
- Uso do bloco `finally`, executado sempre, independentemente de erro ou sucesso — útil para simular o encerramento de uma conexão ou recurso
- Uso de `raise` para lançar exceções manualmente com mensagens customizadas

## ▶️ Como executar

```bash
python validador_checkout.py
```

O programa pede um e-mail e o valor de um ingresso, validando ambos antes de confirmar o checkout.

## 📄 Exemplo de uso

**Caso de sucesso:**
```
=== SISTEMA DE CHECKOUT (VALIDAÇÃO AVANÇADA ) ===
Validar e-mail de usuário:ana@email.com
Digite o valor do ingresso:150

 Sucesso! Dados validados com precisão cirúrgica 
E-mail: ana@email.com | Valor do ingresso: 150.00
Conexão com o validador encerrada com segurança ! 
```

**Caso de e-mail inválido:**
```
=== SISTEMA DE CHECKOUT (VALIDAÇÃO AVANÇADA ) ===
Validar e-mail de usuário:ana@email
Erro de validação: O formato do email está incorreto !
Conexão com o validador encerrada com segurança ! 
```

## 🔍 Possíveis melhorias futuras

- Criar uma exceção customizada específica também para o valor inválido (`ValorInvalidoError`), em vez de usar `ValueError` genérico
- Permitir novas tentativas de digitação em caso de erro, em vez de encerrar o programa
- Validar também o formato de valores monetários digitados com vírgula (padrão brasileiro)
- Adicionar testes automatizados (`unittest` ou `pytest`) para validar diferentes formatos de e-mail

## 👤 Autor

Projeto desenvolvido por DAVI RAPOSO PEREIRA como parte dos estudos de tratamento de exceções e expressões regulares em Python.
