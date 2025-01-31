# print('Abstract'.split('.'))

from src.digest_creator import DigestCreator
import numpy as np

Digest = DigestCreator()
df = Digest.load_data_table(df_path="../../Data/", df_name="view_experts_score_with_src_name_datetime.tsv", sep='\t')

thr = 1

df['sum_scores'] = df['user_1_score'].fillna(0) + df['user_2_score'].fillna(0) + df['user_3_score'].fillna(0)


# Assuming df is your DataFrame
df['min_1'] = np.where(df['sum_scores'] < 1, 0, 1)

print("df['min_1'].value_counts(dropna=False):")
print(df['min_1'].value_counts(dropna=False))

print("\ndf['src_name'].value_counts(dropna=False):")
print(df['src_name'].value_counts(dropna=False))

print("\ndf['src_name'].nunique()")
print(df['src_name'].nunique())

df.sort_values(by='src_name', inplace=True)

# Assuming df is your DataFrame
result = df.groupby('src_name')['min_1'].value_counts().unstack(fill_value=0)
print(result.info())
print(result)

# Convert to lists
sources = result.index.tolist()
src_0_count = result[0].tolist()  # Counts of 0
src_1_count = result[1].tolist()  # Counts of 1

special_weblinks = ['https://eba-cms-prod.azurewebsites.net/media/azure/production/4055/eba_20241030_cross-border_payments_survey_executive_summary.pdf',
                    'https://eba-cms-prod.azurewebsites.net/media/azure/production/4015/eba_20240926_two-page_management-summary_eba-fraud-taxonomy_v11.pdf',
                    'https://eba-cms-prod.azurewebsites.net/media/azure/production/4014/eba_20240916_one-page_management-summary_eba-fraud-taxonomy_v10.pdf',
                    'https://thepaypers.com/payments-general/the-riksbank-opens-its-payment-system--1271153']

df.loc[df['weblink'].isin(special_weblinks) & (df['min_1'] == 1), 'min_1'] = 0

print('\n===AFTER===\n')

print("df['min_1'].value_counts(dropna=False):")
print(df['min_1'].value_counts(dropna=False))

print("\ndf['src_name'].value_counts(dropna=False):")
print(df['src_name'].value_counts(dropna=False))

print("\ndf['src_name'].nunique()")
print(df['src_name'].nunique())

# Display the lists
print("Sources:", sources)
print("Counts of 0:", src_0_count)
print("Counts of 1:", src_1_count)




