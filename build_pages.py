#!/usr/bin/env python3
"""Rebuild the generated parts of rankcontrol.github.io (2026-11-12). Run from medium-posts/: python3 github-site/build_pages.py

- medium.md: every published Search Shift story on Medium (title, date, plain followed link), newest first, from
  schedule/order.json (status, title, published date) and distribution-tracker.csv (canonical medium_url). Google
  finds new Medium stories through this page once the site is crawled (Search Console sitemap).
- _data/profiles.yml: the profile list used by the About page and the footer (PROFILES below), also written into
  _config.yml `social.links` so jekyll-seo-tag emits it as JSON-LD sameAs.
Then commit and push (as RankControl, no co-author line): see MULTI-PLATFORM-PLAN.md.
"""
import csv
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)

# The Search Shift accounts (PROFILE-LINKS.md is the master list; keep both in step).
PROFILES = [
    ("Medium", "https://medium.com/@thesearchshift"),
    ("Substack", "https://thesearchshift.substack.com"),
    ("Hashnode", "https://searchshift.hashnode.dev"),
    ("dev.to", "https://dev.to/thesearchshift"),
    ("HackerNoon", "https://hackernoon.com/u/searchshift"),
    ("Bear Blog", "https://searchshift.bearblog.dev"),
    ("Search Shift Notes (Google Sites)", "https://sites.google.com/view/search-shift-notes"),
    ("AI Search Data Library (Notion)", "https://typhoon-cheese-d66.notion.site/AI-Search-Data-Library-5326d7142291822583f50143e78b0c8b"),
    ("GitHub", "https://github.com/rankcontrol"),
    ("YouTube", "https://www.youtube.com/channel/UCABAzklFXscQt60GxRP46dw"),
    ("X", "https://x.com/the_searchshift"),
    ("Bluesky", "https://bsky.app/profile/searchshift.bsky.social"),
    ("Threads", "https://www.threads.com/@thesearchshift"),
    ("Instagram", "https://www.instagram.com/thesearchshift"),
    ("Pinterest", "https://www.pinterest.com/searchshift"),
    ("Telegram", "https://t.me/thesearchshift"),
    ("Quora", "https://www.quora.com/profile/Ram-12260"),
]


# Shown on the site (user, 2026-11-12: "limit to 5-8 per platform, it can look spammy"). The full PROFILES list
# goes only into the JSON-LD sameAs, which readers don't see.
VISIBLE = ["Medium", "Substack", "Hashnode", "dev.to", "HackerNoon", "Bear Blog", "Search Shift Notes (Google Sites)", "YouTube"]


def medium_page():
    order = json.load(open(os.path.join(ROOT, "schedule", "order.json"), encoding="utf-8"))
    urls = {r["order"]: r["medium_url"] for r in csv.DictReader(open(os.path.join(ROOT, "distribution-tracker.csv"), encoding="utf-8")) if r.get("medium_url")}
    rows = [r for r in order if r.get("status") == "Published" and urls.get(str(r["order"]))]
    rows.sort(key=lambda r: (r.get("published") or "", r["order"]), reverse=True)
    lines = ["---", "layout: page", "title: On Medium", "permalink: /medium/", "---", "",
             f"Every Search Shift story published on [Medium](https://medium.com/@thesearchshift), newest first ({len(rows)} so far). "
             "Each one is a dated test, count or sourced roundup on what Google and the AI answer engines show and cite.", ""]
    for r in rows:
        lines.append(f"- {r.get('published', '')}: [{r['title']}]({urls[str(r['order'])]})")
    open(os.path.join(HERE, "medium.md"), "w", encoding="utf-8").write("\n".join(lines) + "\n")
    return len(rows)


def profiles():
    os.makedirs(os.path.join(HERE, "_data"), exist_ok=True)
    with open(os.path.join(HERE, "_data", "profiles.yml"), "w", encoding="utf-8") as f:
        for name, url in PROFILES:
            if name in VISIBLE:
                f.write(f'- name: "{name}"\n  url: "{url}"\n')
    cfg_p = os.path.join(HERE, "_config.yml")
    cfg = open(cfg_p, encoding="utf-8").read()
    block = "social:\n  name: Search Shift\n  links:\n" + "".join(f"    - {u}\n" for _, u in PROFILES)
    cfg = re.sub(r"social:\n  name: .*?\n  links:\n(?:    - .*\n)*", "", cfg)
    open(cfg_p, "w", encoding="utf-8").write(cfg.rstrip("\n") + "\n" + block)


if __name__ == "__main__":
    n = medium_page()
    profiles()
    print(f"medium.md: {n} stories; _data/profiles.yml: {len(VISIBLE)} shown; _config.yml sameAs: {len(PROFILES)}")
