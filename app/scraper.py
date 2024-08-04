import requests
from bs4 import BeautifulSoup


def scrape_amazon_return_policy(url="https://www.amazon.co.uk/gp/help/customer/display.html?nodeId=GKM69DUUYKQWKWX7"):
    """
    Scrapes the Amazon return policy page and extracts text content from <p> tags.

    Args:
        url (str): The URL of the Amazon return policy page to scrape. Defaults to the UK Amazon return policy page.

    Returns:
        str: The extracted policy content from the page.
    """
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
        "Accept-Language": "en-US,en;q=0.5",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate, br",
        "Referer": "https://www.amazon.co.uk/"
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 403:
            raise PermissionError("Access denied. The server responded with status code 403.")
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
        return ""
    except requests.exceptions.ProxyError as proxy_err:
        print(f"Proxy error occurred: {proxy_err}")
        return ""
    except PermissionError as perm_err:
        print(f"Permission error occurred: {perm_err}")
        return ""
    except Exception as err:
        print(f"Other error occurred: {err}")
        return ""

    soup = BeautifulSoup(response.content, 'html.parser')

    # Debug output
    print("Page content fetched successfully.")

    policy_content = ''
    paragraphs = soup.find_all('p')
    if not paragraphs:
        print("No <p> tags found on the page.")

    for paragraph in paragraphs:
        policy_content += paragraph.get_text() + '\n'

    if not policy_content:
        print("No content found in <p> tags.")
    else:
        print("Content successfully extracted.")

    # Write to file with specified encoding
    with open('return_policy.txt', 'w', encoding='utf-8') as file:
        file.write(policy_content)

    return policy_content
