import joblib
import pandas as pd
from sklearn.cluster import KMeans
import numpy as np
import ast
data = pd.read_csv("student_encoded.csv")
# Independent features (encoded subjects only)
X = np.array(
    data["Failed_Subjects_12th"].apply(ast.literal_eval).tolist()
)

# K-Means Model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)
# Train Model
model.fit(X)
# Save Model
# joblib.dump(model, "kmeans_model.pkl")
# Assign Clusters
data["Cluster"] = model.labels_
# save Results
# data.to_csv("student_clusters.csv", index=False)
# Display Results
print("Students and their clusters:")
print(data[["Roll_No", "Student_Name", "Cluster"]].head(20))

# Cluster Summary
print("\nCluster Summary:")
print(data.groupby("Cluster").size())
print("\nModel saved successfully!")