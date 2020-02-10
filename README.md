### bigdata2020UTM
Alumno: Erick Javier Matos Ramos 5°A IRD
# The importance of the data.

## Explain the impact of the data today:
The study of data has radically impacted the solution of problems in different branches of the time, Because thanks 
to them many discoveries have been made and better decisions have been made.

## Explain the reasons why data generation has increased.
The increase is due to the fact that decisions are no longer taken lightly, before making a decision a 
probabilistic study is carried out through technological tools of a set of data collected about a problem, in 
order to have a better solution or decision.

# Fundamentals of Big Data. 

## Define the Big Data concept:
It is a term that describes the large volume of data, both structured and unstructured, that flood a 
company on a day-to-day basis.

## Differentiate between open data and private data:
Open data is data that is available to everyone, without restrictions or anything.
Private data is the opposite of open data, since they need permits or certificates to use
them and are used exclusively by the different companies that collect them.

## Differentiate between structured and unstructured data:
Structured data is data that can be sorted and displayed in rows and columns so that any data analysis
administrator can easily process it.
Unstructured data is generally binary data that does not have an identifiable internal structure. In other words, they are data that still cannot be analyzed to reach a conclusion and / or solution.

## Differentiate between stored data and moving data:
Moving data is data that is transmitted in real time on a network. Something like dynamic data.
The data stored as the name implies, are data that different pages, companies and organizations collect from the 
registration and backup systems and are stored for use at any time and their analysis in different applications 
through APIS or some type of Carry This data elsewhere.

# Fundamentals of data analysis.

## Define the meaning of data analysis:
Data analysis is a process that involves inspecting, cleaning and transforming data to highlight useful
information, suggest conclusions and support in decision making.

## Explain the impact of data analysis on organizations:
In organizations the impact of data analysis has been very large, and one could say that it is 
currently the most important because it is the basis of all the achievements, the basis of the decision-making 
that is made, etc.

## Explain the different types of data analysis:
1. Descriptive Analytics:
It consists of simplifying and summarizing the data in small packages, so that they become more manageable.
2. Predictive Analytics:
Predictive analytics is the technique that allows analysts to make predictions based on probability.
3. Prescriptive analysis:
Suggests the possible decisions to be taken against these scenarios, and the probable consequences of those decisions.

## Handoop 
Is a framework that allows for the distributed processing of large data sets across clusters of computers using simple programming models. Is a library.

## MapReduce
Map Reduce is a programming environmentconsists of distributing a large amount of data in many clusters and processing them faster.

## Apache Spark
Spark is a distributed data processing engine that allows you to handle large volumes of information.

## Lambda Y Kappa

Lambda: This architecture is characterized by using different layers for batch processing and streaming.

Kappa: Unlike lambda, his proposal is to eliminate the batch layer leaving only the streaming layer.

# GitHub Commands

Git Init: Turn an existing directory into a git repository
```github
Git Init  
```
Git Commit -m "Message": Records file snapshots permanently in version history
```github
Git Commit -m Myfile.txt
```
Git reset: Undoes all commits after [commit], preserving changes locally
```github
Git reset
```
Git log: Lists version history for the current branch
```github
Git log
```
Git Status: Check the files that don't are agregate in commit. 
Show modified files in working directory, staged for your next commit
```github
Git Status
```
Git add "File.txt": add a file as it looks now to your next commit (stage)
```github
Git add "MyFile.txt"
```
Git rm: This command delete the file from project and stage the removal for commit
```github
Git rm MyFile.txt
```
Git mv : Change an existing file path and stage the move.
```github
git mv [existing-path] [new-path]
```

Git diff: show the diff of changes of a file before to apply commit
```github
git diff [existing-path] [new-path]
```
Git checkout: switch to another branch and check it out into your working directory
```github
git checkout xxxxxxxxxxxxxxx
```
Git reset: Unstage a file while retaining the changes in working directory
```github
git reset File.txt
```
Git ammend: It is a practical way to modify the most recent confirmation. It allows you to combine the changes prepared with the previous confirmation instead of creating a new confirmation.
```github
git commit --amend
```
# Second partial :books:

+ Data life cycle in BIG DATA: Given the characteristics of Big Data: volume, speed and variety; They require a different type of collection and analysis than any other type of data.
The Big Data analysis presents a great challenge, not only for the management of a large amount of data but also for the need to know the life cycle of the data and establish a base based on the nature of the Big Data.
  
  - The phases of the data life cycle in Big Data are as follows:
    
    - Análisis interno
    - Recogida y filtrado de datos
    - Extracción de datos
    - Validación y limpieza de los datos
    - Análisis de los datos
    - Visualización de los datos
    
 + Internal analysis: The Big Dara life cycle must begin with the understanding of the business and a justification of the need to carry out an analysis of this type, as well as the establishment of the objectives to be achieved. This stage of analysis allows us to understand the current situation of the company and what resources will be required throughout the analysis.
