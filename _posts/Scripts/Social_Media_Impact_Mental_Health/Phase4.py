import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import recall_score, classification_report

# ==========================================
# 1. LOAD CLEAN DATASET
# ==========================================
df_clean = pd.read_csv('Teen_Mental_Health_Clean.csv')

# ==========================================
# 2. Isolate features (X) and target (y)
# ==========================================
x = df_clean[['daily_social_media_hours']]
y = df_clean['depression_label']

# ==========================================
# 3 & 4. Perform 80/20 stratified split
# ==========================================
x_train, x_test, y_train, y_test = train_test_split(
    x, y, 
    test_size=0.2,      # 20% for testing, 80% for training
    stratify=y,         # Maintains class proportions in both splits
    random_state=42     # Ensures reproducible results
)

# ==========================================
# 5. INITIALIZE THE MODEL
# ==========================================
# We use a random_state here as well so your results remain reproducible
#model = LogisticRegression(random_state=42)
model = LogisticRegression(class_weight='balanced', random_state=42)

# ==========================================
# 6. TRAIN (FIT) THE MODEL
# ==========================================
# The model learns the relationship between social media hours and depression
model.fit(x_train, y_train)

print("Model successfully trained!")

# ==========================================
# 7. MAKE PREDICTIONS ON THE TEST DATA
# ==========================================
# The model looks at the test features and guesses the label (0 or 1)
predictions = model.predict(x_test)

# ==========================================
# 8. EVALUATE ACCURACY
# ==========================================
# We compare the model's guesses against the actual answers
accuracy = accuracy_score(y_test, predictions)

print(f"Model Accuracy: {accuracy * 100:.2f}%")

# ==========================================
# 9. CONFUSION MATRIX
# ==========================================
# Generate the raw numbers
cm = confusion_matrix(y_test, predictions)
print("Confusion Matrix:\n", cm)

# Visualize it using a heatmap for better readability
plt.figure(figsize=(6, 4))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', 
            xticklabels=['No Depression (0)', 'Depression (1)'],
            yticklabels=['No Depression (0)', 'Depression (1)'])
plt.ylabel('Actual Label')
plt.xlabel('Predicted Label')
plt.title('Confusion Matrix: Social Media vs. Teen Depression')
plt.show()

# ==========================================
# 10. EVALUATE RECALL & CLASSIFICATION REPORT
# ==========================================
# Calculate Recall specifically for the depression class (label 1)
recall = recall_score(y_test, predictions)

print(f"Model Recall (Sensitivity): {recall * 100:.2f}%")

# Generate a complete metric overview
print("\nFull Classification Report:")
print(classification_report(
    y_test, 
    predictions, 
    target_names=['No Depression (0)', 'Depression (1)']
))

