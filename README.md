# 🌍 AI-Based Travel Planning Assistant Using LangChain

A complete, production-ready AI-powered travel planning application that autonomously creates personalized trip itineraries with flights, hotels, attractions, weather forecasts, and budget breakdowns.

## 🎯 Project Highlights

| Feature | Details |
|---------|---------|
| **AI Framework** | LangChain + OpenAI GPT (Agentic AI) |
| **Interface** | Streamlit Web Application |
| **Tools** | 5 integrated tools (Flights, Hotels, Attractions, Weather, Budget) |
| **Weather API** | Open-Meteo (Free, No API Key Required) |
| **Data** | JSON-based flight, hotel, and attraction datasets |
| **Code Quality** | Production-ready with error handling, PEP 8 standards |
| **Languages** | Python 3.8+ |

## 📋 Project Requirements Met

✅ **Problem Statement** - Solves the problem of tedious manual trip planning  
✅ **Agentic AI** - Uses LangChain ReAct pattern for autonomous reasoning  
✅ **Multiple Tools** - 5 integrated tools for complete trip planning  
✅ **Real Data** - JSON datasets + Open-Meteo API integration  
✅ **Structured Output** - Clean, detailed itinerary format  
✅ **UI** - Streamlit interactive interface  
✅ **Clean Code** - Modular, documented, error-handled  
✅ **Error Handling** - Try-except blocks throughout  

## 🚀 Quick Start

### 1. Clone/Setup Project
```bash
mkdir travel-assistant
cd travel-assistant
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 2. Create .env File
```
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Run Application
```bash
streamlit run app.py
```

### 5. Open Browser
Navigate to `http://localhost:8501`

## 📂 Project Structure

```
travel-assistant/
├── app.py                    # Streamlit UI (main entry point)
├── agent.py                  # LangChain agent with tools
├── tools.py                  # All 5 tool implementations
├── data/
│   ├── flights.json         # 10+ flight options
│   ├── hotels.json          # 10+ hotel options
│   └── places.json          # 12+ attractions
├── .env                     # API keys (create this)
├── requirements.txt         # Python dependencies
├── setup-guide.md           # Installation guide
├── running-guide.md         # Detailed running instructions
└── README.md                # This file
```

## 🔧 Technologies Used

### Core
- **Python 3.8+** - Programming language
- **LangChain** - Agentic AI framework
- **OpenAI API** - GPT-3.5-turbo for reasoning
- **Streamlit** - Web UI framework

### APIs & Data
- **Open-Meteo API** - Weather forecasts (free)
- **JSON Files** - Flight, hotel, places databases
- **Requests Library** - HTTP requests

### Tools & Libraries
- **python-dotenv** - Environment variable management
- **pandas** - Data handling
- **datetime** - Date manipulation

## 🎯 Five Core Tools

### 1️⃣ Flight Search Tool
```python
search_flights(source: str, destination: str, prefer: str)
```
- Filters flights by origin and destination
- Options: cheapest or fastest
- Returns best match with price, time, duration

### 2️⃣ Hotel Search Tool
```python
search_hotels(city: str, prefer: str)
```
- Finds hotels in destination city
- Options: best_rated, cheapest, luxury
- Returns name, rating, price, amenities

### 3️⃣ Attractions Tool
```python
search_attractions(city: str, category: str)
```
- Discovers top-rated attractions
- Optional category filtering
- Returns top 5 by rating with descriptions

### 4️⃣ Weather Tool
```python
get_weather(city: str, lat: float, lon: float, days: int)
```
- Real-time forecast from Open-Meteo API
- No API key required
- Returns temperature and weather condition

### 5️⃣ Budget Calculator
```python
estimate_budget(flight_price, hotel_per_night, num_nights, ...)
```
- Calculates total trip cost
- Includes flights, hotels, food, transport, attractions
- Returns detailed breakdown

## 💡 How It Works

```
User Input
    ↓
[Streamlit UI] → Takes trip requirements
    ↓
[LangChain Agent] → Understands query
    ↓
[Tool Calling] → Autonomously decides which tools to use
    ├─ Calls search_flights()
    ├─ Calls search_hotels()
    ├─ Calls search_attractions()
    ├─ Calls get_weather()
    └─ Calls estimate_budget()
    ↓
[Data Processing] → Analyzes results
    ↓
[Itinerary Generation] → Creates day-wise plan
    ↓
[Formatting] → Structures output beautifully
    ↓
[Display] → Shows in Streamlit UI
```

## 📝 Example Usage

### Input
```
Plan a 3-day trip to Goa from Delhi. 
I prefer beaches and water sports. 
Budget: 15000 rupees.
```

### Output
```
YOUR 3-DAY TRIP TO GOA

FLIGHT SELECTED:
✈️ SpiceJet Flight
  From: Delhi → To: Goa
  Time: 08:00 - 10:15 (2h 15m)
  Price: ₹4,200
  Seats: Available

HOTEL RECOMMENDATION:
🏨 Sunbeach Cottage
  Rating: ⭐ 4.3/5
  Price: ₹2,800/night
  Amenities: Beach Access, Restaurant, WiFi, Spa
  
WEATHER FORECAST:
🌤️ Day 1: Sunny (31°C)
⛅ Day 2: Partly Cloudy (30°C)  
🌊 Day 3: Light Breeze (29°C)

DAILY ITINERARY:
📍 Day 1: Arrival → Baga Beach → Candolim Market
📍 Day 2: Water Sports at Calangute → Local dining
📍 Day 3: Heritage tour → Beach sunset

BUDGET BREAKDOWN:
  Flight: ₹4,200
  Hotel (3 nights): ₹8,400
  Meals: ₹4,500
  Transport: ₹900
  Attractions: ₹600
  ───────────────
  TOTAL: ₹18,600
```

