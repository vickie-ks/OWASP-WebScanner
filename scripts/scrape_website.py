import requests
from bs4 import BeautifulSoup

def fetch_website_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        html_content = response.text
        
        soup = BeautifulSoup(html_content, 'html.parser')
        scripts = [script.string for script in soup.find_all('script') if script.string]
        js_content = ' '.join(scripts)
        
        return html_content, js_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the website content: {e}")
        return None, None

if __name__ == "__main__":
    url = 'https://example.com'  # Replace with the actual URL
    html_content, js_content = fetch_website_content(url)
    if html_content and js_content:
        print("HTML Content:", html_content[:500])  # Print the first 500 characters for brevity
        print("JS Content:", js_content[:500])  # Print the first 500 characters for brevity
