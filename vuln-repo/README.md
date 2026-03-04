# vuln-repo — CVE Reachability Test Coverage

Flat directory layout: one folder per **CVE × package-version pair**.

Each directory contains:
- `requirements.txt` — single pinned vulnerable package
- `<CVE-ID>.py`      — empty placeholder (drop your test file here)

## Structure

```
<package>_<CVE-ID>_<version>/
├── requirements.txt   # e.g. werkzeug==1.0.1
└── CVE-XXXX-XXXXX.py  # test file placeholder
```

## Stats
| Metric | Count |
|---|---|
| Directories | 51 |
| Unique packages | 18 |
| CVEs covered | 51 |

## Package index
aiohttp, cbor2, celery, certifi, cryptography, flask, idna, Jinja2,
lightgbm, nbconvert, protobuf, pycryptodome, PyJWT, PyMySQL, PyYAML,
requests, tornado, urllib3, uWSGI, werkzeug, wheel
