# Task_04_Descriptive_Stats

# Task 04 – Descriptive Statistics Engine

This repository contains three independent implementations that produce identical descriptive-statistics outputs for the 2024 US-presidential-election social-media datasets:

---

## 1 · Project Overview

The goal was to build a reproducible “stats engine” that generates identical descriptive-statistics outputs using three different strategies:

* Base Python (standard library only)
* Pandas
* Polars

The project not only focuses on producing the same numerical output but also documents the experience of comparing each approach: challenges, performance, usability, and recommendations.

| Script                  | Tech stack                     |
| ----------------------- | ------------------------------ |
| pure\_python\_fb\_\*.py | Python 3 standard library only |
| pandas\_fb\_\*.py       | pandas                         |
| polars\_fb\_\*.py       | polars                         |

Each script processes:

* Facebook Ads
* Facebook Posts
* Twitter Posts

Each script produces identical `.csv` summaries in `output/`, with `data/` excluded from GitHub.

---

## 2 · Quick Start

### #1 · Clone repo & enter folder

```bash
git clone https://github.com/<your-handle>/Task_04_Descriptive_Stats.git
cd Task_04_Descriptive_Stats
```

### #2 · Create & activate virtual env

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

### #3 · Drop CSVs into data/ folder

Place these files (excluded from GitHub):

* 2024\_fb\_ads\_president\_scored\_anon.csv
* 2024\_fb\_posts\_president\_scored\_anon.csv
* 2024\_tw\_posts\_president\_scored\_anon.csv

### #4 · Run any engine per dataset

```bash
# Facebook Ads
python pure_python_fb_ads.py
python pandas_fb_ads.py
python polars_fb_ads.py

# Facebook Posts
python pure_python_fb_posts.py
python pandas_fb_posts.py
python polars_fb_posts.py

# Twitter Posts
python pure_python_tw_posts.py
python pandas_tw_posts.py
python polars_tw_posts.py
```

Each script outputs a summary CSV to the `output/` folder.

---

## 3 · Performance Benchmark (M2 MacBook Air)

| Dataset   | Engine | Runtime (s) |
| --------- | ------ | ----------- |
| tw\_posts | Pandas | 0.18        |
| tw\_posts | Polars | 0.05        |
| tw\_posts | Stdlib | 0.97        |
| fb\_ads   | Pandas | 11.64       |
| fb\_ads   | Polars | 0.60        |
| fb\_ads   | Stdlib | 25.47       |
| fb\_posts | Pandas | 0.68        |
| fb\_posts | Polars | 0.07        |
| fb\_posts | Stdlib | 1.86        |

---

## 4 · Key Findings

### Performance Takeaways

| Observation            | Evidence                        | Why It Matters                |
| ---------------------- | ------------------------------- | ----------------------------- |
| **Polars is fastest**  | 3—5× faster than Pandas         | Best for large data workflows |
| **Stdlib is slowest**  | 25s vs 0.6s on fb\_ads          | Only good for teaching/demo   |
| **fb\_ads is largest** | pandas: 11.64s vs polars: 0.60s | Stresses engine performance   |

### Experience Summary

* It was challenging to ensure identical grouping and value counting across all engines due to differences in defaults and data type handling.
* Polars required careful renaming of value counts columns to enable sorting.
* Pure Python required custom aggregation logic and was verbose.

### Recommendations

* ✅ Use **Polars** for >1MB or 50k+ rows
* ✅ Use **Pandas** for productivity, merging, and ecosystem support
* 🚫 Avoid **Stdlib** except for educational purposes

---

## 5 · Answers to Professor’s Reflection Prompts

* **Was it a challenge to produce identical results?**

  * Yes. Data type inconsistencies and missing values were handled differently. Ensuring consistent value counting, especially on categorical fields, was tricky.

* **How did you overcome challenges?**

  * Standardized null removal, string conversions, sorted value counts, and verified using same column order in outputs.

* **Which engine do you prefer and why?**

  * Polars: clean, fast, intuitive once syntax is familiar. Performs best with large files.

* **Which would you recommend to a junior analyst?**

  * Start with Pandas. It has the most documentation and flexibility.

* **Did you use ChatGPT to generate starter code?**

  * Yes. It provided helpful templates and function outlines, especially for pure Python logic and for structuring value\_counts/sorting in Polars.

* **Does AI recommend one engine by default?**

  * Yes, ChatGPT generally defaults to Pandas unless asked specifically. It sees Pandas as the industry standard.

* **Do you agree with AI's default recommendation of using one engine when asked to produce descriptive statistics??**

  * Yes, I agree that Pandas is often recommended by default because of its wide adoption, rich documentation, and intuitive syntax. However, based on this project, I would now recommend Polars as the new default when working with medium to large datasets. Polars is significantly faster, uses less memory, and scales better. For beginners, Pandas is still a great starting point, but for performance, Polars clearly leads.

---

## 6 · Technical Pipeline

CSV → DataFrame →

* numeric cols → count / mean / std / min / max
* categorical cols → top 3 values + counts
* group-by `page_id`, `ad_id` → aggregation stats
* output written to `output/` folder

---


