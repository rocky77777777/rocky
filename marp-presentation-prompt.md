# Marpプレゼンテーション作成プロンプト

以下の形式で、16:9のMarpプレゼンテーションを作成してください：

## 基本設定
```yaml
---
marp: true
theme: default
paginate: false
size: 16:9
backgroundColor: #fff
style: |
  section {
    font-family: 'Hiragino Sans', 'Meiryo', sans-serif;
    padding: 60px 80px;
    display: flex;
    flex-direction: column;
    justify-content: center;
  }
  h1 {
    color: #2563eb;
    font-size: 2rem;
    margin-bottom: 0.5em;
  }
  h2 {
    color: #1e40af;
    font-size: 1.6rem;
    margin-bottom: 0.5em;
  }
  h3 {
    color: #3730a3;
    font-size: 1.2rem;
    margin-bottom: 0.3em;
  }
  strong {
    color: #dc2626;
  }
  li {
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 0.2em;
  }
  ul, ol {
    margin-top: 0.5em;
    margin-bottom: 0.5em;
  }
---
```

## スライド作成ルール

### 1. 表紙スライド
- `<!-- _class: lead -->` を使用
- タイトルは大きく中央配置
- 視覚的なアイコン（絵文字）を効果的に使用
- インラインスタイルで装飾

例：
```markdown
<!-- _class: lead -->

<div style="text-align: center; padding: 2em 0;">
  <h1 style="font-size: 3.5rem; color: #1e40af; margin-bottom: 0.3em; line-height: 1.2;">
    メインタイトル<br>
    サブタイトル
  </h1>
  
  <div style="margin: 3em 0;">
    <div style="font-size: 5em;">🚀</div>
    <h2 style="font-size: 2.5rem; color: #2563eb; margin: 0.5em 0;">キーメッセージ</h2>
    <p style="font-size: 1.3rem; color: #6b7280;">説明文</p>
  </div>
</div>
```

### 2. インフォビジュアルの活用

#### プログレスフロー
```markdown
<div style="display: flex; justify-content: space-around; align-items: center; margin: 2em 0;">
  <div style="text-align: center;">
    <div style="font-size: 3em; color: #3b82f6;">30%</div>
    <div style="font-size: 0.9em;">初期段階</div>
  </div>
  <div style="font-size: 2em;">→</div>
  <div style="text-align: center;">
    <div style="font-size: 3em; color: #10b981;">60%</div>
    <div style="font-size: 0.9em;">中間段階</div>
  </div>
  <div style="font-size: 2em;">→</div>
  <div style="text-align: center;">
    <div style="font-size: 3em; color: #f59e0b;">100%</div>
    <div style="font-size: 0.9em;">完成</div>
  </div>
</div>
```

#### アイコングリッド
```markdown
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 1em; margin: 1em 0;">
  <div style="background: #dbeafe; padding: 1em; border-radius: 8px; text-align: center;">
    <div style="font-size: 2em;">⚡</div>
    <div style="font-weight: bold;">速度優先</div>
  </div>
  <div style="background: #dcfce7; padding: 1em; border-radius: 8px; text-align: center;">
    <div style="font-size: 2em;">📋</div>
    <div style="font-weight: bold;">テンプレート活用</div>
  </div>
  <div style="background: #fef3c7; padding: 1em; border-radius: 8px; text-align: center;">
    <div style="font-size: 2em;">📊</div>
    <div style="font-weight: bold;">データドリブン</div>
  </div>
</div>
```

#### ステップフロー
```markdown
<div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin: 1em 0;">
  <div style="text-align: center; margin: 0.5em;">
    <div style="background: #dbeafe; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; margin: 0 auto;">
      <span style="font-size: 1.5em;">📝</span>
    </div>
    <div style="font-size: 0.9em; margin-top: 0.5em;">ステップ1</div>
  </div>
  <!-- 他のステップも同様 -->
</div>
```

### 3. 色の使い分け
- **青系 (#3b82f6, #dbeafe)**: メイン、重要な情報
- **緑系 (#10b981, #dcfce7)**: 成功、達成
- **黄系 (#f59e0b, #fef3c7)**: 注意、ポイント
- **赤系 (#dc2626, #fee2e2)**: 強調、警告
- **紫系 (#3730a3, #e0e7ff)**: サブ情報

### 4. レイアウトパターン

#### 左右分割
```markdown
<div style="display: flex; justify-content: space-between; align-items: flex-start; margin: 1em 0;">
  <div style="flex: 1;">
    <!-- 左側コンテンツ -->
  </div>
  <div style="text-align: center; margin: 0 2em;">
    <!-- 中央のビジュアル -->
  </div>
</div>
```

#### ボックス強調
```markdown
<div style="background: #f0f9ff; padding: 1em; border-radius: 8px; margin-bottom: 1em;">
  <div style="font-weight: bold; margin-bottom: 0.5em;">🤖 タイトル</div>
  <ul style="margin: 0; font-size: 0.9em;">
    <li>項目1</li>
    <li>項目2</li>
  </ul>
</div>
```

### 5. その他のポイント
- 各スライドは情報を詰め込みすぎない
- 見出しは階層を明確に（h2→h3）
- 視覚的な要素（絵文字、色、図形）を効果的に使用
- テキストは簡潔に、ポイントを絞る
- スライド内に収まるようフォントサイズとmargin/paddingを調整