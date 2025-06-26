import os
import json
from typing import Dict, List, Optional
from anthropic import Anthropic
from datetime import datetime


class ContentGenerator:
    """須崎純一氏の文体でブログ記事を生成するクラス"""
    
    def __init__(self, api_key: str, style_profile_path: str):
        self.client = Anthropic(api_key=api_key)
        self.style_profile = self._load_style_profile(style_profile_path)
        
    def _load_style_profile(self, profile_path: str) -> Dict:
        """文体プロファイルを読み込み"""
        if os.path.exists(profile_path):
            with open(profile_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        else:
            raise FileNotFoundError(f"文体プロファイルが見つかりません: {profile_path}")
    
    def generate_article(self, 
                        keyword: str, 
                        related_keywords: List[str],
                        word_count: int = 3000) -> Dict[str, str]:
        """キーワードに基づいて記事を生成"""
        
        # 文体特徴の要約を作成
        style_summary = self._create_style_summary()
        
        # プロンプトの作成
        prompt = self._create_generation_prompt(
            keyword, 
            related_keywords, 
            word_count, 
            style_summary
        )
        
        # Claude APIで記事生成
        response = self.client.messages.create(
            model="claude-3-opus-20240229",
            max_tokens=8000,
            temperature=0.7,
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )
        
        # 生成された記事を構造化
        article_content = response.content[0].text
        return self._structure_article(article_content, keyword)
    
    def _create_style_summary(self) -> str:
        """文体プロファイルから特徴的な要素を要約"""
        profile = self.style_profile
        
        # 頻出フレーズの上位10個を抽出
        common_phrases = [phrase for phrase, _ in profile.get('common_phrases', [])[:10]]
        
        # 接続詞・副詞の使用傾向
        transition_words = [word for word, _ in profile.get('transition_words', [])[:10]]
        
        # 文章の長さの特徴
        avg_length = profile.get('average_sentence_length', 50)
        
        style_summary = f"""
文体の特徴:
- 平均文長: 約{int(avg_length)}文字
- よく使うフレーズ: {', '.join(common_phrases)}
- 特徴的な接続詞・副詞: {', '.join(transition_words)}
- 句読点の使用: 読点を適度に使い、リズミカルな文章
- 開始パターン: 読者への問いかけや共感から始めることが多い
- 終了パターン: 行動を促すメッセージで締めくくる
"""
        return style_summary
    
    def _create_generation_prompt(self, 
                                keyword: str, 
                                related_keywords: List[str],
                                word_count: int,
                                style_summary: str) -> str:
        """記事生成用のプロンプトを作成"""
        
        prompt = f"""あなたは須崎純一です。以下の特徴を持つ文体で記事を書いてください。

{style_summary}

メインキーワード: {keyword}
関連キーワード: {', '.join(related_keywords)}

以下の構成で約{word_count}文字の記事を書いてください：

1. 導入（約{int(word_count * 0.15)}文字）
   - 読者の共感を得る問いかけや状況描写から始める
   - なぜこのトピックが重要なのかを明確にする

2. 問題提起（約{int(word_count * 0.2)}文字）
   - 読者が抱えている具体的な課題や悩みを掘り下げる
   - 統計データや事例を交えて説得力を持たせる

3. 解決策の提示（約{int(word_count * 0.35)}文字）
   - 須崎純一独自の視点から解決策を提案
   - 実践的で具体的なアドバイスを含める
   - 専門知識を分かりやすく解説

4. 具体例・ケーススタディ（約{int(word_count * 0.2)}文字）
   - 実際の成功事例や失敗事例を紹介
   - 読者が自分事として捉えられるような例を選ぶ

5. まとめとCTA（約{int(word_count * 0.1)}文字）
   - 要点を簡潔にまとめる
   - 読者に次のアクションを促す
   - 希望を持てるメッセージで締めくくる

記事を書く際の注意点：
- 専門用語は必要最小限に留め、使う場合は分かりやすく説明する
- 読者との対話を意識し、「あなた」という呼びかけを適度に使う
- 具体的な数字や事例を織り交ぜて説得力を高める
- 段落は3-4文程度でまとめ、読みやすさを重視する
- メインキーワードは自然に3-5回、関連キーワードは各1-2回使用する

では、記事を書いてください。"""
        
        return prompt
    
    def _structure_article(self, content: str, keyword: str) -> Dict[str, str]:
        """生成された記事を構造化"""
        # タイトルの生成
        title = self._generate_seo_title(keyword, content)
        
        # メタディスクリプションの生成
        meta_description = self._generate_meta_description(content)
        
        # カテゴリーとタグの推定
        categories, tags = self._extract_categories_and_tags(keyword, content)
        
        return {
            'title': title,
            'content': content,
            'meta_description': meta_description,
            'categories': categories,
            'tags': tags,
            'slug': self._generate_slug(keyword),
            'created_at': datetime.now().isoformat()
        }
    
    def _generate_seo_title(self, keyword: str, content: str) -> str:
        """SEOに最適化されたタイトルを生成"""
        # 簡易的な実装：キーワードを含む最初の見出しを抽出
        lines = content.split('\n')
        for line in lines[:10]:  # 最初の10行から探す
            if keyword in line and len(line) < 60:
                return line.strip()
        
        # 見つからない場合はデフォルト
        return f"{keyword}について知っておくべき重要なポイント"
    
    def _generate_meta_description(self, content: str) -> str:
        """メタディスクリプションを生成（150-160文字）"""
        # 最初の段落から抽出
        first_paragraph = content.split('\n\n')[0]
        if len(first_paragraph) > 160:
            return first_paragraph[:157] + "..."
        return first_paragraph
    
    def _extract_categories_and_tags(self, keyword: str, content: str) -> tuple:
        """記事内容からカテゴリーとタグを推定"""
        # 簡易的な実装：キーワードベースでカテゴリーを推定
        categories = []
        tags = [keyword]
        
        # ビジネス関連のキーワード
        if any(word in content for word in ['ビジネス', '経営', '起業', 'マーケティング']):
            categories.append('ビジネス')
            
        # テクノロジー関連
        if any(word in content for word in ['AI', 'デジタル', 'テクノロジー', 'IT']):
            categories.append('テクノロジー')
            
        # ライフスタイル関連
        if any(word in content for word in ['生活', 'ライフスタイル', '健康', 'ウェルビーイング']):
            categories.append('ライフスタイル')
        
        # デフォルトカテゴリー
        if not categories:
            categories.append('一般')
            
        return categories, tags
    
    def _generate_slug(self, keyword: str) -> str:
        """URLスラッグを生成"""
        # 日本語をローマ字に変換する簡易的な実装
        # 実際の実装では、より高度な変換ライブラリを使用することを推奨
        import re
        
        # 英数字のみを抽出
        slug = re.sub(r'[^a-zA-Z0-9\s-]', '', keyword)
        slug = slug.strip().lower()
        slug = re.sub(r'\s+', '-', slug)
        
        # 空の場合はタイムスタンプを使用
        if not slug:
            slug = f"article-{datetime.now().strftime('%Y%m%d%H%M%S')}"
            
        return slug