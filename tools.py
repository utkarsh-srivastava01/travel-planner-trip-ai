"""
Tools for Travel Planning Agent
"""

import json
import os
from datetime import datetime, timedelta

def search_flights(source, destination, preference="cheapest"):
    """Search for flights - returns mock data"""
    flights = {
        "flights": [
            {
                "airline": "IndiGo",
                "price": 2500,
                "duration": "2h 15m",
                "departure": "08:00 AM",
                "arrival": "10:15 AM"
            },
            {
                "airline": "Air India",
                "price": 3200,
                "duration": "2h 30m",
                "departure": "10:30 AM",
                "arrival": "1:00 PM"
            },
            {
                "airline": "SpiceJet",
                "price": 2200,
                "duration": "2h 20m",
                "departure": "6:00 PM",
                "arrival": "8:20 PM"
            }
        ],
        "source": source,
        "destination": destination
    }
    
    if preference == "cheapest":
        flights["flights"] = sorted(flights["flights"], key=lambda x: x["price"])
    elif preference == "fastest":
        flights["flights"] = sorted(flights["flights"], key=lambda x: int(x["duration"].split("h")[0]))
    
    return flights

def search_hotels(city, preference="best_rated"):
    """Search for hotels - returns mock data"""
    hotels = {
        "hotels": [
            {
                "name": "Taj Hotel",
                "rating": 4.8,
                "price_per_night": 8000,
                "amenities": ["WiFi", "Pool", "Gym", "Restaurant"]
            },
            {
                "name": "ITC Hotels",
                "rating": 4.6,
                "price_per_night": 6500,
                "amenities": ["WiFi", "Gym", "Restaurant"]
            },
            {
                "name": "Budget Stay Inn",
                "rating": 4.2,
                "price_per_night": 2000,
                "amenities": ["WiFi", "Basic Breakfast"]
            }
        ],
        "city": city
    }
    
    if preference == "best_rated":
        hotels["hotels"] = sorted(hotels["hotels"], key=lambda x: x["rating"], reverse=True)
    elif preference == "cheapest":
        hotels["hotels"] = sorted(hotels["hotels"], key=lambda x: x["price_per_night"])
    
    return hotels

def search_attractions(city, category=None):
    """Search for attractions - returns mock data"""
    attractions = {
        "attractions": [
            {"name": "Beach", "type": "Nature", "rating": 4.7},
            {"name": "Fort", "type": "History", "rating": 4.5},
            {"name": "Market", "type": "Shopping", "rating": 4.3},
            {"name": "Temple", "type": "Religious", "rating": 4.6}
        ],
        "city": city
    }
    
    if category:
        attractions["attractions"] = [a for a in attractions["attractions"] if a["type"].lower() == category.lower()]
    
    return attractions

def get_weather(city, lat=0, lon=0, days=3):
    """Get weather forecast - returns mock data"""
    weather = {
        "city": city,
        "forecast": [
            {"day": "Day 1", "temp": "28°C", "condition": "Sunny", "humidity": "65%"},
            {"day": "Day 2", "temp": "26°C", "condition": "Partly Cloudy", "humidity": "70%"},
            {"day": "Day 3", "temp": "29°C", "condition": "Sunny", "humidity": "60%"}
        ]
    }
    return weather

def estimate_budget(flight_price=0, hotel_per_night=0, num_nights=3):
    """Calculate trip budget"""
    food_cost = num_nights * 1000
    activities_cost = num_nights * 800
    total = flight_price + (hotel_per_night * num_nights) + food_cost + activities_cost
    
    return {
        "flight_cost": flight_price,
        "hotel_cost": hotel_per_night * num_nights,
        "food_cost": food_cost,
        "activities_cost": activities_cost,
        "total_budget": total,
        "breakdown": f"Flights: ₹{flight_price}, Hotels: ₹{hotel_per_night * num_nights}, Food: ₹{food_cost}, Activities: ₹{activities_cost}"
    }

def get_city_coordinates(city):
    """Get city coordinates - returns mock data"""
    coordinates = {
        "Delhi": (28.6139, 77.2090),
        "Goa": (15.4909, 73.8278),
        "Mumbai": (19.0760, 72.8777),
        "Bangalore": (12.9716, 77.5946),
        "Kerala": (10.8505, 76.2711),
        "Agra": (27.1767, 78.0081)
    }
    
    lat, lon = coordinates.get(city, (0, 0))
    return lat, lon
