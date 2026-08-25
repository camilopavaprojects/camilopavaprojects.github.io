import pandas as pd

# 1. Set display options to see all columns
pd.set_option('display.max_columns', None)

# 2. Load the data
df = pd.read_csv('Teen_Mental_Health_Dataset.csv')

# 3. Ordinal Encoding (Social Interaction)
df['social_interaction_encoded'] = df['social_interaction_level'].map({
    'low': 0, 
    'medium': 1, 
    'high': 2
})

# 4. One-Hot Encoding (Platform Usage and Gender)
df_clean = pd.get_dummies(df, columns=['platform_usage', 'gender'], dtype=int)

# 5. Take a look at the new columns we created!
# Let's print the head of our newly engineered dataset
print(df_clean.head())

# Save the newly cleaned data to a new CSV file
df_clean.to_csv('Teen_Mental_Health_Clean.csv', index=False)
print("Phase 1 complete. Cleaned data saved!")