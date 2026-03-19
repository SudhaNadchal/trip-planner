import streamlit as st
from openai import OpenAI
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# UI Configuration
st.set_page_config(page_title="AI Travel Planner", page_icon="✈️")
st.title("🌍 Smart Travel Planner")
st.subheader("Where to next?")

# Sidebar for preferences
with st.sidebar:
    st.header("Settings")
    days = st.slider("Number of days", 1, 14, 3)
    budget = st.selectbox("Budget level", ["Budget", "Mid-range", "Luxury"])

# Main input
user_prompt = st.text_area(
    "Describe your vibe (e.g., 'A romantic 3-day trip to Kyoto focusing on food and temples')",
    placeholder="I want a 5-day adventure in Iceland..."
)

if st.button("Generate Itinerary"):
    if user_prompt:
        with st.spinner("Mapping out your journey..."):
            try:
                # Constructing the system prompt
                system_msg = f"You are an expert travel consultant. Create a {days}-day {budget} itinerary."
                
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
                    messages=[
                        {"role": "system", "content": system_msg},
                        {"role": "user", "content": user_prompt}
                    ]
                )
                
                itinerary = response.choices[0].message.content
                
                st.success("Your Trip is Ready!")
                st.markdown(itinerary)
                
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please tell me a bit about where you want to go!")