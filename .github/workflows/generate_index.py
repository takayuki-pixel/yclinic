#!/usr/bin/env python3
import os, glob, subprocess
from bs4 import BeautifulSoup
from datetime import datetime

SITE_TITLE    = "Project yClinic"
SITE_SUBTITLE = "SPIC | Confidential"
PASSWORD      = "spic2026"

CAT_LABELS = {
    'kickoff':  {'ja': 'キックオフ', 'en': 'Kickoff',  'zh': '啟動'},
    'meeting':  {'ja': '定例MTG',    'en': 'Meeting',   'zh': '會議'},
    'report':   {'ja': 'レポート',   'en': 'Report',    'zh': '報告'},
    'protocol': {'ja': 'プロトコル', 'en': 'Protocol',  'zh': '流程'},
    'research': {'ja': 'リサーチ',   'en': 'Research',  'zh': '研究'},
    'other':    {'ja': 'その他',     'en': 'Other',     'zh': '其他'},
}
CAT_COLORS = {
    'kickoff':  '#2B5BA8',
    'meeting':  '#2A8A5A',
    'report':   '#7B4A9E',
    'protocol': '#B08D4A',
    'research': '#1E7A8A',
    'other':    '#5A5A6A',
}

def get_git_date(filepath):
    try:
        r = subprocess.run(['git','log','-1','--format=%ad','--date=format:%Y-%m-%d','--',filepath],capture_output=True,text=True)
        d = r.stdout.strip()
        return d if d else datetime.today().strftime('%Y-%m-%d')
    except:
        return datetime.today().strftime('%Y-%m-%d')

def fmt_date(d):
    try: return datetime.strptime(str(d),'%Y-%m-%d').strftime('%Y.%m.%d')
    except: return str(d)

def filename_to_title(fname):
    base = os.path.splitext(fname)[0]
    return base.replace('-',' ').replace('_',' ').title()

def read_meta(filepath, filename):
    try:
        with open(filepath, encoding='utf-8', errors='ignore') as f:
            soup = BeautifulSoup(f.read(), 'lxml')
    except:
        soup = None
    def meta(name, fallback=''):
        if soup:
            tag = soup.find('meta', attrs={'name': f'yclinic:{name}'})
            if tag and tag.get('content'):
                return tag['content'].strip()
        return fallback
    title = meta('title', filename_to_title(filename))
    return {
        'file':     filename,
        'title':    title,
        'title_en': meta('title_en', title),
        'title_zh': meta('title_zh', title),
        'desc':     meta('description', ''),
        'desc_en':  meta('description_en', meta('description','')),
        'desc_zh':  meta('description_zh', meta('description','')),
        'category': meta('category', 'other'),
        'badge':    meta('badge', ''),
        'date':     meta('date', get_git_date(filepath)),
    }

def make_card(p):
    cat   = p['category']
    color = CAT_COLORS.get(cat, '#5A5A6A')
    cja   = CAT_LABELS.get(cat, CAT_LABELS['other'])['ja']
    cen   = CAT_LABELS.get(cat, CAT_LABELS['other'])['en']
    czh   = CAT_LABELS.get(cat, CAT_LABELS['other'])['zh']
    badge = f'<span class="card-badge">{p["badge"]}</span>' if p['badge'] else ''
    date  = fmt_date(p['date'])
    return f\"\"\"<a class=\"card\" href=\"{p['file']}\" onclick=\"return goPage(this,event)\">{badge}
      <div class=\"card-cat t-ja\" style=\"background:{color}20;color:{color};\">{cja}</div>
      <div class=\"card-cat t-en\" style=\"background:{color}20;color:{color};\">{cen}</div>
      <div class=\"card-cat t-zh\" style=\"background:{color}20;color:{color};\">{czh}</div>
      <div class=\"card-title t-ja\">{p['title']}</div>
      <div class=\"card-title t-en\">{p['title_en']}</div>
      <div class=\"card-title t-zh\">{p['title_zh']}</div>
      <div class=\"card-desc t-ja\">{p['desc']}</div>
      <div class=\"card-desc t-en\">{p['desc_en']}</div>
      <div class=\"card-desc t-zh\">{p['desc_zh']}</div>
      <div class=\"card-foot\">
        <span class=\"card-date\">{date}</span>
        <span class=\"card-arrow\">→</span>
      </div></a>\"\"\"
