# Optify

O **Optify** é um aplicativo desenvolvido para ajudar a melhorar a saúde e o bem-estar no ambiente de trabalho ou estudo, lembrando os usuários de pausas regulares, se hidratarem e sobre a regra 20-20-20. Como míope, um aplicativo como esse me ajuda a manter a saúde ocular e evitar de ficar cego :D

## Funcionalidades

- Lembretes da **regra 20-20-20**: Uma notificação a cada 20 minutos lembrando o usuário de olhar para algo a 20 pés (~6 metros) por 20 segundos.
- Lembrete de **pausa horária**: Lembrete a cada hora para o usuário levantar e se mover por 5 minutos.
- Lembrete de **hidratação**: Notificação a cada hora para o usuário beber água.

## Instalação

Para instalar e executar o Optify, siga os seguintes passos:

1. **Clone o repositório:**

   ```bash
   git clone https://github.com/raul772/optify.git
   cd optify
   ```

2. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Execute o aplicativo:**

   ```bash
   python main.py
   ```

4. **Empacote o aplicativo (Windows 10+) (Opcional):**

   Se você quiser empacotar o aplicativo como um executável `.exe` usando **PyInstaller**, basta rodar o seguinte comando:

   ```bash
   pyinstaller optify.specs
   ```

   O comando acima criará um arquivo `.exe` dentro da pasta `dist/`.
   Por vezes, o arquivo `.exe` gerado pode ser apontado como ameaça, isso ocorre por falta de assinatura digital do software. Para todos os efeitos, o código é simples e pode ser conferido antes de ser executado.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- `main.py`: O script principal que executa o aplicativo, gerencia as notificações e a bandeja do sistema.
- `icon.ico`: O ícone do aplicativo utilizado nas notificações e na bandeja do sistema.
- `optify.spec`: Arquivo de configuração do PyInstaller para empacotar o aplicativo.
- `requirements.txt`: Lista de dependências do projeto.
- `version.txt`: Arquivo que contém informações sobre a versão do aplicativo.

## Dependências

Este projeto utiliza as seguintes bibliotecas:

- **plyer**: Para exibir notificações nativas no sistema operacional.
- **pystray**: Para criar o ícone de bandeja do sistema.
- **Pillow**: Para manipular imagens, como o ícone da bandeja.
- **win10toast**: Para exibir notificações no Windows 10+.
- **pyinstaller**: Para empacotamento em exe.


