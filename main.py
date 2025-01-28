from digest_creator import DigestCreator

Digest = DigestCreator()

Digest.create_digest(df_path="../Data/", df_name="view_experts_score_with_datetime(17.12.2024).tsv", df_sep='\t',
                     save_path="../Digests/", digest_name='digest', translate_text=False, score_sum_threshold=1)
