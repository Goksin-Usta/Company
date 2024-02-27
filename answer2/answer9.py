import re

# Örnek veri tabanı
database = {
    "AXO145": [
        "<Xml><Access_Link>https://xcd32112.smart_meter.com/123</Access_Link></Xml>",
        "<Xml><Access_Link>http://AbCdeF.smart_meter.com/456</Access_Link></Xml>",
        "<Xml><Access_Link>FTP://YYZ_123.smart_meter.com/789</Access_Link></Xml>"
    ],
    "XYZ789": [
        "<Xml><Access_Link>http://example.com</Access_Link></Xml>",
        "<Xml><Access_Link>https://subdomain.example.com</Access_Link></Xml>"
    ]
}

# Regex deseni
pattern = r"<access_link>(https?://[a-z0-9._]+)<\/access_link>"

# Cihaz türlerine göre işleme
for device, access_links in database.items():
    extracted_urls = []
    for link in access_links:
        # Regex ile URL'yi ara ve çıkar
        matches = re.findall(pattern, link.lower())
        extracted_urls.extend(matches)
    
    # URL'leri ekrana yazdır
    print(f"Device Type: {device}")
    for url in extracted_urls:
        print(url)
    print()