## 🎮 Features

### Agent Capabilities
- ✅ Multi-step reasoning (ReAct pattern)
- ✅ Autonomous tool selection
- ✅ Dynamic decision making
- ✅ Error recovery
- ✅ Detailed explanations

### UI Features
- ✅ Beautiful Streamlit interface
- ✅ Real-time processing feedback
- ✅ Example query buttons
- ✅ Sidebar with settings
- ✅ View agent reasoning steps
- ✅ Responsive design

### Data Features
- ✅ 10+ flights per route
- ✅ 10+ hotels per city
- ✅ 12+ attractions
- ✅ 10 supported cities
- ✅ Real weather data
- ✅ Extensible JSON databases

## 🔑 Supported Cities

**India:**
- Delhi, Mumbai, Bangalore, Chennai, Kolkata, Hyderabad, Pune, Goa

**International:**
- Bali, Bangkok

## 📊 Sample Datasets

### Flights (flights.json)
```json
{
  "airline": "IndiGo",
  "source": "Delhi",
  "destination": "Goa",
  "departure": "14:00",
  "arrival": "16:30",
  "price": 4800,
  "duration": "2h 30m",
  "seats_available": 15
}
```

### Hotels (hotels.json)
```json
{
  "name": "Sea View Resort",
  "city": "Goa",
  "rating": 4.5,
  "price_per_night": 3200,
  "amenities": ["WiFi", "Pool", "Beach Access"],
  "rooms_available": 10
}
```

### Places (places.json)
```json
{
  "name": "Baga Beach",
  "city": "Goa",
  "category": "Beach",
  "rating": 4.4,
  "description": "Popular beach with water sports",
  "entry_fee": 0
}
```

## 🛠️ Installation Details

### Prerequisites
- Python 3.8 or higher
- pip package manager
- OpenAI API key (free tier available)
- Internet connection (for weather API & LLM)

### Step-by-Step Setup

1. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Key**
   - Get key from https://platform.openai.com/api-keys
   - Create `.env` file:
     ```
     OPENAI_API_KEY=sk-...
     ```

4. **Run Application**
   ```bash
   streamlit run app.py
   ```

## 🧪 Testing

### Test Agent from CLI
```bash
python agent.py
```

### Test Individual Tools
```python
from tools import search_flights, search_hotels
result = search_flights("Delhi", "Goa", "cheapest")
print(result)
```

## 📚 Code Quality Standards

✅ **PEP 8 Compliance**
- Proper naming conventions
- Consistent formatting
- Proper spacing

✅ **Documentation**
- Docstrings for all functions
- Type hints
- Inline comments

✅ **Error Handling**
- Try-except blocks
- Graceful fallbacks
- User-friendly errors

✅ **Modularity**
- Separated concerns
- Reusable functions
- Clean architecture

## 🚨 Troubleshooting

| Issue | Solution |
|-------|----------|
| "FileNotFoundError: flights.json" | Ensure `data/` folder exists with JSON files |
| "OPENAI_API_KEY not found" | Add key to `.env` or paste in UI sidebar |
| "ModuleNotFoundError: langchain" | Run `pip install -r requirements.txt` |
| "Port 8501 already in use" | Use `streamlit run app.py --server.port 8502` |
| Weather API fails | Normal if offline; system handles gracefully |

## 🔄 Extending the Project

### Add New Cities
Edit `CITY_COORDINATES` in `tools.py`:
```python
CITY_COORDINATES = {
    "New City": (latitude, longitude),
}
```

### Add More Flights/Hotels
Edit JSON files in `data/` folder

### Use Different LLM
In `agent.py`, change:
```python
model="gpt-4"  # Instead of gpt-3.5-turbo
```

### Add Custom Tools
Define with `@tool` decorator in `agent.py`

## 📈 Performance

- **Agent Response Time:** 10-30 seconds
- **API Calls:** ~5-10 per request
- **Data Load Time:** <1 second
- **UI Responsiveness:** Real-time

## 🎓 Learning Outcomes

By completing this project, you'll learn:

1. **LangChain Concepts**
   - Agents and tool calling
   - ReAct pattern
   - Prompt engineering

2. **Agentic AI**
   - Autonomous decision making
   - Multi-step reasoning
   - Tool selection logic

3. **API Integration**
   - OpenAI GPT API
   - Open-Meteo Weather API
   - Custom REST calls

4. **Full Stack Development**
   - Backend (Python)
   - Frontend (Streamlit)
   - Data (JSON)

5. **Production Skills**
   - Error handling
   - Code organization
   - Documentation
   - Testing

## 📝 Project Checklist

- [x] Problem statement addressed
- [x] LangChain agent implemented
- [x] 5 tools fully functional
- [x] JSON databases created
- [x] Real API integration (weather)
- [x] Streamlit UI built
- [x] Error handling implemented
- [x] Code documented
- [x] PEP 8 compliant
- [x] Production ready

## 🎉 Result

A fully functional **AI Travel Planning Assistant** that:
- Understands natural language queries
- Autonomously searches multiple data sources
- Integrates real-time APIs
- Generates personalized itineraries
- Provides detailed cost breakdowns
- Offers justifications for recommendations
- Has beautiful interactive UI

## 📞 Support & Documentation

- **Setup Guide:** `setup-guide.md`
- **Running Guide:** `running-guide.md`
- **Code Comments:** Throughout codebase
- **Docstrings:** All functions documented

## 📄 License

This is an educational project.

## 🙏 Acknowledgments

- OpenAI for GPT API
- Open-Meteo for free weather API
- LangChain for agentic AI framework
- Streamlit for UI framework

---

**🌍 Happy Traveling with AI! ✈️**

Built with ❤️ for learning agentic AI and travel planning.
