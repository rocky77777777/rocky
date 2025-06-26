# ブログ自動化システム

須崎純一氏の文体を学習し、ロングテールキーワードを狙ったSEO最適化記事を自動生成してWordPressに投稿するシステムです。

## 機能

- 📝 過去記事から文体特徴を自動抽出
- 🔍 ロングテールキーワードの自動発見
- ✍️ Claude APIを使用した高品質な記事生成
- 🚀 WordPress REST APIによる自動投稿
- 📊 SEO最適化（タイトル、メタディスクリプション、キーワード密度）
- ⏰ スケジュール投稿機能

## セットアップ

### 1. 必要な環境

- Python 3.8以上
- MeCab（日本語形態素解析用）
- WordPress（REST APIとアプリケーションパスワード有効化）

### 2. インストール

```bash
# リポジトリのクローン
git clone https://github.com/yourusername/blog-automation-system.git
cd blog-automation-system

# MeCabのインストール（Mac）
brew install mecab mecab-ipadic

# MeCabのインストール（Ubuntu/Debian）
sudo apt-get install mecab libmecab-dev mecab-ipadic-utf8

# Pythonパッケージのインストール
pip install -r requirements.txt
```

### 3. 設定

1. `.env.example`を`.env`にコピー：
```bash
cp .env.example .env
```

2. `.env`ファイルを編集して必要な情報を設定：
```env
WORDPRESS_URL=https://your-site.com
WORDPRESS_USERNAME=your-username
WORDPRESS_APP_PASSWORD=your-app-password
CLAUDE_API_KEY=your-claude-api-key
```

3. WordPressでアプリケーションパスワードを生成：
   - WordPress管理画面 → ユーザー → プロフィール
   - 「アプリケーションパスワード」セクションで新規生成

### 4. 過去記事の準備

須崎純一氏の過去記事を`data/past_articles/`ディレクトリに`.txt`形式で配置してください。

```bash
# 例
data/past_articles/article1.txt
data/past_articles/article2.txt
data/past_articles/article3.txt
```

## 使用方法

### 基本的な使い方

1. **文体分析**（最初に実行）：
```bash
python src/main.py --analyze-style
```

2. **キーワード生成**：
```bash
python src/main.py --generate-keywords
# または特定のシードキーワードから
python src/main.py --generate-keywords --seed "AI活用"
```

3. **記事生成と投稿**：
```bash
python src/main.py --create-articles --count 5
```

4. **すべてを自動実行**：
```bash
python src/main.py --full-run
```

### スケジュール実行

cronを使用して定期実行：
```bash
# crontabに追加（毎日9時と15時に実行）
0 9,15 * * * cd /path/to/blog-automation-system && python src/main.py --scheduled
```

## ディレクトリ構造

```
blog-automation-system/
├── src/
│   ├── style_analyzer/      # 文体分析モジュール
│   ├── keyword_research/    # キーワードリサーチ
│   ├── content_generator/   # 記事生成
│   ├── wordpress_publisher/ # WordPress投稿
│   └── main.py             # メインスクリプト
├── data/
│   ├── past_articles/      # 過去記事
│   ├── keywords/           # キーワードリスト
│   └── templates/          # テンプレート
├── config/
│   └── settings.py         # 設定ファイル
├── logs/                   # ログファイル
├── backups/                # バックアップ
└── requirements.txt        # 依存関係
```

## カスタマイズ

### 記事の長さを変更

`config/settings.py`で調整：
```python
ARTICLE_MIN_LENGTH = 2000  # 最小文字数
ARTICLE_MAX_LENGTH = 4000  # 最大文字数
```

### キーワードの条件を変更

```python
KEYWORD_MIN_SEARCH_VOLUME = 100   # 最小検索ボリューム
KEYWORD_MAX_SEARCH_VOLUME = 1000  # 最大検索ボリューム
KEYWORD_MAX_COMPETITION = 0.5     # 最大競合度
```

### 投稿スケジュールを変更

```python
POSTING_SCHEDULE = {
    'monday': ['09:00', '15:00'],
    'tuesday': ['09:00', '15:00'],
    # ...
}
```

## トラブルシューティング

### MeCabエラー

```bash
# 辞書パスを確認
echo `mecab-config --dicdir`"/mecab-ipadic-neologd"
```

### WordPress投稿エラー

1. REST APIが有効か確認
2. パーマリンク設定を確認
3. アプリケーションパスワードを再生成

### 文字化け

すべてのファイルがUTF-8エンコーディングであることを確認してください。

## 注意事項

- APIの利用制限に注意してください
- 生成された記事は必ず人間がレビューすることを推奨します
- SEOのためには定期的なパフォーマンス分析が重要です

## ライセンス

MIT License