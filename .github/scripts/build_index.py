"""
build_index.py
y Clinic — index.html 自動生成スクリプト

新しいファイルを追加したら FILES リストに追記してください。
カテゴリ: philosophy / strategy / minutes / presentation
"""

import datetime
import zoneinfo

# ============================================================
# 資料マスターデータ  ← ここだけ編集してください
# ============================================================
FILES = [

    # ── 思想・宣言・フレームワーク ────────────────────────────
    dict(
        file="y_clinic_declaration.html",
        cat="philosophy",
        lang="JA / ZH",
        date="2026.04.15",
        title_ja="y Clinic — 設立宣言",
        title_zh="y Clinic — 設立宣言",
        desc_ja="鎌倉からの20年の歴史を起点に「なぜこのクリニックをつくるのか」を宣言。行動の正統性・社会的インフラ構想・設立の3旗を収録。日本語／繁體中文対応。",
        desc_zh="以鎌倉20年歷史為起點，宣告「為何打造這家診所」。收錄行動正統性、社會基礎建設構想與設立3旗。日文／繁體中文對應。",
    ),
    dict(
        file="y_clinic_framework.html",
        cat="philosophy",
        lang="JA / ZH",
        date="2026.04.15",
        title_ja="y Clinic — フレームワーク",
        title_zh="y Clinic — 框架",
        desc_ja="宣言を実装に変える6層モデル（Entry→Assessment→Interpretation→Intervention→Continuum→Institute）の設計図。世界5施設対応・Absorption Design軸を収録。",
        desc_zh="將宣言轉化為實作的6層模型設計圖。收錄與世界5機構的對應及Absorption Design軸。",
    ),
    dict(
        file="y_clinic_philosophy.html",
        cat="philosophy",
        lang="JA / ZH",
        date="2026.04.15",
        title_ja="y Clinic — 思想・宣言・フレームワーク（統合版）",
        title_zh="y Clinic — 思想・宣言・框架（整合版）",
        desc_ja="設立宣言とフレームワークを一冊に統合した資料。ヒーローに使命文・Part I 宣言→Part II 設計図の順で構成。概要把握に最適。",
        desc_zh="將設立宣言與框架整合為一冊的資料。以使命文為封面，依照Part I宣言→Part II設計圖順序構成。最適合概覽掌握。",
    ),

    # ── 戦略・分析 ───────────────────────────────────────────
    dict(
        file="y_clinic_deep_research_bilingual.html",
        cat="strategy",
        lang="JA / ZH",
        date="2026.04.14",
        title_ja="世界12施設 深層分析（日本語 / 繁體中文）",
        title_zh="全球12診所深度分析（日文 / 繁體中文）",
        desc_ja="Mayo Clinic・Neko Health・Sheba・Chi・Buchinger等12施設を徹底分析。設計哲学・強み・限界・y Clinicへの示唆を施設別に収録。日中バイリンガル版。",
        desc_zh="對Mayo Clinic、Neko Health、Sheba、Chi、Buchinger等12家機構進行深度分析。按機構收錄設計哲學、優勢、局限與啟示。日中雙語版。",
    ),
    dict(
        file="y_clinic_deep_research.html",
        cat="strategy",
        lang="JA",
        date="2026.04.14",
        title_ja="世界12施設 深層分析（日本語版）",
        title_zh="全球12診所深度分析（日文版）",
        desc_ja="世界の先端ロンジェビティ・予防医療クリニック12施設の深層分析。施設ごとに理念・診療構造・運営モデル・y Clinicとの差異を詳述。",
        desc_zh="對世界頂尖長壽及預防醫療診所12家機構的深度分析。按機構詳述理念、診療結構、運營模型及與y Clinic的差異。",
    ),
    dict(
        file="y_clinic_global_benchmark.html",
        cat="strategy",
        lang="JA",
        date="2026.04.13",
        title_ja="世界クリニック分析 — y Clinic 戦略フレームワーク",
        title_zh="全球診所分析 — y Clinic 戰略框架",
        desc_ja="世界のロンジェビティクリニックを市場・ポジショニング・サービス設計の観点で比較分析。y Clinicの戦略的ポジションと差別化軸を提示した初期分析資料。",
        desc_zh="從市場、定位、服務設計角度對比分析世界各地長壽診所。提示y Clinic戰略定位與差異化優勢的初期分析資料。",
    ),

    # ── 議事録 ──────────────────────────────────────────────
    dict(
        file="y_clinic_minutes_20260413.html",
        cat="minutes",
        lang="JA",
        date="2026.04.13",
        title_ja="第1回 キックオフMTG 議事録",
        title_zh="第1次啟動會議 會議記錄",
        desc_ja="2026年4月13日 横浜スカイビル25F 開催。出席：芝田崇行・柳澤先生・松村先生・Charles・坂端宏治・中西。全体構想・機能設計・標準化・アクションアイテムを収録。",
        desc_zh="2026年4月13日 於橫濱Sky Building 25F舉行。出席：芝田崇行、柳澤先生、松村先生、Charles、坂端宏治、中西。收錄整體構想、功能設計、標準化及行動項目。",
    ),

    # ── 計画・提案 ──────────────────────────────────────────
    dict(
        file="y_clinic_kickoff.html",
        cat="presentation",
        lang="JA",
        date="2026.04.13",
        title_ja="y Clinic クリニック事業 キックオフ計画書",
        title_zh="y Clinic 診所事業啟動計畫書",
        desc_ja="横浜スカイビル25F 約80坪・2026年10月開業目標のクリニック事業計画書。医療OS型クリニックの全体像・役割分担・スケジュールを収録。",
        desc_zh="橫濱Sky Building 25F 約80坪・以2026年10月開業為目標的診所事業計畫書。收錄醫療OS型診所整體概況、角色分工與時程。",
    ),
]

