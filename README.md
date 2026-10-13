# Good weather, city by city

A city-first climate atlas for people planning a trip or considering a move. Compare **cities within each country**, choose a weather preference and inspect the monthly data behind the shortlist.

**90 city/station candidates · 23 countries · 1991-2020 climate normals · research checked 13 October 2026.**

## Start here

**[Open the live climate atlas](https://vb-instinct.github.io/best-weather-cities/)**

If Pages is unavailable, download [index.html](index.html) and open it in any modern browser. It is self-contained: no dependencies, tracking, accounts or network requests needed for the comparisons.

1. Choose a country.
2. Choose your travel month, or compare the whole year.
3. Switch between **mild + drier**, **mild temperature** and **warmer** preferences.
4. Open a city's monthly values. Read its station caveat before treating the data as the weather in your neighbourhood.

## The short answer

Coastal San Diego and Los Angeles, Funchal, Agadir and Essaouira are useful long-season starting points in this candidate set. But there is no universal winner. Pereira and Coffs Harbour have mild monthly temperature averages and substantial rain. Mediterranean cities often suit spring or autumn better than the peak summer. Highland towns can be cool but wet.

The atlas ranks candidates **within countries**, never whole countries against each other. It also explains why changing your rain or temperature preference changes the answer.

## What a rank does and does not mean

The default rule counts months with average daily highs of 18-28 C, lows of 8-20 C and monthly precipitation at most 100 mm. These are editorial preferences, not scientific comfort limits. A fit month is a monthly historical average, not a promise of comfortable weather every day.

This is a curated shortlist, not every city in the world or in each country. A missing city is not a negative verdict. Ranks do not include humidity, wind, fog, sunshine, UV, air quality, sea temperature, extreme-event risk, housing, visas, healthcare, safety or living costs.

## Evidence and reuse

| File | What it is for |
| --- | --- |
| [index.html](index.html) | Interactive, mobile-first atlas. Country, month and preference controls; full monthly values and source links. |
| [METHODOLOGY.md](METHODOLOGY.md) | Thresholds, tie-breaks, sampling limits, station proxies, exclusions and update process. |
| [SOURCES.md](SOURCES.md) | Exact sources, claims used, retrieval date and source-file hashes. |
| [cities-monthly.csv](cities-monthly.csv) | 1,080 station-month records, labelled in C and mm, with station IDs and source-family keys (exact links in JSON and source ledger). |
| [cities.json](cities.json) | Structured city records and all monthly arrays used by the page. |
| [check_data.py](check_data.py) | Re-run the data audit locally with Python 3; no network or dependencies. |
| [QUALITY.md](QUALITY.md) | Data and interface checks, remaining limitations and upgrade priorities. |

Most numbers come from national meteorological-service submissions to the WMO, hosted by NOAA NCEI. Portugal uses IPMA station PDFs. The same **1991-2020** baseline is kept throughout. The supplied [SMH Traveller article](https://www.smh.com.au/traveller/reviews-and-advice/the-worlds-greatest-climates-top-cities-to-visit-for-perfect-weather-all-year-round-20161104-gshzcu.html) inspired the question; its historic rankings and values were not reused as current data.

## Countries in this edition

Argentina, Australia, Brazil, Chile, China, Colombia, Cyprus, France, India, Italy, Japan, Mexico, Morocco, New Zealand, Portugal, Rwanda, South Africa, Spain, Tunisia, Türkiye, United Kingdom, United States and Uruguay.

The samples vary in size. Italy and the UK have only two cities each, so their ranking is particularly limited. Ecuador and Namibia are not ranked despite appearing in the inspiration article: comparable verified station data were not obtained in this run.

## Before using this to make a decision

Climate normals are historical averages, not forecasts or present-day guarantees. For travel, check current forecasts and official warnings before booking. For relocation, test the actual neighbourhood in the least comfortable season and research the non-climate factors separately.

No personal data, credentials or source article text are included. Original data rights remain with their publishers. This project is climate context, not a relocation or safety recommendation.
