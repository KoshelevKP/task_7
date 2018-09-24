
# coding: utf-8

# In[145]:


import pandas as pd

def count_top3(years):
    
    files_name = []
    
    if type(years) != list:
        years = [years]
    
    for year in years:
        files_name.append('yob'+str(year)+'.txt')
    
    fr_all_year = None

    for file in files_name:
        fr = pd.read_csv(file, names = ['name', 'sex', 'count'])
        if fr_all_year is None:
            fr_all_year = fr
        else:
            fr_all_year = pd.concat([fr, fr_all_year])

    fr_sum = fr_all_year.groupby(['name', 'sex'], as_index = False).sum()

    top_3 = fr_sum.nlargest(3, 'count', keep='first')

    return [str(top_3.name[top_3.index[0]]), str(top_3.name[top_3.index[1]]), str(top_3.name[top_3.index[2]])]

def count_dynamics(years):
    
    dynamics ={'F': [], 'M': []}
    
    if type(years) != list:
        years = [years]
    
    for year in years:
        
        files_name = 'yob'+str(year)+'.txt'
        
        fr = pd.read_csv(file, names = ['name', 'sex', 'count'])
        
        fr_count = fr['sex'].value_counts()
        
        dynamics['F'].append(fr_count['F'])
        dynamics['M'].append(fr_count['M'])

    return dynamics
        
        
years = [2000,2001,2002,2003]
print(count_top3(years))
print(count_dynamics(years))

