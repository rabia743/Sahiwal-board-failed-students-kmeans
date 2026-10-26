# Student Failure Analysis & Clustering Using K-Means

An unsupervised machine learning project that analyzes 12th-grade students' failed subjects and groups students with similar failure patterns using **K-Means Clustering**. An HTML dashboard presents subject-wise information and summary statistics.

## Key Features

- **Data Preprocessing:** Loads student records and prepares the data.
- **Feature Engineering:** Converts failed subjects into binary features using `MultiLabelBinarizer`.
- **K-Means Clustering:** Groups students into 3 clusters based on their failed-subject patterns.
- **Model Saving:** Saves the trained model using Joblib.
- **Interactive Dashboard:** Displays subject-wise student tables and summary statistics.

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- HTML, CSS, JavaScript

## Project Structure

```text
student-failure-analysis-clustering/
├── 12th_failed_students.csv
├── feature.py
├── k-mean.py
├── kmeans_model.pkl
├── index.html
└── README.md
```

## Machine Learning Workflow

```text
Student Dataset
      ↓
Data Preprocessing
      ↓
Multi-Label Encoding
      ↓
K-Means Clustering
      ↓
Save Model & Display Results
```

## Installation

Clone the repository:

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd student-failure-analysis-clustering
```

Install the required libraries:

```bash
pip install pandas numpy scikit-learn joblib
```

## How to Run

**Step 1: Encode failed subjects**

```bash
python feature.py
```

**Step 2: Apply K-Means clustering**

```bash
python k-mean.py
```

**Step 3: Open the dashboard**

Open `index.html` in your browser.

*Note: Ensure the dashboard's required data files are available and the filenames match those used in your code.*

## Project Outcomes

- Identifies commonly failed subjects.
- Groups students with similar subject-failure patterns.
- Helps explore academic difficulties through data analysis.
- Demonstrates the practical application of unsupervised machine learning.

## Important Note

K-Means clusters represent similarities in failed-subject patterns. Cluster numbers do not indicate student rankings, and the project does not predict future examination results.

---


