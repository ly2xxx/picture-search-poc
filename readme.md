
### Prerequisites
- Python 3.9 or higher
- Git
<!-- - Ollama setup "ollama run mistral" (see https://dev.to/0xkoji/how-to-run-large-language-models-locally-on-a-windows-machine-using-wsl-and-ollama-55fd) -->

### Installation
Clone the repository :
```bash
git clone https://github.com/ly2xxx/picture-search-poc.git
```

Navigate to the project directory :
```bash
cd picture-search-poc
```

Create a virtual environment :
```bash
python -m venv .venv
.\.venv\Scripts\activate
```

Install the required dependencies in the virtual environment :
```bash
pip install -r requirements.txt
```

<!-- Setup gpt-2 tokenizer manually for langchain ConversationalRetrievalChain :
Copy 
`models\models--gpt2`
to
`C:\Users\[windows-username]\.cache\huggingface\hub\models--gpt2`
![gpt2 manual copy screenshot](Gallery/menu/gpt-2-setup.png?raw=true "gpt2 setup") -->

Launch the chat service locally :
```bash
streamlit run streamlit_app.py
```
#### That's it! The AI chatbot is now up and running locally. 🤗