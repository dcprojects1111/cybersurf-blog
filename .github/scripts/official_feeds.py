#!/usr/bin/env python3
"""Fetch official feeds that block Darryl's n8n server (CISA advisories) from GitHub's network and
save one small JSON file for n8n. Only commits when something changed.
Note: cyber.gov.au (ACSC) blocks overseas networks including GitHub, so it is NOT collected here."""
import json, re, sys, datetime, email.utils, urllib.request, xml.etree.ElementTree as ET

UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
FEEDS = [
    ("CISA advisories", "https://www.cisa.gov/cybersecurity-advisories/all.xml", "cisa"),
]
OUT = "data/official-feed.json"

def local(tag):
    return tag.split("}", 1)[-1]

def text(el, *names):
    for child in el:
        if local(child.tag) in names and (child.text or "").strip():
            return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", child.text)).strip()
    return ""

def parse_date(s):
    try:
        d = email.utils.parsedate_to_datetime(s)
    except Exception:
        try:
            d = datetime.datetime.fromisoformat(s.replace("Z", "+00:00"))
        except Exception:
            return None
    if d.tzinfo is None:
        d = d.replace(tzinfo=datetime.timezone.utc)
    return d.astimezone(datetime.timezone.utc)

def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/rss+xml,application/xml,text/xml,*/*", "Accept-Language": "en-AU,en;q=0.9"})
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.read()

items, status = [], {}
for name, url, kind in FEEDS:
    try:
        root = ET.fromstring(fetch(url))
        n = 0
        for el in root.iter():
            if local(el.tag) not in ("item", "entry"):
                continue
            title = text(el, "title")
            link = text(el, "link")
            if not link:
                for c in el:
                    if local(c.tag) == "link" and c.attrib.get("href"):
                        link = c.attrib["href"]
                        break
            d = parse_date(text(el, "pubDate", "published", "updated", "date"))
            if title and link and d:
                items.append({"src": name, "kind": kind, "title": title[:200], "link": link, "ts": d.isoformat(), "snip": text(el, "description", "summary")[:300]})
                n += 1
        status[name] = {"ok": True, "n": n}
    except Exception as e:
        status[name] = {"ok": False, "error": str(e)[:100]}
items.sort(key=lambda i: i["ts"], reverse=True)
items = items[:90]
new = {"feeds": status, "items": items}
try:
    old = json.load(open(OUT))
    old.pop("generatedAt", None)
except Exception:
    old = None
if old != new:
    new["generatedAt"] = datetime.datetime.now(datetime.timezone.utc).isoformat()
    json.dump(new, open(OUT, "w"), indent=1)
    print("updated", OUT, json.dumps(status))
else:
    print("no change", json.dumps(status))
