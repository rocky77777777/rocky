#!/usr/bin/env python3
import sys
import os
import argparse
import logging
from datetime import datetime
import json

# ������n���ǣ���Pythonѹk��
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from config import settings
from src.style_analyzer.analyzer import StyleAnalyzer
from src.keyword_research.researcher import KeywordResearcher
from src.content_generator.generator import ContentGenerator
from src.wordpress_publisher.publisher import WordPressPublisher


class BlogAutomationSystem:
    """���������n���"""
    
    def __init__(self):
        self._setup_logging()
        self.logger = logging.getLogger(__name__)
        
    def _setup_logging(self):
        """���n-�"""
        logging.basicConfig(
            level=getattr(logging, settings.LOG_LEVEL),
            format=settings.LOG_FORMAT,
            handlers=[
                logging.FileHandler(
                    os.path.join(settings.LOG_DIR, f'blog_automation_{datetime.now().strftime("%Y%m%d")}.log')
                ),
                logging.StreamHandler()
            ]
        )
    
    def analyze_writing_style(self):
        """N��K��S��"""
        self.logger.info("�S����W~Y...")
        
        analyzer = StyleAnalyzer()
        
        # N��LX(Y�K��ï
        if not os.listdir(settings.PAST_ARTICLES_DIR):
            self.logger.error(f"N��L�dK�~[�: {settings.PAST_ARTICLES_DIR}")
            print(f"\nN��� {settings.PAST_ARTICLES_DIR} kMnWfO`UD")
            return False
        
        # �S�n�L
        style_profile = analyzer.analyze_articles(settings.PAST_ARTICLES_DIR)
        
        # ��ա��n�X
        analyzer.save_profile(style_profile, settings.STYLE_PROFILE_PATH)
        
        self.logger.info(f"�S�L��W~W_��ա���X: {settings.STYLE_PROFILE_PATH}")
        print("\n�S�L��W~W_")
        print(f"- sG�w: {style_profile['average_sentence_length']:.1f}�W")
        print(f"- �Yp: {style_profile['vocabulary_size']}")
        print(f"- ;�����p: {len(style_profile['common_phrases'])}")
        
        return True
    
    def generate_keywords(self, seed_keyword: str = None):
        """��������ɒ"""
        self.logger.info("��������W~Y...")
        
        researcher = KeywordResearcher(
            google_api_key=settings.GOOGLE_API_KEY,
            ubersuggest_api_key=None
        )
        
        # ��ɭ����L�U�fDjD4o����K�֗
        if not seed_keyword:
            trending = researcher.get_trending_topics()
            if trending:
                seed_keyword = trending[0]['topic']
            else:
                seed_keyword = "Ӹ͹��"
        
        # ���������nz�
        keywords = researcher.find_longtail_keywords(
            seed_keyword,
            min_volume=settings.KEYWORD_MIN_SEARCH_VOLUME,
            max_volume=settings.KEYWORD_MAX_SEARCH_VOLUME
        )
        
        # �����n�X
        keywords_file = os.path.join(
            settings.KEYWORDS_DIR,
            f'keywords_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        )
        researcher.save_keywords(keywords, keywords_file)
        
        self.logger.info(f"{len(keywords)}n����ɒW~W_: {keywords_file}")
        print(f"\n{len(keywords)}n��������ɒz�W~W_")
        
        # 
M5�h:
        for i, kw in enumerate(keywords[:5], 1):
            print(f"{i}. {kw['keyword']} ("�: {kw['search_volume']}, ��: {kw['competition']})")
        
        return keywords
    
    def create_articles(self, count: int = 1):
        """��WfWordPressk�?"""
        self.logger.info(f"{count}n����W~Y...")
        
        # Łj�������n
        if not os.path.exists(settings.STYLE_PROFILE_PATH):
            self.logger.error("�S��ա��L�dK�~[�Hk --analyze-style ��LWfO`UD")
            return
        
        generator = ContentGenerator(
            api_key=settings.CLAUDE_API_KEY,
            style_profile_path=settings.STYLE_PROFILE_PATH
        )
        
        publisher = WordPressPublisher(
            site_url=settings.WORDPRESS_URL,
            username=settings.WORDPRESS_USERNAME,
            app_password=settings.WORDPRESS_APP_PASSWORD
        )
        
        #  �n�����ա��֗
        keyword_files = sorted([
            f for f in os.listdir(settings.KEYWORDS_DIR) 
            if f.endswith('.json')
        ], reverse=True)
        
        if not keyword_files:
            self.logger.error("�����ա��L�dK�~[�Hk --generate-keywords ��LWfO`UD")
            return
        
        researcher = KeywordResearcher()
        keywords = researcher.load_keywords(
            os.path.join(settings.KEYWORDS_DIR, keyword_files[0])
        )
        
        # �pn��
        successful_posts = 0
        for i in range(min(count, len(keywords))):
            keyword_data = keywords[i]
            
            try:
                self.logger.info(f"�- ({i+1}/{count}): {keyword_data['keyword']}")
                
                # �
                article = generator.generate_article(
                    keyword=keyword_data['keyword'],
                    related_keywords=keyword_data.get('tags', []),
                    word_count=settings.ARTICLE_MIN_LENGTH
                )
                
                # �n����ï
                if settings.QUALITY_CHECK_ENABLED:
                    if not self._check_article_quality(article):
                        self.logger.warning(f"����ïk1W: {keyword_data['keyword']}")
                        continue
                
                # WordPressk�?
                result = publisher.publish_article(article)
                
                if result['success']:
                    successful_posts += 1
                    self.logger.info(f"�?�: {result['post_url']}")
                    print(f"\n �?�: {article['title']}")
                    print(f"  URL: {result['post_url']}")
                else:
                    self.logger.error(f"�?1W: {result['error']}")
                    print(f"\n �?1W: {article['title']}")
                
            except Exception as e:
                self.logger.error(f"����: {str(e)}")
                print(f"\n ���: {keyword_data['keyword']} - {str(e)}")
        
        print(f"\n��: {successful_posts}/{count} ���?W~W_")
    
    def _check_article_quality(self, article: dict) -> bool:
        """�n����ï"""
        content = article['content']
        
        # �Wp��ï
        if len(content) < settings.ARTICLE_MIN_LENGTH:
            return False
        
        # �����Ʀ��ï
        keyword = article.get('keyword', '')
        if keyword:
            keyword_count = content.lower().count(keyword.lower())
            keyword_density = keyword_count / len(content.split())
            if keyword_density > settings.MAX_KEYWORD_DENSITY:
                return False
        
        return True
    
    def run_scheduled_posts(self):
        """������k�cf���?"""
        current_time = datetime.now()
        current_day = current_time.strftime('%A').lower()
        current_hour = current_time.strftime('%H:%M')
        
        # ,�n�?B����ï
        if current_day in settings.POSTING_SCHEDULE:
            scheduled_times = settings.POSTING_SCHEDULE[current_day]
            
            for scheduled_time in scheduled_times:
                # �(B;L�?B�n�5�j��?
                if abs((datetime.strptime(current_hour, '%H:%M') - 
                       datetime.strptime(scheduled_time, '%H:%M')).seconds) < 300:
                    self.logger.info(f"������?��L: {scheduled_time}")
                    self.create_articles(count=1)


def main():
    """��p"""
    parser = argparse.ArgumentParser(
        description=' ���������',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
(�:
  # �S�n�L
  python src/main.py --analyze-style
  
  # �����
  python src/main.py --generate-keywords
  python src/main.py --generate-keywords --seed "AI;("
  
  # �h�?
  python src/main.py --create-articles --count 5
  
  # Yyf�jk�L
  python src/main.py --full-run
        """
    )
    
    parser.add_argument('--analyze-style', action='store_true',
                       help='N��K��S��')
    parser.add_argument('--generate-keywords', action='store_true',
                       help='��������ɒ')
    parser.add_argument('--seed', type=str,
                       help='�����n��ɭ����')
    parser.add_argument('--create-articles', action='store_true',
                       help='��Wf�?')
    parser.add_argument('--count', type=int, default=1,
                       help='Y��p�թ��: 1	')
    parser.add_argument('--scheduled', action='store_true',
                       help='������?��L')
    parser.add_argument('--full-run', action='store_true',
                       help='Yyfn��jk�L')
    
    args = parser.parse_args()
    
    # pLU��U�fDjD4o��גh:
    if not any(vars(args).values()):
        parser.print_help()
        return
    
    # ����n
    system = BlogAutomationSystem()
    
    # ����
    if args.full_run:
        print("=== ��������� ����� ===\n")
        
        # 1. �S�
        if system.analyze_writing_style():
            # 2. �����
            keywords = system.generate_keywords(args.seed)
            
            if keywords:
                # 3. �
                system.create_articles(count=args.count)
        
        print("\n=== ���� ===")
        return
    
    # %�L
    if args.analyze_style:
        system.analyze_writing_style()
    
    if args.generate_keywords:
        system.generate_keywords(args.seed)
    
    if args.create_articles:
        system.create_articles(count=args.count)
    
    if args.scheduled:
        system.run_scheduled_posts()


if __name__ == '__main__':
    main()