from src.digest_creator import DigestCreator

Digest = DigestCreator()

exclude = False
if exclude:
    with open('../../ExclusionLists/to_exclude_feb.txt', 'r') as file:
        # Read each line in the file
        exclude_from_min_1 = [line.strip() for line in file]
else:
    exclude_from_min_1 = []

Digest.create_digest(df_path="../../Data/", df_name="Для_отбора_в_дайджест_2025-03-26_19-16.xlsx", df_sep='\t',
                     save_path="../../Digests/", digest_name='digest', translate_text=False, score_sum_threshold=1,
                     exclude_from_min_1=exclude_from_min_1, use_to_digest_col=True)
