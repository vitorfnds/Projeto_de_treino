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

## salvar_local
- **O que faz:** adiciona todos os arquivos modificados e cria um commit apenas no diretório local.
- **Uso:** `salvar_local` ou `salvar_local: mensagem do commit`
- **Descrição:** não faz push para o GitHub; apenas salva a alteração no histórico local.

## salvar_web
- **O que faz:** adiciona todos os arquivos modificados, cria um commit e envia para o GitHub.
- **Uso:** `salvar_web` ou `salvar_web: mensagem do commit`
- **Descrição:** salva localmente e atualiza o repositório remoto em seguida.

## add_cd
- **O que faz:** sinaliza que uma alteração no código deve ser feita pelo assistente.
- **Uso:** `add_cd`
- **Descrição:** adicione esse comando antes de pedir qualquer modificação no código para evitar alterações não autorizadas.

## Observações
- O comando `atualizar_tudo` continua disponível como atalho para salvar e enviar para o GitHub.
- Use `salvar_local` quando quiser apenas salvar o histórico local e não enviar imediatamente.
- Use `salvar_web` quando quiser salvar localmente e atualizar o GitHub em seguida.
- Caso haja conflitos entre o repositório local e o remoto, será necessário resolver e sincronizar manualmente.
- O GitHub será atualizado automaticamente depois que o push for executado com sucesso com `salvar_web` ou `atualizar_tudo`.
