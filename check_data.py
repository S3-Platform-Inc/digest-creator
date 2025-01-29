from digest_creator import DigestCreator

Digest = DigestCreator()

df = Digest.load_data_table(df_path="../Data/", df_name="view_experts_score_with_src_name_datetime.tsv", sep='\t')
print(df.info())
print(df.head())
# for el in list(df['src_name'].unique()):
#     print(el)
df['sum_scores'] = df['user_1_score'].fillna(0) + df['user_2_score'].fillna(0) + df['user_3_score'].fillna(0)

print(df[df['sum_scores'] >= 3].head()[['user_1_score', 'user_2_score', 'user_3_score']])
print(df[df['sum_scores'] >= 3].shape)
print(f'До удаления дублиактов: {df.shape}')
print(f"После удаления дубликатов: {df.drop_duplicates(subset=['title', 'published', 'weblink']).shape}")
