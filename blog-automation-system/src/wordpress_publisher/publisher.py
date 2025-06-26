import requests
import base64
from typing import Dict, List, Optional
from datetime import datetime
import json


class WordPressPublisher:
    """WordPress REST APIを使用して記事を投稿するクラス"""
    
    def __init__(self, site_url: str, username: str, app_password: str):
        self.site_url = site_url.rstrip('/')
        self.username = username
        self.app_password = app_password
        self.auth = self._create_auth()
        self.api_base = f"{self.site_url}/wp-json/wp/v2"
        
    def _create_auth(self) -> str:
        """Basic認証用のヘッダーを作成"""
        credentials = f"{self.username}:{self.app_password}"
        token = base64.b64encode(credentials.encode()).decode('utf-8')
        return f"Basic {token}"
    
    def publish_article(self, article_data: Dict[str, any]) -> Dict:
        """記事をWordPressに投稿"""
        
        # カテゴリーIDの取得または作成
        category_ids = self._get_or_create_categories(article_data.get('categories', []))
        
        # タグIDの取得または作成
        tag_ids = self._get_or_create_tags(article_data.get('tags', []))
        
        # アイキャッチ画像の取得（Unsplash API使用）
        featured_media_id = self._get_featured_image(article_data.get('keyword', ''))
        
        # 投稿データの準備
        post_data = {
            'title': article_data['title'],
            'content': self._format_content(article_data['content']),
            'status': 'publish',  # または'draft'で下書き保存
            'slug': article_data['slug'],
            'categories': category_ids,
            'tags': tag_ids,
            'meta': {
                'description': article_data.get('meta_description', '')
            }
        }
        
        if featured_media_id:
            post_data['featured_media'] = featured_media_id
        
        # 記事の投稿
        headers = {
            'Authorization': self.auth,
            'Content-Type': 'application/json'
        }
        
        response = requests.post(
            f"{self.api_base}/posts",
            headers=headers,
            json=post_data
        )
        
        if response.status_code == 201:
            post = response.json()
            return {
                'success': True,
                'post_id': post['id'],
                'post_url': post['link'],
                'message': '記事が正常に投稿されました'
            }
        else:
            return {
                'success': False,
                'error': response.text,
                'status_code': response.status_code,
                'message': '記事の投稿に失敗しました'
            }
    
    def _format_content(self, content: str) -> str:
        """記事内容をWordPress用にフォーマット"""
        # 段落をpタグで囲む
        paragraphs = content.split('\n\n')
        formatted_paragraphs = []
        
        for paragraph in paragraphs:
            paragraph = paragraph.strip()
            if paragraph:
                # 見出しの処理（簡易的な実装）
                if paragraph.startswith('## '):
                    formatted_paragraphs.append(f"<h2>{paragraph[3:]}</h2>")
                elif paragraph.startswith('### '):
                    formatted_paragraphs.append(f"<h3>{paragraph[4:]}</h3>")
                else:
                    formatted_paragraphs.append(f"<p>{paragraph}</p>")
        
        return '\n'.join(formatted_paragraphs)
    
    def _get_or_create_categories(self, category_names: List[str]) -> List[int]:
        """カテゴリー名からIDを取得、存在しない場合は作成"""
        category_ids = []
        
        headers = {'Authorization': self.auth}
        
        for name in category_names:
            # 既存のカテゴリーを検索
            response = requests.get(
                f"{self.api_base}/categories",
                headers=headers,
                params={'search': name}
            )
            
            if response.status_code == 200:
                categories = response.json()
                
                # 完全一致するカテゴリーを探す
                matching_category = None
                for cat in categories:
                    if cat['name'] == name:
                        matching_category = cat
                        break
                
                if matching_category:
                    category_ids.append(matching_category['id'])
                else:
                    # カテゴリーを新規作成
                    new_cat_response = requests.post(
                        f"{self.api_base}/categories",
                        headers={**headers, 'Content-Type': 'application/json'},
                        json={'name': name}
                    )
                    
                    if new_cat_response.status_code == 201:
                        new_category = new_cat_response.json()
                        category_ids.append(new_category['id'])
        
        return category_ids
    
    def _get_or_create_tags(self, tag_names: List[str]) -> List[int]:
        """タグ名からIDを取得、存在しない場合は作成"""
        tag_ids = []
        
        headers = {'Authorization': self.auth}
        
        for name in tag_names:
            # 既存のタグを検索
            response = requests.get(
                f"{self.api_base}/tags",
                headers=headers,
                params={'search': name}
            )
            
            if response.status_code == 200:
                tags = response.json()
                
                # 完全一致するタグを探す
                matching_tag = None
                for tag in tags:
                    if tag['name'] == name:
                        matching_tag = tag
                        break
                
                if matching_tag:
                    tag_ids.append(matching_tag['id'])
                else:
                    # タグを新規作成
                    new_tag_response = requests.post(
                        f"{self.api_base}/tags",
                        headers={**headers, 'Content-Type': 'application/json'},
                        json={'name': name}
                    )
                    
                    if new_tag_response.status_code == 201:
                        new_tag = new_tag_response.json()
                        tag_ids.append(new_tag['id'])
        
        return tag_ids
    
    def _get_featured_image(self, keyword: str) -> Optional[int]:
        """Unsplash APIを使用してアイキャッチ画像を取得し、WordPressにアップロード"""
        # 注意: Unsplash APIキーが必要です
        # ここでは簡易的な実装を示します
        
        # TODO: Unsplash APIからの画像取得とWordPressへのアップロード実装
        # 現時点ではNoneを返す
        return None
    
    def update_post(self, post_id: int, updates: Dict) -> Dict:
        """既存の投稿を更新"""
        headers = {
            'Authorization': self.auth,
            'Content-Type': 'application/json'
        }
        
        response = requests.post(
            f"{self.api_base}/posts/{post_id}",
            headers=headers,
            json=updates
        )
        
        if response.status_code == 200:
            return {
                'success': True,
                'message': '記事が更新されました'
            }
        else:
            return {
                'success': False,
                'error': response.text,
                'status_code': response.status_code
            }
    
    def get_post_analytics(self, post_id: int) -> Dict:
        """投稿のパフォーマンスデータを取得（要プラグイン）"""
        # 注意: Google AnalyticsやJetpack統計などのプラグインが必要
        # ここでは基本的な投稿情報のみを返す
        
        headers = {'Authorization': self.auth}
        response = requests.get(
            f"{self.api_base}/posts/{post_id}",
            headers=headers
        )
        
        if response.status_code == 200:
            post = response.json()
            return {
                'title': post['title']['rendered'],
                'url': post['link'],
                'date': post['date'],
                'modified': post['modified']
            }
        
        return {}
    
    def schedule_post(self, article_data: Dict, publish_date: datetime) -> Dict:
        """記事を指定日時に予約投稿"""
        article_data_copy = article_data.copy()
        
        # 投稿ステータスを'future'に設定
        post_data = {
            'title': article_data_copy['title'],
            'content': self._format_content(article_data_copy['content']),
            'status': 'future',
            'date': publish_date.isoformat(),
            'slug': article_data_copy['slug']
        }
        
        headers = {
            'Authorization': self.auth,
            'Content-Type': 'application/json'
        }
        
        response = requests.post(
            f"{self.api_base}/posts",
            headers=headers,
            json=post_data
        )
        
        if response.status_code == 201:
            post = response.json()
            return {
                'success': True,
                'post_id': post['id'],
                'scheduled_date': publish_date.isoformat(),
                'message': f'記事が{publish_date}に予約投稿されました'
            }
        else:
            return {
                'success': False,
                'error': response.text,
                'status_code': response.status_code
            }