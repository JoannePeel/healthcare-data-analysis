
# coding: utf-8

# # INEGI
# ---
# 
# Nuestra descripción del proyecto here

# In[ ]:


# Import Dependencies

import requests
import json
import pandas as pd
import numpy as np


# In[ ]:


#API connect

# API Key
key_access_token = "98658d62-9bec-54fb-b211-e67c426a7176"

# url = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/6207051584/es/00000/true/BISE/2.0/98658d62-9bec-54fb-b211-e67c426a7176?type=json"
url_part_1 = "https://www.inegi.org.mx/app/api/indicadores/desarrolladores/jsonxml/INDICATOR/"
url_part_2 = f"/es/09/true/BISE/2.0/{key_access_token}?type=json"


# ### Data Retrieval

# In[ ]:



api_list = ["6200240471", "6200240421", "6200240323", "6200240517", "6200240414", "6200240416", 
            "6207019017", "6207019013", "6207019018", "6207049072", "6207049073"]
indicador_list = ["Porcentaje de la población derechohabiente en el IMSS",
                  "Porcentaje de la población derechohabiente en el ISSSTE", 
                  "Porcentaje de la población derechohabiente en el Seguro popular", 
                  "Porcentaje de la población derechohabiente en otras instituciones", 
                  "Porcentaje de la población derechohabiente en PEMEX, SDN o SM", 
                  "Porcentaje de la población usuaria de servicios de salud en instituciones de seguridad social", 
                  "Porcentaje de la población usuaria de servicios de salud en instituciones de servicios médicos privados", 
                  "Porcentaje de población afiliada a otra institución", 
                  "Porcentaje de población afiliada a seguro privado", 
                  "Porcentaje de población afiliada a servicios de salud", 
                  "Porcentaje de población no afiliada a servicios de salud", 
                  "Porcentaje de población que no especificó su afiliación a servicios de salud"]


#creating data frame for storing the info
inegi_data = pd.DataFrame(columns=['Indicador', 'OBS_VALUE']);

processed = 0

for api_value in api_list:
    print(processed)
    
    query_url = url_part_1 + api_value + url_part_2
    
    try:
        response = requests.get(query_url).json()
        #print(response['Header'])
        data = response['Series']
        data_2 = data[0]['OBSERVATIONS']
        #print("data")
        #print(data_2[0]['OBS_VALUE'])
        print(f'   El indicador: {indicador_list[processed]} \n tiene un valor observado de: ', data_2[0]['OBS_VALUE'])

        inegi_data.at[processed, 'Indicador'] = indicador_list[processed]
        inegi_data.at[processed, 'OBS_VALUE'] = data_2[0]['OBS_VALUE']

        
    except:
        print ("------ Data Error ------")
        print(indicador_list[processed])
        inegi_data.at[processed, 'Indicador'] = indicador_list[processed]
        inegi_data.at[processed, 'OBS_VALUE'] = np.nan
        print ("------------------------")
    
    processed += 1
    
    


# ### Data review

# In[ ]:


inegi_data.head()

