from src.digest_creator import DigestCreator

Digest = DigestCreator()

# Open the file in read mode
with open('../../ExclusionLists/exclude_20250131.txt', 'r') as file:
    # Read each line in the file
    exclude_from_min_1 = [line.strip() for line in file]

Digest.create_digest(df_path="../../Data/", df_name="view_experts_score_with_src_name_datetime.tsv", df_sep='\t',
                     save_path="../../Digests/", digest_name='digest', translate_text=True, score_sum_threshold=1,
                     exclude_from_min_1=exclude_from_min_1)
