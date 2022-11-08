import os
from dotenv import load_dotenv

load_dotenv()


def get_bool(key: str, default: str) -> bool:
    return os.getenv(key, default).lower() in ['true', '1']


REFRESH_OFFLINE_PROBLEM_DATA = get_bool('REFRESH_OFFLINE_PROBLEM_DATA', 'false')
SUBMISSION_LIMIT = int(os.getenv('SUBMISSION_LIMIT', '20'))


USE_VJ = get_bool('USE_VJ', 'true')
VJ_USER = os.getenv('VJ_USER', '')
VJ_PASS = os.getenv('VJ_PASS', '')

USE_UVA = get_bool('USE_UVA', 'false')
UVA_USER = os.getenv("UVA_USER", "")
UVA_PASS = os.getenv("UVA_PASS", "")

USE_CF = get_bool('USE_CF', 'false')
CF_USER = os.getenv("CF_USER", "")
CF_PASS = os.getenv("CF_PASS", "")

USE_SPOJ = get_bool('USE_SPOJ', 'false')
SPOJ_USER = os.getenv("SPOJ_USER", "")
SPOJ_PASS = os.getenv("SPOJ_PASS", "")

USE_LOJ = get_bool('USE_LOJ', 'false')
