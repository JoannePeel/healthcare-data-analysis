

# Project Title: Health Care Data Analysis

## Team Members: 

- Joanne
- Daniel
- Joel 

## Project Description/Outline:

The Mexican healthcare system is divided into two sectors: private and public. 

According to article 4° of the Mexican political constitution, healthcare is a basic right of all Mexicans. Workers who are or were employed formally, as well as their families, receive healthcare from social security institutions. IMSS covers 80% of this population, while ISSSTE covers 18%, and other institutions, such as PEMEX, SEDENA, and SEMAR, cover the rest. People without social security fall under the responsibility of the secretary for health (SSA) and represent about half of the population of the country. In 2008, there were 27 million insurance seekers affiliated to SSA, and 30 million people without healthcare insurance.

Triage, a concept developed and refined on the battlefield, has been central to the practice of emergency medicine for more than half a century. As emergency departments (EDs) face escalating patient volumes, persistent crowding, and patient populations with more complex disease, the need for accurate and reliable triage has intensified.

Mexico’s emergency departments have faced an important increment in patients, with 5,751,797 attended in 2008, and almost twice the amount (10,645,625 patients) in 2014. To deal with the increased patient load Mexican hospitals implement triage systems. 

Triage systems with published evidence of widespread adoption include the Australasian Triage Scale (ATS), Canadian Triage and Acuity Scale (CTAS), Emergency Severity Index (ESI), Manchester Triage Scale (MTS), South African Triage Scale (SATS) and NEWS2. Currently, Mexican hospitals use MTS.

Two thirds of Mexico’s population is urbanized and 35% of the population lives in nine metropolitan areas. Therefore, the objectives of this project were to analyze data from INEGI and the secretary of health: 

(1) to determine the number of people insured by each institution in Mexico City (IMSS, ISSSTE, SSA and others); 

(2) to determine the number and distribution of hospitals in the city and the institutions they belong to; 

(3) to determine the number of hospital beds per 1000 capita by institution (based on insured population) and by delegation (based on population)

(4) to analyze the number of emergencies attended in Mexico City in the period from 2009-2016; 
(5) to calculate the increment rate of demand on emergency services; 

(6) to quantify emergencies by type and delegation.

Finally, for the final phase of this project we are going to propose an electronic case report form (eCRF), for emergency room admission, which will automatically calculate different triage scales (MTS, NEWS2, MEWS for pregnant women, and PEWS for pediatric patients) and facilitate ordered attendance of a large number of patients.

Our hypothesis are that the public healthcare institutions face a high demand of patients (low beds per capita index); that demand of emergency services is increasing; and that a large number of emergencies attended in hospitals are unqualified emergencies.



---

## Research Questions to Answer & Data Sets to be Used

1.	How many people in Mexico City have insurance through each of the public institutions institution in Mexico City (IMSS, ISSSTE, SSA and others)? 
Data: INEGI https://www.inegi.org.mx/app/tabulados/pxweb/inicio.html?rxid=857b90d2-9e40-4741-8e2e-a5655d78437e&db=Derechohabiencia&px=Derechohabiencia_02
2.	How many hospitals are there in Mexico City, where are they distributed (delegations), and which institutions they belong to?
Data: http://www.dgis.salud.gob.mx/contenidos/intercambio/clues_gobmx.html
3.	How many hospital beds per 1000 capita are there by institution (based on insured population) and by delegation (based on population)?
Data: http://www.dgis.salud.gob.mx/contenidos/intercambio/clues_gobmx.html
https://www.inegi.org.mx/app/tabulados/pxweb/inicio.html?rxid=857b90d2-9e40-4741-8e2e-a5655d78437e&db=Derechohabiencia&px=Derechohabiencia_02 http://internet.contenidos.inegi.org.mx/contenidos/productos/prod_serv/contenidos/espanol/bvinegi/productos/nueva_estruc/anuarios_2015/702825076924.pdf

4.	How many emergencies did each of the institutions attend in Mexico City in the period from 2009-2016?
Data: 
https://datos.gob.mx/busca/dataset/urgencias 
5.	How much did the demand on emergency services increase in the 7 years analyzed?
Data:  
https://datos.gob.mx/busca/dataset/urgencias 

