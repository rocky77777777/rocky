---
marp: true
theme: default
size: 1920x1080
paginate: true
class: lead
style: |
  /* 全ページ共通で余白を広げ、はみ出しを隠す */
  section {
    padding: 1.5rem;
    box-sizing: border-box;
    overflow: hidden;
  }
  /* 長いテキストの折り返し設定 */
  p, h1, h2, h3, li {
    overflow-wrap: anywhere;
    word-break: break-all;
  }
  /* 画像を枠内に収める */
  img {
    max-width: 90%;
    max-height: 90%;
  }
  /* フォントサイズの上限設定 */
  h1 { font-size: 36px; }
  h2 { font-size: 28px; }
  p  { font-size: 24px; }
---

# 爆速！Cursor×Marpで **10分** でプロ級スライド  
マークダウンとAIを活用して誰でも即スライド職人！

![bg contain](https://marp.app/assets/marp-for-vs-code.png)

---

## Step 1: 爆速でスライド作る最短ルート

1. **拡張機能インストール**  
   Ctrl + Shift + X → 「Marp for VS Code」を検索し、インストール  
   ![w:300](https://raw.githubusercontent.com/marp-team/marp-vscode/main/docs/screenshot.png)  
   ![w:240](https://cdn.prod.website-files.com/5e0f1144930a8bc8aace526c/66cc4129ee5e84251c652198_www.cursor.com-85dcac6c65e38ee1f880690ccca23897.jpeg)

2. **空の `.md` ファイルをオープン**  
   例: `slides.md` / Ctrl + N

3. **AIで雛形を自動生成**  
   Ctrl + K でAIプロンプト  
   例: 「生成AIの活用法をMarpで8枚のスライドにまとめて」

4. **プレビュー確認**  
   右上の「Preview」 または Alt + L Alt + S

5. **部分編集・翻訳・図挿入**  
   範囲選択 → Ctrl + K / 「ここを図解に」など

6. **エクスポート**  
   Ctrl + Shift + P → **Marp: Export Slide Deck…**

---

## Step 2: もう少し丁寧に—Cursor × Marp完全解説

1. **環境準備**  
   - Cursorを起動  
   - 拡張機能からMarpをインストール  
   - 操作：Ctrl + Shift + X

2. **ファイル作成**  
   - 新規Markdownファイル（例：`slides.md`）  
   - 操作：Ctrl + N

3. **AI雛形生成**  
   - Ctrl + K → プロンプト入力  
   - 例：「◯◯についてMarpで◯枚スライド作成」

4. **プレビュー**  
   - 右上の「Preview」またはAlt + L Alt + S

5. **編集＆翻訳**  
   - 範囲選択 → Ctrl + K → 指示

6. **書き出し**  
   - コマンドパレット → Export  
   - 操作：Ctrl + Shift + P

---

### 覚えておくと10倍早いショートカット

- **Ctrl + K** — AIアクション  
- **Ctrl + Enter** — 生成内容確定  
- **Ctrl + Shift + P** — コマンドパレット  

![w:200](https://notejoy.s3.amazonaws.com/static_images/notejoy_keyboard_shortcuts_remaining_styles.png)

---

## Step 3: サンプルMarkdown（Marp用）

```markdown
---
marp: true
theme: default
paginate: true
class: lead
---

# 生成AI入門  
### 〜60分でわかる最新トレンド〜

---

## AI とは？

- データから **パターン** を学習  
- 人間の思考を **数式化** する技術
`
---
![w:240](https://marp.app/assets/og-image.png)  
![w:240](https://chris-ayers.com/assets/images/vscode-editing-marp.png)

---

## Step 4: もっと凝りたい人向けTips

1. **独自テーマ**  
   - スライドと同じフォルダに `theme.css` を置くだけで適用  
   ![w:220](https://raw.githubusercontent.com/marp-team/marp-vscode/main/docs/custom-theme.gif)

---

2. **画像・図の自動挿入**  
   - 範囲指定 → Ctrl + K → 「Unsplash画像を挿入して」  
   ![w:220](https://static-cse.canva.com/blob/1816081/create_ai-presentation-maker_how-to.jpg)

---

3. **Slidev派のあなたへ**  
   - ターミナルで `npx slidev` を実行するだけ  
   - [Slidev公式サイト](https://slidev.dev/)

---

## Step 5: よくあるハマりどころ

| 症状               | 原因と対処                                   |
| ------------------ | -------------------------------------------- |
| 画像が表示されない | **URL直打ち時、「https:」抜けに注意**         |
| 日本語で文字ズレ   | **theme: gaia** 等、別テーマを試す           |
| PPTXが重い         | 画像圧縮 or 先にPDF→PowerPoint変換           |

![w:200](https://raw.githubusercontent.com/marp-team/marp-cli/main/docs/images/pptx.png)

---

# まとめ

**Cursor + Marp** なら  
**10分** で「プロンプト → プレビュー → PDF」  
資料作成に半日かける時代は終了！

浮いた時間は **コンテンツ磨き** に使おう💡

---

# 参考リンク

- [Marp公式サイト](https://marp.app/)  
- [Cursor公式サイト](https://www.cursor.so/)
```