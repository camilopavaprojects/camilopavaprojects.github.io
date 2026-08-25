import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ==========================================
# 1. LOAD DATA & SELECT FOCUS COLUMNS
# ==========================================
df_clean = pd.read_csv('Teen_Mental_Health_Clean.csv')

focus_columns = [
    'daily_social_media_hours',
    'screen_time_before_sleep',
    'sleep_hours',
    'social_interaction_encoded',
    'stress_level',
    'anxiety_level',
    'depression_label'
]   

# ==========================================
# 2. CORRELATION MATRIX & EXPORT
# ==========================================
correlation_matrix = df_clean[focus_columns].corr()
correlation_matrix.to_csv('correlation_matrix.csv', index=False)

# ==========================================
# 3. FIGURE 1: CORRELATION HEATMAP
# ==========================================
plt.figure(figsize=(10, 8)) # Creates Window 1
sns.heatmap(
    correlation_matrix, 
    annot=True,             
    cmap='coolwarm',        
    fmt=".2f",              
    vmin=-1, vmax=1,        
    linewidths=0.5          
)
plt.title('Teen Mental Health & Social Media Feature Correlations', fontsize=14, pad=15)

# Rotate x-axis labels by 45 degrees and align them to the right
plt.xticks(rotation=45, ha='right')

# Optional but recommended: ensure y-axis labels stay perfectly horizontal
plt.yticks(rotation=0) 

plt.tight_layout()

# ==========================================
# 4. FIGURE 2: DISTRIBUTIONS (HISTOGRAMS & BOXPLOTS)
# ==========================================
fig, axes = plt.subplots(2, 2, figsize=(12, 8)) # Creates Window 2

# Row 1: Histograms
sns.histplot(df_clean['daily_social_media_hours'], kde=True, ax=axes[0, 0], color='skyblue')
axes[0, 0].set_title('Histogram: Social Media Hours', fontsize=12)

sns.histplot(df_clean['sleep_hours'], kde=True, ax=axes[0, 1], color='salmon')
axes[0, 1].set_title('Histogram: Sleep Hours', fontsize=12)

# Row 2: Boxplots
sns.boxplot(x=df_clean['daily_social_media_hours'], ax=axes[1, 0], color='skyblue')
axes[1, 0].set_title('Boxplot: Social Media Hours', fontsize=12)

sns.boxplot(x=df_clean['sleep_hours'], ax=axes[1, 1], color='salmon')
axes[1, 1].set_title('Boxplot: Sleep Hours', fontsize=12)

plt.tight_layout()

# ==========================================
# 5. DISPLAY ALL WINDOWS
# ==========================================
# Calling plt.show() once at the end pops open both Window 1 and Window 2 simultaneously!
plt.show()