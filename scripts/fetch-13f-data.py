#!/usr/bin/env python3
"""
Script to fetch 13F data from SEC EDGAR API
Supports: Berkshire Hathaway, Vanguard, Soros Fund Management
"""

import requests
import json
import os
from datetime import datetime
from typing import Dict, List

class SEC13FDataFetcher:
    def __init__(self):
        self.base_url = "https://www.sec.gov/cgi-bin/browse-edgar"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.sec_api_key = os.environ.get('SEC_API_KEY', '')
        
    def fetch_13f_filings(self, cik: str, fund_name: str) -> List[Dict]:
        """
        Fetch 13F filings for a specific fund
        
        Args:
            cik: Central Index Key (CIK) for the fund
            fund_name: Name of the fund
            
        Returns:
            List of 13F filing information
        """
        print(f"Fetching 13F data for {fund_name}...")
        
        params = {
            'action': 'getcompany',
            'CIK': cik,
            'type': '13F-HR',
            'dateb': '',
            'owner': 'exclude',
            'count': 100,
            'search_text': ''
        }
        
        try:
            response = requests.get(self.base_url, params=params, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            # Parse HTML to extract filing information
            # This is a simplified version - in production, use BeautifulSoup
            filings = self._parse_filings(response.text, fund_name)
            return filings
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching data for {fund_name}: {e}")
            return []
    
    def _parse_filings(self, html: str, fund_name: str) -> List[Dict]:
        """Parse HTML response to extract filing information"""
        # Simplified parsing - in production use BeautifulSoup
        filings = []
        
        # This is a placeholder - actual parsing would extract:
        # - Filing date
        # - Accession number
        # - Holdings information
        
        print(f"Parsed {len(filings)} filings for {fund_name}")
        return filings
    
    def fetch_holdings(self, accession_number: str, fund_name: str) -> Dict:
        """
        Fetch holdings from a specific 13F filing
        
        Args:
            accession_number: SEC accession number for the filing
            fund_name: Name of the fund
            
        Returns:
            Dictionary containing holdings information
        """
        print(f"Fetching holdings for {fund_name} (Accession: {accession_number})...")
        
        # Construct URL to XML file
        xml_url = f"https://www.sec.gov/cgi-bin/viewer?action=view&cik={accession_number.replace('-', '')}&accession_number={accession_number}&xbrl_type=v"
        
        try:
            response = requests.get(xml_url, headers=self.headers, timeout=10)
            response.raise_for_status()
            
            holdings = self._parse_holdings(response.text)
            return holdings
            
        except requests.exceptions.RequestException as e:
            print(f"Error fetching holdings: {e}")
            return {}
    
    def _parse_holdings(self, xml_data: str) -> Dict:
        """Parse XML data to extract holdings"""
        # Simplified parsing - in production use xml.etree.ElementTree
        holdings = {
            'total_value': 0,
            'cash': 0,
            'positions': []
        }
        
        # This is a placeholder for actual XML parsing
        print("Parsed holdings data")
        return holdings

def main():
    """Main function to orchestrate 13F data fetching"""
    
    # Fund CIKs (Central Index Keys)
    funds = {
        '0000086365': 'Berkshire Hathaway Inc',
        '0000102647': 'Vanguard Group Inc',
        '0001086364': 'Soros Fund Management LLC'
    }
    
    fetcher = SEC13FDataFetcher()
    all_data = {}
    
    # Fetch data for each fund
    for cik, fund_name in funds.items():
        print(f"\n{'='*60}")
        print(f"Fetching data for {fund_name}")
        print(f"{'='*60}")
        
        filings = fetcher.fetch_13f_filings(cik, fund_name)
        
        if filings:
            # Get most recent filing
            latest_filing = filings[0]
            holdings = fetcher.fetch_holdings(latest_filing['accession_number'], fund_name)
            all_data[fund_name] = {
                'filing_date': latest_filing['filing_date'],
                'holdings': holdings
            }
    
    # Save data to JSON file
    output_file = 'scripts/13f-data.json'
    os.makedirs('scripts', exist_ok=True)
    
    with open(output_file, 'w') as f:
        json.dump(all_data, f, indent=2, default=str)
    
    print(f"\n✅ Data saved to {output_file}")
    print(f"Last updated: {datetime.now().isoformat()}")

if __name__ == '__main__':
    main()

