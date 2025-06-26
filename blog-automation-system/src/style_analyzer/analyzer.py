import os
import re
import json
from collections import Counter, defaultdict
from typing import Dict, List, Tuple
import MeCab
import numpy as np


class StyleAnalyzer:
    """須崎純一氏の文体を分析するクラス"""
    
    def __init__(self):
        self.mecab = MeCab.Tagger()
        self.style_features = {
            'sentence_lengths': [],
            'punctuation_patterns': defaultdict(int),
            'frequent_phrases': Counter(),
            'vocabulary': Counter(),
            'paragraph_structures': [],
            'opening_patterns': [],
            'closing_patterns': [],
            'transition_words': Counter()
        }
    
    def analyze_articles(self, articles_dir: str) -> Dict:
        """複数の記事から文体特徴を抽出"""
        for filename in os.listdir(articles_dir):
            if filename.endswith('.txt'):
                filepath = os.path.join(articles_dir, filename)
                with open(filepath, 'r', encoding='utf-8') as f:
                    content = f.read()
                    self._analyze_single_article(content)
        
        return self._compile_style_profile()
    
    def _analyze_single_article(self, content: str):
        """単一記事の分析"""
        # 段落に分割
        paragraphs = [p.strip() for p in content.split('\n\n') if p.strip()]
        
        # 段落構造の分析
        self.style_features['paragraph_structures'].append(len(paragraphs))
        
        # 開始・終了パターンの収集
        if paragraphs:
            self.style_features['opening_patterns'].append(paragraphs[0][:100])
            self.style_features['closing_patterns'].append(paragraphs[-1][-100:])
        
        # 文章レベルの分析
        for paragraph in paragraphs:
            sentences = self._split_sentences(paragraph)
            for sentence in sentences:
                # 文長の記録
                self.style_features['sentence_lengths'].append(len(sentence))
                
                # 句読点パターンの分析
                self._analyze_punctuation(sentence)
                
                # 形態素解析
                self._analyze_morphology(sentence)
                
                # フレーズの抽出
                self._extract_phrases(sentence)
    
    def _split_sentences(self, text: str) -> List[str]:
        """文章を文に分割"""
        # 日本語の文末パターンを考慮
        sentences = re.split(r'[。！？]+', text)
        return [s.strip() for s in sentences if s.strip()]
    
    def _analyze_punctuation(self, sentence: str):
        """句読点の使用パターンを分析"""
        punctuation_counts = {
            '、': sentence.count('、'),
            '。': sentence.count('。'),
            '！': sentence.count('！'),
            '？': sentence.count('？'),
            '「': sentence.count('「'),
            '」': sentence.count('」')
        }
        
        for punct, count in punctuation_counts.items():
            if count > 0:
                self.style_features['punctuation_patterns'][punct] += count
    
    def _analyze_morphology(self, sentence: str):
        """形態素解析による語彙と品詞パターンの分析"""
        node = self.mecab.parseToNode(sentence)
        
        while node:
            if node.surface:
                # 語彙の収集
                self.style_features['vocabulary'][node.surface] += 1
                
                # 接続詞・副詞の収集（文体の特徴として重要）
                features = node.feature.split(',')
                if features[0] in ['接続詞', '副詞']:
                    self.style_features['transition_words'][node.surface] += 1
            
            node = node.next
    
    def _extract_phrases(self, sentence: str):
        """特徴的なフレーズを抽出"""
        # 2-4文字の連続したフレーズを抽出
        for n in range(2, 5):
            for i in range(len(sentence) - n + 1):
                phrase = sentence[i:i+n]
                if not re.match(r'^[ぁ-ん]+$', phrase):  # 平仮名のみは除外
                    self.style_features['frequent_phrases'][phrase] += 1
    
    def _compile_style_profile(self) -> Dict:
        """収集した特徴から文体プロファイルを作成"""
        profile = {
            'average_sentence_length': np.mean(self.style_features['sentence_lengths']),
            'sentence_length_std': np.std(self.style_features['sentence_lengths']),
            'common_phrases': self.style_features['frequent_phrases'].most_common(50),
            'transition_words': self.style_features['transition_words'].most_common(20),
            'punctuation_ratio': {
                punct: count / len(self.style_features['sentence_lengths'])
                for punct, count in self.style_features['punctuation_patterns'].items()
            },
            'vocabulary_size': len(self.style_features['vocabulary']),
            'top_vocabulary': self.style_features['vocabulary'].most_common(100),
            'opening_patterns': self._extract_pattern_features(self.style_features['opening_patterns']),
            'closing_patterns': self._extract_pattern_features(self.style_features['closing_patterns'])
        }
        
        return profile
    
    def _extract_pattern_features(self, patterns: List[str]) -> List[str]:
        """パターンから共通の特徴を抽出"""
        # 簡易的な実装：頻出する開始・終了表現を抽出
        if not patterns:
            return []
        
        # 最初の10文字、20文字などで共通パターンを探す
        common_starts = Counter()
        for pattern in patterns:
            for length in [10, 20, 30]:
                if len(pattern) >= length:
                    common_starts[pattern[:length]] += 1
        
        return [pattern for pattern, _ in common_starts.most_common(5)]
    
    def save_profile(self, profile: Dict, output_path: str):
        """文体プロファイルを保存"""
        # CounterオブジェクトをJSONシリアライズ可能な形式に変換
        serializable_profile = {
            'average_sentence_length': profile['average_sentence_length'],
            'sentence_length_std': profile['sentence_length_std'],
            'common_phrases': profile['common_phrases'],
            'transition_words': profile['transition_words'],
            'punctuation_ratio': profile['punctuation_ratio'],
            'vocabulary_size': profile['vocabulary_size'],
            'top_vocabulary': profile['top_vocabulary'][:50],  # 上位50語彙のみ保存
            'opening_patterns': profile['opening_patterns'],
            'closing_patterns': profile['closing_patterns']
        }
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(serializable_profile, f, ensure_ascii=False, indent=2)
    
    def load_profile(self, profile_path: str) -> Dict:
        """保存された文体プロファイルを読み込み"""
        with open(profile_path, 'r', encoding='utf-8') as f:
            return json.load(f)