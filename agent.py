"""
Travel Agent - Google Gemini + LangChain 0.1.17 (pydantic_v1 FIXED)
"""

import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain.agents import initialize_agent, AgentType
from tools import (
    search_flights, search_hotels, search_attractions,
    get_weather, estimate_budget, get_city_coordinates
)

load_dotenv()

@tool
def search_flight(source: str, destination: str, preference: str = "cheapest"):
    """Search for flights between cities."""
    return search_flights(source, destination, preference)

@tool
def search_hotel(city: str, preference: str = "best_rated"):
    """Search for hotels in a city."""
    return search_hotels(city, preference)

@tool
def search_place(city: str, category: str = None):
    """Search for attractions and places to visit."""
    return search_attractions(city, category)

@tool
def check_weather(city: str, days: int = 3):
    """Get weather forecast for a city."""
    lat, lon = get_city_coordinates(city)
    if lat == 0:
        return {"status": "error", "message": f"City {city} not found"}
    return get_weather(city, lat, lon, days)

@tool
def calculate_budget(flight_price: float = 0, hotel_per_night: float = 0, num_nights: int = 3):
    """Calculate trip budget."""
    return estimate_budget(flight_price, hotel_per_night, num_nights)

def create_travel_agent():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY missing! Get free key: https://ai.google.dev/")
    
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=api_key,
        temperature=0.1
    )
    
    tools = [search_flight, search_hotel, search_place, check_weather, calculate_budget]
    
    agent = initialize_agent(
        tools=tools,
        llm=llm,
        agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,  # Works with v0.1.17
        verbose=True,
        handle_parsing_errors=True
    )
    
    return agent

def plan_trip(user_query: str):
    try:
        agent = create_travel_agent()
        result = agent.run(user_query)
        return {"status": "success", "output": result}
    except Exception as e:
        return {
            "status": "error",
            "message": f"Agent error: {str(e)}",
            "error_type": type(e).__name__
        }
