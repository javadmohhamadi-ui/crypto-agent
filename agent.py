import requests

def get_price(symbol: str) -> float | None:
    try:
        url = f"https://api.binance.com/api/v3/ticker/price?symbol={symbol.upper()}"
        data = requests.get(url, timeout=5).json()
        return float(data["price"])
    except:
        return None

def handle_message(text: str) -> str:
    symbol = text.strip().upper()
    price = get_price(symbol)

    if price is None:
        return "نماد نامعتبر یا مشکل در دریافت قیمت."

    return f"نماد: {symbol}\nقیمت فعلی: {price}"
