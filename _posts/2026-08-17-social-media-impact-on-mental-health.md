---
layout: post
title: "Social Media's Impact on Mental Health"
date: 2026-08-17
---

## Introduction

Social media's effect on teen mental health is one of the most debated topics in public health right now, but hard evidence is often mixed and hard to pin down. I wanted to explore a narrower, more concrete version of that question: using behavioral and engagement data, can we predict whether a teenager is at risk of depression?

To dig into this, I used a synthetic dataset from Kaggle — [Social Media Impact on Mental Health](https://www.kaggle.com/datasets/sunil123kumar/social-media-impact-on-mental-health) — covering 1,200 teenagers across 13 features, with `depression_label` as the target variable. Because the data is synthetic, it's a safe sandbox for exploring these dynamics without the ethical and privacy issues that come with real teen mental health data — but it also means the patterns reflect how the dataset was generated, not necessarily real-world behavior. More on that in the caveats below.

What I found challenged my first read of the results: a model can post strong overall accuracy while still missing most of the actual depression cases — the exact group you'd most want to catch.
