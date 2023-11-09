from validate_email import validate_email
#from email_validator import validate_email
import pandas as pd
#import pyarrow

print("Pandas version: " + pd.__version__)
def email_validation(email):
  if validate_email(email):
    return True
  else:
    return False

# Validate emails
data_np = pd.read_csv('np.csv', engine='pyarrow',dtype_backend="pyarrow",delimiter='\t')
data_performing = pd.read_csv('perf.csv', engine='pyarrow',dtype_backend="pyarrow", delimiter='\t')
print(f" Performing: {data_performing.shape[0]}")
print(f" Non-Performing: {data_np.shape[0]}")


df_valid_np = data_np[data_np['Email'].apply(email_validation)]
df_valid_performing = data_performing[data_performing['Email'].apply(email_validation)]

print(f"Valid emails Non-Performing: {df_valid_np.shape[0]}")
print(f"Valid emails Non-Performing: {df_valid_performing.shape[0]}")


# Remove duplicate emails -  Delete duplicate rows based on specific columns
df_valid_np = df_valid_np.drop_duplicates(subset=["Email"], keep='first')
df_valid_performing = df_valid_performing.drop_duplicates(subset=["Email"], keep='first')

print(f"Valid distinct emails Non-Performing: {df_valid_np.shape[0]}")
print(f"Valid distinct emails Non-Performing: {df_valid_performing.shape[0]}")

with pd.ExcelWriter('AfricanExpoPandas2.xlsx') as writer:
  df_valid_performing.to_excel(writer, sheet_name='Performing')
  df_valid_np.to_excel(writer, sheet_name='Non_Performing')
