---
marp: true
theme: default
paginate: false
size: 16:9
backgroundColor: #f0f9ff
style: |
  section {
    font-family: 'Hiragino Sans', 'Meiryo', sans-serif;
    padding: 60px 80px;
    display: flex;
    flex-direction: column;
    justify-content: center;
    background: #eff6ff;
  }
  h1 {
    color: #1e40af;
    font-size: 2rem;
    margin-bottom: 0.5em;
  }
  h2 {
    color: #1d4ed8;
    font-size: 1.6rem;
    margin-bottom: 0.5em;
  }
  h3 {
    color: #2563eb;
    font-size: 1.2rem;
    margin-bottom: 0.3em;
  }
  strong {
    color: #1e40af;
  }
  li {
    font-size: 1rem;
    line-height: 1.6;
    margin-bottom: 0.2em;
    color: #1e293b;
  }
  blockquote {
    border-left: 4px solid #3b82f6;
    padding-left: 1rem;
    color: #475569;
  }
  ul, ol {
    margin-top: 0.5em;
    margin-bottom: 0.5em;
  }
---

<!-- _class: lead -->

<div style="text-align: center; padding: 2em 0;">
  <h1 style="font-size: 3.5rem; color: #1e40af; margin-bottom: 0.3em; line-height: 1.2;">
    サクッと「セミナーの自動化」<br>
    マインドセット
  </h1>
  
  <div style="margin: 3em 0;">
    <div style="font-size: 5em;">🚀</div>
    <h2 style="font-size: 2.5rem; color: #2563eb; margin: 0.5em 0;">30点でリリースの精神</h2>
    <p style="font-size: 1.3rem; color: #6b7280;">まずはリリース、その後ブラッシュアップ</p>
  </div>
  
</div>

---

## 30点でリリースの精神
### まずはリリース、その後ブラッシュアップ

<div style="display: flex; justify-content: space-around; align-items: center; margin: 2em 0;">
  <div style="text-align: center;">
    <div style="font-size: 3em; color: #3b82f6;">30%</div>
    <div style="font-size: 0.9em;">初期リリース</div>
  </div>
  <div style="font-size: 2em;">→</div>
  <div style="text-align: center;">
    <div style="font-size: 3em; color: #10b981;">60%</div>
    <div style="font-size: 0.9em;">フィードバック</div>
  </div>
  <div style="font-size: 2em;">→</div>
  <div style="text-align: center;">
    <div style="font-size: 3em; color: #f59e0b;">100%</div>
    <div style="font-size: 0.9em;">完成形</div>
  </div>
</div>

---

## なぜ30点でリリース？

### リリースが遅れる最大の原因

<div style="display: flex; justify-content: space-between; margin: 1em 0;">
  <div style="flex: 1; margin-right: 2em;">
    <ul>
      <li>はじめから細かくやろうとする</li>
      <li>完璧を求めすぎる</li>
      <li>設定の細部にこだわりすぎる</li>
    </ul>
  </div>
  <div style="text-align: center; padding: 1em;">
    <div style="font-size: 4em;">⏰</div>
    <div style="font-size: 1.2em; color: #dc2626; font-weight: bold;">機会損失</div>
  </div>
</div>

**結果：リリースが遅くなり、機会損失が発生**

---

## 正しいアプローチ

### ステップバイステップの開発

<div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin: 1em 0;">
  <div style="text-align: center; margin: 0.5em;">
    <div style="background: #dbeafe; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; margin: 0 auto;">
      <span style="font-size: 1.5em;">📝</span>
    </div>
    <div style="font-size: 0.9em; margin-top: 0.5em;">テンプレート活用</div>
  </div>
  <div style="text-align: center; margin: 0.5em;">
    <div style="background: #dcfce7; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; margin: 0 auto;">
      <span style="font-size: 1.5em;">🔧</span>
    </div>
    <div style="font-size: 0.9em; margin-top: 0.5em;">動くものを作る</div>
  </div>
  <div style="text-align: center; margin: 0.5em;">
    <div style="background: #fef3c7; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; margin: 0 auto;">
      <span style="font-size: 1.5em;">🚀</span>
    </div>
    <div style="font-size: 0.9em; margin-top: 0.5em;">リリース</div>
  </div>
  <div style="text-align: center; margin: 0.5em;">
    <div style="background: #fce7f3; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; margin: 0 auto;">
      <span style="font-size: 1.5em;">📊</span>
    </div>
    <div style="font-size: 0.9em; margin-top: 0.5em;">データ分析</div>
  </div>
  <div style="text-align: center; margin: 0.5em;">
    <div style="background: #e0e7ff; border-radius: 50%; width: 60px; height: 60px; display: flex; align-items: center; justify-content: center; margin: 0 auto;">
      <span style="font-size: 1.5em;">✨</span>
    </div>
    <div style="font-size: 0.9em; margin-top: 0.5em;">改善</div>
  </div>
