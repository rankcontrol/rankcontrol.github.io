---
title: "Why AI Visibility Isn't One Number: The Per-Engine Citation Data"
description: "I re-opened the per-engine AI citation studies on November 23, 2026: the sites each engine cites, how little they overlap and how fast citations fade."
date: 2026-11-24 12:02:00 +0700
tags: [ai visibility, ai citations, per engine citation data, ai search statistics, citation overlap]
image: /assets/img/gh-037-ai-visibility-per-engine-citation-data-hero.jpg
---

![Five slim blank panels in plum, burnt orange, ivory, rose and sage fanned out like a hand of cards inside a thin white circle, floating in a painted Baroque sky under the title AI Visibility By Engine](/assets/img/gh-037-ai-visibility-per-engine-citation-data-hero.jpg)

On 15th of September, and on 24th of September 2026, two different people posted variants of the same concern in r/SEO_LLM. 
One was trying multiple different AI visibility tools which had completely mismatched numbers. One tool had the brand appearing quite good. Another tool had the brand appearing to be almost non-existent. 
The other was asking how to tell if an increase from 28% to 33% after a content change was indeed related to the content change. Because answers change by themselves.

I work at [RankControl, an AI SEO and AEO platform](https://rctrl.com), where AEO means answer engine optimization, the work of getting pages quoted in AI answers. RankControl's [October 27 post on per-engine citation data](https://rctrl.com/blog/ai-visibility-per-engine-citation-data) collected the studies behind that question, with its sources checked on September 26. I re-opened every one of them on November 23, 2026, and several figures have moved since.

AI visibility (as used in those threads) is the frequency with which a brand/page shows up in the responses of AI assistants.

This visibility may be measured as a citation (source link next to the response) or brand name mention.

TL;DR: On Ahrefs' lists, updated November 3, 2026, Reddit is first for 3 of 7 engines, second for 3 and missing from Copilot's top 50. Only 11.0% of the domains ChatGPT and Perplexity cited were the same in one 100,000-prompt study, and 2.7% of 11,647 domains were cited by all five engines in another. In a study that repeated the same prompts daily, roughly 65% of the cited sources changed from one day to the next, and half of a week's citations drop out in 3.4 weeks on ChatGPT against 5.8 on Perplexity.

## How we checked

**What I checked.** Every figure below comes from a study or list that someone else ran, and I ran no AI queries of my own for this post. I opened the primary page behind each one: Ahrefs' seven per-engine lists, the full text of the arXiv paper "Don't Measure Once", SparkToro's study, and Anthropic's Trust Center list of subprocessors, which I read in a headless browser because that page is built by script. The same went for the write-ups from OtterlyAI, SurfacedBy, Profound, Steady Demand, Scrunch and Stacker, Kevin Indig's Growth Memo, and Search Engine Journal and TechRepublic on Promptwatch's Reddit tracking.

Two Aleyda Solis posts on X through a text mirror. Two r/SEO_LLM threads via AgntData's Reddit API. When the number is expressed on the page, I go by it.

**When.** Everything was read November 23, 2026. The dates are as provided by the publisher of each number. Ahrefs updates all the lists every month. I didn't find an archived September version. So the Sept numbers in the following movement table are as they appear in the RankControl Oct. 27 post (which I couldn't verify again).

**Sample.** The studies run from 2,961 runs by volunteers (SparkToro) to 379,321 Claude citations (OtterlyAI), and Ahrefs reports over 3 million US queries for most of its lists. Their query sets, countries and dates differ, so the sizes cannot be added up or set side by side.

**Limits.** Most of these publishers are offering AI visibility measuring or some variant of it themselves (Ahrefs, Profound, OtterlyAI, SurfacedBy, Promptwatch, Scrunch, Semrush). Plus there's Steady Demand and Stacker that are offering services related to the theme. (SparkToro writes their data partner works at an AI-tracking startup. One author on arXiv paper mentions their affiliation with a company that does something with brand visibility in AI-search.) RankControl offers AI visibility tracking as well. I've only heard of Claude's June 2026 figure from Profound through an agency's article (July 2, 2026).

