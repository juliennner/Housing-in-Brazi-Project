from IPython.display import VimeoVideo

VimeoVideo("656189257", h="3298dbabb7", width=600)


# <font size="+3"><strong>1.1 Organizing Tabular Data in Python</strong></font>

# # What's Tabular Data?

# In[2]:


VimeoVideo("645390762", h="578b5a9e19", width=600)


# <div class="alert alert-info" role="alert">
#     <p><b>Frequent Question:</b> When I try to run this cell ☝️, I get:
#     <blockquote><code>NameError: name 'VimeoVideo' is not defined</code></blockquote></p>
#     <p><b>Tip:</b> <code>NameError</code> usually means that you're asking Python to use a tool that you haven't imported yet. So make sure you run the first cell of this notebook, the one that contains <code>from IPython.display import VimeoVideo</code>.</p>
# </div>

# Information can come in many forms, and part of a data scientist's job is making sure that information is organized in a way that's conducive to analysis. Take for example these five houses from the Mexico real estate dataset we'll use in this project:
#
# ![Five houses showing price, number of rooms, and area in square meters for each](../images/proj-1.001.png)
#
# One common way to organize this information is in a **table**, which is a group of **cells** organized into **rows** and **columns**:
#
# ![Table, organized into rows and columns, with housing information from previous image](../images/proj-1.002.png)
#
# When working with this sort of **tabular data**, it's important to organize row and columns following the principles of "**[tidy data](https://en.wikipedia.org/wiki/Tidy_data)**." What does that mean in the case of our dataset?
#
# 1. Each row corresponds to a single house in our dataset. We'll call each of these houses an **observation**.
# 2. Each column corresponds to a characteristic of each house. We'll call these **features**.
# 3. Each cell contains only one **value**.
#
# ![Three copies of table from previous image, emphasizing observations as rows and features as columns](../images/proj-1.003.png)
#
# So whenever you encounter a new dataset, make sure your data is "tidy." `NOTE: need to add activity here`

# # Tabular Data and Python Data Structures

# ## Working with Lists
#
# Python comes with several data structures that we can use to organize tabular data. Let's start by putting a single observation in a **list**.

# In[3]:


house_0_list = [115910.26, 128, 4]
house_0_list


# In[4]:


VimeoVideo("645390786", h="da0bb831d1", width=600)


# **Task 1.1.1:** One metric that people in the real estate industry look at is price per square meter because it allows them to compare houses of different sizes. Can you use the information in this list to calculate the price per square meter for `house_0`?
#
# - [What's a list?](../%40textbook/01-python-getting-started.ipynb#Lists)
# - [Access an item in a list using Python.](../%40textbook/01-python-getting-started.ipynb#Working-with-Lists)
# - [Perform basic mathematical operations in Python.](../%40textbook/01-python-getting-started.ipynb#Simple-Calculations)

# In[5]:


house_0_price_m2 = house_0_list[0] / house_0_list[1]
house_0_price_m2


# In[6]:


VimeoVideo("645390797", h="86c579a9cb", width=600)


# **Task 1.1.2:** Next, use the [`append`](https://docs.python.org/3/tutorial/datastructures.html#more-on-lists) method to add the price per square meter to the end of the end of `house_0`.
#
# - [Append an item to a list in Python.](../%40textbook/01-python-getting-started.ipynb#Appending-Items)

# In[7]:


house_0_list.append(house_0_price_m2)
house_0_list


# Now that you can work with data for a single house, let's think about how to organize the whole dataset. One option would be to create a list for each observation and then put those together in another list. This is called a [**nested list**](http://127.0.0.1:8888/lab/tree/work/ds_curriculum/%40textbook/Python.ipynb#creating-lists).

# In[14]:


houses_nested_list = [
    [115910.26, 128.0, 4.0],
    [48718.17, 210.0, 3.0],
    [28977.56, 58.0, 2.0],
    [36932.27, 79.0, 3.0],
    [83903.51, 111.0, 3.0],
]

