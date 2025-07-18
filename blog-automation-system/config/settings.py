import os
from dotenv import load_dotenv

# .envա��K���	p���
load_dotenv()

# WordPress-�
WORDPRESS_URL = os.getenv('WORDPRESS_URL', 'https://your-site.com')
WORDPRESS_USERNAME = os.getenv('WORDPRESS_USERNAME', 'your-username')
WORDPRESS_APP_PASSWORD = os.getenv('WORDPRESS_APP_PASSWORD', 'your-app-password')

# Claude API-�
CLAUDE_API_KEY = os.getenv('CLAUDE_API_KEY', 'your-claude-api-key')

# Google API-���������(	
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')
GOOGLE_CSE_ID = os.getenv('GOOGLE_CSE_ID', '')

# Unsplash API-�������;�(	
UNSPLASH_ACCESS_KEY = os.getenv('UNSPLASH_ACCESS_KEY', '')

# �-�
ARTICLE_MIN_LENGTH = 2000
ARTICLE_MAX_LENGTH = 4000
DAILY_POST_LIMIT = 5

# ��������-�
KEYWORD_MIN_SEARCH_VOLUME = 100
KEYWORD_MAX_SEARCH_VOLUME = 1000
KEYWORD_MAX_COMPETITION = 0.5

# ����-�
AUTHOR_NAME = " "
AUTHOR_PROFILE = """
�����n�����|餿�
Ǹ�����ƣ�hӸ͹&e��hW
-mnw/�k15t�
:��
���j��Ф�hK��YD�g�ULB�
"""

# ա��ѹ-�
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
PAST_ARTICLES_DIR = os.path.join(DATA_DIR, 'past_articles')
KEYWORDS_DIR = os.path.join(DATA_DIR, 'keywords')
TEMPLATES_DIR = os.path.join(DATA_DIR, 'templates')
STYLE_PROFILE_PATH = os.path.join(DATA_DIR, 'style_profile.json')

# ��-�
LOG_DIR = os.path.join(BASE_DIR, 'logs')
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(name)s - %(levelname)s - %(message)s'

# �������-�
POSTING_SCHEDULE = {
    'monday': ['09:00', '15:00'],
    'tuesday': ['09:00', '15:00'],
    'wednesday': ['09:00', '15:00'],
    'thursday': ['09:00', '15:00'],
    'friday': ['09:00', '15:00'],
    'saturday': ['10:00'],
    'sunday': ['10:00']
}

# ��ƴ��-�
DEFAULT_CATEGORIES = [
    'Ӹ͹',
    '���ƣ�',
    'Ư����',
    '�չ���',
    'wm�om'
]

# SEO-�
SEO_TITLE_MAX_LENGTH = 60
SEO_META_DESCRIPTION_LENGTH = 160

# ��������-�
MAX_RETRY_ATTEMPTS = 3
RETRY_DELAY_SECONDS = 60

# �ï���-�
BACKUP_ENABLED = True
BACKUP_DIR = os.path.join(BASE_DIR, 'backups')
BACKUP_RETENTION_DAYS = 30

# �թ���-�
ENABLE_CACHING = True
CACHE_EXPIRY_HOURS = 24

# �-�
NOTIFICATION_EMAIL = os.getenv('NOTIFICATION_EMAIL', '')
SEND_SUCCESS_NOTIFICATIONS = True
SEND_ERROR_NOTIFICATIONS = True

# A/Bƹ�-�
AB_TESTING_ENABLED = False
AB_TEST_SAMPLE_SIZE = 0.5  # 50%n�gA/Bƹȟ�

# ����ï-�
QUALITY_CHECK_ENABLED = True
MIN_READABILITY_SCORE = 60  # ��YU���n $
MAX_KEYWORD_DENSITY = 0.03  # �����Ʀn '$3%	
CHECK_DUPLICATE_CONTENT = True

# API ���6P-�
CLAUDE_API_RATE_LIMIT = 50  # 1B_�nꯨ��p
WORDPRESS_API_RATE_LIMIT = 100  # 1B_�nꯨ��p

def create_directories():
    """Łjǣ���\"""
    directories = [
        DATA_DIR,
        PAST_ARTICLES_DIR,
        KEYWORDS_DIR,
        TEMPLATES_DIR,
        LOG_DIR,
        BACKUP_DIR
    ]
    
    for directory in directories:
        os.makedirs(directory, exist_ok=True)

# �������w�Bkǣ���\
create_directories()