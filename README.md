# Transforming-Categorical-Data-To-Numeric-Data
A Guide to convert categorical data into numerical data to build a machine learning model

 - The data that we have to deal with while applying a machine learning might include both of the numerical and categorical values. Many machine learning algorithm can handle categoric values without any manipulation but there are many algorithms that do not. In this regard, one of the most challenging part of a data preprocessing is handling the categorical values.


 - In this repository, the dataset shows the ATM Transactions with the one hour intervals. 
***The column "day" is the categorical value contains the days as "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday".***

### Encoding Categorical Data
 - Different techniques are applied to encode the categorical features to numeric quantities. These techniques are applied to the ***"day"*** column. You can apply these methods to any categorical columns.
   #### 1. Replace Values
   - In this method, you just replace the categories with the desired numbers. The [replace()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.replace.html#pandas.DataFrame.replace) function from pandas can be used in this method.
   #### 2. Label Encoding
   - This method allows you to convery each value in a column to a number. Numerical values are always between 0 and numberofcategories-1. The difference between label encoding and replace values method is that in replace values method you can give the any number you want according to your business requirements. The [.cat.codes](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.Series.cat.codes.html) can be used.
   > Remember that the type of the column should be "category" dtype.
   #### 3. One-Hot Encoding
   - Sometimes giving desired numbers to the categories might be improperly since you also gave weights to the categories. The basic strategy to prevent that is to convert each category value into a new column and assign a 1 or 0 to a colummn. One-hot encoding can be applied using pandas [.get_dummies()](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.get_dummies.html) method.
    #### 4. Binary Encoding
   - In this technique, first the categories are encoded as ordinal and then those integers are converted into binary code. Then the digits from that binary string are split into seperate columns. It provides fewer dimension than one-hot encoding. Yoy can do it using [category_encoders](https://contrib.scikit-learn.org/categorical-encoding/) library.
   > In our example, binary encoding creates 3 extra day column called "day_1, day_2, day_3", because we have 7 categories and this can be representes by using 3 binary digit.
     #### 5. Backward Difference Encoding
   - In this technique, a feature of n categories enters a regression as a sequence of n-1 dummy variable. In this encoding, the mean of the dependent variable for a level is compared with the mean of the dependent variable for the prior level. The category_encoders library can be used.