# ============================================================
# 以下は変更不要
# ============================================================

import os

# ディレクトリに存在するファイルのみに絞り込む
_before = len(FILES)
FILES = [f for f in FILES if os.path.isfile(f["file"])]
_removed = _before - len(FILES)
if _removed:
    print(f"[skip] {_removed} file(s) not found in repo — excluded from index")

BADGE = {
    "philosophy":   ("badge-philosophy", "思想",   "思想"),
    "strategy":     ("badge-strategy",   "分析",   "分析"),
    "minutes":      ("badge-minutes",    "議事録", "記錄"),
    "presentation": ("badge-presentation","資料",  "資料"),
}

CAT_COLOR = {
    "philosophy":   "#B08D4A",
    "strategy":     "#B08D4A",
    "minutes":      "#2B5BA8",
    "presentation": "#2A7A50",
}

SECTIONS = [
    ("philosophy",   "Philosophy",   "思想・宣言・フレームワーク", "思想・宣言・框架"),
    ("strategy",     "Strategy",     "戦略・分析資料",             "戰略・分析資料"),
    ("minutes",      "Minutes",      "議事録",                     "會議記錄"),
    ("presentation", "Presentation", "計画・提案資料",             "計畫・提案資料"),
]


def card(f):
    cls, lbl_ja, lbl_zh = BADGE.get(f["cat"], ("badge-strategy", "資料", "資料"))
    lang_tag = f'<span class="card-lang">{f["lang"]}</span>' if f.get("lang") else ""
    return (
        f'<div class="doc-card cat-{f["cat"]}">'
        f'<a class="card-link" href="{f["file"]}">'
        f'<div class="card-top">'
        f'<span class="card-badge {cls}">'
        f'<span class="tja">{lbl_ja}</span>'
        f'<span class="tzh">{lbl_zh}</span>'
        f'</span>{lang_tag}</div>'
        f'<div class="card-title">'
        f'<span class="tja">{f["title_ja"]}</span>'
        f'<span class="tzh">{f["title_zh"]}</span>'
        f'</div>'
        f'<div class="card-desc">'
        f'<span class="tja">{f["desc_ja"]}</span>'
        f'<span class="tzh">{f["desc_zh"]}</span>'
        f'</div>'
        f'<div class="card-footer">'
        f'<span class="card-date">{f["date"]}</span>'
        f'<span class="card-arrow">&#8594;</span>'
        f'</div>'
        f'</a></div>'
    )


