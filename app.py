"""
🌍 TRAVEL ASSISTANT - 100% WORKING - WITH PERMANENT API KEY!
Gemini 2.5 Flash Lite - API Key Hidden in .env
Developer ~ Utkarsh Srivastava
"""

import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

st.set_page_config(
    page_title="🌍 Travel Assistant AI",
    page_icon="✈️",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>
.main-header {color: #1f77b4; font-size: 3rem; font-weight: bold; text-align: center;}
.success-box {background-color: #d4edda; padding: 1.5rem; border-radius: 15px; border-left: 6px solid #28a745; margin: 1rem 0;}
.error-box {background-color: #f8d7da; padding: 1.5rem; border-radius: 15px; border-left: 6px solid #dc3545; margin: 1rem 0;}
.input-section {background-color: #f8f9fa; padding: 1.5rem; border-radius: 10px; margin: 1rem 0;}
</style>
""", unsafe_allow_html=True)

# ============================================================================
# ✅ LOAD API KEY FROM .env FILE (PERMANENTLY STORED & HIDDEN)
# ============================================================================
api_key_env = os.getenv("GOOGLE_API_KEY")

# ============================================================================
# ✅ DEFINE plan_trip FUNCTION FIRST (BEFORE using it)
# ============================================================================

def plan_trip(api_key, source, destination, days, budget, preferences):
    """Generate perfect travel itinerary using Gemini 2.5 Flash Lite"""
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel('gemini-2.5-flash-lite')
        
        prompt = f"""
You are a world-class travel advisor. Create a PERFECT {days}-day trip itinerary from {source} to {destination}.

**Trip Details:**
- From: {source}
- To: {destination}
- Days: {days}
- Budget: ₹{budget:,}
- Preferences: {preferences}

**PROVIDE THESE SECTIONS:**

**✈️ FLIGHTS** (Top 3 options with airlines, prices, times)

**🏨 HOTELS** (3 options - luxury, mid-range, budget with ratings and prices)

**🗺️ DAY-BY-DAY ITINERARY** (Detailed schedule for each day with times)

**📍 TOP ATTRACTIONS** (Must-see places with timings and entry fees)

**🌤️ WEATHER FORECAST** (Temperature and conditions for each day)

**🍽️ FOOD RECOMMENDATIONS** (Local restaurants and cuisines to try)

**💰 DETAILED BUDGET BREAKDOWN** (Flights, hotels, food, activities, total)

**🚕 TRANSPORTATION TIPS** (How to get around - auto, taxi, local transport)

**💡 PRO TIPS & HACKS** (Insider recommendations, best times to visit, what to pack)

Make it EXCITING, DETAILED, and well-formatted with emojis!
"""
        
        with st.spinner("🎯 AI Creating Your Perfect Travel Plan..."):
            response = model.generate_content(prompt)
        
        st.markdown('<div class="success-box">✅ **Your Dream Trip Plan is Ready!**</div>', unsafe_allow_html=True)
        st.markdown("## 🎉 Your Personalized Travel Itinerary")
        st.markdown(response.text)
        
    except Exception as e:
        st.markdown(f'<div class="error-box">❌ **Error**: {str(e)}</div>', unsafe_allow_html=True)

# ============================================================================
# NOW UI CODE (After function definition)
# ============================================================================

# Header
st.markdown('<h1 class="main-header">✈️ AI Travel Planning Assistant</h1>', unsafe_allow_html=True)
st.markdown("### <center>Plan your dream trip  🚀</center>", unsafe_allow_html=True)

# Sidebar

   
# Main content
col1, col2 = st.columns([2, 1])

with col1:
    st.markdown('<div class="input-section">', unsafe_allow_html=True)
    st.header("📋 Plan Your Perfect Trip")
    
    source = st.text_input("🛫 From City", "Delhi", help="Starting city")
    destination = st.text_input("🛬 To City", "Goa", help="Destination city")
    days = st.slider("📅 Trip Duration (days)", 1, 10, 3)
    budget = st.number_input("💰 Budget (₹)", 10000, 500000, 25000)
    preferences = st.text_area(
        "🎯 Your Preferences", 
        "beach, adventure, luxury hotels, vegetarian food, nightlife",
        height=100
    )
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Plan trip button
    if st.button("🚀 GENERATE MY ITINERARY!", type="primary", use_container_width=True):
        if not api_key_env:
            st.markdown('<div class="error-box">❌ API key not loaded! Create .env file with your API key.</div>', unsafe_allow_html=True)
        elif not source or not destination:
            st.markdown('<div class="error-box">❌ Please enter both source and destination cities!</div>', unsafe_allow_html=True)
        else:
            plan_trip(api_key_env, source, destination, days, budget, preferences)

with col2:
    st.header("✨ What You Get")
    st.markdown("""
    ✈️ **Flights**
    Best deals & times
    
    🏨 **Hotels**
    All budget levels
    
    🗺️ **Itinerary**
    Day-by-day plan
    
    📍 **Attractions**
    Must-visit places
    
    🌤️ **Weather**
    Daily forecast
    
    🍽️ **Food**
    Local cuisine tips
    
    💰 **Budget**
    Complete breakdown
    """)
    
    st.markdown("---")
    st.header("💡 Pro Tips")
    st.markdown("""
    • Be specific about interests
    • Mention dietary needs
    • Include constraints
    • Specify travel style
    • Ask for hidden gems!
    """)

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; padding: 2rem; color: #666;'>
    <h3>Developer ~ Utkarsh Srivastava</h3>
    <p><b>utkarshsri3690@gmail.com</b></p>
    <p><b>Thanks for using this app</b></p>
</div>
""", unsafe_allow_html=True)