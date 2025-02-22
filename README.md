# 🎥 Video Summarizer Agent

## 🚀 Introduction
Welcome to **Video Summarizer Agent**, a powerful AI-driven tool designed to analyze and summarize video content. Using **Google Gemini AI** and **DuckDuckGo**, this application extracts key insights from uploaded videos and provides user-friendly summaries based on user queries.

## 🌟 Features
- 📂 **Upload Video**: Supports `.mp4`, `.mov`, and `.avi` formats (up to 200MB).
- 🧠 **AI-Powered Summarization**: Uses Google Gemini AI to analyze and summarize videos.
- 🌐 **Web-Based Research**: Enhances responses using DuckDuckGo search.
- 🎯 **User-Specific Insights**: Customizable queries for extracting relevant information.
- 🏎️ **Fast & Efficient**: Optimized to handle video processing delays.

## 📦 Tech Stack
- **Frontend**: [Streamlit](https://streamlit.io/) (for the UI)
- **Backend**: Python
- **AI Model**: Google Gemini AI (via `phi.agent`)
- **Search Engine**: DuckDuckGo API
- **Environment Variables**: `dotenv`

## 🛠 Installation

### 1️⃣ Clone the Repository
```bash
  git clone https://github.com/your-username/Video-Summarize-Agent.git
  cd video-summarizer-agent
```

### 2️⃣ Set Up a Virtual Environment (Optional but Recommended)
```bash
  python -m venv venv
  source venv/bin/activate   # On macOS/Linux
  venv\Scripts\activate     # On Windows
```

### 3️⃣ Install Dependencies
```bash
  pip install -r requirements.txt
```

### 4️⃣ Configure API Keys
Create a `.env` file in the project root and add:
```
GOOGLE_API_KEY=your_google_api_key_here
```

### 5️⃣ Run the Application
```bash
  streamlit run app.py
```

## 🎯 Usage Guide
1. **Upload a Video**: Click the upload button and select a video file.
2. **Enter Your Query**: Provide a specific question about the video.
3. **Click 'Summarize'**: The AI will analyze and generate insights.
4. **View Summary**: Read the summarized content right on the interface.

## 🚀 Deployment
To deploy this app on a cloud platform like **Streamlit Cloud**, **Heroku**, or **Render**, follow these steps:
1. Push the repository to GitHub.
2. Configure environment variables on the hosting platform.
3. Deploy using the respective guides for Streamlit, Heroku, or Render.

## ❓ Troubleshooting
- **Error: File is not in an ACTIVE state** → Try increasing the waiting time in the `while` loop.
- **ModuleNotFoundError** → Ensure all dependencies are installed using `pip install -r requirements.txt`.
- **Streamlit not launching** → Ensure Streamlit is installed and activated in the virtual environment.

---
💡 *Star this repo if you find it useful!* ⭐