def section(cat, label, title_ja, title_zh):
    items = [f for f in FILES if f["cat"] == cat]
    if not items:
        return ""
    cards = "".join(card(f) for f in items)
    return (
        f'<div class="section" id="sec-{cat}">'
        f'<div class="section-header">'
        f'<p class="section-num">{label}</p>'
        f'<h2 class="section-title">'
        f'<span class="tja">{title_ja}</span>'
        f'<span class="tzh">{title_zh}</span>'
        f'</h2></div>'
        f'<div class="card-grid">{cards}</div>'
        f'</div>'
    )


jst = zoneinfo.ZoneInfo("Asia/Tokyo")
updated = datetime.datetime.now(jst).strftime("%Y年%m月%d日")
count = len(FILES)
all_sections = "".join(section(*s) for s in SECTIONS)

HTML = """\
<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1.0">
<meta name="robots" content="noindex,nofollow,noarchive,nosnippet">
<title>y Clinic &#8212; 社内資料ポータル</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Noto+Sans+JP:wght@300;400;500;700&family=Noto+Serif+JP:wght@400;700&family=DM+Serif+Display:ital@0;1&display=swap" rel="stylesheet">
<style>
:root{
  --navy:#0F1F3D;--accent:#2B5BA8;--gold:#B08D4A;--gold-lt:#D4AF70;
  --bg:#F8F6F1;--bg2:#EEEBE4;--white:#FFFFFF;
  --text:#1A1A2E;--muted:#6B6B8A;
  --border:rgba(15,31,61,0.10);--borders:rgba(15,31,61,0.22);
  --green:#2A7A50;
}
*,*::before,*::after{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Noto Sans JP',sans-serif;background:var(--bg);color:var(--text);
     font-size:14px;line-height:1.8;-webkit-font-smoothing:antialiased}
/* bilingual */
.tzh{display:none}
body.zh .tja{display:none}
body.zh .tzh{display:inline}
/* topbar */
.bar{position:sticky;top:0;z-index:100;background:var(--navy);
     display:flex;align-items:center;justify-content:space-between;
     padding:8px 32px;border-bottom:1px solid rgba(255,255,255,0.08);gap:12px}
.bar-l{font-size:12px;color:rgba(255,255,255,0.45);letter-spacing:0.08em}
.bar-l strong{color:var(--gold-lt);font-weight:500}
.bar-r{display:flex;align-items:center;gap:8px}
.lbs{display:flex;gap:3px}
.lb,.lo{padding:4px 12px;font-size:11px;font-weight:500;
     border:1px solid rgba(255,255,255,0.2);background:transparent;
     color:rgba(255,255,255,0.5);border-radius:3px;cursor:pointer;
     font-family:'Noto Sans JP',sans-serif;transition:all .15s}
.lb:hover,.lo:hover{background:rgba(255,255,255,0.08);color:rgba(255,255,255,0.85)}
.lb.on{background:var(--gold);color:var(--navy);border-color:var(--gold);font-weight:700}
/* page */
.page{max-width:960px;margin:0 auto;padding:0 32px 80px}
/* cover */
.cover{background:var(--navy);color:#fff;padding:48px 64px 40px;
       margin:0 -32px 48px;position:relative;overflow:hidden}
.cover::before{content:'';position:absolute;top:-60px;right:-60px;
       width:320px;height:320px;border:1px solid rgba(255,255,255,0.05);border-radius:50%}
.cover::after{content:'';position:absolute;bottom:-40px;right:60px;
       width:180px;height:180px;border:1px solid rgba(176,141,74,0.18);border-radius:50%}
.ce{font-size:11px;letter-spacing:0.18em;color:var(--gold-lt);text-transform:uppercase;
    margin-bottom:12px;font-weight:400;position:relative;z-index:1}
.ct{font-family:'DM Serif Display',serif;font-size:52px;line-height:1;
    letter-spacing:-0.01em;margin-bottom:8px;position:relative;z-index:1}
.ct span{color:var(--gold-lt)}
.cs{font-size:13px;color:rgba(255,255,255,0.5);margin-bottom:28px;position:relative;z-index:1}
.cm{display:flex;gap:36px;flex-wrap:wrap;padding-top:20px;
    border-top:1px solid rgba(255,255,255,0.1);position:relative;z-index:1}
.cml{font-size:10px;letter-spacing:0.14em;text-transform:uppercase;
     color:var(--gold-lt);margin-bottom:2px}
.cmv{font-size:13px;color:rgba(255,255,255,0.8);font-weight:300}
/* filter */
.fb{display:flex;gap:6px;flex-wrap:wrap;margin-bottom:32px}
.fn{padding:5px 14px;font-size:11px;font-weight:500;
    border:1px solid var(--borders);background:var(--white);
    color:var(--muted);border-radius:20px;cursor:pointer;
    font-family:'Noto Sans JP',sans-serif;transition:all .15s}
.fn:hover{border-color:var(--navy);color:var(--navy)}
.fn.on{background:var(--navy);color:#fff;border-color:var(--navy)}
/* section */
.section{margin-bottom:52px}
.section-header{display:flex;align-items:baseline;gap:10px;
    margin-bottom:16px;padding-bottom:12px;border-bottom:2px solid var(--navy)}
.section-num{font-size:11px;letter-spacing:0.15em;color:var(--gold);
    text-transform:uppercase;font-weight:500}
.section-title{font-family:'Noto Serif JP',serif;font-size:20px;
    font-weight:700;color:var(--navy)}
/* card grid */
.card-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}
/* card */
.doc-card{background:var(--white);border:1px solid var(--border);
    border-radius:8px;position:relative;overflow:hidden;
    display:flex;flex-direction:column;
    transition:box-shadow .15s,transform .12s}
.doc-card:hover{box-shadow:0 4px 20px rgba(15,31,61,0.10);transform:translateY(-1px)}
.doc-card::before{content:'';position:absolute;top:0;left:0;width:100%;height:3px}
.doc-card.cat-philosophy::before,.doc-card.cat-strategy::before{background:var(--gold)}
.doc-card.cat-minutes::before{background:var(--accent)}
.doc-card.cat-presentation::before{background:var(--green)}
.card-link{display:flex;flex-direction:column;flex:1;
    padding:18px 20px 16px;text-decoration:none;color:var(--text)}
.card-top{display:flex;align-items:flex-start;justify-content:space-between;
    gap:8px;margin-bottom:10px}
.card-badge{font-size:9px;font-weight:700;letter-spacing:0.1em;text-transform:uppercase;
    padding:3px 9px;border-radius:3px;flex-shrink:0;margin-top:2px}
.badge-philosophy,.badge-strategy{background:rgba(176,141,74,0.12);color:var(--gold)}
.badge-minutes{background:rgba(43,91,168,0.1);color:var(--accent)}
.badge-presentation{background:rgba(42,138,90,0.1);color:var(--green)}
.card-lang{font-size:9px;letter-spacing:0.06em;color:var(--muted);
    background:var(--bg2);border:1px solid var(--borders);
    border-radius:2px;padding:2px 6px;white-space:nowrap}
.card-title{font-size:14px;font-weight:700;color:var(--navy);
    line-height:1.5;margin-bottom:8px}
.doc-card:hover .card-title{color:var(--accent)}
.card-desc{font-size:12px;color:var(--muted);line-height:1.75;
    flex:1;margin-bottom:14px}
.card-footer{display:flex;align-items:center;justify-content:space-between;
    padding-top:10px;border-top:1px solid var(--border)}
.card-date{font-size:11px;color:var(--muted);letter-spacing:0.04em}
.card-arrow{font-size:13px;color:var(--borders);transition:color .12s,transform .12s}
.doc-card:hover .card-arrow{color:var(--accent);transform:translateX(3px)}
@media(max-width:680px){.card-grid{grid-template-columns:1fr}}
@media(max-width:600px){
  .page{padding:0 16px 60px}.cover{padding:32px 24px 28px}
  .ct{font-size:36px}.cm{flex-direction:column;gap:12px}.bar{padding:8px 16px}
}
</style>
</head>
<body>
<div class="bar">
  <div class="bar-l">
    <strong>y Clinic</strong> &nbsp;&#8212;&nbsp;
    <span class="tja">社内資料ポータル</span>
    <span class="tzh">社內資料入口</span>
  </div>
  <div class="bar-r">
    <div class="lbs">
      <button class="lb on" id="btn-ja" onclick="sL('ja')">日本語</button>
      <button class="lb"    id="btn-zh" onclick="sL('zh')">繁體中文</button>
    </div>
    <button class="lo" onclick="logout()">
      <span class="tja">ログアウト</span><span class="tzh">登出</span>
    </button>
  </div>
</div>
<div class="page">
  <div class="cover">
    <div class="ce">Future Health by SPIC</div>
    <div class="ct">y<span> Clinic</span></div>
    <div class="cs">
      <span class="tja">プロジェクト 社内資料ポータル</span>
      <span class="tzh">專案 社內資料入口</span>
    </div>
    <div class="cm">
      <div>
        <div class="cml"><span class="tja">資料数</span><span class="tzh">資料數</span></div>
        <div class="cmv">__COUNT__<span class="tja">件</span><span class="tzh">份</span></div>
      </div>
      <div>
        <div class="cml"><span class="tja">自動更新日</span><span class="tzh">自動更新日</span></div>
        <div class="cmv">__UPDATED__</div>
      </div>
      <div>
        <div class="cml"><span class="tja">プロジェクト</span><span class="tzh">專案</span></div>
        <div class="cmv">y Clinic 横浜旗艦 2026</div>
      </div>
    </div>
  </div>
  <div class="fb">
    <button class="fn on" id="f-all"          onclick="sF('all')">
      <span class="tja">すべて</span><span class="tzh">全部</span></button>
    <button class="fn"    id="f-philosophy"   onclick="sF('philosophy')">
      <span class="tja">思想・宣言</span><span class="tzh">思想・宣言</span></button>
    <button class="fn"    id="f-strategy"     onclick="sF('strategy')">
      <span class="tja">戦略・分析</span><span class="tzh">戰略・分析</span></button>
    <button class="fn"    id="f-minutes"      onclick="sF('minutes')">
      <span class="tja">議事録</span><span class="tzh">會議記錄</span></button>
    <button class="fn"    id="f-presentation" onclick="sF('presentation')">
      <span class="tja">計画・提案</span><span class="tzh">計畫・提案</span></button>
  </div>
  __SECTIONS__
</div>
<script>
if(sessionStorage.getItem('yclinic_auth')!=='1'){window.location.href='login.html';}
function logout(){sessionStorage.removeItem('yclinic_auth');window.location.href='login.html';}
function sL(l){
  document.body.classList.toggle('zh',l==='zh');
  document.documentElement.lang=l==='zh'?'zh-TW':'ja';
  ['ja','zh'].forEach(function(x){
    document.getElementById('btn-'+x).classList.toggle('on',x===l);
  });
}
function sF(cat){
  ['all','philosophy','strategy','minutes','presentation'].forEach(function(k){
    var b=document.getElementById('f-'+k);
    if(b)b.classList.toggle('on',k===cat);
    var s=document.getElementById('sec-'+k);
    if(s)s.style.display=(cat==='all'||cat===k)?'':'none';
  });
}
</script>
</body>
</html>
"""

html = (HTML
        .replace("__COUNT__", str(count))
        .replace("__UPDATED__", updated)
        .replace("__SECTIONS__", all_sections))

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print(f"index.html generated — {count} files, {len(html):,} chars")
