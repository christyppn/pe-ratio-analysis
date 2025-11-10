#!/usr/bin/env python3
"""
Update HTML file with latest market data from Yahoo Finance
"""

import json
import re
from datetime import datetime

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
    
    # Update index P/E ratios in dashboard
    replacements = {
        # S&P 500
        r'<div style="font-size: 1\.5em; font-weight: bold; color: #667eea; margin: 10px 0;">29\.2</div>': 
            f'<div style="font-size: 1.5em; font-weight: bold; color: #667eea; margin: 10px 0;">{indices.get("S&P 500", {}).get("pe_ratio", 29.2)}</div>',
        
        # Nasdaq
        r'<div style="font-size: 1\.5em; font-weight: bold; color: #764ba2; margin: 10px 0;">36\.5</div>':
            f'<div style="font-size: 1.5em; font-weight: bold; color: #764ba2; margin: 10px 0;">{indices.get("Nasdaq", {}).get("pe_ratio", 36.5)}</div>',
        
        # Hang Seng
        r'<div style="font-size: 1\.5em; font-weight: bold; color: #22c55e; margin: 10px 0;">11\.8</div>':
            f'<div style="font-size: 1.5em; font-weight: bold; color: #22c55e; margin: 10px 0;">{indices.get("Hang Seng", {}).get("pe_ratio", 11.8)}</div>',
        
        # Dow Jones
        r'<div style="font-size: 1\.5em; font-weight: bold; color: #f97316; margin: 10px 0;">27\.3</div>':
            f'<div style="font-size: 1.5em; font-weight: bold; color: #f97316; margin: 10px 0;">{indices.get("Dow Jones", {}).get("pe_ratio", 27.3)}</div>',
    }
    
    for pattern, replacement in replacements.items():
        html_content = re.sub(pattern, replacement, html_content)
    
    # Update timestamp
    timestamp = datetime.now().strftime('%Y年%m月%d日')
    html_content = re.sub(
        r'發布日期：\d{4}年\d{2}月\d{2}日',
        f'發布日期：{timestamp}',
        html_content
    )
    
    # Update data source note
    html_content = re.sub(
        r'數據來源：多重權威金融數據提供商',
        f'數據來源：Yahoo Finance (更新於 {datetime.now().strftime("%H:%M UTC")})',
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
    try:
        with open('dist/index.html', 'r', encoding='utf-8') as f:
            html_content = f.read()
    except FileNotFoundError:
        print("Error: dist/index.html not found")
        return
    
    print("Updating HTML with new data...")
    updated_html = update_html_data(html_content, data)
    
    print("Writing updated HTML file...")
    with open('dist/index.html', 'w', encoding='utf-8') as f:
        f.write(updated_html)
    
    print("✓ HTML file updated successfully")
    print(f"Update time: {datetime.now().isoformat()}")

if __name__ == '__main__':
    main()
