
import fitz
import pandas as pd
import re
from pathlib import Path

# 1. PDF file path
BASE_DIR = Path(__file__).resolve().parent

pdf_path = BASE_DIR / (
    r"C:\Users\hp\Downloads\3165-bise-sahiwal-12th-class-result-2026-gazette-pdf-2nd-year-(taleem360.com)-6fmHQ.pdf"
)

print("Python program started!", flush=True)
print("PDF exists:", pdf_path.exists(), flush=True)

if not pdf_path.exists():
    raise FileNotFoundError(f"PDF file not found: {pdf_path}")
# 2. Subject codes
subjects = {
    "ENG": "English",
    "ENGE": "English Elective",
    "MATHS": "Mathematics",
    "PHY": "Physics",
    "CH": "Chemistry",
    "BIO": "Biology",
    "CSC": "Computer Science",
    "CST": "Computer Studies",
    "UR": "Urdu",
    "PS": "Pakistan Studies",
    "THQ": "Translation of Holy Quran",
    "EDU": "Education",
    "ECO": "Economics",
    "STAT": "Statistics",
    "CIV": "Civics",
    "IST": "Islamic Studies",
    "IE": "Islamic Education",
    "HPED": "Health and Physical Education",
    "AR": "Arabic",
    "PER": "Persian",
    "SOC": "Sociology",
    "PSY": "Psychology",
    "PUN": "Punjabi",
    "AGRI": "Agriculture",
    "HECO": "Home Economics",
    "BKA": "Book Keeping and Accountancy",
    "BMATHS": "Business Mathematics",
    "PACC": "Principles of Accounting",
    "PECO": "Principles of Economics",
    "PCOM": "Principles of Commerce",
    "FA": "Fine Arts",
    "HIS": "History",
    "LBS": "Library Science",
    "NUR": "Nursing"
}

# 3. Store failed students
students = []

# 4. Open PDF
with fitz.open(pdf_path) as pdf:
    total_pages = len(pdf)
    print("Total PDF pages:", total_pages, flush=True)
    # True = Test first 5 student pages
    # False = Process all pages
    TEST_MODE = False
    start_page = 26
    if TEST_MODE:
        end_page = min(31, total_pages)
    else:
        end_page = total_pages
    print("Starting PDF extraction...", flush=True)

    # 5. Read PDF pages
    for page_index in range(start_page, end_page):
        page = pdf[page_index]
        words = page.get_text(
            "words",
            sort=True
        )
        rolls = []
        # 6. Find roll numbers
        for w in words:

            x, y, x2, y2, value = w[:5]

            if (
                re.fullmatch(r"\d{6}", value)
                and x < 80
            ):
                rolls.append((y, value))
        rolls.sort()

        # 7. Process students
        for i, (roll_y, roll_no) in enumerate(rolls):
            if i + 1 < len(rolls):
                next_y = rolls[i + 1][0]
            else:
                next_y = page.rect.height - 15
            row_words = [
                w for w in words
                if roll_y - 12 <= w[1] < next_y - 12
            ]
            # 8. Extract student name
            name_words = [
                w for w in row_words
                if 80 <= w[0] < 225
            ]
            name_words.sort(
                key=lambda w: (
                    round(w[1] / 5),
                    w[0]
                )
            )
            name = " ".join(
                w[4] for w in name_words
            )
            name = re.sub(
                r"\s+",
                " ",
                name
            ).strip()

            # 9. Extract only 12th-class result
            result_words = [
                w for w in row_words
                if 350 <= w[0] < 530
            ]
            result_words.sort(
                key=lambda w: (w[1], w[0])
            )
            result = " ".join(
                w[4] for w in result_words
            ).strip().upper()
            # Skip empty results
            if not result:
                continue
            # Skip passed students
            if re.fullmatch(r"\d+", result):
                continue
            # 10. Find failed subject codes
            codes = [
                code.strip().upper()
                for code in re.split(
                    r"[,;\s]+",
                    result
                )
                if code.strip()
            ]

            failed_codes = [
                code for code in codes
                if code in subjects
            ]

            # 11. Save failed students
            if failed_codes and name:

                failed_names = [
                    subjects[code]
                    for code in dict.fromkeys(
                        failed_codes
                    )
                ]

                students.append({
                    "Roll_No": roll_no,
                    "Student_Name": name,
                    "Failed_Subjects_12th": ", ".join(
                        failed_names
                    )
                })

        print(
            f"Processed page {page_index + 1} "
            f"| Students found: {len(students)}",
            flush=True
        )
# 12. Create DataFrame
df = pd.DataFrame(
    students,
    columns=[
        "Roll_No",
        "Student_Name",
        "Failed_Subjects_12th"
    ]
)
# 13. Remove duplicate records
df = df.drop_duplicates(
    subset=["Roll_No"]
)
# 14. Save only ONE CSV file
output_path = BASE_DIR / "12th_failed_students.csv"
df.to_csv(
    output_path,
    index=False,
    encoding="utf-8-sig"
)
# 15. Display results
print("\n--------------------------------")
print("PDF extraction completed!")
print("--------------------------------")
print("\nTotal identified failed students:", len(df))
print("\nFirst 10 students:")
print(df.head(10))
print("\nCSV saved successfully!")
print("File location:", output_path)
