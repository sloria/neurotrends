import re
from pymongo import MongoClient

DATES = range(2000, 2014)

mongo = MongoClient()['neurotrends']

query = '''
    (
        "fmri"
        OR "functional mri"
        OR "functional magnetic resonance imaging"
    )
    AND humans[MH]
    AND (
        "psychological phenomena and processes"[MH]
        OR "behavior and behavior mechanisms"[MH]
        OR "brain mapping"[MH]
    )
    AND english[LA]
    AND "journal article"[PT]
    NOT "review"[PT]
    NOT "meta-analysis"[PT]
'''