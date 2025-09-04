

HTML_TEMPLATE = """<!doctype html>
<html lang="en" class="{meta_class}">
<head>
<meta charset="utf-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>{title}</title>
<style>
  :root {{
    --tile: {tile_px}px;
    --gap: 10px;
    --bg: #0e0f12;
    --fg: #eaeaea;
    --muted: #9aa0a6;
    --card: #171922;
    --accent: #3ea6ff;
    --radius: 12px;
  }}
  * {{ box-sizing: border-box; }}
  html, body {{ height: 100%; margin: 0; background: var(--bg); color: var(--fg); font-family: system-ui, -apple-system, Segoe UI, Roboto, Inter, sans-serif; }}
  header {{
    position: sticky; top: 0; z-index: 10;
    background: linear-gradient(180deg, #0e0f12 85%, #0e0f12cc 100%);
    backdrop-filter: blur(6px);
    border-bottom: 1px solid #22242d;
  }}
  .wrap {{ max-width: 1400px; margin: 0 auto; padding: 12px 16px; }}
  .bar {{ display: grid; grid-template-columns: 1fr auto auto auto auto auto; grid-gap: 12px; align-items: center; }}
  .bar2 {{ display: flex; gap: 12px; align-items: center; flex-wrap: wrap; margin-top: 8px; }}
  h1 {{ font-size: 18px; margin: 0; font-weight: 650; letter-spacing: 0.2px; }}
  button, input[type="range"], input[type="text"], select, .tab {{
    appearance: none;
    background: var(--card);
    color: var(--fg);
    border: 1px solid #2a2d39;
    border-radius: 10px;
    padding: 8px 12px;
    font-weight: 600;
  }}
  button {{ cursor: pointer; }}
  button:hover, .tab:hover {{ border-color: var(--accent); }}
  input[type="text"] {{ width: 100%; font-weight: 500; }}
  .hint {{ color: var(--muted); font-size: 12px; }}

  /* Tabs */
  .tabs {{ display:flex; gap:8px; margin-top: 10px; }}
  .tab {{ cursor:pointer; user-select:none; }}
  .tab.active {{ border-color: var(--accent); box-shadow: 0 0 0 1px var(--accent) inset; }}

  /* Views */
  .view {{ display:none; }}
  .view.active {{ display:block; }}

  /* Gallery grid */
  .grid {{
    display: grid;
    grid-template-columns: repeat(auto-fill, minmax(var(--tile), 1fr));
    gap: var(--gap);
    padding: 16px;
    max-width: 1600px; margin: 0 auto;
  }}
  .tile {{
    background: var(--card);
    border: 1px solid #1f2230;
    border-radius: var(--radius);
    overflow: hidden;
    position: relative;
    display: flex; flex-direction: column;
  }}
  .imgwrap {{
    aspect-ratio: 1 / 1;
    background: #0b0c10;
    border-bottom: 1px solid #262b3a;
    display:flex; align-items:center; justify-content:center;
  }}
  .tile a.__imglink {{ position: absolute; inset: 0; }}
  .tile img {{
    width: 100%; height: 100%;
    object-fit: cover; display: block;
    transition: transform .2s ease;
    background: #fff;
  }}
  .tile:hover img {{ transform: scale(1.02); }}
  .meta {{
    padding: 8px 10px; font-size: 12px; line-height: 1.35;
    display: grid; grid-template-columns: 1fr; gap: 4px;
  }}
  .kv {{ display:flex; gap: 6px; }}
  .k {{ color: var(--muted); white-space: nowrap; }}
  .v {{ overflow-wrap:anywhere; }}
  html.meta-hidden .meta {{ display: none; }}

  .counter {{ font-size: 13px; color: var(--muted); }}
  .err {{ color: #ff7a7a; font-size: 12px; margin-left: 8px; }}

  .pager {{ display:flex; gap:8px; align-items:center; font-size: 13px; }}
  .pager .nums {{ opacity: .8; }}
  .footer-space {{ height: 24px; }}

  /* Stats layout */
  .stats-wrap {{ max-width: 1400px; margin: 0 auto; padding: 16px; display:grid; gap:12px; }}
  .stats-controls {{ display:flex; gap:12px; align-items:center; flex-wrap:wrap; }}
  .cards {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 12px; }}
  .card {{
    background: var(--card); border: 1px solid #1f2230; border-radius: var(--radius);
    padding: 12px; display:flex; flex-direction:column; gap:8px;
  }}
  .card h3 {{ margin:0; font-size: 14px; font-weight:700; letter-spacing:.2px; }}
  .small {{ color: var(--muted); font-size: 12px; }}
  .canvas-wrap {{ width:100%; height:220px; }}
  .canvas-wrap canvas {{ width:100%; height:100%; display:block; }}
  .badge {{ background:#0e0f12; border:1px solid #2a2d39; border-radius: 999px; padding:2px 8px; font-size:11px; color: var(--muted); }}

  /* Category sections */
  .category-section {{ margin-bottom: 24px; }}
  .category-header {{ 
    background: var(--card); border: 1px solid #1f2230; border-radius: var(--radius);
    padding: 12px 16px; margin-bottom: 12px; font-weight: 600; font-size: 14px;
    color: var(--accent); border-left: 4px solid var(--accent);
  }}
  .category-cards {{ display:grid; grid-template-columns: repeat(auto-fill, minmax(320px, 1fr)); gap: 12px; }}
</style>
</head>
<body>
<header>
  <div class="wrap">
    <div class="bar">
      <h1>{title}</h1>
      <span class="counter" id="counter">0 / 0</span>
      <label class="hint">Tile size</label>
      <input id="size" type="range" min="120" max="360" value="{tile_px}" />
      <button id="toggle-meta">{toggle_text}</button>
      <div class="pager">
        <button id="first">⏮</button>
        <button id="prev">◀</button>
        <span class="nums"><span id="page-cur">1</span>/<span id="page-total">1</span></span>
        <button id="next">▶</button>
        <button id="last">⏭</button>
        <label class="hint">Page size</label>
        <select id="page-size">
          <option>50</option>
          <option>100</option>
          <option selected>{page_size}</option>
          <option>500</option>
          <option>1000</option>
        </select>
      </div>
    </div>

    <div class="bar2">
      <input id="filter" type="text" placeholder="pandas-style filter, e.g. extension in ['.png','.jpg'] and unique_colors < 500" />
      <button id="apply">Apply</button>
      <button id="clear">Clear</button>
      <button id="shuffle">Shuffle</button>
      <select id="examples">
        <option value="">Examples…</option>
        <option value="extension in ['.png', '.jpg', '.jpeg']">extension in ['.png', '.jpg', '.jpeg']</option>
        <option value="unique_colors < 500">unique_colors < 500</option>
        <option value="uses_transparency == True">uses_transparency == True</option>
        <option value="filename.str.icontains('icon')">filename.str.icontains('icon')</option>
        <option value="(extension == '.gif') and unique_colors < 256">extension == '.gif' and unique_colors < 256</option>
        <option value="(!uses_transparency) and (unique_colors > 500)">(!uses_transparency) and (unique_colors > 500)</option>
      </select>
      <span class="err" id="err"></span>
    </div>

    <!-- Tabs -->
    <div class="tabs">
      <div class="tab active" data-tab="gallery" id="tab-gallery-btn">Gallery</div>
      <div class="tab" data-tab="stats" id="tab-stats-btn">Distributions</div>
    </div>
  </div>
</header>

<main>
  <!-- Gallery view -->
  <section id="view-gallery" class="view active">
    <div id="grid" class="grid"></div>
    <div class="footer-space"></div>
  </section>

  <!-- Stats view -->
  <section id="view-stats" class="view">
    <div class="stats-wrap">
      <div class="stats-controls">
        <label class="hint">Compute over:</label>
        <select id="stats-scope">
          <option value="filtered" selected>Filtered rows</option>
          <option value="all">All rows</option>
        </select>
        <label class="hint">Split by category:</label>
        <select id="categorical-split">
          <option value="">None</option>
        </select>
        <span class="small" id="stats-summary"></span>
      </div>
      <div id="stats-cards" class="cards"></div>
    </div>
  </section>
</main>

<script>
  const DATA = {rows_json};
  const DEFAULT_PAGE_SIZE = {page_size};
  const CHUNK_SIZE = {chunk_size};
  const SHOW_COLS = {show_cols_json};

  const grid = document.getElementById('grid');
  const counter = document.getElementById('counter');
  const err = document.getElementById('err');
  const filterInput = document.getElementById('filter');
  const toggleMetaBtn = document.getElementById('toggle-meta');

  const firstBtn = document.getElementById('first');
  const prevBtn = document.getElementById('prev');
  const nextBtn = document.getElementById('next');
  const lastBtn = document.getElementById('last');
  const pageCur = document.getElementById('page-cur');
  const pageTotal = document.getElementById('page-total');
  const pageSizeSel = document.getElementById('page-size');

  // Tabs
  const tabGalleryBtn = document.getElementById('tab-gallery-btn');
  const tabStatsBtn = document.getElementById('tab-stats-btn');
  const viewGallery = document.getElementById('view-gallery');
  const viewStats = document.getElementById('view-stats');

  // Stats elements
  const statsScopeSel = document.getElementById('stats-scope');
  const categoricalSplitSel = document.getElementById('categorical-split');
  const statsCards = document.getElementById('stats-cards');
  const statsSummary = document.getElementById('stats-summary');

  let filtered = DATA.slice();
  let order = filtered.map(r => r.src);
  let rendered = 0;

  let pageIndex = 0; // 0-based
  let pageSize = parseInt(pageSizeSel.value || DEFAULT_PAGE_SIZE, 10) || DEFAULT_PAGE_SIZE;

  function contains(s, sub) {{ s = (s ?? '').toString(); return s.indexOf(sub) !== -1; }}
  function icontains(s, sub) {{ s = (s ?? '').toString().toLowerCase(); return s.indexOf((sub ?? '').toString().toLowerCase()) !== -1; }}
  function lower(s) {{ return (s ?? '').toString().toLowerCase(); }}
  function upper(s) {{ return (s ?? '').toString().toUpperCase(); }}
  function list(...a) {{ return a; }}
  function includes(val, arr) {{ return (arr || []).includes(val); }}

  function strAccessor(value) {{
    const s = (value ?? '').toString();
    return {{
      contains: (needle) => contains(s, needle),
      icontains: (needle) => icontains(s, needle),
      lower: () => lower(s),
      upper: () => upper(s),
      len: () => s.length,
    }};
  }}

  function makeScope(row) {{
    return new Proxy({{}}, {{
      has: () => true,
      get: (_, key) => {{
        if (key === 'str') return strAccessor;
        if (key in row) return row[key];
        return undefined;
      }}
    }});
  }}

  function translate(expr) {{
    let e = (expr || '').trim();
    e = e.replace(/\\bis\\s+null\\b/gi, ' == null');
    e = e.replace(/\\bis\\s+not\\s+null\\b/gi, ' != null');
    e = e.replace(/\\band\\b/gi, '&&');
    e = e.replace(/\\bor\\b/gi, '||');
    e = e.replace(/\\bnot\\b/gi, '!');
    e = e.replace(/\\bTrue\\b/g, 'true').replace(/\\bFalse\\b/g, 'false').replace(/\\bNone\\b/g, 'null');
    e = e.replace(/(\\b[\\w\\.]+)\\.str\\.icontains\\(/g, 'str($1).icontains(');
    e = e.replace(/(\\b[\\w\\.]+)\\.str\\.contains\\(/g, 'str($1).contains(');
    e = e.replace(/(\\b[\\w\\.]+)\\.str\\.lower\\(\\)/g, 'str($1).lower()');
    e = e.replace(/(\\b[\\w\\.]+)\\.str\\.upper\\(\\)/g, 'str($1).upper()');
    e = e.replace(/(\\b[\\w\\.]+)\\s+in\\s+(\\[[^\\]]*\\])/gi, 'includes($1, $2)');
    return e;
  }}

  function compileFilter(expr) {{
    const js = translate(expr);
    const fn = new Function('scope', `with (scope) {{ return (${{js || 'true'}}); }}`);
    return (row) => !!fn(makeScope(row));
  }}

  function bounds() {{
    const total = order.length;
    const totalPages = Math.max(1, Math.ceil(total / pageSize));
    pageIndex = Math.max(0, Math.min(pageIndex, totalPages - 1));
    const start = pageIndex * pageSize;
    const end = Math.min(start + pageSize, total);
    return {{ total, totalPages, start, end }};
  }}

  function applyFilter(expr) {{
    if (!expr || !expr.trim()) {{
      filtered = DATA.slice();
    }} else {{
      const pred = compileFilter(expr);
      const out = [];
      for (const r of DATA) {{ try {{ if (pred(r)) out.push(r); }} catch (e) {{ throw e; }} }}
      filtered = out;
    }}
    order = filtered.map(r => r.src);
    pageIndex = 0;
    renderAll();
    if (isStatsActive()) renderStats();
  }}

  function updateCounter() {{
    const b = bounds();
    const visible = b.end - b.start;
    const kept = order.length;
    const removed = DATA.length - kept;
    const pct = kept ? ((kept / DATA.length) * 100).toFixed(1) : '0.0';
    counter.textContent = `${{rendered}} / ${{visible}} • page ${{b.totalPages ? (pageIndex + 1) : 1}}/${{b.totalPages}} • kept ${{kept}} of ${{DATA.length}} (${{pct}}%) • removed ${{removed}}`;
    pageCur.textContent = (b.totalPages ? (pageIndex + 1) : 1);
    pageTotal.textContent = b.totalPages;
    firstBtn.disabled = prevBtn.disabled = (pageIndex <= 0);
    nextBtn.disabled = lastBtn.disabled = (pageIndex >= b.totalPages - 1);
  }}

  function clearGrid() {{
    grid.innerHTML = '';
    rendered = 0;
    updateCounter();
  }}

  function kvRow(k, v) {{
    const div = document.createElement('div');
    div.className = 'kv';
    const kk = document.createElement('span'); kk.className = 'k'; kk.textContent = k + ':';
    const vv = document.createElement('span'); vv.className = 'v'; vv.textContent = (v == null) ? '' : String(v);
    div.append(kk, vv);
    return div;
  }}

  function createTile(row) {{
    const tile = document.createElement('div'); tile.className = 'tile';
    const imgwrap = document.createElement('div'); imgwrap.className = 'imgwrap';
    const img = document.createElement('img'); img.loading = 'lazy'; img.decoding = 'async'; img.src = row.src; img.alt = '';
    imgwrap.appendChild(img); tile.appendChild(imgwrap);

    const meta = document.createElement('div'); meta.className = 'meta';
    const cols = (SHOW_COLS && SHOW_COLS.length) ? SHOW_COLS : Object.keys(row).filter(k => k !== 'src');
    for (const k of cols) {{ if (k !== 'src') meta.appendChild(kvRow(k, row[k])); }}
    tile.appendChild(meta);

    const a = document.createElement('a'); a.href = row.src; a.target = '_blank'; a.rel = 'noopener'; a.className = '__imglink';
    tile.appendChild(a);
    return tile;
  }}

  function renderChunk(start, end) {{
    if (rendered >= end - start) return;
    const upto = Math.min(start + rendered + CHUNK_SIZE, end);
    const frag = document.createDocumentFragment();
    const idx = new Map(filtered.map(r => [r.src, r]));
    for (let i = start + rendered; i < upto; i++) {{
      const row = idx.get(order[i]);
      if (row) frag.appendChild(createTile(row));
    }}
    grid.appendChild(frag);
    rendered = upto - start;
    updateCounter();
    if (start + rendered < end) {{ (window.requestIdleCallback || window.requestAnimationFrame)(() => renderChunk(start, end)); }}
  }}

  function renderAll() {{
    const b = bounds();
    clearGrid(); err.textContent = '';
    renderChunk(b.start, b.end);
    window.scrollTo({{top: 0}});
  }}

  function shuffleInPlace(arr) {{
    for (let i = arr.length - 1; i > 0; i--) {{
      const j = Math.floor(Math.random() * (i + 1));
      [arr[i], arr[j]] = [arr[j], arr[i]];
    }}
  }}

  document.getElementById('shuffle').addEventListener('click', () => {{ shuffleInPlace(order); pageIndex = 0; renderAll(); }});
  document.getElementById('size').addEventListener('input', (e) => {{ const px = parseInt(e.target.value, 10) || {tile_px}; document.documentElement.style.setProperty('--tile', px + 'px'); }});
  document.getElementById('apply').addEventListener('click', () => {{ try {{ applyFilter(filterInput.value); }} catch (e) {{ err.textContent = e.message; }} }});
  document.getElementById('clear').addEventListener('click', () => {{ filterInput.value = ''; applyFilter(''); }});
  document.getElementById('examples').addEventListener('change', (e) => {{ if (e.target.value) {{ filterInput.value = e.target.value; e.target.selectedIndex = 0; }} }});

  // Pagination buttons
  firstBtn.addEventListener('click', () => {{ pageIndex = 0; renderAll(); }});
  prevBtn.addEventListener('click', () => {{ pageIndex = Math.max(0, pageIndex - 1); renderAll(); }});
  nextBtn.addEventListener('click', () => {{ const b = bounds(); pageIndex = Math.min(b.totalPages - 1, pageIndex + 1); renderAll(); }});
  lastBtn.addEventListener('click', () => {{ const b = bounds(); pageIndex = b.totalPages - 1; renderAll(); }});
  pageSizeSel.addEventListener('change', () => {{ pageSize = parseInt(pageSizeSel.value, 10) || DEFAULT_PAGE_SIZE; pageIndex = 0; renderAll(); }});

  function setMetaHidden(hidden) {{
    document.documentElement.classList.toggle('meta-hidden', hidden);
    toggleMetaBtn.textContent = hidden ? 'Show meta' : 'Hide meta';
  }}
  toggleMetaBtn.addEventListener('click', () => {{
    const hidden = !document.documentElement.classList.contains('meta-hidden'); setMetaHidden(hidden);
  }});

  // ---- Tabs handling ----
  function isStatsActive() {{ return viewStats.classList.contains('active'); }}
  function afterLayout(fn){{ (window.requestAnimationFrame||setTimeout)(fn,0); }}

  function setTab(name) {{
    const tabs = [['gallery', tabGalleryBtn, viewGallery], ['stats', tabStatsBtn, viewStats]];
    for (const [n,btn,view] of tabs) {{
      const on = (n===name);
      btn.classList.toggle('active',on);
      view.classList.toggle('active',on);
    }}
    if(name==='stats') afterLayout(()=>renderStats());
  }}
  tabGalleryBtn.addEventListener('click',()=>setTab('gallery'));
  tabStatsBtn.addEventListener('click',()=>setTab('stats'));

  // ---- Stats helpers ----
  function valuesFor(col,rows) {{
    const out=[]; let missing=0;
    for(const r of rows) {{
      if(!(col in r) || r[col]==null || r[col]===''){{ missing++; continue; }}
      out.push(r[col]);
    }}
    return {{values:out,missing}};
  }}

  function coerceNumericArray(arr) {{
    const out=[];
    for(const v of arr){{
      if(typeof v==='number'&&Number.isFinite(v)){{out.push(v);continue;}}
      if(typeof v==='string'){{
        const t=v.trim(); if(t!==''&&!isNaN(t)){{out.push(Number(t));continue;}}
      }}
      return null; // mixed types → treat as categorical
    }}
    return out;
  }}

  function numericSummary(xsRaw){{
    if(!xsRaw.length) return{{min:0,q1:0,median:0,q3:0,max:0}};
    const xs=xsRaw.slice().sort((a,b)=>a-b);
    const n=xs.length;
    const pick=p=>xs[Math.min(n-1,Math.max(0,Math.floor(p*(n-1))))];
    return{{min:xs[0],q1:pick(0.25),median:pick(0.5),q3:pick(0.75),max:xs[n-1]}};
  }}

  function chooseBins(n){{ return Math.max(5,Math.min(60,Math.round(Math.sqrt(Math.max(1,n))))); }}

  function makeHistogram(arr){{
    if(!arr.length) return{{bins:[],counts:[],lo:0,hi:1}};
    const{{min,q1,q3,max}}=numericSummary(arr);
    const iqr=q3-q1;
    const lo=Math.min(min,q1-1.5*iqr);
    const hi=Math.max(max,q3+1.5*iqr);
    const k=chooseBins(arr.length);
    const width=(hi-lo)||1;
    const step=width/k;
    const counts=Array(k).fill(0);
    for(const x of arr){{
      const idx=Math.max(0,Math.min(k-1,Math.floor((x-lo)/step)));
      counts[idx]+=1;
    }}
    const bins=Array.from({{length:k}},(_,i)=>lo+i*step);
    return{{bins,counts,lo,hi}};
  }}

  function catCounts(arr,maxCats=15){{
    const m=new Map();
    for(const v of arr){{const key=String(v);m.set(key,(m.get(key)||0)+1);}}
    const entries=Array.from(m.entries()).sort((a,b)=>b[1]-a[1]);
    if(entries.length<=maxCats) return entries;
    const head=entries.slice(0,maxCats-1);
    const tail=entries.slice(maxCats-1);
    const other=tail.reduce((s,[,c])=>s+c,0);
    head.push(['__OTHER__',other]);
    return head;
  }}

  function detectCategoricalColumns(rows) {{
    const cols = Object.keys(rows[0] || {{}}).filter(k => k !== 'src');
    const categorical = [];
    
    for (const col of cols) {{
      const {{values}} = valuesFor(col, rows);
      const numeric = coerceNumericArray(values);
      
      // Consider categorical if:
      // 1. Not numeric (mixed types or all non-numeric)
      // 2. Numeric but has limited unique values (like boolean or small enum)
      if (!numeric || (numeric.length > 0 && new Set(values).size <= 20)) {{
        categorical.push(col);
      }}
    }}
    
    return categorical;
  }}

  function populateCategoricalDropdown(rows) {{
    const categoricalCols = detectCategoricalColumns(rows);
    categoricalSplitSel.innerHTML = '<option value="">None</option>';
    
    for (const col of categoricalCols) {{
      const option = document.createElement('option');
      option.value = col;
      option.textContent = col;
      categoricalSplitSel.appendChild(option);
    }}
  }}

  function groupByCategory(rows, categoryCol) {{
    if (!categoryCol) return {{ 'All': rows }};
    
    const groups = new Map();
    for (const row of rows) {{
      const value = row[categoryCol];
      const key = value == null ? 'Missing' : String(value);
      if (!groups.has(key)) groups.set(key, []);
      groups.get(key).push(row);
    }}
    
    return Object.fromEntries(groups);
  }}

  function drawBars(canvas,labels,values,opts={{}}){{
    const dpr=window.devicePixelRatio||1;
    const Wcss=canvas.clientWidth||canvas.parentElement.clientWidth||320;
    const Hcss=canvas.clientHeight||canvas.parentElement.clientHeight||220;
    const W=Math.max(10,Math.floor(Wcss*dpr));
    const H=Math.max(10,Math.floor(Hcss*dpr));
    canvas.width=W; canvas.height=H;
    const ctx=canvas.getContext('2d');
    ctx.clearRect(0,0,W,H);
    ctx.font=`${{12*dpr}}px system-ui,-apple-system,Segoe UI,Roboto,Inter,sans-serif`;
    ctx.fillStyle='#eaeaea'; ctx.strokeStyle='#2a2d39';
    const pad=10*dpr;
    const x0=pad,y0=H-22*dpr;
    const x1=W-pad,y1=pad;
    const n=Math.max(1,values.length);
    const vmax=Math.max(1,...values,1);
    const bw=(x1-x0)/n;
    ctx.beginPath(); ctx.moveTo(x0,y0); ctx.lineTo(x1,y0); ctx.stroke();
    for(let i=0;i<n;i++){{const v=values[i]||0;const h=(v/vmax)*(y0-y1);const x=x0+i*bw+1*dpr;const y=y0-h;ctx.fillStyle='#3ea6ff';ctx.fillRect(x,y,Math.max(1*dpr,bw-2*dpr),h);}}
    const maxLabels=Math.min(10,n); const step=Math.max(1,Math.round(n/maxLabels));
    ctx.fillStyle='#9aa0a6'; ctx.textAlign='center'; ctx.textBaseline='top';
    for(let i=0;i<n;i+=step){{const x=x0+i*bw+bw/2;const raw=labels[i]??'';const txt=(opts.tickFmt?opts.tickFmt(raw):String(raw));ctx.fillText(txt,x,y0+4*dpr);}}
  }}

  function renderStats(){{
    try{{
      const scope=(statsScopeSel.value==='filtered')?filtered:DATA;
      const rows=scope;
      const cols=Object.keys(rows[0]||{{}}).filter(k=>k!=='src');
      const categoryCol = categoricalSplitSel.value;
      
      statsCards.innerHTML='';
      statsSummary.textContent=`${{rows.length}} rows • ${{cols.length}} columns`;
      if(!rows.length||!cols.length) return;

      // Group data by category if a category column is selected
      const groups = groupByCategory(rows, categoryCol);
      const groupNames = Object.keys(groups).sort();

      for(const groupName of groupNames){{
        const groupRows = groups[groupName];
        const groupCount = groupRows.length;
        
        // Create category section
        const categorySection = document.createElement('div');
        categorySection.className = 'category-section';
        
        // Add category header if we have multiple groups
        if(groupNames.length > 1){{
          const categoryHeader = document.createElement('div');
          categoryHeader.className = 'category-header';
          categoryHeader.textContent = `${{groupName}} (${{groupCount}} items)`;
          categorySection.appendChild(categoryHeader);
        }}
        
        // Create cards container for this category
        const categoryCards = document.createElement('div');
        categoryCards.className = groupNames.length > 1 ? 'category-cards' : 'cards';
        
        // Generate charts for each column in this category
        for(const col of cols){{
          const{{values,missing}}=valuesFor(col,groupRows);
          const card=document.createElement('div'); card.className='card';

          const header=document.createElement('div');
          header.style.display='flex'; header.style.justifyContent='space-between'; header.style.alignItems='baseline';
          const title=document.createElement('h3'); title.textContent=col;
          const meta=document.createElement('span'); meta.className='small'; meta.textContent=`missing: ${{missing}}`;
          header.appendChild(title); header.appendChild(meta);

          const canvasWrap=document.createElement('div'); canvasWrap.className='canvas-wrap';
          const canvas=document.createElement('canvas'); canvasWrap.appendChild(canvas);

          const footer=document.createElement('div'); footer.className='small';

          const numeric=coerceNumericArray(values);
          if(numeric&&numeric.length){{
            const hist=makeHistogram(numeric);
            drawBars(canvas,hist.bins,hist.counts,{{tickFmt:(x)=>{{const num=Number(x);if(!Number.isFinite(num))return'';const s=Math.abs(num)>=1000?(num/1000).toFixed(1)+'k':num.toFixed(2);return s.replace(/\\.00$/,'');}}}});
            const s=numericSummary(numeric);
            footer.innerHTML=`<span class="badge">numeric</span> <span class="small">min ${{s.min}}, q1 ${{s.q1}}, med ${{s.median}}, q3 ${{s.q3}}, max ${{s.max}}</span>`;
          }} else {{
            const counts=catCounts(values,15);
            const labels=counts.map(([k,_])=>k==='__OTHER__'?'Other':k);
            const vals=counts.map(([_,v])=>v);
            drawBars(canvas,labels,vals,{{tickFmt:(t)=>{{const s=String(t);return s.length>8?s.slice(0,8)+'…':s;}}}});
            footer.innerHTML=`<span class="badge">categorical</span> <span class="small">${{labels.length}} shown${{counts.length>labels.length?' (top)':''}}</span>`;
          }}

          card.appendChild(header);
          card.appendChild(canvasWrap);
          card.appendChild(footer);
          categoryCards.appendChild(card);
        }}
        
        categorySection.appendChild(categoryCards);
        statsCards.appendChild(categorySection);
      }}
    }} catch (e) {{
      console.error('renderStats error:', e);
      statsCards.innerHTML = `<div class="small">Error rendering stats: ${{String(e)}}</div>`;
    }}
  }}

  statsScopeSel.addEventListener('change', () => renderStats());
  categoricalSplitSel.addEventListener('change', () => renderStats());
  window.addEventListener('resize', () => {{ if (isStatsActive()) renderStats(); }});

  // ---- Init ----
  window.addEventListener('load', () => {{
    setMetaHidden(document.documentElement.classList.contains('meta-hidden'));
    [...pageSizeSel.options].forEach(o => {{ if (parseInt(o.value,10) === DEFAULT_PAGE_SIZE) o.selected = true; }});
    populateCategoricalDropdown(DATA);
    applyFilter('');
  }});
</script>
</body>
</html>
"""