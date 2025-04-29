from src.digest_creator import DigestCreator
import pandas as pd
from os.path import join

src_name_beautify = {
    'w3c': 'W3C',
    'jcb': 'JCB',
    'visa': 'VISA',
    'emvco': 'EMVCo',
    'paymentsdive': 'PaymentsDive',
    'mit': 'MIT',
    'bis': 'BIS',
    'payments-journal': 'PaymentsJournal',
    'retailloyalty': 'RetailLoyalty',
    'eba': 'European Banking Association',
    'businesswire': 'Businesswire',
    'techcrunch': 'TechCrunch',
    'nfcw': 'NFCW',
    'thepaypers': 'ThePaypers',
    'americanexpress': 'American Express',
    'ieee': 'IEEE',
    'eupay': 'European Payments Council',
    'iso20022': 'ISO20022',
    'fido': 'FIDO',
    'finextra': 'Finextra',
    'kpmg': 'KPMG',
    'rfc': 'RFC',
    'ecb': 'European Central Bank',
    'pci': 'PCI',
    'eucommission': 'European Commission',
    'nist': 'NIST',
    'paypal': 'Paypal',
    'swift': 'SWIFT',
    'openbanking': 'OpenBanking',
    'openid': 'OpendID',
    'pwc': 'PWC'}

Digest = DigestCreator()

df = pd.read_csv(filepath_or_buffer=join("../../Data/", "Таблица оценок_2025-02-26_22-22-03.csv"), sep='\t')

df.rename(columns={'Заголовок': 'title',
                   'Дата публикации': 'published',
                   'Ссылка': 'weblink',
                   'Оценка': 'score',
                   'Дата оценки': 'date_score',
                   'Пользователь': 'user',
                   'Комментарий': 'comment'}, inplace=True)

print(df.info())

Digest.load_data_table(df_path="../../Data/", df_name="Таблица оценок_2025-02-26_22-19-48.csv", sep='\t')

# for el in list(df['src_name'].unique()):
#     print(el)
# df['sum_scores'] = 1 # df['user_1_score'].fillna(0) + df['user_2_score'].fillna(0) + df['user_3_score'].fillna(0)
#
# min_1_vals = []
#
# for i, row in df.iterrows():
#     if row['sum_scores'] >= 1:
#         min_1_vals.append(1)
#     else:
#         min_1_vals.append(0)

df['min_1'] = 1

df['fix_src_name'] = df['src_name'].map(src_name_beautify)

# To verify the changes
print(df[['src_name', 'fix_src_name']])

print(df.info())
print(df.head())

print(df[df['sum_scores'] >= 3].head()[['user_1_score', 'user_2_score', 'user_3_score']])
print(df[df['sum_scores'] >= 3].shape)
print(f'До удаления дублиактов: {df.shape}')
print(f"После удаления дубликатов: {df.drop_duplicates(subset=['title', 'published', 'weblink']).shape}")
