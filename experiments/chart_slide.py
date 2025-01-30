from src.digest_creator import DigestCreator
from src.utils import current_time
import numpy as np

Digest = DigestCreator()

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

df = Digest.load_data_table(df_path="../../Data/", df_name="view_experts_score_with_src_name_datetime.tsv", sep='\t')

df['sum_scores'] = df['user_1_score'].fillna(0) + df['user_2_score'].fillna(0) + df['user_3_score'].fillna(0)

# Assuming df is your DataFrame
df['min_1'] = np.where(df['sum_scores'] < 1, 0, 1)

df['fix_src_name'] = df['src_name'].map(src_name_beautify)

prs = Digest.create_presentation()
Digest.add_graph_slide(presentation=prs, df=df, title='Обзор источников')
Digest.save_presentation(presentation=prs, name=f'chart_slide_{current_time()}', path='../../ChartTests/')