6.	Which were the most frequent emergencies? Which delegation attended more emergencies and what kind?
Data:  
https://datos.gob.mx/busca/dataset/urgencias 
http://www.dgis.salud.gob.mx/contenidos/intercambio/clues_gobmx.html


## Rough Breakdown of Tasks:

### INEGI Data analysis
    
    1. To get the information from the INEGI and government websites.

    2. Understand, filter and cleanup the data, using pandas dataframes.

    3. Visualize the results using matplotlib

### Data Cleanup & Exploration

print code here for clean up...and comment the code

### Discuss insights you had while exploring the data that you didn't anticipate

We were hoping to analyze all the emergencies for all institutions but discovered that the data set “urgencias” only contained data for SSA, but not for the other instutions analyzed.

### Discuss any problems that arose after exploring the data, and how you resolved them
The data set "urgencias" had a different format for every year reported. Several fixes had to be implemented to be able to unify the information and to run an automated analysis.

### Data Analysis
We used five different data sets from different data sources to create this analysis. Data about population size and population insured came from INEGI and corresponds to the year 2015.

We used two data sets about hospitals. The first one is a list of all the hospitals in Mexico and includes their location and size (hospitlas.csv) from 2015, the second one is a data set that consists of 7 separate folders, of which we only used the files named “urgencias. This data set contains information on medical emergencies attended in public hospitals (SSA) all over Mexico in the period from 2009 to 2016.

The last data set contains comparative data on hospital beds per capita in other countries and was obtained from a website.

We filtered the information contained in "hospitals.csv" and the data set "urgencias" to analyze exclusiveley the information provided for Mexico City (cdmx).

### Results

The total population of Mexico City in 2015 was 8,851,080. The delegation with the largest number of people was Iztapalapa (Figure 1).

![](https://github.com/joelsotelods/healthcare-data-analysis/blob/develop/figures/Total_population_by_delegation.png)
Figure 1. Population of Mexico City by delegation.

More than 80% of the population in Mexico City have some form of health insurance (Figure 2). Only 18.7% of the population are uninsured.
![](https://github.com/joelsotelods/healthcare-data-analysis/blob/develop/figures/insurance_percent.png)
Figure 2. Percentage of population insured (by instittion) and uninsured. *IMSS: Instituto Mexicano de Seguro Social; ISSSTE: Instituto de Seguro Social de Trabajadores del Estado; SSA: Secretaria de Salud; SMP: Servicios Médicos Privados; PEMEX: Petróleos Mexicanos; Others: SEDENA, SEMAR, SME, etc.

Iztapalapa is the delegation with most hospitals in Mexico City, while Magdalena Contreras and Cuajimalpa are the delegations with less hospitals (Fig. 3).
![](https://github.com/joelsotelods/healthcare-data-analysis/blob/develop/figures/number_of_hospitals_by_delegation.png)
Figure 3. Number of hospitals in Mexico City by delegation.

The majority of hospitals in Mexico City are private (SMP). Within the public institutions, SSA is the one that has the most hospitals in the City, while PEMEX and ISSSTE have the fewest (Fig. 4).
![](https://github.com/joelsotelods/healthcare-data-analysis/blob/develop/figures/hospitals_institution_hor.png)
Figure 4. Number of hospitals in Mexico City by institution.

Miguel Hidalgo and Cauthemoc have the highest amount of beds per capita (Fig. 5).
![](https://github.com/joelsotelods/healthcare-data-analysis/blob/develop/figures/number_of_bed_by_delegation_capita.png)
Figure 5. Hospital beds per thousand by delegation in Mexico City.

Private institutions have the highest per capita index per thousand with more than 9 beds per insured person. ISSSTE has the lowest number of beds per capita in Mexico City. The average for the city is 2.5 hospital beds per 1000 (Fig. 6).
![](https://github.com/joelsotelods/healthcare-data-analysis/blob/develop/figures/beds_capita_institution_hor.png)
Figure 6. Hospital beds per thousand by institution in Mexico City (dotted line: Mexico City average).
## Tabla comparativa (beds per capita institución)
Table 1 shows beds per capita for other countries. ISSSTE and IMSS are comparable to the average of El Salvador, while SSA is comparable to the average in the USA.

Table 1.

|Other Countries|Beds per 1000|
|-------------|-------------|
|**EU Average**|6.42|
|**USA Average**|3.30|
|**El Salvador Avr.**|1.65|

