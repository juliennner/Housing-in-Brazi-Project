import pandas as pd
from IPython.display import VimeoVideo


# # Import

# The first part of any data science project is preparing your data, which means making sure its in the right place and format for you to conduct your analysis. The first step of any data preparation is importing your raw data and cleaning it.
#
# If you look in the `small-data` directory on your machine, you'll see that the data for this project comes in three CSV files: `mexico-real-estate-1.csv`, `mexico-real-estate-2.csv`, and `mexico-real-estate-3.csv`.

# In[2]:


VimeoVideo("656321516", h="e85e3bf248", width=600)


# **Task 1.2.1:** Read these three files into three separate DataFrames named `df1`, `df2`, and `df3`, respectively.
#
# - [What's a DataFrame?](../%40textbook/03-pandas-getting-started.ipynb#Pandas)
# - [What's a CSV file?](../%40textbook/03-pandas-getting-started.ipynb#CSV-Files)
# - [Read a CSV file into a DataFrame using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Working-with-DataFrames)

# In[20]:


df1 = pd.read_csv("data/mexico-real-estate-1.csv")
df2 = pd.read_csv("data/mexico-real-estate-2.csv")
df3 = pd.read_csv("data/mexico-real-estate-3.csv")


# ## Clean `df1`

# Now that you have your three DataFrames, it's time to inspect them to see if they need any cleaning. Let's look at them one-by-one.

# In[5]:


VimeoVideo("656320563", h="a6841fed28", width=600)


# **Task 1.2.2:** Inspect `df1` by looking at its [`shape`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.shape.html) attribute. Then use the [`info`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.info.htm) method to see the data types and number of missing values for each column. Finally, use the [`head`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.head.html) method to determine to look at the first five rows of your dataset.
#
# - [Inspect a DataFrame using the `shape`, `info`, and `head` in pandas.](../%40textbook/03-pandas-getting-started.ipynb#Inspecting-DataFrames)

# In[7]:


df1.shape


# In[8]:


df1.info()


# In[9]:


df1.head()


# It looks like there are a couple of problems in this DataFrame that you need to solve. First, there are many rows with `NaN` values in the `"lat"` and `"lon"` columns. Second, the data type for the `"price_usd"` column is `object` when it should be `float`.

# In[10]:


VimeoVideo("656316512", h="33eb5cb26e", width=600)


# **Task 1.2.3:** Clean `df1` by dropping rows with `NaN` values. Then remove the `"$"` and `","` characters from `"price_usd"` and recast the values in the column as floats.
#
# - [What's a data type?](../%40textbook/01-python-getting-started.ipynb#Data-Types)
# - [Drop rows with missing values from a DataFrame using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Dropping-Rows)
# - [Replace string characters in a column using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Replacing-String-Characters)
# - [Recast a column as a different data type in pandas.](../%40textbook/03-pandas-getting-started.ipynb#Recasting-Data)

# In[21]:


df1.dropna(inplace=True)
df1["price_usd"] = (
    df1["price_usd"]
    .str.replace("$","",regex=False)
    .str.replace(",","")
    .astype(float)
)


# In[19]:


df1.info()


# ## Clean `df2`

# Now it's time to tackle `df2`. Take a moment to inspect it using the same commands you used before. You'll notice that it has the same issue of `NaN` values, but there's a new problem, too: The home prices are in Mexican pesos (`"price_mxn"`), not US dollars (`"price_usd"`). If we want to compare all the home prices in this dataset, they all need to be in the same currency.

# In[22]:


VimeoVideo("656315668", h="c9bd116aca", width=600)


# **Task 1.2.4:** First, drop rows with `NaN` values in `df2`. Next, use the `"price_mxn"` column to create a new column named `"price_usd"`. (Keep in mind that, when this data was collected in 2014, a dollar cost 19 pesos.) Finally, drop the `"price_mxn"` from the DataFrame.
#
# - [Drop rows with missing values from a DataFrame using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Dropping-Rows)
# - [Create new columns derived from existing columns in a DataFrame using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Adding-Columns)
# - [Drop a column from a DataFrame using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Dropping-Columns)

