# Comandos Git do projeto

Este arquivo descreve os comandos personalizados e o que eles fazem. Use-o como referência caso esqueça algum passo.

## atualizar_tudo
- **O que faz:** adiciona todos os arquivos modificados, cria um commit e envia para o GitHub.
- **Uso padrão:** `atualizar_tudo`
- **Descrição:** quando não houver mensagem específica, o commit será feito com uma mensagem padrão.

## atualizar_tudo: mensagem do commit
- **O que faz:** adiciona todos os arquivos modificados, cria um commit com a mensagem fornecida e envia para o GitHub.
- **Uso:** `atualizar_tudo: Implementar nova tela de menu`
- **Descrição:** use sempre que quiser registrar o motivo da alteração.

## Observações
- O comando `atualizar_tudo` deve ser usado após testar e verificar que o código está funcionando.
- Caso haja conflitos entre o repositório local e o remoto, será necessário resolver e sincronizar manualmente.
- O GitHub será atualizado automaticamente depois que o push for executado com sucesso.
