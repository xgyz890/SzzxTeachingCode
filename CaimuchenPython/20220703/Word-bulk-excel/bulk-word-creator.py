# Gao Yang on 20220701, based on Svan's work

# type this: pip install pandas openpyxl docxtpl

# 1 single word file.

import datetime
from docxtpl import DocxTemplate
import os

base_dir = os.getcwd()
word_template_path = base_dir + "/vendor-contract.docx"

today = datetime.datetime.today()
today_in_one_week = today + datetime.timedelta(days=7)

doc = DocxTemplate(word_template_path)
context = {
    "CLIENT": "Maurice C",
    "VENDOR": "Shenzhen Inc.",
    "LINE1": "GOOD MORNING",
    "LINE2": "AND GOOD NIGHT",
    "AMOUNT": 2**16,
    "NONREFUNDABLE": round(1234*0.2,2),
    "TODAY": today.strftime("%Y-%m-%d"),
    "TODAY_IN_ONE_WEEK":today_in_one_week.strftime("%y-%m-%d")
}
doc.render(context)
doc.save(base_dir + "/generated-contract.docx")









# 2 multiple word files.

import pandas as pd  # pip install pandas openpyxl
from docxtpl import DocxTemplate  # pip install docxtpl
import os

base_dir = os.getcwd()
word_template_path = base_dir + "/vendor-contract.docx"
excel_path = base_dir + "/contracts-list.xlsx"
output_dir = base_dir + "/Output"

# Create output folder for the word documents
os.mkdir(output_dir)

# Convert Excel sheet to pandas dataframe
df = pd.read_excel(excel_path, sheet_name="Sheet1")

# Keep only date part YYYY-MM-DD (not the time)
df["TODAY"] = pd.to_datetime(df["TODAY"]).dt.date
df["TODAY_IN_ONE_WEEK"] = pd.to_datetime(df["TODAY_IN_ONE_WEEK"]).dt.date

# Iterate over each row in df and render word document
for index, record in enumerate(df.to_dict(orient="records")):
    print(f"Client:{record['CLIENT']}")
    doc = DocxTemplate(word_template_path)
    doc.render(record)
    output_path = output_dir + "/" + f"{index}_{record['VENDOR']}-contract.docx"
    doc.save(output_path)
print("Finished!")



