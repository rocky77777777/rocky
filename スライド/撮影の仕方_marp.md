---
marp: true
theme: uncover
class: invert
size: 1080x1920
paginate: false
header: ''
style: |
  @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@400;700;900&display=swap');
  
  section {
    font-family: 'Noto Sans JP', sans-serif;
    background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
  }
  
  h1 {
    font-weight: 900;
    font-size: 60px;
    letter-spacing: 2px;
    text-transform: uppercase;
    background: linear-gradient(45deg, #fff, #64b5f6);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 30px;
  }
  
  h2 {
    font-weight: 700;
    font-size: 42px;
    color: #64b5f6;
    border-bottom: 4px solid #64b5f6;
    padding-bottom: 15px;
    margin-bottom: 30px;
  }
  
  h3 {
    font-weight: 700;
    font-size: 32px;
    color: #90caf9;
  }
  
  .grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 30px;
    margin: 40px 0;
  }
  
  .card {
    background: rgba(255,255,255,0.1);
    border: 2px solid rgba(255,255,255,0.2);
    border-radius: 20px;
    padding: 30px;
    text-align: center;
    transition: all 0.3s ease;
    backdrop-filter: blur(10px);
  }
  
  .card:hover {
    transform: translateY(-5px);
    background: rgba(255,255,255,0.15);
  }
  
  .feature-box {
    background: linear-gradient(135deg, rgba(255,255,255,0.1) 0%, rgba(255,255,255,0.05) 100%);
    border-left: 5px solid #64b5f6;
    padding: 25px;
    margin: 20px 0;
    border-radius: 10px;
  }
  
  .icon-large {
    font-size: 80px;
    margin: 20px 0;
  }
  
  code {
    background: rgba(255,255,255,0.2);
    padding: 8px 16px;
    border-radius: 8px;
    font-size: 20px;
  }
  
  table {
    width: 100%;
    border-collapse: separate;
    border-spacing: 0;
    border-radius: 10px;
    overflow: hidden;
    background: rgba(255,255,255,0.1);
  }
  
  th {
    background: #64b5f6;
    padding: 15px;
    font-weight: 700;
  }
  
  td {
    padding: 15px;
    border-bottom: 1px solid rgba(255,255,255,0.1);
  }
  
  .highlight {
    background: linear-gradient(135deg, #f06292 0%, #ec407a 100%);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    margin: 30px 0;
  }
  
  .step-container {
    display: flex;
    justify-content: space-around;
    align-items: center;
    margin: 40px 0;
  }
  
  .step {
    text-align: center;
    flex: 1;
    position: relative;
  }
  
  .step::after {
    content: '→';
    position: absolute;
    right: -30px;
    top: 50%;
    transform: translateY(-50%);
    font-size: 30px;
    color: #64b5f6;
  }
  
  .step:last-child::after {
    display: none;
  }
  
  section.lead h1 {
    font-size: 80px;
    text-align: center;
  }
  
  section.lead h2 {
    border: none;
    text-align: center;
  }
---

<!-- _class: lead -->

# さくっと動画撮影
# マスターガイド

<div class="icon-large">🎬</div>

### 誰でも簡単に始められる動画制作

---

# なぜ動画が重要なのか？

<div class="grid" style="margin-top: 60px;">
  <div class="card">
    <div style="font-size: 60px;">📈</div>
    <h3>エンゲージメント</h3>
    <p>テキストの<strong>10倍</strong>の効果</p>
  </div>
  <div class="card">
    <div style="font-size: 60px;">🎯</div>
    <h3>コンバージョン</h3>
    <p>購買率<strong>64%</strong>向上</p>
  </div>
  <div class="card">
    <div style="font-size: 60px;">⏱️</div>
    <h3>滞在時間</h3>
    <p>サイト滞在<strong>2倍</strong>増加</p>
  </div>
</div>

---

# 収録スタイル選択ガイド

<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 40px; margin-top: 50px;">
  <div style="text-align: center;">
    <div style="font-size: 100px;">📱</div>
    <h3>カメラ前トーク</h3>
    <p style="font-size: 24px;">パーソナリティ重視</p>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 100px;">🖥️</div>
    <h3>画面＋ワイプ</h3>
    <p style="font-size: 24px;">説明＋信頼感</p>
  </div>
  <div style="text-align: center;">
    <div style="font-size: 100px;">💻</div>
    <h3>画面収録のみ</h3>
    <p style="font-size: 24px;">コンテンツ集中</p>
  </div>
</div>

---

## スタイル①：カメラ前トーク

<div style="display: flex; justify-content: space-between; align-items: center; gap: 40px;">
  <div style="flex: 1;">
    <div class="feature-box" style="margin-bottom: 20px;">
      <h3 style="font-size: 28px;">📱 必要機材</h3>
      <ul style="font-size: 24px;">
        <li>スマホ/カメラ</li>
        <li>三脚（必須）</li>
        <li>マイク</li>
      </ul>
    </div>
    <div class="feature-box">
      <h3 style="font-size: 28px;">✅ 最適な用途</h3>
      <ul style="font-size: 24px;">
        <li>自己紹介</li>
        <li>商品レビュー</li>
        <li>Vlog・教育</li>
      </ul>
    </div>
  </div>
  <div style="flex: 1; text-align: center;">
    <div style="font-size: 120px;">🤳</div>
    <p style="font-size: 26px; margin-top: 20px;">視聴者との距離が近い</p>
  </div>
</div>

---

## スタイル②：画面収録＋ワイプ

<div style="display: flex; justify-content: space-between; align-items: center; gap: 40px;">
  <div style="flex: 1; text-align: center;">
    <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 20px; display: inline-block;">
      <div style="font-size: 80px;">🖥️</div>
      <div style="position: relative; bottom: 20px; right: -30px; font-size: 40px; background: #64b5f6; width: 50px; height: 50px; border-radius: 10px; display: inline-flex; align-items: center; justify-content: center;">👤</div>
    </div>
  </div>
  <div style="flex: 1;">
    <div class="feature-box" style="margin-bottom: 20px;">
      <h3 style="font-size: 28px;">🖥️ 推奨ツール</h3>
      <ul style="font-size: 24px;">
        <li><strong>Zoom</strong> - 簡単</li>
        <li><strong>OBS</strong> - 高機能</li>
        <li><strong>Loom</strong> - 手軽</li>
      </ul>
    </div>
    <div class="feature-box">
      <h3 style="font-size: 28px;">✅ 効果的な場面</h3>
      <ul style="font-size: 24px;">
        <li>オンライン講座</li>
        <li>製品デモ</li>
        <li>プレゼン</li>
      </ul>
    </div>
  </div>
</div>

---

## スタイル③：画面収録のみ

<div class="highlight" style="text-align: center; padding: 40px;">
  <h3 style="color: white; font-size: 36px; margin-bottom: 30px;">シンプル＆効率的</h3>
  <div style="display: flex; justify-content: space-around; gap: 30px;">
    <div>
      <h4 style="color: white; font-size: 24px;">Mac</h4>
      <code style="font-size: 24px;">Shift + Cmd + 5</code>
    </div>
    <div>
      <h4 style="color: white; font-size: 24px;">Windows</h4>
      <code style="font-size: 24px;">Win + G</code>
    </div>
  </div>
  <p style="margin-top: 30px; font-size: 24px;">チュートリアル・技術解説に最適</p>
</div>

---

# 機材優先順位マトリクス

<table style="font-size: 22px; margin-top: 30px;">
  <tr>
    <th style="padding: 12px;">カテゴリ</th>
    <th style="padding: 12px;">必須</th>
    <th style="padding: 12px;">推奨</th>
    <th style="padding: 12px;">あると良い</th>
  </tr>
  <tr>
    <td style="padding: 12px;"><strong>映像</strong></td>
    <td style="padding: 12px;">スマホ/PC</td>
    <td style="padding: 12px;">外付けカメラ</td>
    <td style="padding: 12px;">一眼レフ</td>
  </tr>
  <tr>
    <td style="padding: 12px;"><strong>音声</strong></td>
    <td style="padding: 12px;">イヤホンマイク</td>
    <td style="padding: 12px;">ピンマイク</td>
    <td style="padding: 12px;">コンデンサー<br>マイク</td>
  </tr>
  <tr>
    <td style="padding: 12px;"><strong>安定</strong></td>
    <td style="padding: 12px;">三脚/スタンド</td>
    <td style="padding: 12px;">ジンバル</td>
    <td style="padding: 12px;">スライダー</td>
  </tr>
  <tr>
    <td style="padding: 12px;"><strong>照明</strong></td>
    <td style="padding: 12px;">自然光</td>
    <td style="padding: 12px;">リングライト</td>
    <td style="padding: 12px;">ソフトボックス</td>
  </tr>
</table>

<div style="text-align: center; margin-top: 30px;">
  <p style="font-size: 28px; color: #64b5f6;">💡 <strong>重要：音質 ＞ 画質</strong></p>
</div>

---

# プロの照明セットアップ

<div style="display: flex; justify-content: space-between; gap: 40px; margin-top: 30px;">
  <div style="flex: 1;">
    <h3 style="font-size: 28px;">3点照明の基本</h3>
    <div style="background: rgba(255,255,255,0.1); padding: 30px; border-radius: 20px; text-align: center; font-size: 22px; line-height: 1.8;">
      <div>☀️ キーライト(主光源)</div>
      <div>💡 フィルライト(補助光)</div>
      <div>✨ バックライト(輪郭光)</div>
    </div>
  </div>
  <div style="flex: 1;">
    <h3 style="font-size: 28px;">簡易セットアップ</h3>
    <div class="feature-box">
      <p style="font-size: 22px;"><strong>窓際</strong>で撮影(自然光)</p>
      <p style="font-size: 22px;"><strong>顔の正面</strong>から光を当てる</p>
      <p style="font-size: 22px;"><strong>背景</strong>との分離を意識</p>
    </div>
  </div>
</div>

---

# 撮影前チェックリスト

<div class="step-container" style="margin-top: 40px;">
  <div class="step">
    <div style="font-size: 50px;">🎯</div>
    <h4 style="font-size: 22px;">環境確認</h4>
    <p style="font-size: 20px;">背景・照明<br>騒音チェック</p>
  </div>
  <div class="step">
    <div style="font-size: 50px;">🎤</div>
    <h4 style="font-size: 22px;">音声テスト</h4>
    <p style="font-size: 20px;">30秒録音<br>レベル確認</p>
  </div>
  <div class="step">
    <div style="font-size: 50px;">📹</div>
    <h4 style="font-size: 22px;">映像確認</h4>
    <p style="font-size: 20px;">フレーミング<br>露出調整</p>
  </div>
  <div class="step">
    <div style="font-size: 50px;">💾</div>
    <h4 style="font-size: 22px;">保存設定</h4>
    <p style="font-size: 20px;">容量確認<br>形式選択</p>
  </div>
</div>

---

# 顔出し判断フローチャート

<div style="text-align: center; margin-top: 30px;">
  <div style="display: inline-block; background: rgba(255,255,255,0.1); padding: 30px; border-radius: 20px;">
    <h3 style="margin-bottom: 25px; font-size: 28px;">あなたの目的は？</h3>
    <div style="display: flex; justify-content: center; gap: 40px;">
      <div style="flex: 1; max-width: 250px;">
        <div class="highlight" style="background: linear-gradient(135deg, #66bb6a 0%, #4caf50 100%); padding: 25px;">
          <h4 style="color: white; font-size: 24px;">信頼構築</h4>
          <p style="font-size: 20px;">関係性重視<br>パーソナルブランド</p>
          <p style="font-size: 26px; margin-top: 15px;">👤 顔出し推奨</p>
        </div>
      </div>
      <div style="flex: 1; max-width: 250px;">
        <div class="highlight" style="background: linear-gradient(135deg, #42a5f5 0%, #2196f3 100%); padding: 25px;">
          <h4 style="color: white; font-size: 24px;">コンテンツ重視</h4>
          <p style="font-size: 20px;">技術解説<br>プライバシー保護</p>
          <p style="font-size: 26px; margin-top: 15px;">💻 画面のみ</p>
        </div>
      </div>
    </div>
  </div>
</div>

---

# 収録ワークフロー

<div style="background: rgba(255,255,255,0.05); padding: 40px; border-radius: 30px; margin-top: 30px;">
  <div class="step-container">
    <div class="step">
      <div style="font-size: 60px;">🎬</div>
      <h4 style="font-size: 22px;">準備</h4>
      <p style="font-size: 20px;">機材セット<br>環境整備</p>
    </div>
    <div class="step">
      <div style="font-size: 60px;">⏺️</div>
      <h4 style="font-size: 22px;">録画</h4>
      <p style="font-size: 20px;">開始確認<br>インジケーター</p>
    </div>
    <div class="step">
      <div style="font-size: 60px;">🗣️</div>
      <h4 style="font-size: 22px;">実行</h4>
      <p style="font-size: 20px;">台本確認<br>自然な話し方</p>
    </div>
    <div class="step">
      <div style="font-size: 60px;">💾</div>
      <h4 style="font-size: 22px;">保存</h4>
      <p style="font-size: 20px;">バックアップ<br>整理整頓</p>
    </div>
  </div>
</div>

---

# トラブルシューティング

<table style="font-size: 28px; margin-top: 40px; width: 100%;">
  <tr>
    <th style="text-align: left; padding: 20px;">😱 問題</th>
    <th style="text-align: left; padding: 20px;">💡 解決策</th>
  </tr>
  <tr>
    <td style="padding: 15px;"><strong>🔇 音がこもる</strong></td>
    <td style="padding: 15px;">マイク位置15cm以内</td>
  </tr>
  <tr>
    <td style="padding: 15px;"><strong>📹 映像がブレる</strong></td>
    <td style="padding: 15px;">三脚使用・手持ち禁止</td>
  </tr>
  <tr>
    <td style="padding: 15px;"><strong>🌑 顔が暗い</strong></td>
    <td style="padding: 15px;">窓を前に・ライト追加</td>
  </tr>
</table>

---

<!-- _class: lead -->

# ⚠️ 最重要ポイント

<div class="highlight" style="margin-top: 60px; text-align: center; padding: 60px;">
  <h2 style="color: white; border: none; font-size: 48px; margin-bottom: 40px;">録画ボタンの確認</h2>
  <p style="font-size: 28px; line-height: 2.0;">
    🔴 録画インジケーター
    ⏱️ タイムカウンター
    📊 音声レベルメーター
  </p>
  <p style="margin-top: 40px; font-size: 26px;">必ず3つすべて確認！</p>
</div>

---

<!-- _class: lead -->

# 🚀 今すぐ始めよう！

<div style="text-align: center; margin-top: 60px;">
  <h2 style="border: none; font-size: 44px; margin-bottom: 40px;">次のステップ</h2>
  
  <div style="display: flex; justify-content: center; gap: 40px; font-size: 36px; color: white;">
    <div>✂️ カット編集</div>
    <div style="color: white;">→</div>
    <div>📤 公開</div>
    <div style="color: white;">→</div>
    <div>📊 分析</div>
  </div>
  
  <div style="margin-top: 60px;">
    <p style="font-size: 28px; color: white;">完璧を求めず、まず1本撮ってみる</p>
    <p style="font-size: 26px; color: #90caf9; margin-top: 20px;">Action beats perfection!</p>
  </div>
</div>