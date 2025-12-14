🚢 Titanic Survival Prediction — Model Performance Summary

The Titanic Survival Prediction model demonstrates strong overall performance, achieving an accuracy of 82.12% on a test dataset of 179 passengers.

📊 Overall Model Performance

Accuracy: 0.82 (82.12%)

Macro Average F1-score: 0.81

Weighted Average F1-score: 0.82

📉 Confusion Matrix
[[96   9]
 [23  51]]


True Negatives (TN): 96

False Positives (FP): 9

False Negatives (FN): 23

True Positives (TP): 51

🔍 Class-wise Performance Breakdown
Metric	Class 0 (Did Not Survive)	Class 1 (Survived)
Precision	0.81	0.85
Recall	0.91	0.69
F1-score	0.86	0.76
Support	105	74
📉 Class 0 — Did Not Survive

The model performs very well in identifying passengers who did not survive.

Recall: 0.91 → Correctly identifies 91% of actual non-survivors

Precision: 0.81 → 81% of Class 0 predictions are correct

True Negatives: 96

➡️ The model is highly reliable for detecting non-survivors, with very few false alarms.

📈 Class 1 — Survived

The model shows moderate performance in identifying survivors, with room for improvement.

Recall: 0.69 → Misses 31% of actual survivors

Precision: 0.85 → Most predicted survivors are correct

True Positives: 51

False Negatives: 23 survivors predicted as non-survivors

➡️ Improving recall for Class 1 is critical to reduce missed survivor predictions.

🧠 Key Insights

The model achieves a balanced accuracy of ~82%, making it a strong baseline.

Performance is biased slightly toward Class 0, which is common in imbalanced classification tasks.

High precision but lower recall for Class 1 suggests the model is conservative when predicting survival.

🧪 Conclusion

The Titanic Survival Prediction model provides a solid and interpretable baseline, with strong overall accuracy and excellent detection of non-survivors. However, the lower recall for survivors indicates that the model tends to miss some passengers who actually survived.
<img width="1912" height="983" alt="Screenshot (53)" src="https://github.com/user-attachments/assets/c5c6ab96-d27f-4f0d-bec2-4522f014d321" />

<img width="1905" height="996" alt="Screenshot (54)" src="https://github.com/user-attachments/assets/a35c29fd-7234-4b0a-af86-fcaacd831762" />