houses_nested_list


# Now that we have more observations, it doesn't make sense to calculate the price per square meter for each house one-by-one. Instead, we can automate this repetitive task using a `for` loop.

# In[9]:


VimeoVideo("645390807", h="4536120cf5", width=600)


# **Task 1.1.3:** Append the price per square meter to each observation in `houses_nested_list` using a `for` loop.
#
# - [What's a for loop?](../%40textbook/01-python-getting-started.ipynb#Python-for-Loops)
# - [Write a for loop in Python.](../%40textbook/01-python-getting-started.ipynb#Working-with-for-Loops)

# In[15]:


for i in range(len(houses_nested_list)):
    houses_nested_list[i].append(houses_nested_list[i][0]/houses_nested_list[i][1])
#for house in houses_nested_list:
#    house.append(house[0]/house[1])
houses_nested_list


# ## Working with Dictionaries

# Lists are a good way to organize data, but one drawback is that we can only represent values. Why is that a problem? For example, someone looking at `[115910.26, 128.0, 4]` wouldn't know which values corresponded to price, area, etc. A better option might be a [**dictionary**](http://127.0.0.1:8888/lab/tree/work/ds_curriculum/%40textbook/Python.ipynb#whats-a-dictionary), where each value is associated with a key. Here's what `house_0` looks like as a dictionary instead of a list.

# In[16]:


house_0_dict = {
    "price_aprox_usd": 115910.26,
    "surface_covered_in_m2": 128,
    "rooms": 4,
}

house_0_dict


# In[17]:


VimeoVideo("645390821", h="884613d46b", width=600)


# **Task 1.1.4:** Calculate the price per square meter for `house_0` and add it to the dictionary under the key `"price_per_m2"`.
#
# - [What's a dictionary?](../%40textbook/01-python-getting-started.ipynb#Python-Dictionaries)
# - [Access an item in a dictionary in Python.](../%40textbook/01-python-getting-started.ipynb#Working-with-Dictionaries)

# In[18]:


house_0_dict["price_per_m2"] = house_0_dict["price_aprox_usd"] / house_0_dict["surface_covered_in_m2"]
house_0_dict


# If we wanted to combine all our observations together, the best way would be to create a list of dictionaries.

# In[19]:


houses_rowwise = [
    {
        "price_aprox_usd": 115910.26,
        "surface_covered_in_m2": 128,
        "rooms": 4,
    },
    {
        "price_aprox_usd": 48718.17,
        "surface_covered_in_m2": 210,
        "rooms": 3,
    },
    {
        "price_aprox_usd": 28977.56,
        "surface_covered_in_m2": 58,
        "rooms": 2,
    },
    {
        "price_aprox_usd": 36932.27,
        "surface_covered_in_m2": 79,
        "rooms": 3,
    },
    {
        "price_aprox_usd": 83903.51,
        "surface_covered_in_m2": 111,
        "rooms": 3,
    },
]

houses_rowwise


# This way of storing data is so popular, it has its own name: [**JSON**](http://127.0.0.1:8888/lab/tree/work/ds_curriculum/%40textbook/Python.ipynb#JSON). We'll learn more about it later in the course. For now, let's build another for loop, but this time, we'll add a add the price per square meter to each dictionary.

# In[20]:


VimeoVideo("645390833", h="0d3963c0d0", width=600)


# **Task 1.1.5:** Using a `for` loop, calculate the price per square meter and store the result under a `"price_per_m2"` key for each observation in `houses_rowwise`.
#
# - [What's JSON?](../%40textbook/01-python-getting-started.ipynb#JSON)
# - [Write a for loop in Python.](../%40textbook/01-python-getting-started.ipynb#Working-with-for-Loops)

# In[21]:


for house in houses_rowwise:
    house["price_per_m2"] = house["price_aprox_usd"] / house["surface_covered_in_m2"]
houses_rowwise


