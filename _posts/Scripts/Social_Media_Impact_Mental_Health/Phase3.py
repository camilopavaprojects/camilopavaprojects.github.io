import pandas as pd
from scipy import stats

# ==========================================
# 1. LOAD CLEAN DATASET
# ==========================================
df_clean = pd.read_csv('Teen_Mental_Health_Clean.csv')

# ==========================================
# 2. SPEARMAN TEST: Social Media vs. Sleep
# ==========================================
sm_hours = df_clean['daily_social_media_hours']
sleep_hours = df_clean['sleep_hours']

# Calculate
spearman_stat, p_value_spearman = stats.spearmanr(sm_hours, sleep_hours)

# Output
print("\n--- Phase 3: Spearman Test (Social Media vs. Sleep) ---")
print(f"Statistic: {spearman_stat:.4f} | p-value: {p_value_spearman:.4f}")

if p_value_spearman < 0.05:
    print("Result: SIGNIFICANT. There is a mathematical relationship.")
else:
    print("Result: NOT SIGNIFICANT. Any observed correlation is likely random chance.")

# ==========================================
# 3. T-TEST: Social Media vs. Depression
# ==========================================
# Filter social media hours by depression label (0 = No, 1 = Yes)
sm_no_depression = df_clean[df_clean['depression_label'] == 0]['daily_social_media_hours']
sm_yes_depression = df_clean[df_clean['depression_label'] == 1]['daily_social_media_hours']

# Calculate
t_stat, p_value_ttest = stats.ttest_ind(sm_no_depression, sm_yes_depression)

# Output
print("\n--- Phase 3: T-Test (Social Media vs. Depression) ---")
print(f"Avg SM Hours (No Depression): {sm_no_depression.mean():.2f}")
print(f"Avg SM Hours (Depression):    {sm_yes_depression.mean():.2f}")
print(f"Statistic: {t_stat:.4f} | p-value: {p_value_ttest:.4f}")

if p_value_ttest < 0.05:
    print("Result: SIGNIFICANT. Depressed teens consume different amounts of social media.")
else:
    print("Result: NOT SIGNIFICANT. No mathematical difference between groups.")