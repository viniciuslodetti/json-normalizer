# JSON Normalizer

> Uma ferramenta leve em Python para limpar, padronizar e normalizar arquivos JSON, preservando sua estrutura original.

🇺🇸 **English version:** [README.md](README.md)

---

## ✨ Funcionalidades

- 🧹 Remove tags HTML
- 📄 Remove espaços em branco desnecessários
- ✍️ Normaliza textos
- 📅 Padroniza a formatação de datas
- 📂 Preserva a estrutura original do JSON
- ⚡ Rápido e leve
- 🔗 Fácil de integrar a outros projetos

---

## 📁 Pasta dos arquivos

Coloque o(s) arquivo(s) JSON que deseja tratar dentro da pasta:

```text
/jsons
```

---

## 🚀 Como executar

### Clone o repositório

```bash
git clone https://github.com/viniciuslodetti/json-normalizer.git
```

Ou faça o download do projeto em formato ZIP.

### Instale as dependências

```bash
pip install -r requirements.txt
```

### Execute o programa

```bash
python main.py
```

---

## 📄 Resultado

Após a execução, será gerado um novo arquivo JSON com o nome original acrescido do sufixo **Tratado**.

Exemplo:

```text
products.json
        ↓
productsTratado.json
```

---

## 📌 Observações

- O arquivo original nunca é alterado.
- O JSON tratado é salvo automaticamente.
- Todos os arquivos de entrada devem estar na pasta `/jsons`.

---

## 🤝 Contribuições

Sugestões, melhorias e contribuições são sempre bem-vindas.

Sinta-se à vontade para abrir uma Issue ou enviar um Pull Request.

---

## 📄 Licença

Este projeto está licenciado sob a licença MIT.
