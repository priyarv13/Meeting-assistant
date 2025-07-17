
# 🤖 Meeting Assistant Agent

A smart, agentic AI-powered assistant that transforms meeting transcripts into structured task assignments — and follows through with scheduling, emailing, and logging.

---

## 🧠 What It Does

This app simulates an **autonomous meeting assistant**:

- 📝 Accepts raw meeting transcripts
- 🤖 Extracts structured action items using an LLM
- 📅 Adds tasks as events to Google Calendar
- 📧 Sends task reminders via email to team members
- 🗂️ Logs tasks into a file for future tracking
- 📥 Lets you download the full task list as CSV

---

## 🔍 Example Workflow

Paste this into the app:

```
Priya will complete the UI design by July 20. Sneha will finish the backend by July 21. Rahul will deploy the code on July 22. Meena will handle testing and documentation by July 23.
```

The agent will:
✅ Extract tasks  
✅ Assign deadlines  
✅ Email and add them to calendar  
✅ Log everything to a file

---

## 📁 Project Structure

```
Meeting_Assistance/
├── dashboard.py              # Streamlit dashboard (main app)
├── extractor.py              # LLM prompt + response parser
├── deadline_parser.py        # Converts natural language to date
├── calendar_event.py         # Google Calendar event creator
├── email_sender.py           # Sends emails via Gmail SMTP
├── task_logger.py            # Saves tasks to JSON file
├── tasks.json                # Auto-created log file
├── .env                      # API keys & email app password
├── credentials.json          # Google Calendar API credentials
├── token.json                # User auth token (auto-created)
```

---

## 🛠️ Tech Stack

| Component          | Tech Used                        |
|--------------------|----------------------------------|
| LLM                | Together AI (`meta-llama-3`)     |
| UI                 | Streamlit                        |
| Scheduling         | Google Calendar API              |
| Email Notification | Gmail SMTP + App Password        |
| Task Logging       | JSON file logging                |

---

## 🔐 Setup Instructions

### 1. Clone & Install
```bash
git clone https://github.com/your-username/meeting-assistant.git
cd meeting-assistant
pip install -r requirements.txt
```

### 2. Set up `.env`
⚠️ Note:
This project uses environment variables for API keys.
Please create a .env file and add your keys like this:

```
TOGETHER_API_KEY=your_together_api_key
EMAIL_APP_PASSWORD=your_generated_app_password
```

> 🔒 Generate app password: https://myaccount.google.com/apppasswords

### 3. Get Google Calendar API Credentials

🔐 This project requires a credentials.json file for Google Calendar API.
You can generate it from the Google Cloud Console by enabling Calendar API and creating OAuth 2.0 credentials.

- Go to [Google Cloud Console](https://console.cloud.google.com/)
- Enable **Google Calendar API**
- Create **OAuth 2.0** credentials (Desktop app)
- Download `credentials.json` into your project folder

---

## ▶️ Run the App

```bash
streamlit run dashboard.py

```

streamlit run dashboard.py
✅ Features Covered
 Agentic behavior (multi-step decision and automation)

 Natural language understanding (LLM-driven)

 Google Calendar integration

 Email reminders with task info

 Deadline parsing (natural to date)

 Task logging for auditability

 CSV export of action items


👨‍💻 Author
GitHub: @priyarv13