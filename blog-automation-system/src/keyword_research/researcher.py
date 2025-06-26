import requests
import json
from typing import List, Dict, Tuple
from datetime import datetime
import time


class KeywordResearcher:
    """ロングテールキーワードを収集・分析するクラス"""
    
    def __init__(self, google_api_key: str = None, ubersuggest_api_key: str = None):
        self.google_api_key = google_api_key
        self.ubersuggest_api_key = ubersuggest_api_key
        self.keywords_cache = {}
        
    def find_longtail_keywords(self, 
                              seed_keyword: str, 
                              min_volume: int = 100,
                              max_volume: int = 1000) -> List[Dict]:
        """シードキーワードからロングテールキーワードを発見"""
        
        keywords = []
        
        # 1. Google Suggest APIから関連キーワードを取得
        suggestions = self._get_google_suggestions(seed_keyword)
        
        # 2. キーワードの拡張（前後に修飾語を追加）
        expanded_keywords = self._expand_keywords(seed_keyword)
        
        # 3. すべての候補キーワードを統合
        all_candidates = list(set(suggestions + expanded_keywords + [seed_keyword]))
        
        # 4. 各キーワードの検索ボリュームと競合度を評価
        for keyword in all_candidates:
            keyword_data = self._analyze_keyword(keyword)
            
            # ロングテールキーワードの条件を満たすものを選択
            if (keyword_data['search_volume'] >= min_volume and 
                keyword_data['search_volume'] <= max_volume and
                keyword_data['competition'] <= 0.5):  # 競合度が低い
                
                keywords.append({
                    'keyword': keyword,
                    'search_volume': keyword_data['search_volume'],
                    'competition': keyword_data['competition'],
                    'cpc': keyword_data.get('cpc', 0),
                    'trend': keyword_data.get('trend', 'stable'),
                    'intent': self._determine_search_intent(keyword),
                    'content_ideas': self._generate_content_ideas(keyword)
                })
        
        # 検索ボリュームで降順ソート
        keywords.sort(key=lambda x: x['search_volume'], reverse=True)
        
        return keywords[:20]  # 上位20個を返す
    
    def _get_google_suggestions(self, keyword: str) -> List[str]:
        """Google Suggest APIから関連キーワードを取得"""
        suggestions = []
        
        # Google Suggest APIのエンドポイント
        url = "http://suggestqueries.google.com/complete/search"
        params = {
            'client': 'firefox',
            'q': keyword,
            'hl': 'ja'  # 日本語
        }
        
        try:
            response = requests.get(url, params=params)
            if response.status_code == 200:
                data = response.json()
                if len(data) > 1:
                    suggestions = data[1]  # サジェストのリスト
        except Exception as e:
            print(f"Google Suggest API error: {e}")
        
        return suggestions
    
    def _expand_keywords(self, seed_keyword: str) -> List[str]:
        """キーワードを拡張（修飾語を追加）"""
        expanded = []
        
        # 前置詞
        prefixes = [
            '初心者', '簡単', '無料', '最新', '2024年',
            'おすすめ', '人気', '効果的な', '失敗しない',
            '成功する', 'プロが教える', '完全ガイド'
        ]
        
        # 後置詞
        suffixes = [
            'とは', '方法', 'やり方', 'コツ', '比較',
            'ランキング', '選び方', '使い方', '始め方',
            'メリット', 'デメリット', '注意点', '手順'
        ]
        
        # 質問形式
        questions = [
            f'{seed_keyword}はどうやって',
            f'{seed_keyword}は何',
            f'{seed_keyword}をする理由',
            f'{seed_keyword}の効果',
            f'{seed_keyword}で失敗しない方法'
        ]
        
        # 組み合わせを生成
        for prefix in prefixes:
            expanded.append(f"{prefix} {seed_keyword}")
            
        for suffix in suffixes:
            expanded.append(f"{seed_keyword} {suffix}")
            
        expanded.extend(questions)
        
        return expanded
    
    def _analyze_keyword(self, keyword: str) -> Dict:
        """キーワードの詳細分析（検索ボリューム、競合度など）"""
        
        # キャッシュチェック
        if keyword in self.keywords_cache:
            return self.keywords_cache[keyword]
        
        # 実際のAPIを使用する場合はここで実装
        # 現在はモックデータを返す
        import random
        
        mock_data = {
            'search_volume': random.randint(50, 2000),
            'competition': round(random.random(), 2),
            'cpc': round(random.uniform(10, 500), 2),
            'trend': random.choice(['rising', 'stable', 'declining']),
            'difficulty': random.randint(1, 100)
        }
        
        # キャッシュに保存
        self.keywords_cache[keyword] = mock_data
        
        return mock_data
    
    def _determine_search_intent(self, keyword: str) -> str:
        """検索意図を判定"""
        
        # インフォメーショナル（情報収集）
        info_patterns = ['とは', '方法', 'やり方', '意味', '違い', '比較']
        
        # トランザクショナル（購買・行動）
        trans_patterns = ['購入', '買う', '申込', '予約', 'ダウンロード', '登録']
        
        # ナビゲーショナル（特定サイトへの移動）
        nav_patterns = ['公式', 'ログイン', 'サイト', 'ホームページ']
        
        # コマーシャル（商業的調査）
        comm_patterns = ['おすすめ', 'ランキング', '比較', 'レビュー', '口コミ', '評判']
        
        keyword_lower = keyword.lower()
        
        if any(pattern in keyword_lower for pattern in info_patterns):
            return 'informational'
        elif any(pattern in keyword_lower for pattern in trans_patterns):
            return 'transactional'
        elif any(pattern in keyword_lower for pattern in nav_patterns):
            return 'navigational'
        elif any(pattern in keyword_lower for pattern in comm_patterns):
            return 'commercial'
        else:
            return 'informational'  # デフォルト
    
    def _generate_content_ideas(self, keyword: str) -> List[str]:
        """キーワードに基づくコンテンツアイデアを生成"""
        intent = self._determine_search_intent(keyword)
        ideas = []
        
        if intent == 'informational':
            ideas = [
                f"{keyword}の基本を徹底解説",
                f"{keyword}について知っておくべき10のこと",
                f"初心者でもわかる{keyword}入門ガイド",
                f"{keyword}の真実：専門家が語る本当の話"
            ]
        elif intent == 'commercial':
            ideas = [
                f"【2024年版】{keyword}のおすすめTOP10",
                f"{keyword}を徹底比較！あなたに最適なのはどれ？",
                f"{keyword}の選び方：失敗しない5つのポイント",
                f"プロが選ぶ{keyword}ベスト3"
            ]
        elif intent == 'transactional':
            ideas = [
                f"{keyword}の手順を画像付きで解説",
                f"{keyword}で失敗しないための完全ガイド",
                f"今すぐできる{keyword}の方法",
                f"{keyword}のメリット・デメリットまとめ"
            ]
        
        return ideas[:3]  # 上位3つのアイデアを返す
    
    def analyze_competitors(self, keyword: str) -> List[Dict]:
        """競合サイトの分析"""
        # 実際の実装では、検索結果の上位サイトを分析
        # ここではモックデータを返す
        
        competitors = [
            {
                'url': 'https://example1.com/article',
                'title': f'{keyword}について詳しく解説',
                'word_count': 3500,
                'headings_count': 12,
                'images_count': 5,
                'ranking_position': 1
            },
            {
                'url': 'https://example2.com/guide',
                'title': f'{keyword}の完全ガイド',
                'word_count': 4200,
                'headings_count': 15,
                'images_count': 8,
                'ranking_position': 2
            }
        ]
        
        return competitors
    
    def get_trending_topics(self, category: str = None) -> List[Dict]:
        """トレンドトピックを取得"""
        # Google Trends APIやSNS APIを使用して実装
        # ここではモックデータを返す
        
        trending = [
            {
                'topic': 'AI活用術',
                'growth_rate': 150,
                'search_volume': 850,
                'category': 'テクノロジー'
            },
            {
                'topic': 'リモートワーク効率化',
                'growth_rate': 120,
                'search_volume': 620,
                'category': 'ビジネス'
            }
        ]
        
        if category:
            trending = [t for t in trending if t['category'] == category]
            
        return trending
    
    def save_keywords(self, keywords: List[Dict], filepath: str):
        """キーワードリストを保存"""
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump({
                'generated_at': datetime.now().isoformat(),
                'keywords': keywords
            }, f, ensure_ascii=False, indent=2)
    
    def load_keywords(self, filepath: str) -> List[Dict]:
        """保存されたキーワードリストを読み込み"""
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
            return data['keywords']