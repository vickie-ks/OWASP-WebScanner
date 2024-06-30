import csv
import random

vulnerability_types = [
  "Broken Client-side Access Control",
  "DOM-based XSS",
  "Sensitive Data Leakage",
  "Vulnerable and Outdated Components",
  "Lack of Third-party Origin Control",
  "JavaScript Drift",
  "Sensitive Data Stored Client-Side",
  "Client-side Security Logging and Monitoring Failures",
  "Not Using Standard Browser Security Controls",
  "Including Proprietary Information on the Client-Side"
]

def generate_code_snippet(vulnerability):
  if vulnerability == "DOM-based XSS":
    options = [
      f"<script>document.write(location.hash.slice({random.randint(1,10)}));</script>",
      f"<div id='output'></div><script>document.getElementById('output').innerHTML = location.search;</script>",
      f"<script>eval(location.hash.slice({random.randint(1,10)}));</script>"
    ]
    return random.choice(options)
  elif vulnerability == "Sensitive Data Leakage":
    return "<script>console.log(document.cookie);</script>"
  elif vulnerability == "Vulnerable and Outdated Components":
    return "<script src='http://example.com/old-version.js'></script>"
  elif vulnerability == "Broken Client-side Access Control":
    return "<script>if (user.isAdmin) { showAdminControls(); } else { hideAdminControls(); }</script>"
  elif vulnerability == "Lack of Third-party Origin Control":
    return "<script src='http://untrusted.example.com/script.js'></script>"
  elif vulnerability == "JavaScript Drift":
    return "<script>document.body.innerHTML = localStorage.getItem('userSettings');</script>"
  elif vulnerability == "Sensitive Data Stored Client-Side":
    return "<script>localStorage.setItem('sessionToken', 'abc123');</script>"
  elif vulnerability == "Client-side Security Logging and Monitoring Failures":
    return "<script>console.error = function () {};</script>"
  elif vulnerability == "Not Using Standard Browser Security Controls":
    return "<meta http-equiv='Content-Security-Policy' content='default-src 'self'; script-src 'none';'>"
  elif vulnerability == "Including Proprietary Information on the Client-Side":
    return "<script>const apiKey = 'abcdef123456';</script>"
  return "<script>alert('This is a placeholder snippet');</script>"

num_entries = 10000

with open('synthetic_vulnerability_dataset.csv', mode='w', newline='') as file:
  writer = csv.writer(file)
  writer.writerow(['ID', 'Code_Snippet', 'Vulnerability', 'Label'])

  for i in range(1, num_entries + 1):
    vulnerability = random.choice(vulnerability_types)
    code_snippet = generate_code_snippet(vulnerability)
    label = 1 if "None" not in vulnerability else 0
    writer.writerow([i, code_snippet, vulnerability, label])

print(f"Generated {num_entries} entries in 'synthetic_vulnerability_dataset.csv'")
