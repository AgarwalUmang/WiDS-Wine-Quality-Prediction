# ****Wine Quality Prediction using Machine Learning**** 
**By** _Sandeep Kumar_
## **Abstract**
The red wine industry has shown recent exponential growth as social drinking continues. Nowadays, industries are using product quality certifications to promote their products. This process is time-consuming and requires assessment given by human tasters, which makes this process very personal opinions based. Another factor in red wine quality assessment is laboratory-based physicochemical tests, which consider factors like acidity, pH level, sugar, and other chemical properties. The red wine market would be interested if the human quality of tasting could be related to wine’s chemical properties so that certification,taste, and  quality are more controlled. This project aims to determine which features are most responsible for determination of wine quality. 

## **Introduction**
Identifying and classifying wine quality is a significant part of modern food production and trade. Wine contains about 97% water and ethanol, remaining 3% of other substances. These chemical compositions determine the quality of the wine. 
Fluctuations in these chemicals can be observed by examining the physicochemical properties of the wine. These physicochemical properties, like pH value, alcohol content, sulfur content,and other properties of wine, can significantly reflect its quality. 
Research on wine has revealed the interesting fact that there is an intrinsic link between the physicochemical features of the wine and that two or more components may work together to influence certain qualities of a wine.
Traditionally, wine quality assessment has relied on manual sensory evaluation. The disadvantages of this method are obvious: firstly, manual sensory evaluation depends on personal perception and may give different results based on the tester. Secondly, it lacks standardized quality evaluation criteria. 
Unlike humans, Artificial Intelligence (AI) can remember and learn from massive amounts of data. After being trained by large amounts of data, AI can work regardless of subjective factors to adapt to enormous modern production. With the rise of ML techniques and their success in the past decade, there have been various efforts in determining wine quality by using the available data. In this work, it has been shown how ML can be used to identify the best parameter on which the wine quality depends and in turn predict wine quality.

## **Data Preparation**

The Red Wine Quality set, available on the UCI machine learning repository(https://archive.ics.uci.edu/ml/datasets/wine+quality), has been used in this analysis. 
I obtained the red wine samples to model quality based on physicochemical tests. The dataset contains a total of 12 variables, which were recorded for 1,599 observations. This data will allow us to create different regression models to determine how other independent variables help predict our dependent variable, quality.

#### Data Exploration and Transformation
To see which variables are likely to affect the quality of red wine the most, I ran a correlation analysis of our independent variables against our dependent variable and quality. This analysis ended up with a list of variables of interest that had the highest correlations with quality.
In order of highest correlation, alcohol content has highest correlation with quality and sulphate has second. 
I can observe three different patterns:
1.There are positive relationships between quality and critic acids, alcohol, and sulfates. Even though wines with a higher level of alcohol may make them less popular, they should be highly rated in quality.
2.There are negative relationships between quality and volatile acidity, density, and pH. It is reasonable that less sweet wines and a lower acidity are favored in quality tests.
3.These independent variables show no significant relationship with quality: residual sugar, chlorides, and total sulfur dioxide.
I built different three-dimensional plots to dive deep into relationships within independent variables and with quality. When inspecting the two variables, alcohol and volatile acidity with quality, we can see that with red wines’ alcohol level between 9% to 12%, the level of volatile acidity decreases as the wines’ alcohol level increases. For higher alcohol content, the pattern reverses, implying high-quality wines’ popularity.

## **Machine Learning Algorithms**
A wide range of machine learning algorithms such as logistic regression,  support vector machine, decision tree, random forest, and some others are applied. Each technique has its strength and weakness. I used the following supervised learning algorithms in this modeling to predict wine quality.
#### 1. Logistic Regression
Logistic regression is a fundamental classification technique. It belongs to the group of linear classifiers and is similar to polynomial and linear regression. Logistic regression is fast and relatively uncomplicated, and it’s convenient for you to interpret the results. Although it’s essentially a method for binary classification, it can also be applied to multiclass problems.
#### 2. Decision Tree
The decision Tree algorithm belongs to the family of supervised learning algorithms. Unlike other supervised learning algorithms, the decision tree algorithm can also be used for regression and classification problems.
The goal of using a Decision Tree is to create a training model to predict the class or value of the target variable by learning simple decision rules inferred from preliminary data(training data).
In Decision Trees, we start from the tree's root to predict a class label for a record. We compare the values of the root attribute with the record’s attribute. Based on the comparison, we follow the branch corresponding to that value and jump to the next node.
#### 3. Support Vector Machine
Support Vector Machine(SVM) is a supervised machine learning algorithm for classification and regression. However, we say regression problems as well its best suited for classification. The objective of the SVM algorithm is to find a hyperplane in an N-dimensional space that distinctly classifies the data points. The dimension of the hyperplane depends upon the number of features. If the number of input features is two, then the hyperplane is just a line. If the number of input features is three, then the hyperplane becomes a 2-D plane. It becomes difficult to imagine when the number of elements exceeds three. 
#### 4. K-Nearest Neighbours
The k-nearest neighbors (KNN) algorithm is a simple, easy-to-implement supervised machine learning algorithm that can be used to solve both classification and regression problems.K-NN algorithm assumes the similarity between the new case/data and available cases and puts the new topic into the most similar category to the general categories.The K-NN algorithm stores all the available data and classifies a new data point based on the similarity. This means when new data appears then, it can be easily classified into a well suite category by using K- NN algorithm. K-NN algorithm can be used for Regression as well as for Classification but mostly it is used for the Classification problems.

#### 5. Naive Bayes
A Naive Bayes classifier is a probabilistic machine learning model that’s used for classification task. The crux of the classifier is based on the Bayes theorem. Naive Bayes classifiers are highly scalable, requiring a number of parameters linear in the number of variables in a learning problem. Maximum-likelihood training can be done by evaluating a closed-form expression, which takes linear time, rather than by expensive iterative approximation as used for many other types of classifiers. 
#### 6. Random Forest
Random forest is a Supervised Machine Learning Algorithm that is used widely in Classification and Regression problems. It builds decision trees on different samples and takes their majority vote for classification and average in case of regression.
One of the most important features of the Random Forest Algorithm is that it can handle the data set containing continuous variables as in the case of regression and categorical variables as in the case of classification. It performs better results for classification problems.

## **Results and Discussion**
To assess the performance of the different ML algorithms, I have used six machine learning algorithms, namely: Logistic Regression , Decision Tree, Support Vector Machine (SVM), K-Nearest Neighbours, Naive Bayes and Random forest to predict the wine quality in the red wine data. This allows us the freedom to select the most suitable ML algorithm to predict the wine quality with the given variables. The accuracy_score method is used to calculate the accuracy of either the faction or count of correct prediction in Python Scikit learn. Mathematically it represents the ratio of the sum of true positives and true negatives out of all the predictions.
| Machine Learning Algorithm | Accuracy |
|---|---|
| Logistic Regression | 86-87%|
| Decision Tree | 85-86%|
| Support Vector Machine | 88-89%|
| K-Nearest Neighbours | 86-87%|
| Naive Bayes | 81-82%|
| Random Forest | 90-92%|
