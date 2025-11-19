import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configure Gemini API
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    st.error("❌ GEMINI_API_KEY not found. Please check your .env file")
    st.stop()

genai.configure(api_key=api_key)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Set page config
st.set_page_config(
    page_title="Arduino & ESP Code Generator",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS for better styling
st.markdown("""
    <style>
    .chat-message {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
        display: flex;
        gap: 1rem;
    }
    .user-message {
        background-color: #e3f2fd;
        border-left: 4px solid #2196F3;
    }
    .assistant-message {
        background-color: #f5f5f5;
        border-left: 4px solid #4CAF50;
    }
    .code-block {
        background-color: #1e1e1e;
        color: #d4d4d4;
        padding: 1rem;
        border-radius: 0.5rem;
        font-family: 'Courier New', monospace;
        overflow-x: auto;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar
with st.sidebar:
    st.title("⚙️ Configuration")
    
    # Select board type
    board_type = st.selectbox(
        "Select Board Type:",
        ["Arduino UNO", "Arduino Mega", "Arduino Nano", "ESP32", "ESP8266", "ESP32-S3"]
    )
    
    # Select project type
    project_type = st.selectbox(
        "Project Category:",
        [
            "Temperature & Humidity Sensor (DHT11/DHT22)",
            "Motion Detection (PIR Sensor)",
            "Distance Measurement (Ultrasonic)",
            "Light Sensor (LDR)",
            "Soil Moisture Sensor",
            "Gas Detection (MQ-5/MQ-7)",
            "Flame Detection",
            "LCD Display",
            "Servo Motor Control",
            "RFID Reader",
            "GPS Module",
            "Bluetooth Module (HC-05)",
            "WiFi Connectivity",
            "Cloud Integration (ThingSpeak/Firebase)",
            "IoT Data Logging",
            "Custom Project"
        ]
    )
    
    st.divider()
    st.info("💡 Tip: Provide detailed descriptions for better code generation!")
    
    if st.button("🗑️ Clear Chat History", use_container_width=True):
        st.session_state.messages = []
        st.rerun()

# Main header
st.title("🤖 Arduino & ESP Code Generator")
st.caption("AI-powered code generation for your IoT and embedded projects")

# Display chat history
for message in st.session_state.messages:
    if message["role"] == "user":
        st.markdown(f"""
        <div class="chat-message user-message">
            <div>👤 <b>You:</b><br/>{message["content"]}</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div class="chat-message assistant-message">
            <div>🤖 <b>AI Assistant:</b><br/>{message["content"]}</div>
        </div>
        """, unsafe_allow_html=True)

# Input area
st.divider()
col1, col2 = st.columns([0.9, 0.1])

with col1:
    user_input = st.text_input(
        "Enter your requirement:",
        placeholder="E.g., Create code to read temperature from DHT22 and display on serial monitor...",
        label_visibility="collapsed"
    )

with col2:
    send_button = st.button("📤 Send", use_container_width=True)

# Process user input
if send_button and user_input.strip():
    # Add user message to history
    st.session_state.messages.append({"role": "user", "content": user_input})
    
    # Create the prompt for Gemini
    system_prompt = f"""You are an expert embedded systems and IoT programmer specializing in Arduino and ESP board programming. 
    
The user is asking for code to work with: {board_type}
Project Category: {project_type}

When generating code:
1. Provide complete, working code with all necessary includes and configurations
2. Add detailed comments explaining each section
3. Include pin definitions clearly
4. Add setup() and loop() functions for Arduino-style code
5. Include any necessary sensor initialization and calibration
6. Add error handling where appropriate
7. Provide library recommendations if external libraries are needed
8. Format code clearly with proper indentation
9. Include example output or expected behavior
10. Add troubleshooting tips if relevant

The user asks: {user_input}"""
    
    try:
        # Call Gemini API
        # Using gemini-2.5-flash: Latest, fastest, and most efficient model
        model = genai.GenerativeModel("gemini-2.5-flash")
        response = model.generate_content(system_prompt)
        assistant_message = response.text
        
        # Add assistant response to history
        st.session_state.messages.append({"role": "assistant", "content": assistant_message})
        
        # Rerun to display the new message
        st.rerun()
        
    except Exception as e:
        st.error(f"❌ Error generating response: {str(e)}")
        st.info("Please check your API key and internet connection")

# Footer
st.divider()
st.markdown("""
---
<div style='text-align: center'>
    <p style='font-size: 0.9em; color: #666'>
        Arduino & ESP Code Generator | Powered by Google Gemini AI
    </p>
</div>
""", unsafe_allow_html=True)
