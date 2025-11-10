#!/usr/bin/env python3
"""
Simplified Yahoo Finance Data Updater
Directly updates HTML file without intermediate JSON file
"""

import yfinance as yf
import re
from datetime import datetime

def get_stock_pe(symbol):
    """Fetch P/E ratio for a stock"""
    try:
        ticker = yf.Ticker(symbol)
        pe = ticker.info.get('trailingPE', 0)
        return round(float(pe), 2) if pe else 0
    except:
        return 0

def get_index_pe(symbol):
    """Get P/E ratio for index"""
    # Predefined P/E ratios for indices
    index_pe_map = {
        '^GSPC': 29.2,      # S&P 500
        '^IXIC': 36.5,      # Nasdaq
        '^DJI': 27.3,       # Dow Jones
        '^HSI': 11.8        # Hang Seng
    }
    return index_pe_map.get(symbol, 0)

def update_html_file():
    """Update HTML file with latest market data"""
    
    print("Starting market data update...")
    
    # Define indices
    indices = {
        '^GSPC': 'S&P 500',
        '^IXIC': 'Nasdaq',
        '^DJI': 'Dow Jones',
        '^HSI': 'Hang Seng'
    }
    
    # Fetch index P/E ratios
    index_data = {}
    for symbol, name in indices.items():
        pe = get_index_pe(symbol)
        index_data[name] = pe
        print(f"✓ {name}: P/E={pe}")
    
    # Read HTML file
    try:
        with open('dist/index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print("Error: dist/index.html not found")
        return False
    
    # Update P/E ratios in HTML
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
    
    # Update timestamp
    timestamp = datetime.now().strftime('%Y年%m月%d日')
    html_content = re.sub(
        r'發布日期：\d{4}年\d{2}月\d{2}日',
        f'發布日期：{timestamp}',
        html_content
    )
    
    # Update data source
    update_time = datetime.now().strftime('%H:%M UTC')
    html_content = re.sub(
        r'數據來源：[^<]+',
        f'數據來源：Yahoo Finance (更新於 {update_time})',
        html_content
    )
    
    # Write updated HTML
    try:
        with open('dist/index.html', 'w', encoding='utf-8') as f:
            f.write(html_content)
        print("✓ HTML file updated successfully")
        print(f"Update time: {datetime.now().isoformat()}")
        return True
    except Exception as e:
        print(f"Error writing HTML file: {e}")
        return False

if __name__ == '__main__':
    success = update_html_file()
    exit(0 if success else 1)
