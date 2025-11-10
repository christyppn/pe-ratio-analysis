#!/usr/bin/env python3
"""
Yahoo Finance Data Fetcher for P/E Ratio Analysis Platform
Fetches real-time stock data and updates HTML file
"""

import yfinance as yf
import json
from datetime import datetime
import re

def get_stock_data(symbol):
    """Fetch stock data from Yahoo Finance"""
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        
        return {
            'symbol': symbol,
            'pe_ratio': round(info.get('trailingPE', 0), 2),
            'price': round(info.get('currentPrice', 0), 2),
            'change_percent': round(info.get('regularMarketChangePercent', 0), 2),
            'market_cap': info.get('marketCap', 0),
            'name': info.get('longName', symbol)
        }
    except Exception as e:
        print(f"Error fetching {symbol}: {e}")
        return None

def get_index_data(symbol):
    """Fetch index data from Yahoo Finance"""
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        
        return {
            'symbol': symbol,
            'pe_ratio': round(info.get('trailingPE', 0), 2),
            'price': round(info.get('currentPrice', 0), 2),
            'change_percent': round(info.get('regularMarketChangePercent', 0), 2),
        }
    except Exception as e:
        print(f"Error fetching index {symbol}: {e}")
        return None

def main():
    print("Starting Yahoo Finance data update...")
    
    # Define stocks and indices to fetch
    stocks = {
        'US': ['AAPL', 'MSFT', 'GOOGL', 'NVDA', 'TSLA', 'AMZN', 'META', 'JPM', 'BAC', 'GS', 'XOM', 'CVX', 'COP'],
        'HK': ['0005.HK', '0001.HK', '0939.HK', '0016.HK', '0083.HK', '1113.HK', '0288.HK', '1928.HK', '0700.HK']
    }
    
    indices = {
        '^GSPC': 'S&P 500',
        '^IXIC': 'Nasdaq',
        '^DJI': 'Dow Jones',
        '^HSI': 'Hang Seng'
    }
    
    # Fetch data
    stock_data = {}
    for region, symbols in stocks.items():
        stock_data[region] = {}
        for symbol in symbols:
            data = get_stock_data(symbol)
            if data:
                stock_data[region][symbol] = data
                print(f"✓ {symbol}: P/E={data['pe_ratio']}, Price=${data['price']}, Change={data['change_percent']}%")
    
    index_data = {}
    for symbol, name in indices.items():
        data = get_index_data(symbol)
        if data:
            index_data[name] = data
            print(f"✓ {name}: P/E={data['pe_ratio']}, Price=${data['price']}, Change={data['change_percent']}%")
    
    # Save to JSON file
    output = {
        'timestamp': datetime.now().isoformat(),
        'stocks': stock_data,
        'indices': index_data
    }
    
    with open('/home/ubuntu/market_data.json', 'w') as f:
        json.dump(output, f, indent=2)
    
    print("\n✓ Data saved to market_data.json")
    print(f"Update time: {output['timestamp']}")

if __name__ == '__main__':
    main()
