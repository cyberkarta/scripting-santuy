from xmlrpc.server import list_public_methods
import pandas as pd
import json

file_name1 = 'studentData.csv'
file_name2 = 'assessmentDetails.csv'

df1, df2 = pd.read_csv(file_name1), pd.read_csv(file_name2)

def assessmentJson(df=df2, out='assessmentDetails.json'): 
  df['module'] = df[['code_module', 'module_name']].to_dict('records')
  out = df[['module', 'code_presentation', 'id_assessment', 'assessment_type', 'id_student', 'deadline', 'date_submitted', 'weight', 'score']].to_json(out, orient='records', indent=4)

def studentJson(df=df1, out='studentData.json'):
  out = df[['id_student', 'name', 'gender', 'region', 'highest_education', 'imd_band', 'age_band', 'disability']].to_json(out, orient='records', indent=4)

def merging(df1=df1, df2=df2): 
  pointer = 0
  row_count = df1.shape[0]
  list_json = []

  for i in range(row_count):
    key_id = df1.iloc[i]['id_student']
    scan = df2.loc[df2['id_student'] == key_id]
    scan2 = df1.loc[df1['id_student'] == key_id]

    scan = scan[['code_module', 'module_name', 'code_presentation', 'id_assessment', 'assessment_type', 'deadline', 'date_submitted', 'weight', 'score']].to_dict('records')

    out = scan2[['id_student', 'name', 'gender', 'region', 'highest_education', 'imd_band', 'age_band', 'disability']].to_dict('records')

    dict_scan = { }
    dict_scan['assessments'] = scan
    
    try :
      out[0].update(dict_scan)
    except IndexError :
      list_json.append(out[0])
      out = { }
    
    list_json.append(out[0])
    out = { }
    
    pointer += 1
    print(pointer, "/", row_count)
  
  list_json = json.dumps(list_json, indent=4)
  print(list_json)

  with open('embedding.json','w') as file:
    file.write(list_json)

# assessmentJson()
# studentJson()
# merging()

