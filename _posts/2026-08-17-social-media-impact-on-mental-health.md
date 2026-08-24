---
layout: post
title: "Social Media's Impact on Mental Health"
date: 2026-08-17
---

I explored a synthetic dataset of 1,200 teenagers to see whether daily social media usage could predict depression risk. The headline number looked great, but digging initial overall accuracy revealed the model was quietly failing at the one thing that mattered most: catching the teens actually at risk.

## Introduction

Social media's effect on teen mental health is one of the most debated topics in public health right now, but hard evidence is often mixed and hard to pin down. I wanted to explore a narrower, more concrete version of that question: using behavioral and engagement data, can we predict whether a teenager is at risk of depression?

To dig into this, I used a synthetic dataset from Kaggle — [Social Media Impact on Mental Health](https://www.kaggle.com/datasets/sunil123kumar/social-media-impact-on-mental-health) — covering 1,200 teenagers across 13 variables, with `depression_label` as the target variable. Because the data is synthetic, it's a safe sandbox for exploring these dynamics without the ethical and privacy issues that come with real teen mental health data — but it also means the patterns reflect how the dataset was generated, not necessarily real-world behavior. More on that in the caveats below.

What I found challenged my first read of the results: a model can display strong overall accuracy while still missing most of the actual depression cases — the exact group you'd most want to catch.

## The Data

The dataset's 13 variables fall into four natural groups:

**Demographics**
- Age
- Gender

**Social media behavior**
- Daily social media hours
- Platform usage
- Screen time before sleep

**Lifestyle factors**
- Sleep hours
- Academic performance
- Physical activity
- Social interaction level

**Mental health indicators**
- Stress level
- Anxiety level
- Addiction level
- Depression level (the target variable, `depression_label`)

To frame the analysis, I treated social media engagement — mainly platform usage and screen time before sleep — as the independent variables of interest, and the mental health indicators (stress, anxiety, and depression) as the outcomes I was trying to explain.

## Project Roadmap

The project comprises five phases:
1. Data preparation & preprocessing
2. Exploratory data analysis & descriptive analytics
3. Statistical hypothesis testing
4. Predictive modelling/machine learning
5. Communication & design

## 1. Data preparation & preprocessing

I run a Extraction, Transformation and Load (ETL) process that also included handling missing values, fixing typos, and encoding text variables into numbers (Ordinal and One-Hot encoding).

Ordinal Encoding for [social_interaction_level]
- Low -> 0
- Medium --> 1
- High --> 2

One-Hot encoding for [gender]
Instagram -> 1 Yes / 0 No
TikTok -> 1 Yes / 0 No
Both -> 1 Yes / 0 No

The outcome of phase I was the generation of a new clean data set 'Teen_Mental_Health_Clean.csv'

## 2. Exploratory data analysis & descriptive analytics

Goal: Explore relationships and validate hypotheses.

Steps: descriptive statistics, checking column counts, computing correlation matrices, and generating plots/visualizations (heatmaps) to see how variables interact.

I focused on `depression_label` as the target, treated lifestyle factors as covariates, and tested a specific hypothesis: does social media disrupt sleep, and does that disrupted sleep drive anxiety and depression — rather than social media affecting mental health directly?

![Correlation heatmap of social media, sleep, and mental health variables](/Assets/Images/HeatMapCorrelations.png)

The results didn't support it. Social media hours, bedtime screen time, and sleep hours all showed essentially zero correlation with each other (r ≈ -0.01). The one real signal was a weak direct link between social media use and depression (r = 0.18) — bypassing sleep entirely.

Likely explanation: this is synthetic data, and some columns appear to have been generated independently of each other. A clean null result here says more about the dataset's construction than about real teenagers — a good reminder to sanity-check synthetic data before trusting its correlations.

## 3. Statistical hypothesis testing

Goal: Confirm whether the relationships spotted in the heatmap are statistically real, or just noise from this particular sample.

Steps: Run a Spearman rank correlation test (rather than Pearson) to check the sleep–social media relationship, since the data's bimodal distribution makes a straight-line Pearson correlation unreliable. Then use an independent two-sample T-test to compare average social media hours between the depressed and non-depressed groups, since `depression_label` is categorical rather than continuous.

The Spearman test confirmed Phase II's read: ρ = -0.0086, p = 0.77 — not statistically significant. Any apparent link between social media and sleep is random noise in this dataset, not a real effect.

The T-test told a different story. Teens with a depression label averaged 6.72 hours of daily social media use, versus 4.48 hours for those without — a gap far too large to be chance (p < 0.0001). Whatever the mechanism, it isn't sleep: it's a direct, statistically solid relationship between social media use and depression.

## 4. Predictive modelling / machine learning

Goal: Predict `depression_label` using the variables Phase III flagged as significant, and see how well a model actually performs.

Steps: Split the data 80/20 into train and test sets, stratified so both sets kept the same ratio of depressed vs. non-depressed teens. Trained a Logistic Regression model on `daily_social_media_hours` to predict depression, then evaluated it with accuracy, a confusion matrix, and recall.

First result: 97.5% accuracy. Looked great, until I checked what the model was actually doing. It had learned to predict "not depressed" for everyone. Since only 6 of 240 teens in the test set were labeled depressed, guessing "no" every time was enough to score 97.5% — while catching zero actual depression cases. Recall: 0%.

That's the accuracy trap: a metric that looks strong while the model fails at the one job that mattered.

I refit the model with `class_weight='balanced'`, which penalizes the model for missing the minority class. Recall jumped to 66.7% (4 of 6 caught), but accuracy dropped to 74.6%, with 59 false alarms along the way. Classic precision-recall trade-off.

Given the context, I'd rather over-flag healthy teens than miss ones at risk — a false alarm costs a follow-up conversation, a missed case costs a lot more. This is a baseline, not a finished model; adding more variables beyond social media hours alone is the obvious next step.