## The websites each engine cites most

The SEO software company ahrefs provides a list for each AI engine of the 50 most-cited sites from their Brand Radar tracking of US queries (update each month). The lists are sorted by "mention share", the % of citations for a domain compared to all the citations for the top 50 domains (not the % of all citations for the engine).

According to Ahrefs, Copilot, Gemini and Google AI Overviews are all built on >3 million US queries, Perplexity >3.1 million queries and Grok >1.9 million queries. But on their ChatGPT and Google AI Mode pages they just have "broad US queries".

| Engine | First | Second | Third | Also on the list |
|---|---|---|---|---|
| ChatGPT | Wikipedia, 10.1% | Reddit, 6.2% | Consumer Reports, 4.4% | Walmart is fourth at 4.1% |
| Perplexity | Reddit, 24.6% | YouTube, 14.2% | Wikipedia, 7.2% | Amazon is fourth at 4.3% |
| Gemini | Reddit, 29.9% | Wikipedia, 8.6% | YouTube, 6.3% | Facebook is fourth at 5.9% |
| Google AI Mode | google.com, 23.4% | Reddit, 18.1% | YouTube, 17.0% | Facebook is fourth at 8.3% |
| Google AI Overviews | YouTube, 24.5% | Reddit, 18.1% | Facebook, 12.4% | google.com is fourth at 8.6% |
| Copilot | Amazon, 16.1% | Walmart, 11.8% | Wikipedia, 6.5% | Reddit is not in the top 50 |
| Grok (June 2026 list) | Reddit, 16.3% | YouTube, 15.1% | Facebook, 13.9% | x.com is 12th at 1.4% |

*Mention share from Ahrefs' lists of the 50 most-cited websites per engine, United States, updated November 3, 2026 (Grok: June 2026), read on November 23, 2026.*

Reddit appears on six of the seven lists, first on three of them (Perplexity, Gemini and Grok) and second on three. Copilot is the list that breaks the pattern: its first two places go to the retailers Amazon and Walmart, which hold 27.9% of the top-50 citations between them, and Reddit is missing.

On ChatGPT's list, Wikipedia has the larger share at 10.1%, yet Ahrefs counts 172,760 distinct Reddit pages cited against 109,914 Wikipedia pages, and its citation-change column marks Reddit down 32%.

That ChatGPT order is new. RankControl's October 27 post, working from Ahrefs' September 2 update, had Reddit first on ChatGPT at 16.8% with Wikipedia at 7.0%. The table below sets those September figures beside the November 3 ones for every domain the October post named.

| Engine | Domain | September 2 update, as printed by RankControl | November 3 update |
|---|---|---|---|
| ChatGPT | Reddit | 16.8%, first | 6.2%, second |
| ChatGPT | Wikipedia | 7.0%, second | 10.1%, first |
| Perplexity | Reddit | 21.6%, first | 24.6%, first |
| Perplexity | YouTube | 20.8%, second | 14.2%, second |
| Gemini | Reddit | 28.5%, first | 29.9%, first |
| Gemini | YouTube | 14.6%, second | 6.3%, third |
| Google AI Mode | Reddit | 17.9%, first | 18.1%, second |
| Google AI Mode | YouTube | 17.8%, second | 17.0%, third |
| Google AI Mode | google.com | 12.5%, third | 23.4%, first |
| Google AI Overviews | YouTube | 22.9%, first | 24.5%, first |
| Google AI Overviews | Reddit | 18.5%, second | 18.1%, second |
| Google AI Overviews | Facebook | 10.1%, third | 12.4%, third |
| Copilot | Amazon | 16.8%, first | 16.1%, first |
| Copilot | Walmart | 12.6%, second | 11.8%, second |

