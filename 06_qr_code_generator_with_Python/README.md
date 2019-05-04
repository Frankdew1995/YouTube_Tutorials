
### Dependencies to install (Some of them you might not happen to use):

    Django==2.2.1
    image==1.5.27
    numpy==1.16.3
    pandas==0.24.2
    Pillow==6.0.0
    PyQRCode==1.2.1
    python-dateutil==2.8.0
    pytz==2019.1
    qrcode==6.1
    six==1.12.0
    sqlparse==0.3.0
    xlrd==1.2.0
    
### Before you start,  make sure to install all the dependencies. 

### 1. Make a simple SVG format QR Code with pyqrcode

It's very straightforward to make a simple QR Code with Python module [**pyqrcode**](https://github.com/mnooner256/pyqrcode).

Let's first start with import the module:


```python
import pyqrcode
```

Let's store a sample text data into the QR Code and generate this QR Code. 


```python
# Declare a variable called 'text'
text = "hey, there!"
```

Now we can embed this text data into a QR Code


```python
# Pass the variable "text" into the parenthesis as the parameter:
image = pyqrcode.create(text)
```

Let's now generate the QR Code image in SVG format with the sample text data saved in:


```python
# scale represents the size of the image so that you can tweak this parameter until 
# you have the ideal size for the image. 

image.svg("QR.svg", scale="5")
```

Above code will generate a QR Code named as "QR.svg" in your current working directory. Any QR Code scanner, e.g. a smart phone, can scan this qr code and read the info **"hey, there!"**

### 2. Read data from a CSV file and write data into the QR Code

Let's first take a look at the data of sample Data.csv file (in this case, we need a flagship Python data analysis library called [**pandas**](http://pandas.pydata.org/pandas-docs/stable/)):


```python
import pandas as pd
df = pd.read_csv("Data.csv")
df.head() # Read only first 5 rows into the pandas DataFrame
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Brand</th>
      <th>Name</th>
      <th>Category</th>
      <th>Barcode</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>Makeup Revolution</td>
      <td>Makeup Revolution Camouflage Corrector Palette</td>
      <td>Cosmetics</td>
      <td>5029066099020</td>
    </tr>
    <tr>
      <th>1</th>
      <td>Makeup Revolution</td>
      <td>Makeup Revolution Pro HD Camouflage Light</td>
      <td>Cosmetics</td>
      <td>5029066099051</td>
    </tr>
    <tr>
      <th>2</th>
      <td>Makeup Revolution</td>
      <td>Makeup Revolution Pro HD Camouflage Light Medium</td>
      <td>Cosmetics</td>
      <td>5029066099082</td>
    </tr>
    <tr>
      <th>3</th>
      <td>Makeup Revolution</td>
      <td>Makeup Revolution Ultra Pro HD Camouflage Medi...</td>
      <td>Cosmetics</td>
      <td>5029066099112</td>
    </tr>
    <tr>
      <th>4</th>
      <td>Makeup Revolution</td>
      <td>Makeup Revolution Brush Flex 01 Blend and Buff</td>
      <td>Cosmetics</td>
      <td>5060495301087</td>
    </tr>
  </tbody>
</table>
</div>



The idea is that our Python app can read each row as a single data record from this csv file and write this data record into one QR Code generation run. 

We can iterate each row from this dataframe and save them into a new Python string. In order to do this, we can use the [**df.iterrows()**](https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.iterrows.html) method from Pandas.


```python

# Call the iterrows() method from a df obejct. 
# In this case, we also do tuple unpacking. 
# because df.iterrows() render a tuple where the first indexed-element is the df row index
# and the second-indexed element is the special Pandas series obeject (excel-wise: a column)

for index, values in df.iterrows(): # Although, in this case we won't use 'index' variable
        
        # values is a pandas series and can be indexed like a Python dictionary.
        brand = values["Brand"]
        name = values["Name"]
        category = values["Category"]
        barcode = values["Barcode"]
        
        # Use Python f-String to embed the variables into a Python string.
        data = f'''

        Name: {name} \n
        Barcode: {barcode} \n
        Category: {category} \n
        Brand: {brand} \n
        '''
        
        # Write this text data into the QR Code. 
        image = pyqrcode.create(data)
        
        # Finally name the generated QR codes with the 'name' and 'barcode' variables for being 
        # unique.
        image.svg(f"{name}_{barcode}.svg", scale="5")
        
        # Print the text data for debugging purposes. 
        print(data)
```

Let's make this code more modular and wrap up everything shown in section 2 and make a new function:


```python
import pyqrcode

import pandas as pd

def createQRCode():


    df = pd.read_csv("Data.csv")

    for index, values in df.iterrows():

        brand = values["Brand"]
        name = values["Name"]
        category = values["Category"]
        barcode = values["Barcode"]

        data = f'''

        Name: {name} \n
        Barcode: {barcode} \n
        Category: {category} \n
        Brand: {brand}
        '''
        image = pyqrcode.create(data)
        image.svg(f"{name}_{barcode}.svg", scale="5")
        print(data)

```

Run the function to generate the QR Codes from the CSV File. 


```python
createQRCode()
```
