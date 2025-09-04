# 🍽️ AI-Powered Restaurant Menu Generator

An interactive web app that generates **restaurant names** and **menu items** based on a chosen cuisine, powered by **LLMs (LangChain + GPT)**. The app also fetches and displays **food images dynamically** for each menu item using the **Google Custom Search API** (or any stock photo API).

---

## ✨ Features
- 🔮 **AI-Generated Restaurant Names** – creative branding ideas with GPT.  
- 📜 **Menu Suggestions** – cuisine-specific dishes, generated via LangChain chains.  
- 🖼️ **Dynamic Food Images** – fetched automatically with Google Images API (or Unsplash/Pexels/Pixabay).  
- 🎨 **Clean UI** – Streamlit front-end with sidebar inputs, structured cards, and images.  
- ⚡ **Full-Stack Prototype** – demonstrates prompt engineering, API integration, and rapid prototyping.

---

## 🛠️ Tech Stack
- **Python 3.10+**
- [Streamlit](https://streamlit.io/) – web front-end  
- [LangChain](https://www.langchain.com/) – LLM orchestration  
- [OpenAI / OpenRouter](https://openai.com/) – GPT models  
- [Google Custom Search API](https://developers.google.com/custom-search) (or alternative: Unsplash, Pexels, Pixabay) – stock food images  

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/yourusername/ai-restaurant-menu-generator.git
cd ai-restaurant-menu-generator
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Set up API keys
Create a file `.streamlit/secrets.toml` in the project root:

```toml
OPENAI_API_KEY = "your_openai_or_openrouter_key"
OPENAI_BASE_URL = "https://openrouter.ai/api/v1"  # optional, for OpenRouter
GOOGLE_API_KEY = "your_google_api_key"
GOOGLE_CSE_ID = "your_custom_search_engine_id"
```

*(Or replace with `UNSPLASH_ACCESS_KEY`, `PEXELS_API_KEY`, or `PIXABAY_API_KEY` if using those providers instead of Google.)*

### 4. Run the app
```bash
streamlit run main.py
```

---

## 📸 Demo
<img width="1918" height="920" alt="image" src="https://github.com/user-attachments/assets/25e14b5d-164a-4178-9c32-47d36d66fa84" />
[DEMO](https://ai-restaurant-menu-generator.streamlit.app/)
---

## 📂 Project Structure
```
├── main.py          # Streamlit front-end
├── model.py         # LangChain chains and LLM logic
├── requirements.txt # Dependencies
└── .streamlit/
    └── secrets.toml # API keys (not committed to GitHub)
```

---

## 🔑 Example Usage
1. Enter a cuisine type (e.g., *Italian*, *Japanese*, *Mexican*) in the sidebar.  
2. The app generates:
   - A creative **restaurant name**  
   - A list of **menu items**  
   - Relevant **food images** displayed dynamically.  

---

## 📌 Skills Demonstrated
- Prompt Engineering  
- LLM Application Development (LangChain + GPT)  
- API Integration (OpenAI, Google, stock image APIs)  
- Full-Stack Prototyping with Streamlit  
- Clean UI/UX Design  

---

## 🧑‍💻 Author
**MAROUAN MORAKIB** – [LinkedIn](https://www.linkedin.com/in/marouan-morakib/) 
