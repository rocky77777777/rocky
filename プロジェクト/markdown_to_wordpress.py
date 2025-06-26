#!/usr/bin/env python3
import requests
import json
import sys
import os
from pathlib import Path

# WordPress設定（環境変数または直接設定）
WP_URL = "https://あなたのサイト.com"  # あなたのWordPressサイトURL
WP_USER = "あなたのユーザー名"         # WordPressユーザー名
WP_APP_PASSWORD = "xxxx xxxx xxxx xxxx xxxx xxxx"  # アプリケーションパスワード（スペース削除）

def markdown_to_html(markdown_content):
    """簡単なMarkdown→HTML変換（必要に応じて拡張）"""
    import re
    
    # 見出しの変換
    content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', markdown_content, flags=re.MULTILINE)
    content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', content, flags=re.MULTILINE)
    content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', content, flags=re.MULTILINE)
    
    # 強調の変換
    content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', content)
    content = re.sub(r'\*(.+?)\*', r'<em>\1</em>', content)
    
    # リンクの変換
    content = re.sub(r'\[(.+?)\]\((.+?)\)', r'<a href="\2">\1</a>', content)
    
    # リストの変換
    content = re.sub(r'^- (.+)$', r'<li>\1</li>', content, flags=re.MULTILINE)
    content = re.sub(r'(<li>.*</li>\n)+', lambda m: '<ul>\n' + m.group(0) + '</ul>\n', content)
    
    # コードブロックの変換
    content = re.sub(r'```(\w+)?\n(.*?)\n```', r'<pre><code>\2</code></pre>', content, flags=re.DOTALL)
    content = re.sub(r'`(.+?)`', r'<code>\1</code>', content)
    
    # 段落の変換
    paragraphs = content.split('\n\n')
    content = '\n'.join([f'<p>{p}</p>' if not p.startswith('<') else p for p in paragraphs if p.strip()])
    
    return content

def post_to_wordpress(title, content, status='draft'):
    """WordPressに記事を投稿"""
    
    # REST APIエンドポイント
    api_url = f"{WP_URL}/wp-json/wp/v2/posts"
    
    # 認証情報
    auth = (WP_USER, WP_APP_PASSWORD.replace(' ', ''))
    
    # 投稿データ
    post_data = {
        'title': title,
        'content': content,
        'status': status,  # 'draft' または 'publish'
        'format': 'standard',
    }
    
    # 投稿リクエスト
    response = requests.post(
        api_url,
        auth=auth,
        json=post_data,
        headers={'Content-Type': 'application/json'}
    )
    
    if response.status_code == 201:
        post_info = response.json()
        print(f"✅ 投稿成功！")
        print(f"   タイトル: {title}")
        print(f"   URL: {post_info['link']}")
        print(f"   状態: {status}")
        return True
    else:
        print(f"❌ エラー: {response.status_code}")
        print(f"   詳細: {response.text}")
        return False

def main():
    """メイン処理"""
    if len(sys.argv) < 2:
        print("使い方: python markdown_to_wordpress.py [Markdownファイル]")
        sys.exit(1)
    
    # Markdownファイルを読み込み
    md_file = Path(sys.argv[1])
    if not md_file.exists():
        print(f"❌ ファイルが見つかりません: {md_file}")
        sys.exit(1)
    
    with open(md_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # タイトルを抽出（最初の#行）
    lines = content.split('\n')
    title = "無題"
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break
    
    # HTMLに変換
    html_content = markdown_to_html(content)
    
    # 下書きか公開か確認
    print(f"\n📝 投稿する記事: {title}")
    print("投稿方法を選択してください:")
    print("1. 下書きとして保存")
    print("2. すぐに公開")
    choice = input("選択 (1/2): ")
    
    status = 'publish' if choice == '2' else 'draft'
    
    # WordPressに投稿
    post_to_wordpress(title, html_content, status)

if __name__ == "__main__":
    main()