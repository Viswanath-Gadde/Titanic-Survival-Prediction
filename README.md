🚢 Titanic Survival Prediction — Model Performance Summary

The Titanic Survival Prediction Model demonstrates strong overall performance, achieving an accuracy of 81.01% on a dataset of 179 observations.

📊 Overall Model Performance

Accuracy: 0.81 (81.01%)

🔍 Class-wise Performance Breakdown
Metric	Class 0 (Did Not Survive)	Class 1 (Survived)
Recall	0.89	0.70
Precision	0.81	0.81
📉 Class 0 — Did Not Survive

The model performs strongly in identifying passengers who did not survive.

True Negatives (TN): 93

Recall: 0.89 → Correctly identifies 89% of actual non-survivors

Precision: 0.81 → 81% of Class 0 predictions are correct

➡️ Overall, the model is reliable for detecting non-survivors.

📈 Class 1 — Survived

This class shows room for improvement, as the model struggles more here.

True Positives (TP): 52

Recall: 0.70 → The model misses 30% of actual survivors

Precision: 0.81

False Negatives (FN): 22 → Survivors predicted as non-survivors

➡️ Improving recall for this class is crucial to reduce missed survivor predictions.

🧠 Conclusion

The model’s overall accuracy of 81% makes it a solid baseline. However, the lower Recall for Class 1 (0.70) indicates that the model has difficulty identifying actual survivors.
