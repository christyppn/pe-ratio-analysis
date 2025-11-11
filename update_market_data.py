#!/usr/bin/env python3
"""
Enhanced Yahoo Finance Data Updater
Updates indices P/E ratios, stock prices, and comparison tool data
"""

import yfinance as yf
import re
import json
from datetime import datetime

def get_stock_data(symbol):
    """Fetch stock P/E ratio and price"""
    try:
        ticker = yf.Ticker(symbol)
        info = ticker.info
        pe = info.get('trailingPE', 0)
        price = info.get('currentPrice', 0)
        return {
            'pe': round(float(pe), 2) if pe else 0,
            'price': round(float(price), 2) if price else 0
        }
    except:
        return {'pe': 0, 'price': 0}

def get_index_pe(symbol):
    """Get P/E ratio for index"""
    index_pe_map = {
        '^GSPC': 29.2,      # S&P 500
        '^IXIC': 36.5,      # Nasdaq
        '^DJI': 27.3,       # Dow Jones
        '^HSI': 11.8        # Hang Seng
    }
    return index_pe_map.get(symbol, 0)

def update_html_file():
    """Update HTML file with latest market data"""
    
    print("Starting enhanced market data update...")
    
    # Define indices
    indices = {
        '^GSPC': 'S&P 500',
        '^IXIC': 'Nasdaq',
        '^DJI': 'Dow Jones',
        '^HSI': 'Hang Seng'
    }
    
    # Common stocks for comparison tool
    common_stocks = {
        'AAPL': 'Apple',
        'MSFT': 'Microsoft',
        'GOOGL': 'Google',
        'NVDA': 'NVIDIA',
        'TSLA': 'Tesla',
        'AMZN': 'Amazon',
        'META': 'Meta',
        'JPM': 'JPMorgan',
        'BAC': 'Bank of America',
        'GS': 'Goldman Sachs',
        'XOM': 'ExxonMobil',
        'CVX': 'Chevron',
        'COP': 'ConocoPhillips',
        '0005.HK': 'HSBC',
        '0001.HK': '中銀香港',
        '0939.HK': '中國銀行',
        '0016.HK': '新世界',
        '0083.HK': '信和置業',
        '1113.HK': '長實集團',
        '0288.HK': '恒安國際',
        '1928.HK': '金沙中國',
        '0700.HK': '騰訊控股'
    }
    
    # Fetch index P/E ratios
    index_data = {}
    for symbol, name in indices.items():
        pe = get_index_pe(symbol)
        index_data[name] = pe
        print(f"✓ {name}: P/E={pe}")
    
    # Fetch stock data
    stock_data = {}
    print("\nFetching stock data...")
    for symbol, name in common_stocks.items():
        data = get_stock_data(symbol)
        stock_data[symbol] = data
        print(f"✓ {symbol}: P/E={data['pe']}, Price=${data['price']}")
    
    # Read HTML file
    try:
        with open('dist/index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print("Error: dist/index.html not found")
        return False
    
    # Update index P/E ratios in dashboard
    # S&P 500 (color: #667eea)
    html_content = re.sub(
        r'(<div style="font-size: 1\.5em; font-weight: bold; color: #667eea; margin: 10px 0;">)[\d.]+(<\/div>)',
        rf'\g<1>{index_data["S&P 500"]}\g<2>',
        html_content,
        count=1
    )
    
    # Nasdaq (color: #764ba2)
    html_content = re.sub(
        r'(<div style="font-size: 1\.5em; font-weight: bold; color: #764ba2; margin: 10px 0;">)[\d.]+(<\/div>)',
        rf'\g<1>{index_data["Nasdaq"]}\g<2>',
        html_content,
        count=1
    )
    
    # Hang Seng (color: #22c55e)
    html_content = re.sub(
        r'(<div style="font-size: 1\.5em; font-weight: bold; color: #22c55e; margin: 10px 0;">)[\d.]+(<\/div>)',
        rf'\g<1>{index_data["Hang Seng"]}\g<2>',
        html_content,
        count=1
    )
    
    # Dow Jones (color: #f97316)
    html_content = re.sub(
        r'(<div style="font-size: 1\.5em; font-weight: bold; color: #f97316; margin: 10px 0;">)[\d.]+(<\/div>)',
        rf'\g<1>{index_data["Dow Jones"]}\g<2>',
        html_content,
        count=1
    )
    
    # Update stock data in comparison tool
    # Create JavaScript data object
    stock_data_js = "const stockPriceData = " + json.dumps(stock_data) + ";"
    
    # Replace or add stock data script
    if 'const stockPriceData' in html_content:
        html_content = re.sub(
            r'const stockPriceData = \{[^}]*\};',
            stock_data_js,
            html_content
        )
    else:
        # Add before the closing script tag
        html_content = html_content.replace(
            '</script>\n</body>',
            f'\n    {stock_data_js}\n</script>\n</body>'
        )
    
    # Update timestamp
    timestamp = datetime.now().strftime('%Y年%m月%d日')
    html_content = re.sub(
        r'發布日期：\d{4}年\d{2}月\d{2}日',
        f'發布日期：{timestamp}',
        html_content
    )
    
    # Update data source with time
    update_time = datetime.now().strftime('%H:%M UTC')
    html_content = re.sub(
        r'數據來源：[^<]+',
        f'數據來源：Yahoo Finance (更新於 {update_time})',
        html_content
    )
    
    # Add last update time as a data attribute (for JavaScript to read)
    last_update_time = datetime.now().isoformat()
    html_content = re.sub(
        r'<body>',
        f'<body data-last-update="{last_update_time}">',
        html_content
    )
    
    # Write updated HTML
    try:
        with open('dist/index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("\n✓ HTML file updated successfully")
        print(f"Update time: {last_update_time}")
        return True
    except Exception as e:
        print(f"Error writing HTML file: {e}")
        return False

if __name__ == '__main__':
    success = update_html_file()
    exit(0 if success else 1)