# In[23]:


df2.shape


# In[24]:


df2.info()


# In[25]:


df2.head()


# In[30]:


df2.dropna(inplace=True)
df2["price_usd"] = (df2["price_mxn"] / 19).round(2)
df2.drop(columns = ["price_mxn"], inplace=True)
df2.head()


# ## Clean `df3`

# Great work! We're now on the final DataFrame. Use the same `shape`, `info` and `head` commands to inspect the `df3`. Do you see any familiar issues?
#
# You'll notice that we still have `NaN` values, but there are two new problems:
#
# 1. Instead of separate `"lat"` and `"lon"` columns, there's a single `"lat-lon"` column.
# 2. Instead of a `"state"` column, there's a `"place_with_parent_names"` column.
#
# We need the resolve these problems so that `df3` has the same columns in the same format as `df1` and `df2`.

# In[31]:


VimeoVideo("656314718", h="8d1127a93f", width=600)


# In[33]:


df3.shape


# In[34]:


df3.info()


# In[36]:


df3.head()


# **Task 1.2.5:** Drop rows with `NaN` values in `df3`. Then use the [`split`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html) method to create two new columns from `"lat-lon"` named `"lat"` and `"lon"`, respectively.
#
# - [Drop rows with missing values from a DataFrame using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Dropping-Rows)
# - [Split the strings in one column to create another using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Splitting-Strings)

# In[37]:


df3.dropna(inplace=True)

df3[["lat","lon"]] = df3["lat-lon"].str.split(",", expand = True)
df3.head()


# In[38]:


VimeoVideo("656314050", h="13f6a677fd", width=600)


# **Task 1.2.6:** Use the [`split`](https://pandas.pydata.org/docs/reference/api/pandas.Series.str.split.html) method again, this time to extract the state for every house. (Note that the state name always appears after `"México|"` in each string.) Use this information to create a `"state"` column. Finally, drop the `"place_with_parent_names"` and `"lat-lon"` columns from the DataFrame.
#
# - [Split the strings in one column to create another using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Splitting-Strings)
# - [Drop a column from a DataFrame using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Dropping-Columns)

# In[39]:


df3["place_with_parent_names"].str.split("|", expand = True).head()


# In[41]:


df3["place_with_parent_names"].str.split("|", expand = True)[2].head()


# In[42]:


df3["state"] = df3["place_with_parent_names"].str.split("|", expand = True)[2]
df3.head()


# In[44]:


df3.drop(columns=["place_with_parent_names","lat-lon"], inplace=True)
df3.head()


# ## Concatenate DataFrames

# Great work! You have three clean DataFrames, and now it's time to combine them into a single DataFrame so that you can conduct your analysis.

# In[45]:


VimeoVideo("656313395", h="ccadbc2689", width=600)


# **Task 1.2.7:** Use [`pd.concat`](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.concat.html) to concatenate `df1`, `df2`, `df3` as new DataFrame named `df`. Your new DataFrame should have 1,736 rows and 6 columns:`"property_type"`, `"state"`, `"lat"`, `"lon"`, `"area_m2"`, `"price_usd"`, and `"price_per_m2"`.
#
# - [Concatenate two or more DataFrames using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Concatenating-DataFrames)

# In[46]:


df = pd.concat([df1, df2, df3])
print(df.shape)
df.head()


# ## Save `df`

# The data is clean and in a single DataFrame, and now you need to save it as a CSV file so that you can examine it in your exploratory data analysis.

# In[47]:


VimeoVideo("656312464", h="81ee04de15", width=600)


# **Task 1.2.8:** Save `df` as a CSV file using the [`to_csv`](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_csv.html) method. The file path should be `"./data/mexico-real-estate-clean.csv"`. Be sure to set the `index` argument to `False`.
#
# - [What's a CSV file?](../%40textbook/03-pandas-getting-started.ipynb#CSV-Files)
# - [Save a DataFrame as a CSV file using pandas.](../%40textbook/03-pandas-getting-started.ipynb#Saving-a-DataFrame-as-a-CSV)

# In[48]:


df.to_csv("data/mexico-real-estate-clean.csv", index = False)
