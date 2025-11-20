#!/usr/bin/env python3
"""
Script to update HTML files with latest 13F data
"""

import json
import re
from datetime import datetime
from pathlib import Path

class HTMLDataUpdater:
    def __init__(self):
        self.data_file = 'scripts/13f-data.json'
        self.html_files = [
            'dist/index.html',
            'dist/multi-fund-comparison.html'
        ]
    
    def load_data(self):
        """Load 13F data from JSON file"""
        try:
            with open(self.data_file, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            print(f"Data file not found: {self.data_file}")
            return {}
    
    def update_berkshire_data(self, html_content: str, data: Dict) -> str:
        """Update Berkshire Hathaway data in HTML"""
        
        if 'Berkshire Hathaway Inc' not in data:
            return html_content
        
        berkshire_data = data['Berkshire Hathaway Inc']
        
        # Update filing date
        filing_date = berkshire_data.get('filing_date', '')
        html_content = re.sub(
            r'<span>數據日期：.*?</span>',
            f'<span>數據日期：{filing_date}</span>',
            html_content
        )
        
        # Update total portfolio value
        total_value = berkshire_data.get('holdings', {}).get('total_value', 422.3)
        html_content = re.sub(
            r'<div class="summary-value">\$422\.3B</div>',
            f'<div class="summary-value">${total_value:.1f}B</div>',
            html_content,
            count=1
        )
        
        # Update cash position
        cash = berkshire_data.get('holdings', {}).get('cash', 167.6)
        html_content = re.sub(
            r'<div class="summary-value">\$167\.6B</div>',
            f'<div class="summary-value">${cash:.1f}B</div>',
            html_content,
            count=1
        )
        
        print("✅ Berkshire data updated")
        return html_content
    
    def update_vanguard_data(self, html_content: str, data: Dict) -> str:
        """Update Vanguard data in HTML"""
        
        if 'Vanguard Group Inc' not in data:
            return html_content
        
        vanguard_data = data['Vanguard Group Inc']
        
        # Update Vanguard fund size
        fund_size = vanguard_data.get('holdings', {}).get('total_value', 750.2)
        html_content = re.sub(
            r'<div class="summary-value">\$750\.2B</div>',
            f'<div class="summary-value">${fund_size:.1f}B</div>',
            html_content
        )
        
        print("✅ Vanguard data updated")
        return html_content
    
    def update_soros_data(self, html_content: str, data: Dict) -> str:
        """Update Soros Fund data in HTML"""
        
        if 'Soros Fund Management LLC' not in data:
            return html_content
        
        soros_data = data['Soros Fund Management LLC']
        
        # Update Soros fund size
        fund_size = soros_data.get('holdings', {}).get('total_value', 32.8)
        html_content = re.sub(
            r'<div class="summary-value">\$32\.8B</div>',
            f'<div class="summary-value">${fund_size:.1f}B</div>',
            html_content
        )
        
        print("✅ Soros data updated")
        return html_content
    
    def update_last_updated_time(self, html_content: str) -> str:
        """Update the last updated timestamp"""
        now = datetime.now().strftime('%Y年%m月%d日 %H:%M:%S')
        html_content = re.sub(
            r'最後更新：\d{4}年\d{2}月\d{2}日.*?UTC',
            f'最後更新：{now} UTC',
            html_content
        )
        return html_content
    
    def update_all_files(self):
        """Update all HTML files with new data"""
        data = self.load_data()
        
        if not data:
            print("No data to update")
            return
        
        for html_file in self.html_files:
            if not Path(html_file).exists():
                print(f"File not found: {html_file}")
                continue
            
            print(f"\nUpdating {html_file}...")
            
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Apply updates
            content = self.update_berkshire_data(content, data)
            content = self.update_vanguard_data(content, data)
            content = self.update_soros_data(content, data)
            content = self.update_last_updated_time(content)
            
            # Write back
            with open(html_file, 'w', encoding='utf-8') as f:
                f.write(content)
            
            print(f"✅ {html_file} updated successfully")

def main():
    """Main function"""
    updater = HTMLDataUpdater()
    updater.update_all_files()
    print("\n✅ All HTML files updated successfully")

if __name__ == '__main__':
    main()

