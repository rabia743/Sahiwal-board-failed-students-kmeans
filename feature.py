import pandas as pd
from sklearn.preprocessing import MultiLabelBinarizer
import joblib
data = pd.read_csv("12th_failed_students.csv")
subjects = data["Failed_Subjects_12th"].fillna("").str.split(", ")
# MultiLabelBinarizer() same working as the multiple hot encoding
encoder = MultiLabelBinarizer()
encoded = encoder.fit_transform(subjects)
data["Failed_Subjects_12th"] = encoded.tolist()
# data.to_csv("student_encoded.csv", index=False)

print(data.head(3))
# joblib.dump(encoder, "subject_encoder.pkl")
