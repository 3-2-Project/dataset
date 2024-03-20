import pandas as pd

# Load the updated_data1.csv file
df = pd.read_csv('updated_data1.csv')

# Convert values below 0.5 to 0 and above 0.5 to 1 in the occupancy column
df['occupancy'] = df['occupancy'].apply(lambda x: 0 if x < 0.5 else 1)

# Save the modified DataFrame to a new CSV file
df.to_csv('updated_data1_modified1.csv', index=False)
import pandas as pd

# Load the data
df_excel = pd.read_csv('data.csv')

# Convert date columns to datetime objects
try:
    df_excel['StartDate'] = pd.to_datetime(df_excel['StartDate'], format='%m/%d/%Y')
    df_excel['EndDate'] = pd.to_datetime(df_excel['EndDate'], format='%m/%d/%Y')
except ValueError as e:
    print("No Error in date conversion:", e)

# Define a function to calculate occupancy
def get_occupancy(start_date, end_date, start_time, end_time):
    try:
        start_datetime = pd.to_datetime(str(start_date) + ' ' + str(start_time))
        end_datetime = pd.to_datetime(str(end_date) + ' ' + str(end_time))
        occupancy_hours = (end_datetime - start_datetime).total_seconds() / (60 * 60)
        return occupancy_hours if occupancy_hours >= 0 else 0
    except Exception as e:
        print("Error in occupancy calculation:", e)
        return None

# Apply the get_occupancy function to each row
try:
    df_excel['occupancy'] = df_excel.apply(lambda row: get_occupancy(row['StartDate'], row['EndDate'], row['StartTime'], row['EndTime']), axis=1)
except Exception as e:
    print("Error in applying occupancy function:", e)

# Save the updated DataFrame to a new CSV file
df_excel.to_csv('updated_data1.csv', index=False)

# Convert values below 0.5 to 0 and above 0.5 to 1 in the occupancy column
df['occupancy'] = df['occupancy'].apply(lambda x: 0 if x < 0.5 else 1)

# Save the modified DataFrame to a new CSV file
df.to_csv('updated_data1_modified1.csv', index=False)