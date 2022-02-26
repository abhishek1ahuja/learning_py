# goal
# to read weather data
# filter out rows which have temp less than a certain threshold
# and belonging to a certain city
# print number of records in original data
# store filtered data in a new file
import pandas
PATH_TO_INPUT_FILE = "D:\college\q6\DS_TA\DPV\SuperSales\SuperSales\SuperstoreSales_main.csv"

# function 1
# read file into a dataframe
sales_df = pandas.read_csv(PATH_TO_INPUT_FILE, sep=';', decimal=',', encoding_errors='ignore')
print("sales_df: \n", sales_df)
print("sales_df.head(20): \n",sales_df.head(20))
print("sales_df.columns: ", sales_df.columns)

# select some columns from the 21
cols_to_select = ["Row ID", "Order ID", "Sales", "Shipping Cost"]
sales_df_selected = sales_df[cols_to_select]
print("sales_df_selected.head(20): \n", sales_df_selected.head(20))

sales_df_list = sales_df_selected.to_dict()
print(type(sales_df_list))
# print("sales_df_list: \n", sales_df_list)

# function 2
# transform data


# function 3
# store results

# invoke the above functions here

# now ponder - why use functions, why not do this without functions