Likewise, those KPIs necessary to understand the results of the analysis and their ability to meet the established goals and objectives must be established.

+ Data collection and filtering: This part of the Big Data Life Cycle is dedicated to identifying those data relevant to the analysis, identifying the sources to find patterns and correlations.
The selection of data depends on the nature of the problem and the objectives established in the first part of the cycle. The data is collected and subjected to a filtering of corrupt data or data that does not respond to the established objectives.

+ Information extraction: The main objective of the data is to transform these into information. At this stage the data extraction and its transformation into an understandable format are carried out in order to perform a data analysis.

+ Validation and cleaning of data: Incorrect or invalid data can lead to false results that harm the analysis. The unstructured nature of Big Data makes their validation difficult. Therefore, this stage of the Big Data Life Cycle is essential, since it allows to reach the most relevant data for the objectives set.
In addition, this analysis not only allows the discarding of invalid data, but the analysis and observation of said data allow establishing patterns and trends that contribute to improving the understanding of the data to be analyzed

+ Data analysis: At this stage the integration of data sets is developed in order to give a unified view of the information. Throughout this stage of the cycle several problems of data structure and labels can occur.

+ Data visualization: Once the data is organized, it is necessary to transform it into information that provides value. All the useful information extracted must be “translated” in the form of reports that allow the correct interpretation of these.

  Reference: <https://piperlab.es/2019/05/14/el-ciclo-de-vida-de-los-datos-las-5-fases-para-llevar-a-exito-un-proyecto-de-big-data/>
***

 
+ Exploratory Data Analysis (A.E.D.): Is a set of statistical techniques whose purpose is to achieve a basic understanding of the       data and the relationships between the analyzed variables. To achieve this goal the A.E.D. provides simple systematic methods for       organizing and preparing data, detecting failures in the design and collection of data, treatment and evaluation of missing data,       identification of atypical cases (outliers) and verification of the underlying assumptions in most of multivariate techniques           (normality, linearity, homocedasticity). The prior examination of the data is a necessary step, which takes time, and is usually         neglected by data analysts. The tasks implicit in such an examination may seem insignificant and without consequences at first sight,   but they are an essential part of any statistical analysis.

  - STAGES OF THE AED To perform an AED:
   
    - Prepare the data to make them accessible to any statistical technique.
    - Perform a graphic examination of the nature of the individual variables to be analyzed and a numerical descriptive analysis that         allows quantifying some graphic aspects of the data.
    - Perform a graphic examination of the relationships between the analyzed variables and a numerical descriptive analysis that             quantifies the degree of interrelation between them.
    - Evaluate, if necessary, some basic assumptions underlying many statistical techniques, such as normality, linearity and                 homoscedasticity.
    - Identify possible atypical cases (outliers) and evaluate the potential impact they may have in subsequent statistical analyzes.
    - Evaluate, if necessary, the potential impact that missing data may have on the representativeness of the analyzed data.

***

+ Extraction, transformation and loading process(ETL): It is a data pipeline that is used to collect data from various sources, transform the data according to business rules and load it into a destination data store. Transformation work in ETL takes place in a specialized engine and often involves the use of temporary storage tables to temporarily retain data as they are transformed and eventually loaded into their destination.The data transformation that takes place often involves several operations such as filtering, sorting, aggregation, data merging, data cleaning, duplication and data validation.


   ![alt text](https://docs.microsoft.com/es-es/azure/architecture/data-guide/images/etl.png)
Frequently, the three phases of the ETL process run in parallel to save time. For example, while data is being extracted, a transformation process on the data already received and preparation for loading may be working, and a load process may begin to work on the prepared data, instead of having to wait for That ends the entire extraction process.

***

+ Statistical data analysis: They are basically of 2 types, continuous data and discrete data. The continuous information is the one that cannot be told. For example, the intensity of a light can be measured but cannot be counted. Discreet information is what can be told. For example, you can count the number of bulbs.
Continuous data in the analysis of statistical data is distributed under the function of continuous distribution, which can also be called the probability density function or fdp
The discrete data in the statistical data analysis is distributed under the discrete distribution function, which can also be called the probabilized mass function fmp.

***

+ Data flow diagram: Trace the flow of information for any process or system. It uses defined symbols, such as rectangles, circles and arrows, in addition to short text labels, to display data inputs and outputs, storage points and routes between each destination. The data flow diagrams can vary from simple process scenarios even hand-drawn, to very detailed DFD and with multiple levels that progressively deepen how the data is handled.
  
  - Example:

     ![alt text](https://image.slidesharecdn.com/dfdprofyedra-160313133606/95/diagrama-de-flujo-de-datos-dfd-16-638.jpg?cb=1457877018)
