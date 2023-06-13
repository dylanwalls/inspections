import pandas as pd

# Import rental_units sheet
rental_units_df = pd.read_excel('ozow.xlsx', sheet_name='rental_units')

# Import ozow_payments sheet
ozow_payments_df = pd.read_excel('ozow.xlsx', sheet_name='ozow_payments')

# Create an empty list to store matching unit numbers
matching_unit_numbers = []

# Iterate through each row in ozow_payments sheet
for index, payment_row in ozow_payments_df.iterrows():
    ref_no = payment_row['RefNo']  # Get the RefNo from ozow_payments
    
    # Find matching row in rental_units based on RefNo
    matching_row = rental_units_df.loc[rental_units_df['RefNo'] == ref_no]

    if not matching_row.empty:
        unit_no = matching_row.iloc[0]['unitNo']  # Get the unitNo from rental_units
        matching_unit_numbers.append(unit_no)  # Add unitNo to the list
        matching_unit_numbers = list(set(matching_unit_numbers))
        matching_unit_numbers.sort()

# Print the list of matching unit numbers
i = 0
for unit in matching_unit_numbers:
    i += 1
    print(str(i) + '. ' + unit)
