# Analysis-of-Customer-Purchasing-Behaviour-using-K-Means-Clustering (Unsupervised machine learning)

This study is designed primarily to enable organisations know the distinct kinds of customers they have. This will in turn help them to tailor customers' need based on the segment they fall into. 

The algorithm was created with two different user interface systems. These interface systems are Tkinter and user input.

The Tkinter Interface: The Tkinter interface simplifies the process for users by eliminating the need to specify which columns should be segmented, as this is handled during the data pre-processing stage. The relevant columns for analysis are extracted and saved in a new file. When running the algorithm, users are prompted to select this file and specify the number of clusters for segmentation. This interface is advantageous for users with limited technical skills, as they only need to select the alraedy saved file containing the exact columns. Additionally, it features an attractive and user-friendly interface.

The User Interface: Conversely, with the user input interface, pre-selecting the columns for analysis is not required. The system prompts users to input their desired columns and specify the number of clusters. This interface requires users to be familiar with the business needs. It offers more flexibility, allowing users to switch between different columns based on those needs.

The dataset used to test this algorithm was gotten from kaggle.com website. It has 5 attributes with 200 observations. The attributes are listed below:
1. Customer ID: It unique number to identify each customer. It categorical variable. (Not required to test this algorithm but for identification)
2. Gender: It is a categorical variable that contains male and female customers.
3. Age of customers which ranges between 18 years to 70 years old. It is numerical.
4. Income of customers between $15,000 and $70,000. It is numerical.
5. Spending score between 1 and 100 for each customer. It is numerical.
