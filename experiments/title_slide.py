from src.digest_creator import DigestCreator
from src.utils import current_time

Digest = DigestCreator()

prs = Digest.create_presentation()
Digest.add_title_slide(presentation=prs)
Digest.save_presentation(presentation=prs, name=f'title_slide_{current_time()}', path='../../ImageTests/')
