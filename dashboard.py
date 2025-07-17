import streamlit as st
import pandas as pd
import json
import re

from extractor import extract_action_items
from deadline_parser import convert_deadline_to_date
from calendar_event import create_calendar_event
from email_sender import send_task_email
from task_logger import save_task_entry

# ---- 1. Page setup ----
st.set_page_config(page_title="Meeting Assistant", layout="centered")
st.title("🤖 Meeting Assistant Agent")

# ---- 2. Input: Meeting transcript ----
transcript = st.text_area("📝 Paste your meeting transcript here")

# ---- 3. Extract Action Items ----
if st.button("📤 Extract Action Items"):
    with st.spinner("Processing with LLM..."):
        raw_output = extract_action_items(transcript)
        st.subheader("🧠 Raw Output from LLM")
        st.code(raw_output)

        try:
            # Extract JSON array using regex
            match = re.search(r'\[.*\]', raw_output, re.DOTALL)
            if not match:
                raise ValueError("No JSON array found in LLM response.")
            action_items = json.loads(match.group(0))

            # Parse deadlines to ISO format
            for item in action_items:
                dl = item.get("deadline")
                item["date"] = convert_deadline_to_date(dl) if dl else "Not given"

            # Save to Streamlit session
            st.session_state["action_items"] = action_items

            # Display structured table
            st.subheader("📋 Structured Action Items")
            st.table(action_items)

            # CSV download
            df = pd.DataFrame(action_items)
            csv = df.to_csv(index=False).encode('utf-8')
            st.download_button("📥 Download CSV", data=csv, file_name="action_items.csv", mime="text/csv")

        except Exception as e:
            st.error(f"⚠️ Could not parse JSON from LLM: {e}")
            st.code(raw_output)



# ---- 4. Bulk email, calendar, logging ----
user_emails = {
    "Priya": "priyarvishwaroop2003@gmail.com",
    "Sneha": "sneha11@gmail.com",
    "Rahul": "rahul@gmail.com",
    "Meena": "meena12@gmail.com"
}

if st.button("📧 Send Emails + Calendar + Log All"):
    action_items = st.session_state.get("action_items", [])
    
    if not action_items:
        st.warning("⚠️ No action items found. Please extract first.")
    else:
        for task in action_items:
            name = task.get('name')
            email = user_emails.get(name)
            task_text = task.get('task')
            task_date = task.get('date')

            if name and task_text and task_date and email and task_date != "Not given":
                link = create_calendar_event(task_text, task_date, email)
                send_task_email(email, name, task_text, task_date)
                save_task_entry(name, email, task_text, task_date)
                st.success(f"✅ Task for {name} added to Calendar + Email sent + Logged")
            else:
                st.warning(f"⚠️ Missing info for task: {task}")
