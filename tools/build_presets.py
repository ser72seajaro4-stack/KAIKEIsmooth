# -*- coding: utf-8 -*-
"""tools/apps_data.py から js/presets.js と docs/app-list.csv / docs/app-list.md を作る"""
import csv
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from apps_data import APPS, CATEGORIES, SCHEMES, READINGS  # noqa: E402

LEVEL_NAMES = {'T': 'URLスキームで起動', 'N': 'ストアを開く'}

cat_names = dict(CATEGORIES)

# 重複・抜けのチェック
ids = [a[0] for a in APPS]
assert len(ids) == len(set(ids)), '同じidが2回あります'
for a in APPS:
    assert a[1] in cat_names, f'{a[0]}: カテゴリが不正'
    assert a[4] or a[5], f'{a[0]}: どちらのストア情報もありません'
    assert READINGS.get(a[0]), f'{a[0]}: 読み方（READINGS）がありません'
assert not set(READINGS) - set(ids), f'READINGSに不明なid：{set(READINGS) - set(ids)}'

presets = []
for pid, cat, name, icon, ios, android, scheme, note in APPS:
    level, cands, _ = SCHEMES.get(pid, ('', [scheme] if scheme else [], ''))
    presets.append({'pid': pid, 'cat': cat, 'name': name, 'icon': icon,
                    'iosAppId': ios, 'androidPackage': android,
                    'url': cands[0] if cands else '', 'schemeLevel': level, 'schemeCandidates': cands, 'note': note, 'kana': READINGS[pid]})

js = (
    "// presets.js プリセットアプリの定義（自動生成：tools/build_presets.py）\n"
    "// 直接編集せず、tools/apps_data.py を直してから python3 tools/build_presets.py を実行する。\n"
    "//\n"
    "// iosAppId       … App Storeのアプリ番号（ストアの掲載ページで確認済み）\n"
    "// androidPackage … Google Playのパッケージ名（同上）\n"
    "// url            … URLスキームの初期値（schemeCandidates の先頭）\n"
    "// schemeLevel    … T=URLスキームで起動する / N=URLスキームを使わずストアを開く\n"
    "// schemeCandidates … 起動に使うURLスキーム（T は1つ、N は空）\n"
    "// kana           … 検索用の読み方（ひらがな・スペース区切り）\n"
    "'use strict';\n\n"
    f"const PRESET_CATEGORIES = {json.dumps([{'id': c, 'name': n} for c, n in CATEGORIES], ensure_ascii=False)};\n\n"
    "const PRESETS = [\n"
    + ''.join('  ' + json.dumps(p, ensure_ascii=False) + ',\n' for p in presets)
    + "];\n"
)
with open(os.path.join(ROOT, 'js', 'presets.js'), 'w', encoding='utf-8') as f:
    f.write(js)

os.makedirs(os.path.join(ROOT, 'docs'), exist_ok=True)
header = ['カテゴリ', 'アプリ名', 'App Store（アプリ番号）', 'App StoreのURL', 'Google Play（パッケージ名）', 'Google PlayのURL', 'URLスキーム', 'テスト結果', 'メモ', '備考']
rows = []
for pid, cat, name, icon, ios, android, scheme, note in APPS:
    rows.append([
        cat_names[cat], name,
        ios or '配信なし', f'https://apps.apple.com/jp/app/id{ios}' if ios else '',
        android or '配信なし', f'https://play.google.com/store/apps/details?id={android}' if android else '',
        (SCHEMES[pid][1] or ['なし（ストアを開く）'])[0], LEVEL_NAMES[SCHEMES[pid][0]], SCHEMES[pid][2], note,
    ])
with open(os.path.join(ROOT, 'docs', 'app-list.csv'), 'w', encoding='utf-8-sig', newline='') as f:
    w = csv.writer(f)
    w.writerow(header)
    w.writerows(rows)

md = ['# 対応アプリ一覧', '',
      f'全{len(APPS)}アプリ（2026年10月30日時点）。App Storeのアプリ番号とGoogle Playのパッケージ名は、各ストアの掲載ページで確認しました。', '',
      'URLスキームは2026年10月30日のテスト結果（docs/scheme-test-result-20261030.txt）で決めています。テストで開けた（○）ものはそのURLスキームで起動し、開けなかった（×）ものはURLスキームを使わずストア（App Store／Google Play）のページを開きます。', '',
      f'URLスキームで起動：{sum(1 for v in SCHEMES.values() if v[0] == "T")}件 ／ ストアを開く：{sum(1 for v in SCHEMES.values() if v[0] == "N")}件', '']
for cat, cname in CATEGORIES:
    items = [a for a in APPS if a[1] == cat]
    md += [f'## {cname}（{len(items)}）', '',
           '| アプリ名 | App Store | Google Play | URLスキーム | テスト結果 | 備考 |',
           '| --- | --- | --- | --- | --- | --- |']
    for pid, _, name, icon, ios, android, scheme, note in items:
        ios_cell = f'[id{ios}](https://apps.apple.com/jp/app/id{ios})' if ios else '配信なし'
        and_cell = f'[{android}](https://play.google.com/store/apps/details?id={android})' if android else '配信なし'
        lv, cands, why = SCHEMES[pid]
        scheme_cell = ' / '.join('`' + c + '`' for c in cands) or 'なし（ストアを開く）'
        md.append(f'| {name} | {ios_cell} | {and_cell} | {scheme_cell} | {LEVEL_NAMES[lv]}{("：" + why) if why else ""} | {note} |')
    md.append('')
with open(os.path.join(ROOT, 'docs', 'app-list.md'), 'w', encoding='utf-8') as f:
    f.write('\n'.join(md))

both = sum(1 for a in APPS if a[4] and a[5])
from collections import Counter
print('levels', Counter(v[0] for v in SCHEMES.values()))
print(f'{len(APPS)} apps / 両方のストア {both} / iOSのみ {sum(1 for a in APPS if a[4] and not a[5])} / Androidのみ {sum(1 for a in APPS if a[5] and not a[4])} / スキームあり {sum(1 for a in APPS if a[6])}')
