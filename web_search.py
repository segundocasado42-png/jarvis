# Web Search Module - Search functionality for Jarvis

import requests
from bs4 import BeautifulSoup
from config import OPENWEATHER_API_KEY, NEWS_API_KEY
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


def search_web(query):
    """Search on Google using web scraping"""
    try:
        url = f"https://www.google.com/search?q={query}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
        }
        response = requests.get(url, headers=headers, timeout=5)
        soup = BeautifulSoup(response.content, "html.parser")
        
        # Extract search results
        results = soup.find_all("div", class_="g")
        search_results = []
        
        for result in results[:5]:
            try:
                link = result.find("a", href=True)
                title = result.find("h3")
                snippet = result.find("span", class_="VwiC3b")
                
                if link and title:
                    search_results.append({
                        "title": title.text,
                        "url": link["href"],
                        "snippet": snippet.text if snippet else ""
                    })
            except:
                continue
        
        return search_results if search_results else None
    except Exception as e:
        logger.error(f"Error in web search: {e}")
        return None


def get_weather(city):
    """Get weather information for a city"""
    try:
        if not OPENWEATHER_API_KEY:
            return "API key no configurada para el clima. Configúralo en .env"
        
        url = f"https://api.openweathermap.org/data/2.5/weather"
        params = {
            "q": city,
            "appid": OPENWEATHER_API_KEY,
            "units": "metric",
            "lang": "es"
        }
        
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        
        if response.status_code == 200:
            temp = data["main"]["temp"]
            description = data["weather"][0]["description"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            feels_like = data["main"]["feels_like"]
            
            weather_text = (
                f"En {city}: {description.capitalize()}. "
                f"Temperatura: {temp}°C (sensación térmica: {feels_like}°C). "
                f"Humedad: {humidity}%. "
                f"Velocidad del viento: {wind_speed} m/s"
            )
            return weather_text
        else:
            return f"No encontré información para {city}"
    
    except Exception as e:
        logger.error(f"Error getting weather: {e}")
        return None


def get_news():
    """Get latest news"""
    try:
        if not NEWS_API_KEY:
            return "API key no configurada para noticias. Configúralo en .env"
        
        url = "https://newsapi.org/v2/top-headlines"
        params = {
            "country": "es",
            "apiKey": NEWS_API_KEY,
            "pageSize": 5
        }
        
        response = requests.get(url, params=params, timeout=5)
        data = response.json()
        
        if response.status_code == 200 and data.get("articles"):
            news_text = "Últimas noticias:\n"
            for i, article in enumerate(data["articles"][:5], 1):
                news_text += f"{i}. {article['title']}\n"
            return news_text
        else:
            return "No hay noticias disponibles"
    
    except Exception as e:
        logger.error(f"Error getting news: {e}")
        return None


def get_stock_price(symbol):
    """Get stock price for a symbol"""
    try:
        url = f"https://query1.finance.yahoo.com/v10/finance/quoteSummary/{symbol}"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers, timeout=5)
        
        if response.status_code == 200:
            data = response.json()
            try:
                price = data["quoteSummary"]["result"][0]["price"]["regularMarketPrice"]["raw"]
                currency = data["quoteSummary"]["result"][0]["price"]["currency"]
                return f"El precio de {symbol} es {price} {currency}"
            except:
                return f"No encontré información para {symbol}"
        else:
            return f"No encontré información para {symbol}"
    except Exception as e:
        logger.error(f"Error getting stock price: {e}")
        return None


def convert_currency(amount, from_currency, to_currency):
    """Convert between currencies"""
    try:
        url = f"https://api.exchangerate-api.com/v4/latest/{from_currency}"
        response = requests.get(url, timeout=5)
        data = response.json()
        
        if to_currency in data["rates"]:
            rate = data["rates"][to_currency]
            result = amount * rate
            return f"{amount} {from_currency} = {result:.2f} {to_currency}"
        else:
            return f"Moneda {to_currency} no encontrada"
    except Exception as e:
        logger.error(f"Error converting currency: {e}")
        return None
