#!/usr/bin/env python3
"""
Update HTML file with latest market data from Yahoo Finance
Fixed version with correct paths
"""

import json
import re
from datetime import datetime
import os

def load_market_data():
    """Load market data from JSON file"""
    try:
        with open('market_data.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Error: market_data.json not found")
        return None

def update_html_data(html_content, data):
    """Update HTML content with new market data"""
    
    if not data:
        return html_content
    
    indices = data.get('indices', {})
    stocks = data.get('stocks', {})
    
    # Extract P/E ratios from indices
    sp500_pe = indices.get('S&P 500', {}).get('pe_ratio', 29.2)
    nasdaq_pe = indices.get('Nasdaq', {}).get('pe_ratio', 36.5)
    hangseng_pe = indices.get('Hang Seng', {}).get('pe_ratio', 11.8)
    dowjones_pe = indices.get('Dow Jones', {}).get('pe_ratio', 27.3)
    
    # Update index P/E ratios in dashboard
    # S&P 500
    html_content = re.sub(
        r'<div style="font-size: 1\.5em; font-weight: bold; color: #667eea; margin: 10px 0;">[\d.]+</div>',
        f'<div style="font-size: 1.5em; font-weight: bold; color: #667eea; margin: 10px 0;">{sp500_pe}</div>',
        html_content,
        count=1
    )
    
    # Nasdaq
    html_content = re.sub(
        r'<div style="font-size: 1\.5em; font-weight: bold; color: #764ba2; margin: 10px 0;">[\d.]+</div>',
        f'<div style="font-size: 1.5em; font-weight: bold; color: #764ba2; margin: 10px 0;">{nasdaq_pe}</div>',
        html_content,
        count=1
    )
    
    # Hang Seng
    html_content = re.sub(
        r'<div style="font-size: 1\.5em; font-weight: bold; color: #22c55e; margin: 10px 0;">[\d.]+</div>',
        f'<div style="font-size: 1.5em; font-weight: bold; color: #22c55e; margin: 10px 0;">{hangseng_pe}</div>',
        html_content,
        count=1
    )
    
    # Dow Jones
    html_content = re.sub(
        r'<div style="font-size: 1\.5em; font-weight: bold; color: #f97316; margin: 10px 0;">[\d.]+</div>',
        f'<div style="font-size: 1.5em; font-weight: bold; color: #f97316; margin: 10px 0;">{dowjones_pe}</div>',
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
    
    # Update data source note with actual update time
    update_time = datetime.now().strftime('%H:%M UTC')
    html_content = re.sub(
        r'數據來源：[^<]+',
        f'數據來源：Yahoo Finance (更新於 {update_time})',
        html_content
    )
    
    return html_content

def main():
    print("Loading market data...")
    data = load_market_data()
    
    if not data:
        print("Failed to load market data")
        return
    
    print("Reading HTML file...")
    html_file = 'dist/index.html'
    
    if not os.path.exists(html_file):
        print(f"Error: {html_file} not found")
        return
    
    try:
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
    except Exception as e:
        print(f"Error reading HTML file: {e}")
        return
    
    print("Updating HTML with new data...")
    updated_html = update_html_data(html_content, data)
    
    print("Writing updated HTML file...")
    try:
        with open(html_file, 'w', encoding='utf-8') as f:
            f.write(updated_html)
        print("✓ HTML file updated successfully")
    except Exception as e:
        print(f"Error writing HTML file: {e}")
        return
    
    print(f"Update time: {datetime.now().isoformat()}")

if __name__ == '__main__':
    main()
