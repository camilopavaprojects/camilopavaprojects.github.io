---
layout: post
title: "Social Media's Impact on Mental Health"
date: 2026-08-17
---

I explored a synthetic dataset of 1,200 teenagers to see whether daily social media usage could predict depression risk. The overall accuracy looked great, but after delving into it the outcome revealed that the model was quietly failing at the one thing that mattered most: catching the teens actually at risk.

## Introduction

Social media's effect on teen mental health is one of the most debated topics in public health right now, but factual evidence is often mixed and hard to pin down. I wanted to explore a narrower, more concrete version of that question: using behavioral and engagement data, can we predict whether a teenager is at risk of depression?

To this end, I used a synthetic dataset from Kaggle: [Social Media Impact on Mental Health](https://www.kaggle.com/datasets/sunil123kumar/social-media-impact-on-mental-health). It reports 1,200 teenagers across 13 variables, with `depression_label` as the target variable. Because the data is synthetic, it's a safe choice for exploring these dynamics without the ethical and privacy issues that come with real patient (mental) health data. It also means the patterns reflect how the dataset was generated, not necessarily real-world behavior. More on that in the caveats below.

What I found challenged my first read of the results: a model can display strong overall accuracy while still missing most of the actual depression cases, the very group you would care the most.

## The Data

The dataset's 13 variables fall into four natural groups:

**Demographics**
- Age
- Gender

**Social media behavior**
- daily_social_media_hours
- Platform usage
- Screen time before sleep

**Lifestyle factors**
- sleep_hours
- Academic performance
- Physical activity
- Social interaction level

**Mental health indicators**
- Stress level
- Anxiety level
- Addiction level
- Depression level (the target variable, `depression_label`)

To frame the analysis, I treated social media engagement, mainly platform usage and screen time before sleep, as the independent variables of interest, and the mental health indicators (stress, anxiety, and depression) as the outcomes I was trying to explain.

## Project Roadmap

The project comprises five phases:
1. Data preparation & preprocessing
2. Exploratory data analysis & descriptive analytics
3. Statistical hypothesis testing
4. Predictive modelling/machine learning
5. Communication & design

## 1. Data preparation & preprocessing

I ran a Extraction, Transformation and Load (ETL) process that also included handling missing values, fixing typos, and encoding text variables into numbers (Ordinal and One-Hot encoding).

**Ordinal Encoding for `[social_interaction_level]`**

| Interaction Level | Encoded Value |
|---|:---:|
| Low | 0 |
| Medium | 1 |
| High | 2 |

**One-Hot Encoding for `[platform_usage]`**

| Original Category | `is_Instagram` | `is_TikTok` | `is_Both` |
|---|:---:|:---:|:---:|
| Instagram | 1 | 0 | 0 |
| TikTok | 0 | 1 | 0 |
| Both | 0 | 0 | 1 |

The outcome of phase 1 was the generation of a new clean data set 'Teen_Mental_Health_Clean.csv'

## 2. Exploratory data analysis & descriptive analytics

Goal: Explore relationships and validate hypotheses.

Steps: descriptive statistics, checking column counts, computing correlation matrices, and generating plots/visualizations (heatmaps) to see how variables interact.

Figure 1 displays the distributions of daily_social_media_hours and sleep_hours. It reveals a non-bell shape distribution.

<figure align="center">
  <img src="/Assets/Images/Histograms_Boxplots.png" alt="Distribution of daily social media hours and sleep hours" width="100%">
  <figcaption><em>Figure 1: Distributions of daily social media hours and sleep hours (histograms and boxplots).</em></figcaption>
</figure>

I focused on `depression_label` as the target parameter, treated lifestyle factors as covariates, and tested a specific hypothesis: does social media disrupt sleep, and does that disrupted sleep drive anxiety and depression, rather than social media affecting mental health directly?

The results didn't support it. Looking at the correlation matrix in Figure 2, daily_social_media_hours, screen_time_before_sleep, and sleep hours all showed essentially zero correlation with each other (r ≈ -0.01). The one real signal was a weak direct link between social media use and depression (r = 0.18) — bypassing sleep entirely.

<p align="center">
  <img src="/Assets/Images/HeatMapCorrelations.png" alt="Correlation heatmap of social media, sleep, and mental health variables" width="90%"><br>
  <em>Figure 2. Correlation matrix.</em>
</p>

Likely explanation: this is synthetic data, and some columns appear to have been generated independently of each other. A clean null result here says more about the dataset's construction than about real teenagers.

## 3. Statistical hypothesis testing

Goal: Confirm whether the relationships spotted in the heatmap are statistically real, or just noise from this particular sample.

Steps: Run a Spearman rank correlation test (rather than Pearson) to check the sleep–social media relationship, since the data's bimodal distribution makes a straight-line Pearson correlation unreliable. Then use an independent two-sample T-test to compare average social media hours between the depressed and non-depressed groups, since `depression_label` is categorical rather than continuous.

The Spearman test confirmed Phase 2's read: ρ = -0.0086, p = 0.77 which not statistically significant. Any apparent link between social media and sleep is random noise in this dataset, not a real effect.

The T-test told a different story. Teens with a depression label averaged 6.72 hours of daily social media use, versus 4.48 hours for those without — a gap far too large to be chance (p < 0.0001). Whatever the mechanism, it isn't sleep: it's a direct, statistically solid relationship between social media use and depression.

## 4. Predictive modelling / machine learning

Goal: Predict `depression_label` using the variables Phase III flagged as significant, and see how well a model actually performs.

Steps: Split the data 80/20 into train and test sets, stratified so both sets kept the same ratio of depressed vs. non-depressed teens. Trained a Logistic Regression model on `daily_social_media_hours` to predict depression, then evaluated it with accuracy, a confusion matrix, and recall.

First result: 97.5% accuracy. Looked great, until I checked what the model was actually doing. It had learned to predict "not depressed" for everyone. Since only 6 of 240 teens in the test set were labeled depressed, guessing "no" every time was enough to score 97.5% while catching zero actual depression cases i.e. Recall: 0%.

That's the accuracy trap: a metric that looks strong while the model fails at the one job that mattered:

<p align="center">
  <img src="/Assets/Images/ConfusionMatrix_no_balanced.png" alt="Confusion Matrix: Social Media vs. Teen Depression" width="80%"><br>
  <em>Figure 3: Baseline model — predicts "not depressed" for everyone.</em>
</p>

I adjusted the model with `class_weight='balanced'`, which penalizes the model for missing the minority class. Recall jumped to 66.7% (4 of 6 caught), but accuracy dropped to 74.6%, with 59 false alarms along the way. Classic precision-recall trade-off.

<p align="center">
  <img src="/Assets/Images/ConfusionMatrix_class_weight_balanced.png" alt="Confusion matrix, class-weight balanced" width="80%"><br>
  <em>Figure 4: After setting class_weight='balanced' recall improves, false positives rise.</em>
</p>

Given the context, I'd rather over-flag healthy teens than miss ones at risk, a false alarm costs a follow-up conversation, a missed case costs a lot more. This is a baseline, not a finished model; adding more variables beyond social media hours alone is the obvious next step.

## Conclusion

This project set out to answer a simple question: can social media habits predict teen depression risk? It ended up teaching a bigger lesson than the answer itself. Sleep didn't turn out to be the hidden link I expected. Social media use did show a real, statistically significant relationship with depression. And the model built on that relationship looked excellent by one metric while being nearly useless by the metric that actually mattered.

That gap between "the model looks good" and "the model does its job" is the core takeaway. It's also the reason Phase III (hypothesis testing) and Phase IV (evaluation beyond accuracy) exist as distinct steps rather than shortcuts to skip.

This was a first pass, built on a single variable and a synthetic dataset. The natural next step is bringing in more predictors — sleep, stress, anxiety, physical activity — and testing whether a richer model can catch more at-risk teens without the trade-off getting worse.
