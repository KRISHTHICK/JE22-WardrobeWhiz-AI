# JE22-WardrobeWhiz-AI
Gen Ai
🧺 WardrobeWhiz AI – Smart Closet Organizer & Fashion Planner

🔹 Topic Overview:
WardrobeWhiz AI is an AI-powered app that helps users organize clothing images, suggest outfit combinations based on seasons and colors, and lets them interact with an AI fashion agent. It supports Retrieval-Augmented Generation (RAG) by allowing users to upload fashion PDFs and ask questions from them.

🔧 Key Features:
Upload Clothing Images: AI detects type, color, and seasonal wear.

Outfit Combination Generator: Matches clothes to suggest stylish combos.

Fashion AI Agent: Answer style questions using Ollama models.

PDF-Based RAG: Upload your fashion guide PDFs and ask questions.


🎯 Overview:
WardrobeWhiz AI is an intelligent virtual closet assistant that lets users upload pictures of their real clothes, automatically tags and categorizes them (color, type, season), and then helps plan outfits for different events or weather using an AI agent. Optionally, it uses RAG to answer styling questions based on user-uploaded PDF style guides or trend reports.

🌟 Key Features:
Feature	Description
👕 Virtual Wardrobe Upload	Upload clothing photos; system detects type (shirt, jeans), color, season
🧠 AI Outfit Planner Agent	Asks AI: "What should I wear for a summer wedding?"
🧩 Outfit Combiner	Suggests top + bottom + accessory combinations from the uploaded wardrobe
📆 Look Planner Calendar	Plan outfits for the week or special events
📄 RAG-based Style Advisor	Upload fashion PDFs → Ask questions (e.g., "What's in trend for 2025?")
✍️ Blog & Caption Generator	Auto-write captions or blog posts about planned outfits

## 🚀 How to Run

### Step 1: Clone Repo
```bash
git clone https://github.com/yourname/WardrobeWhiz-AI.git
cd WardrobeWhiz-AI
Step 2: Install dependencies
bash
Copy
Edit
pip install -r requirements.txt
Step 3: Start Ollama and pull model
bash
Copy
Edit
ollama serve
ollama pull tinyllama
Step 4: Run the App
bash
Copy
Edit
streamlit run app.py
