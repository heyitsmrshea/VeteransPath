
# 🇺🇸 VeteransPath

**VeteransPath** is a personalized web app built with [Streamlit](https://streamlit.io/) that helps transitioning service members navigate their civilian career journey with AI-powered support.

## ✨ Features

- 🔍 Smart onboarding — capture branch, MOS, rank, and goals
- 📄 Resume Builder — paste FITREP/eval content and receive tailored civilian resume bullets using GPT-4
- 📁 Downloadable resume templates — curated for PM, Cyber, and more
- 🧠 Future roadmap: interview prep, job matching, FITREP auto translation, and more

## 🛠 How It Works

1. Choose your transition goal (e.g., "Build my resume")
2. Upload your FITREP or paste a summary of experience
3. Enter the target civilian role you're applying for
4. Let GPT-4 generate high-quality resume bullets
5. Download a curated template and start building

## 🚀 Getting Started (Local Dev)

1. Clone the repo:
```bash
git clone https://github.com/heyitsmrshea/VeteransPath.git
cd VeteransPath
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set your OpenAI key:
```bash
export OPENAI_API_KEY=sk-...
```

4. Run the app:
```bash
streamlit run app.py
```

## 🔐 Secrets for Deployment

For Streamlit Cloud, store your OpenAI key in `.streamlit/secrets.toml`:

```toml
OPENAI_API_KEY = "sk-..."
```

## 📄 License

MIT License — free to use, modify, and deploy to support your veteran community.

## 🙌 Built by Andrew Shea

Veteran. Cybersecurity leader. Dedicated to helping others transition with purpose and clarity.
