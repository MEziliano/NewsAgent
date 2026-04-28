# NewsAgent 📰🤖

O **NewsAgent** é um sistema inteligente de curadoria de notícias automatizado, construído com o framework **CrewAI**. Ele utiliza múltiplos agentes de IA para monitorar feeds RSS, analisar o contexto das notícias e gerar uma newsletter profissional e elegante em formato HTML.

O projeto foi projetado para rodar localmente utilizando o **Ollama**, garantindo privacidade e baixo custo.

---

## 🚀 Funcionalidades

-   🔍 **Monitoramento de RSS**: Coleta automática de notícias de múltiplas fontes.
-   🧠 **Análise Inteligente**: Avaliação do impacto e contexto das notícias usando LLMs locais.
-   🌐 **Pesquisa Complementar**: Busca informações adicionais na web via DuckDuckGo para enriquecer a análise.
-   🎨 **Newsletter Premium**: Geração de um relatório final em HTML com design moderno (Glassmorphism + Tailwind CSS).
-   💻 **Execução Local**: Totalmente integrado com Ollama (Llama 3.2, etc).

---

## 🏗️ Arquitetura dos Agentes

O sistema opera com três agentes especialistas que trabalham de forma sequencial:

1.  **News Scanner (Scanner de Notícias)**: Especializado em monitorar fluxos de dados e extrair as manchetes mais relevantes dos feeds RSS.
2.  **Market Analyst (Analista de Mercado)**: Responsável por contextualizar as notícias, avaliar tendências e buscar informações extras na internet.
3.  **Senior Editor (Editor Sênior)**: Transforma a análise técnica em uma newsletter envolvente, profissional e fácil de ler.

---

## 🛠️ Tecnologias Utilizadas

-   **[CrewAI](https://crewai.com)**: Orchestramento de agentes inteligentes.
-   **[Ollama](https://ollama.ai)**: Execução de modelos de linguagem (LLMs) localmente.
-   **[LangChain](https://langchain.com)**: Integração com ferramentas de busca e utilitários.
-   **[UV](https://github.com/astral-sh/uv)**: Gerenciador de pacotes e ambientes Python de ultra-performance.
-   **Tailwind CSS**: Estilização da newsletter gerada.

---

## 📋 Pré-requisitos

Antes de começar, você precisará ter instalado em sua máquina:

-   **Python 3.10+**
-   **Ollama**: [Baixar Ollama](https://ollama.ai/)
-   **UV**: (Opcional, mas recomendado) `curl -LsSf https://astral.sh/uv/install.sh | sh`

Certifique-se de que o Ollama está rodando e que você baixou o modelo desejado:
```bash
ollama pull llama3.2:3b
```

---

## ⚙️ Instalação e Configuração

1. **Clonar o repositório**:
   ```bash
   git clone <url-do-repositorio>
   cd NewsAgent
   ```

2. **Instalar dependências**:
   Utilizando o `uv`:
   ```bash
   uv sync
   ```

3. **Configurar variáveis de ambiente**:
   Crie um arquivo `.env` na raiz do projeto (ou copie do `.env.example`):
   ```bash
   cp .env.example .env
   ```
   Edite o arquivo `.env` para apontar para o seu modelo do Ollama:
   ```env
   OLLAMA_MODEL=llama3.2:3b
   ```

---

## 🏃 Como Executar

Para iniciar o processo de curadoria, basta rodar o comando:

```bash
uv run main.py
```

Após a conclusão, o sistema exibirá o resultado no terminal e gerará um arquivo chamado **`newsletter.html`** na raiz do projeto. Basta abri-lo em seu navegador para ver o resultado final.

---

## 📁 Estrutura do Projeto

```text
NewsAgent/
├── src/
│   ├── tools/          # Ferramentas customizadas (RSS Reader, etc)
│   ├── utils/          # Geradores de HTML e templates
│   ├── agents.py       # Definição das personalidades dos agentes
│   ├── tasks.py        # Definição das missões e objetivos
│   ├── crew.py         # Configuração do fluxo da equipe (Crew)
├── main.py             # Ponto de entrada da aplicação
├── pyproject.toml      # Gerenciamento de dependências
└── .env                # Configurações de modelo e chaves
```

---

## 📝 Licença

Este projeto está sob a licença MIT. Veja o arquivo para mais detalhes.

---
*Desenvolvido com ❤️ por Murilo Eziliano.*