</div>

---
## PDCAではなくDCAP

<div style="display: flex; justify-content: center; align-items: center; margin: 3em 0;">
  <div style="display: flex; gap: 2em;">
    <div style="text-align: center;">
      <div style="font-size: 4em; color: #dc2626;">D</div>
      <div style="font-size: 1.2em;">Do</div>
    </div>
    <div style="text-align: center;">
      <div style="font-size: 4em; color: #f59e0b;">C</div>
      <div style="font-size: 1.2em;">Check</div>
    </div>
    <div style="text-align: center;">
      <div style="font-size: 4em; color: #10b981;">A</div>
      <div style="font-size: 1.2em;">Act</div>
    </div>
    <div style="text-align: center;">
      <div style="font-size: 4em; color: #3b82f6;">P</div>
      <div style="font-size: 1.2em;">Plan</div>
    </div>
  </div>
</div>

---

## 実践的なヒント

### 動画コンテンツの扱い

<div style="display: flex; align-items: center; justify-content: space-around; margin: 2em 0;">
  <div style="text-align: center;">
    <div style="font-size: 3em;">🎬</div>
    <div style="font-size: 0.9em;">プレースホルダー</div>
    <div style="font-size: 0.8em; color: #6b7280;">最初はこれでOK</div>
  </div>
  <div style="font-size: 2em;">→</div>
  <div style="text-align: center;">
    <div style="font-size: 3em;">🎥</div>
    <div style="font-size: 0.9em;">本番動画</div>
    <div style="font-size: 0.8em; color: #6b7280;">後から差し替え</div>
  </div>
</div>

### 大切なのは「出してみる」こと

---

## 問題解決のフロー

### わからないことがあったら

<div style="display: flex; justify-content: space-around; align-items: center; margin: 1.5em 0;">
  <div style="text-align: center;">
    <div style="font-size: 3em;">📖</div>
    <div style="font-weight: bold; color: #2563eb;">Step 1</div>
    <div style="font-size: 0.9em;">マニュアル確認</div>
  </div>
  <div style="font-size: 2em; color: #2563eb;">→</div>
  <div style="text-align: center;">
    <div style="font-size: 3em;">❓</div>
    <div style="font-weight: bold; color: #2563eb;">Step 2</div>
    <div style="font-size: 0.9em;">質問する</div>
  </div>
  <div style="text-align: center; background: #dbeafe; padding: 1em; border-radius: 8px;">
    <div style="font-size: 0.9em;">📸 スクショ</div>
    <div style="font-size: 0.9em;">🎥 画面録画</div>
  </div>
</div>

**メリット：回答者も素早く的確にサポート可能**

---

## AIの積極活用

### AIをどんどん使いましょう

<div style="display: flex; justify-content: space-between; align-items: flex-start; margin: 1em 0;">
  <div style="flex: 1;">
    <div style="background: #f0f9ff; padding: 1em; border-radius: 8px; margin-bottom: 1em;">
      <div style="font-weight: bold; margin-bottom: 0.5em;">🤖 活用シーン</div>
      <ul style="margin: 0; font-size: 0.9em;">
        <li>「これでいいのかな？」と迷ったとき</li>
        <li>文章の確認・改善</li>
        <li>LPの構成チェック</li>
        <li>メールマガジンの内容確認</li>
      </ul>
    </div>
  </div>
  <div style="text-align: center; margin: 0 2em;">
    <div style="font-size: 4em;">🎯</div>
    <div style="font-size: 1.5em; color: #10b981; font-weight: bold;">70-80%</div>
    <div style="font-size: 0.8em;">の品質まで素早く到達</div>
  </div>
</div>

---

## まとめ

### 30点でリリースの精神

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
  <div style="background: #fce7f3; padding: 1em; border-radius: 8px; text-align: center;">
    <div style="font-size: 2em;">🤖</div>
    <div style="font-weight: bold;">AI活用</div>
  </div>
  <div style="background: #e0e7ff; padding: 1em; border-radius: 8px; text-align: center;">
    <div style="font-size: 2em;">💬</div>
    <div style="font-weight: bold;">効率的な連携</div>
  </div>
  <div style="background: #fee2e2; padding: 1em; border-radius: 8px; text-align: center;">
    <div style="font-size: 2em;">🔄</div>
    <div style="font-weight: bold;">継続的改善</div>
  </div>
</div>

**目標：素早くリリースし、継続的に改善する文化の構築**