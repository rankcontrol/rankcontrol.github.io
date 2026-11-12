---
layout: page
title: About
permalink: /about/
---

Search Shift is written by Ram, who writes about SEO, AEO and GEO at [RankControl, an AI SEO and AEO platform](https://rctrl.com). RankControl's [AI visibility tracker](https://rctrl.com/ai-visibility) tracks citations across 7 AI engines.

The posts here are tests and counts: what a search engine or an AI answer showed for a set of questions on a given day, how many runs, and what that sample can and cannot tell you. The raw files behind them are in the [ai-search-datasets](https://github.com/rankcontrol/ai-search-datasets) repository (CC BY 4.0).

Corrections are welcome as an issue on [this site's repository](https://github.com/rankcontrol/rankcontrol.github.io/issues).

## Elsewhere

Where Search Shift publishes (each topic is published once, on one of these):

<ul>
{% for p in site.data.profiles %}<li><a rel="me" href="{{ p.url }}">{{ p.name }}</a></li>
{% endfor %}</ul>
