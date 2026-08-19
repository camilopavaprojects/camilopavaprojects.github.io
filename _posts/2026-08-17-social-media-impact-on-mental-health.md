---
layout: post
title: "Social Media's Impact on Mental Health"
date: 2026-08-17
---

I explored a synthetic dataset of 1,200 teenagers to see whether daily social media usage could predict depression risk. The headline number looked great — but digging past overall accuracy revealed the model was quietly failing at the one thing that mattered most: catching the teens actually at risk.

## Introduction

Social media's effect on teen mental health is one of the most debated topics in public health right now, but hard evidence is often mixed and hard to pin down. I wanted to explore a narrower, more concrete version of that question: using behavioral and engagement data, can we predict whether a teenager is at risk of depression?

To dig into this, I used a synthetic dataset from Kaggle — [Social Media Impact on Mental Health](https://www.kaggle.com/datasets/sunil123kumar/social-media-impact-on-mental-health) — covering 1,200 teenagers across 13 features, with `depression_label` as the target variable. Because the data is synthetic, it's a safe sandbox for exploring these dynamics without the ethical and privacy issues that come with real teen mental health data — but it also means the patterns reflect how the dataset was generated, not necessarily real-world behavior. More on that in the caveats below.

What I found challenged my first read of the results: a model can post strong overall accuracy while still missing most of the actual depression cases — the exact group you'd most want to catch.

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

## Project Roadmap (brief overview of all 5 phases)

The project comprises five phases:
1. Data preparation & preprocessing
2. Exploratory data analysis & descriptive analytics
3. Statistical hypothesis testing
4. Predictive modelling/machine learning
5. Communication & design