# JSON is a great way to organize data, but it does have some downsides. Note that each dictionary represents a single house or, if we think about it as tabular data, a row in our dataset. This means that it's pretty easy to do row-wise calculations (like we did with price per square meter), but column-wise calculations are more complicated. For instance, what if we wanted to know the mean house price for our dataset? First we'd need to collect the price for each house in a list and then calculate mean.

# In[22]:


VimeoVideo("645390848", h="889a3cfb33", width=600)


# **Task 1.1.6:** To calculate the mean price for `houses_rowwise` by completing the code below.
#
# - [Write a for loop in Python.](../%40textbook/01-python-getting-started.ipynb#Working-with-for-Loops)
# - [Append an item to a list in Python.](../%40textbook/01-python-getting-started.ipynb#Appending-Items)

# In[23]:


house_prices = []
for house in houses_rowwise:
    house_prices.append(house["price_aprox_usd"])

mean_house_price = sum(house_prices) / len(house_prices)

mean_house_price


# One way to make this sort of calculation easier is to organize our data by features instead of observations. We'll still use dictionaries and lists, but we'll implement them a slightly differently.

# In[24]:


houses_columnwise = {
    "price_aprox_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
    "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
    "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
}

houses_columnwise


# In[25]:


VimeoVideo("645390869", h="ef4d49bf66", width=600)


# **Task 1.1.7:** Calculate the mean house price in `houses_columnwise`
#
# - [Perform common aggregation tasks on a list in Python.](../%40textbook/01-python-getting-started.ipynb#Aggregating-Items)

# In[26]:


mean_house_price = sum(houses_columnwise["price_aprox_usd"]) / len(houses_columnwise["price_aprox_usd"])

mean_house_price


# Of course, when we organize our data according to columns / features, row-wise operations become more difficult.

# In[27]:


VimeoVideo("645396267", h="66eda35f00", width=600)


# **Task 1.1.8:** Create a `"price_per_m2"` column in `houses_columnwise`?
#
# - [Add a a key-value pair to a dictionary in Python.](../%40textbook/01-python-getting-started.ipynb#Creating-Dictionaries)
# - [Zip two lists together in Python.](../%40textbook/01-python-getting-started.ipynb#Zipping-Items)
# - [Write a for loop in Python.](../%40textbook/01-python-getting-started.ipynb#Working-with-for-Loops)

# In[30]:


price_per_m2 = []
for price, area in zip(houses_columnwise["price_aprox_usd"], houses_columnwise["surface_covered_in_m2"]):
    price_per_m2.append(price / area)
houses_columnwise["price_per_m2"] = price_per_m2
houses_columnwise


# # Tabular Data and pandas DataFrames

# <iframe src="https://player.vimeo.com/video/645396345?h=ba25c25741&amp;title=0&amp;byline=0&amp;portrait=0&amp;speed=0&amp;badge=0&amp;autopause=0&amp;player_id=0&amp;app_id=58479" width="1920" height="1080" frameborder="0" allow="autoplay; fullscreen; picture-in-picture" allowfullscreen title="011-9"></iframe>

# In[31]:


VimeoVideo("645396345", h="ba25c25741", width=600)


# While you've shown that you can wrangle data using lists and dictionaries, it's not as intuitive as working with, say, a spreadsheet. Fortunately, there are lots of libraries for Python that make it an even better tool for tabular data — way better than spreadsheet applications like Microsoft Excel or Google Sheets! One of the best known data science libraries is **pandas**, which allows you to organize data into **DataFrames**.
#
# Let's import pandas and then create a DataFrame from `houses_columnwise`.

# In[32]:


import pandas as pd

data = {
    "price_aprox_usd": [115910.26, 48718.17, 28977.56, 36932.27, 83903.51],
    "surface_covered_in_m2": [128.0, 210.0, 58.0, 79.0, 111.0],
    "rooms": [4.0, 3.0, 2.0, 3.0, 3.0],
}

df_houses = pd.DataFrame(data)

df_houses
