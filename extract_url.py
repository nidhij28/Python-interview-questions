import re

text = "Visit https://www.example.com or http://test.org for details."

urls = re.findall(r'https?://\S+', text)
print(urls)