2 months with 4 big moves: ChatGPT -10.6 down Reddit; Wikipedia +3.1 up; AI Mode +10.9 google.com first place; YouTube Gemini -8.3, Perplexity -6.6. All other numbers in the table are within 3.0 points. Google AI Overviews maintaining YouTube, Reddit and Facebook as 3-peat. Copilot maintaining Amazon in front of Walmart.

## Claude sits outside the Ahrefs lists

379,321 Claude citations (over 16,406 domains) were analyzed by OtterlyAI in June 2026, categorized into 11 source categories. Company & product sites accounted for 64.0% of citations; News & Media 14.9%.; social media was 0.9%, of which LinkedIn accounted for 43.1% of social media citations; Reddit was cited 0 times. The top 10 domains accounted for 9.5% of all Claude citations. 32.9% of cited domains were cited only once.

Claude's web search uses third-party providers which [Anthropic's Trust Center](https://trust.anthropic.com/subprocessors) lists. As of Nov 23 2026, the subprocessor page includes these three for web search: Brave Search (all products), TurboPuffer (all products except Claude for Government), Parallel Web Systems, Inc. (same scope as TurboPuffer). No indication is provided of which one is used for which query.

Just re-running Claude vs Brave in June 2026 by Profound showed a reduction to 79.2% of urls in top10 of Brave out of ~400 queries compared to what they showed in March 2025 of 86.7% (13 out of 15 results on 3 queries). The agency blog I was reading it out of (dated July 2 2026) only mentions Brave and TurboPuffer though so it would appear the June 2026 test precedes the appearance of Parallel Web Systems in the list.

## How little the engines agree on sources

If they all accessed the same pool, then you would typically see pages cited by ChatGPT being cited by Perplexity too. When I look at some of these studies, this doesn't seem to be the case. I've put the overlap numbers for the studies I looked at into the table.

| Comparison | Overlap found | Data | Publisher and date |
|---|---|---|---|
| ChatGPT and Perplexity, cited domains | 11.0% in both, 37.4% ChatGPT only, 51.6% Perplexity only | 100,000 prompts | Profound, page posted July 1, 2025 and last modified April 9, 2026 |
| ChatGPT, Claude, Gemini, Perplexity and Google AI Mode | 2.7% of domains (309 of 11,647) in all five, 69.6% in exactly one | 127,198 citations from about 16,400 answers, March 29 to June 27, 2026 | SurfacedBy, June 27, 2026 |
| Claude and ChatGPT | 13% of cited domains, 4.2% of cited URLs | Claude citations from June 2026 | OtterlyAI, June 30, 2026 |
| Gemini and ChatGPT, local-service questions | 8% shared domains, the same top business 4.2% of the time | 1,487 queries, 50 US metros | Steady Demand, reported by MarTech on August 20, 2026 |
| ChatGPT at minimal and at high reasoning | 25.6% of cited domains | 100 prompts run twice | Kevin Indig using Semrush data, May 18, 2026 |
| One engine, consecutive days | 34% to 42% of cited sources in common, by topic area | 4,044 day pairs, 4 engines | arXiv paper, April 8, 2026 |

Concentration is also different and that affects how difficult it is to crack the engines. A SEO consultant named Aleyda Solis wrote on X on May 15, 2026, that she took 9 months of Semrush AI Visibility Index data for 5 categories for ChatGPT and Google AI Mode. For overall 80% share of voice (share of all brand mentions for brand) in April 2026, ChatGPT required 1,621 brands and Google AI Mode required 299 brands (5.4 times different).

The same post found that the April top-10 source overlap between the two platforms ran from 4 of 10 to 6 of 10 by category, and that Reddit was in the top 10 for every category on both. It also found that Wikipedia, ChatGPT's first or second overall source from August 2025 to March 2026, fell to fifth in April.

In her post to X on August 2, she analysed the top 10 cited source domains for the top 15 brands in SaaS, Ecommerce and Finance using the Semrush Enterprise data. for google AI Mode, Gemini and ChatGPT. In all of the verticals, the brand's own domain is a minority. In SaaS, it's 82.3% citing sources outside of the brand's domain. In Finance, 79.4% and in Ecommerce, 69.6%. The data showed that, in all three verticals, AI Mode is the most social led platform. ChatGPT gives more of an evaluative written layer and Gemini falls somewhere in between.

## One engine, many numbers

The first split is engine. Because one engine behaves differently at a given time and in a certain mode. Kevin Indig made a study using semrush ai visibility toolkit and fed twice 100 prompts through ChatGPT GPT-5.2 once with the minimum reasoning and another time with the high reasoning. For 20 buyer journeys in 4 categories.

And got only 25.6% of shared domains from all of them.

Higher reasoning had a source in 68% of answers versus 50%. It increased the average number of sources in the cited answer from 2.6 to 4.5. It used 173 unique domains versus 127. 99 of these domains didn't show up in minimal reasoning.

Plus there's noise (run-to-run). For example, 600 volunteers tried out 12 prompts in three tools (ChatGPT, Claude and Google's AI Overviews, or AI Mode if no Overview) in [SparkToro's study](https://sparktoro.com/blog/new-research-ais-are-highly-inconsistent-when-recommending-brands-or-products-marketers-should-take-care-when-tracking-ai-visibility/), published January 28, 2026. That's 2,961 runs. The chance that two would return the same list of brands was less than 1 in 100. The chance that two would return the same list of brands in the same order was less than 1 in 1000.

The arXiv paper ["Don't Measure Once"](https://arxiv.org/abs/2604.07585), submitted on April 8, 2026 by three researchers at the University of St. Gallen, is the one source that splits the noise by engine. It sent 8 prompts in each of 4 Swiss-German topic areas (telecommunications, real estate sales, sporting goods and consumer electronics) to ChatGPT, Gemini, Google AI Mode and Perplexity daily over a 45 to 46 day window, January 24 to March 20, 2026.

The authors found that for 4044 consecutive day pairs, the average similarity of sources cited varied from 0.34 to 0.42, depending on topic area, suggesting a turnover of around 65% of sources cited from one day to the next. (Jaccard similarity is the fraction of items common to 2 runs, divided by the total items mentioned in either, with 1.0 being exact identity.)

| Engine | Source similarity within 24 hours | Brand similarity within 24 hours | Citation concentration (Gini) |
|---|---|---|---|
| ChatGPT | 0.233 | 0.437 | 0.684 |
| Perplexity | 0.282 | 0.492 | 0.671 |
| Gemini | 0.505 | 0.409 | 0.723 |
| Google AI Mode | 0.318 | 0.375 | 0.782 |

*Jaccard similarity of repeated runs within 24 hours (up to 10 repeats per prompt), and the mean Gini coefficient of citations per domain over January 24 to March 20, 2026, where 0 means every domain gets equal citations and 1.0 means one domain takes them all. From Tables 6 and 15 of the arXiv paper. Gemini returned results on only 22 to 26 days per topic area, against 38 to 44 for the other three.*

in that data, within a day the Gemini sources were most stable and ChatGPT sources were least stable. Also the citations were the most concentrated for AI Mode and least concentrated for Perplexity. Regarding how many repeat are needed for a stable number, they found that detection rate SE for a brand is < 0.10 at 7 runs and source coverage SE is < 0.10 at 8. They recommend at least 7 runs per prompt per day.

Steady Demand's local-search test showed the same effect for one engine: repeating a Gemini query returned overlapping cited sources only about 40% of the time, and Gemini named the same top business about 7% of the time, against about 90% for the same top listing in Google's local pack.

The response to the 28% to 33% question on r/SEO_LLM pointed out it may be a good idea to maintain an unchanged set of similar queries as holdout since a major change in model behavior can be interpreted as the effect of your change in content.

## Citations fade at different speeds

Different engines decay at different rates, too. Scrunch and Stacker looked at 3.5 million citation events between September 2025 and March 2026 and calculated the number of weeks it takes for half of citations for a week to fall off the rotation (what they call the half-life).

| Group | Half-life in weeks |
|---|---|
| ChatGPT | 3.4 |
| Google AI Mode, Gemini and Google AI Overviews | 4.3 to 4.8 |
| All platforms together | About 4.5 |
| Perplexity | 5.8 |
| Domains in Stacker's publisher network | Nearly 10 |

*Scrunch and Stacker, published March 26, 2026, covering September 2025 to March 2026.*

On those averages, about half of the citations ChatGPT hands out in the first week of October would be gone by the end of the month, while half of Perplexity's from the same week would hold on until about mid-November. That is arithmetic on the averages, not something either company reported for a named week.

network row is from an interested party (stacker pushes out content via their publisher network, which they used for this study with scrunch). note that the per-engine differences are not dependent on the result.

![Poster of six figures from 2026 studies: 11% of domains shared by ChatGPT and Perplexity, 2.7% of domains cited by all 5 engines, 25.6% overlap between minimal and high reasoning, 65% of cited sources change daily, 3.4 versus 5.8 weeks to lose half the citations, and 0 Reddit citations among 379,321 Claude citations](/assets/img/gh-037-ai-visibility-per-engine-citation-data-info-t1.jpg)

*Figures from the studies above, read on November 23, 2026. The 65% is the arXiv paper's day-to-day change in cited sources, and 3.4 and 5.8 weeks are the half-lives on ChatGPT and Perplexity.*

## The denominator problem

Each AI visibility number is a percentage of something... but what exactly that something is depends on the tool. On ChatGPT, Reddit has three numbers, two different denominators. For example, an AI citation tracking tool called Promptwatch said that, on average, from July 18 to August 7 2026, Reddit was 3.83% of ChatGPT Search citations. Then, from August 14-17, it was 0.52%, which is a 86.4% relative decrease (covered by Search Engine Journal on August 19).

Ahrefs counts Reddit against the top 50 domains in a different query set instead, and gave it 16.8% in the September 2 update (as RankControl printed it) and 6.2% on November 3. Search Engine Journal called the cause of the August drop unconfirmed, while RankControl's own post on it ties the drop to the GPT-5.6 rollout on August 8.

Gemini's query mix illustrates this. In the general US list provided by ahrefs, reddit makes up 29.9% of the top 50 citations in gemini. From steady demand's analysis of 14,472 Gemini citations to 1,487 local service queries for 50 metro areas in the US: 59.9% of the citations were to the business' website. Reddit was the next at 13.7%. Directories were 10.4%.

Another example: Wikipedia on ChatGPT. Solis seemed to be looking at data from Semrush showing that Wikipedia dropped to #5 in April 2026. Ahrefs' lists say Wikipedia was climbing from 2nd in September to 1st by November.

Having a blended score gives you yet another denominator, weighting engines that it picked for you. That's what happened to the first poster on r/SEO_LLM when two tools were giving different info about the same brand.

## What a per-engine AI visibility report records

In RankControl's post from October they talk about reporting AI visibility. The correct way to report AI visibility is the same way the data arrives. It's one line per engine. Same way every week. Every engine it's good to have four things for a report:

- The share of your fixed buyer questions where one of your pages is cited
- The share where your brand is named, with or without a link
- The competitors named in the same answers
- The outside domains the engine cited, which show where to pitch next

RankControl's [AI visibility tracker](https://rctrl.com/ai-visibility) tracks citations across 7 AI engines: ChatGPT, Perplexity, Claude, Gemini, Grok, Google AI Mode and Google AI Overviews. Its page says each of 50 tracked questions is checked every week on all seven, and that each citation is logged with the engine, the question and the page cited. Copilot is not one of the seven, so the Copilot row in the first table has no RankControl tracking behind it.

It's labor intensive. RankControl guesses that checking 50 questions against 7 engines is like 6 hours per week, or about a minute per check. Extra checks (repeating) multiply that. Posting 8 good articles a month is another 16-24 hrs. You can make your own per-engine report if you have a spreadsheet and a protected hour a week. Or you can have a tool do the weekly check for you. That's the role of RankControl's tracker.
