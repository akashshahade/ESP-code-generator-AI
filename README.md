# Arduino & ESP Code Generator 🤖

An AI-powered Streamlit application that generates complete code for Arduino and ESP board projects using Google's **Gemini 2.5 Flash** API. Perfect for IoT and embedded systems projects!

## ⚡ Model Information

This project uses **Gemini 2.5 Flash** - Google's latest, fastest, and most efficient LLM:

| Feature | Benefit |
|---------|---------|
| **Latest Model** | Gemini 2.5 Flash (Released 2025) |
| **Speed** | Ultra-fast response times - perfect for real-time code generation |
| **Efficiency** | Optimized token usage reduces costs and latency |
| **Accuracy** | Highly accurate code generation for embedded systems |
| **Context Window** | Large enough to handle complex IoT projects |
| **Cost-Effective** | Most efficient model in its class |

---

## Features ✨

- **Chat Interface**: Easy-to-use conversational UI for code generation
- **Multiple Board Support**: Arduino UNO, Mega, Nano, ESP32, ESP8266, ESP32-S3
- **Project Templates**: Pre-configured categories for common IoT projects
- **AI-Powered**: Uses Google Gemini 2.5 Flash API for intelligent code generation
- **Complete Code**: Generates production-ready code with comments and error handling
- **Real-time Chat History**: Keep track of all your code generation requests

## Project Categories 📚

The application supports code generation for:
- Temperature & Humidity Sensors (DHT11/DHT22)
- Motion Detection (PIR Sensors)
- Distance Measurement (Ultrasonic Sensors)
- Light Sensors (LDR)
- Soil Moisture Sensors
- Gas Detection (MQ-5/MQ-7)
- Flame Detection
- LCD Displays
- Servo Motor Control
- RFID Readers
- GPS Modules
- Bluetooth Modules (HC-05)
- WiFi Connectivity
- Cloud Integration (ThingSpeak/Firebase)
- IoT Data Logging
- Custom Projects

## Prerequisites 📋

- Python 3.8 or higher
- A Google Cloud account with Gemini API access
- pip (Python package manager)

## Setup Instructions 🚀

### Step 1: Get Your Gemini API Key

1. Go to [Google AI Studio](https://aistudio.google.com/app/apikey)
2. Click on "Create API Key" button
3. Select or create a Google Cloud project
4. Copy the generated API key

### Step 2: Install Dependencies

Navigate to the project directory and install required packages:

```bash
pip install -r requirements.txt
```

### Step 3: Configure Your API Key

**Choose ONE of the following methods:**

#### Method 1: Using `.env` File (Recommended) 📌

1. In the project directory, rename `.env.example` to `.env`:
   ```bash
   copy .env.example .env
   ```
   Or on macOS/Linux:
   ```bash
   cp .env.example .env
   ```

2. Open the `.env` file in a text editor and replace the placeholder:
   ```
   GEMINI_API_KEY=your_actual_api_key_here
   ```

3. Save the file

**File Location:** `c:\Users\Akash\gemini trial\arduino_code_generator\.env`

#### Method 2: Using Environment Variable

Set the environment variable in your system:

**Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY = "your_actual_api_key_here"
```

**Windows (Command Prompt):**
```cmd
set GEMINI_API_KEY=your_actual_api_key_here
```

**macOS/Linux:**
```bash
export GEMINI_API_KEY="your_actual_api_key_here"
```

### Step 4: Run the Application

From the project directory, run:

```bash
streamlit run app.py
```

The application will open in your default web browser at `http://localhost:8501`

## Usage Guide 📖

1. **Select Board Type**: Choose your target board from the sidebar (e.g., ESP32, Arduino UNO)
2. **Choose Project Category**: Select what type of project you're working on
3. **Describe Your Requirements**: Write a detailed description of what you need
4. **Generate Code**: Click the "Send" button to generate code using AI
5. **View Results**: The generated code appears in the chat interface

### Example Queries:

- "Generate code to read DHT22 sensor and send data to ThingSpeak"
- "Create a motion detection system with alarm buzzer"
- "Write code for WiFi-enabled temperature and humidity monitoring"
- "Generate code for an RFID-based door lock system"

## Project Structure 📁

```
arduino_code_generator/
├── app.py                 # Main Streamlit application
├── requirements.txt       # Python dependencies
├── .env.example          # API key configuration template
└── .env                  # Your actual API key (CREATE THIS FILE)
```

## Important Security Notes 🔒

- **NEVER** commit the `.env` file to version control
- **NEVER** share your API key publicly
- If you accidentally expose your key, regenerate it immediately from [Google AI Studio](https://aistudio.google.com/app/apikey)
- Use `.env` file for local development only

## Troubleshooting 🔧

### Error: "GEMINI_API_KEY not found"
- Ensure `.env` file exists in the project directory
- Verify the file contains: `GEMINI_API_KEY=your_key`
- Make sure there are no spaces around the `=` sign
- Restart the Streamlit app after creating/modifying `.env`

### Error: "API Key invalid or expired"
- Check your API key in [Google AI Studio](https://aistudio.google.com/app/apikey)
- Regenerate a new key if needed
- Ensure the key is correctly pasted without extra spaces

### Streamlit not found
- Install Streamlit: `pip install -r requirements.txt`
- Verify installation: `streamlit --version`

### Port 8501 already in use
- Use a different port: `streamlit run app.py --server.port 8502`

## API Limits ⚠️

Google Gemini API has usage limits:
- Free tier: 60 requests per minute
- For production use, check Google's pricing and quota management

## Customization 🎨

To modify the application:

1. **Add More Boards**: Edit the `board_type` selectbox in the sidebar
2. **Add More Project Types**: Edit the `project_type` selectbox in the sidebar
3. **Customize Styling**: Modify the CSS in the `st.markdown()` section
4. **Change System Prompt**: Edit the `system_prompt` variable to adjust AI behavior

## Required Python Packages

- `streamlit==1.32.0` - Web framework (Latest stable)
- `google-generativeai==0.8.4` - Gemini API client (Latest)
- `python-dotenv==1.0.0` - Environment variable loader

## Support 💬

For issues with:
- **Streamlit**: [Streamlit Documentation](https://docs.streamlit.io/)
- **Gemini API**: [Google AI Documentation](https://ai.google.dev/)
- **Arduino/ESP**: [Arduino Official Site](https://www.arduino.cc/) | [ESP32 Documentation](https://docs.espressif.com/)

## License 📄

This project is open source and available for personal and educational use.

---

**Happy Coding! 🚀**
