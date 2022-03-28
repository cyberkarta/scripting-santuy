import pandas as pd
import names

file_name = "Backup\\Original Data\\studentInfo.csv"

def removeDuplicate(file_name=file_name, output_file="studentData.csv") :
  df = pd.read_csv(file_name)
  df = df[["id_student", "gender", "region", "highest_education", "imd_band", "age_band", "disability"]]

  df.drop_duplicates(subset="id_student", inplace=True)
  df.to_csv(output_file, index=False)

def addName(file_name="studentData.csv", output_file="studentData.csv") :
  df = pd.read_csv(file_name)
  if "name" not in df.head(0) :
    df.insert(1, column="name", value="Change")
    
  pointer = 0
  row_count = df.shape[0]

  for i in range(row_count):
    if df.loc[i, "name"] == "Change":
      if df.loc[i, "gender"] == "M":
        name = names.get_full_name(gender="male")
      else :
        name = names.get_full_name(gender="female")
      
      df.loc[i, "name"] = name
      pointer += 1
      print(pointer, " / ", row_count)
    
    else:
      pointer += 1
      print(pointer, " / ", row_count)
      continue

  df.to_csv(output_file, index=False)

def addAssessmentDetails(file_name="Backup\\Original Data\\studentAssessment.csv", file_name2="Backup\\Original Data\\assessments.csv", output_file="assessmentDetails.csv"):

  df1, df2 = pd.read_csv(file_name), pd.read_csv(file_name2)

  if "is_banked" in df1.head(0):
    df1.pop("is_banked")

  inner_join = pd.merge(df1, df2, on="id_assessment", how="inner")

  reorder = ["code_module", "code_presentation", "id_assessment", "assessment_type", "id_student", "date", "date_submitted", "weight", "score"]

  inner_join = inner_join[reorder]

  if "date" in inner_join.head(0):
    inner_join = inner_join.rename(columns={"date": "deadline"})
  
  inner_join.to_csv(output_file, index=False)

def addModuleName(file_name="assessmentDetails.csv", output_file="assessmentDetails.csv"):
  df = pd.read_csv(file_name)
  module_codes = {
    "AAA": "Big Data Analysis",
    "BBB": "Introduction to Machine Learning",
    "CCC": "Information Security",
    "DDD": "Algorithm and Data Structure",
    "EEE": "Blockchain Technology",
    "FFF": "Business Analysis",
    "GGG": "Software Development"
  }

  if "module_name" not in df.head(0):
    df.insert(1, column="module_name", value="Change")

  row_count = df.shape[0]

  for i in range(row_count):
    if df.loc[i, "module_name"] == "Change":
      key = df.loc[i, "code_module"]
      df.loc[i, "module_name"] = module_codes[key]

  df.to_csv(output_file, index=False)




# removeDuplicate()
# addName()
# addAssessmentDetails()
# addModuleName()






    


