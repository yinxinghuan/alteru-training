#!/usr/bin/env python3
"""
AlterU Training Slide Deck Generator.

Run: python3 build.py
Outputs: index.html (= 00-cover) and 01-..34 .html files.
"""

from pathlib import Path
import shutil

# ─────────────────────────────────────────────────────────────────────
# SLIDES — each is (slug, short_title, layout_class, body_html, speaker_notes_html)
# Body is the inner HTML of <section class="slide {layout_class}">.
# Layouts available (see _shared.css):
#   cover, split, split flip, matrix-2x2, matrix-3x3, matrix-4, callout
# Use plain inline HTML — no jinja, no escaping needed beyond Python strings.
# ─────────────────────────────────────────────────────────────────────

SLIDES = []


def add(slug, short, layout, body, notes="",
        short_en=None, body_en=None, notes_en=None):
    """Each slide is stored with optional English versions.
    If a field's _en is None, the English view falls back to a 'translation
    coming soon' badge + the Chinese content (so the page is never empty)."""
    SLIDES.append({
        "slug": slug, "layout": layout,
        "short": short, "short_en": short_en or short,
        "body": body, "body_en": body_en,
        "notes": notes, "notes_en": notes_en,
    })


# ═════════════════════════════════════════════════════════════════════
# 00 — Cover
# ═════════════════════════════════════════════════════════════════════
add("cover", "Cover", "cover", """
<span class="eyebrow"><span class="dot"></span>The AlterU Playbook · 2026 · For makers</span>
<h1 class="title">在 AlterU 上<br/>做一个 <em>游戏</em>。</h1>
<p class="sub">
半天,从"AlterU 到底是什么"到"明天就能动手做一个 demo"。
不讲代码——讲<strong>脑子里要装的模型</strong>,做出来的东西才不会被划走。
</p>
<p class="micro pink">↑↓ / ← → 翻页 · F 全屏 · S 备忘 · M 菜单 · L 中/EN</p>
""", """
<p>30 秒钉死目标:这是<strong>产品脑子里的模型</strong>,不是代码。
读完应该能 elevator pitch 一款 AlterU 游戏,并知道哪些设计直觉是错的。</p>
<p>这套 deck 半天读完最舒服。每个 Part 末尾留 2-3 分钟思考。配套游戏建议在手机上打开真机感受。</p>
""",
short_en="Cover",
body_en="""
<span class="eyebrow"><span class="dot"></span>The AlterU Playbook · 2026 · For makers</span>
<h1 class="title">Building a game<br/>on <em>AlterU</em>.</h1>
<p class="sub">
Half a day, from "what is AlterU really" to "I could ship a demo tomorrow."
Not a code tutorial — a load of <strong>the mental model</strong>
that keeps your game from getting swiped past.
</p>
<p class="micro pink">↑↓ / ← → navigate · F fullscreen · S notes · M menu · L 中/EN</p>
""",
notes_en="""
<p>Nail the goal in 30 seconds: this is <strong>the product model in your head</strong>, not code. By the end, you should be able to pitch an AlterU game in an elevator and know which design instincts are wrong here.</p>
<p>This deck reads cleanly in ~3.5 hours. Leave 2-3 minutes after each Part to sit with it. Open the reference games on your phone when you hit the case-study slides — feel the swipe.</p>
""")


# ═════════════════════════════════════════════════════════════════════
# 01 — Agenda
# ═════════════════════════════════════════════════════════════════════
add("agenda", "Agenda", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>Agenda · 半天 3.5 小时</span>
<h2 class="title">六节课。<br/>每节都有<em>一个案例</em>当锚点。</h2>
<div class="grid" style="grid-template-columns: 1fr 1fr 1fr;">
  <a class="cell" href="02-positioning.html"><span class="cell-num">1</span><h3>AlterU 是什么</h3><p>4 层模型 · 30 min · 锚点:Landing 页 hero</p></a>
  <a class="cell" href="07-identity-hooks.html"><span class="cell-num">2</span><h3>身份层怎么落地</h3><p>4 种 identity hooks · 35 min · 锚点:Kiss Wall</p></a>
  <a class="cell" href="12-platform-overview.html"><span class="cell-num">3</span><h3>平台给你的能力</h3><p>AI 4 件套 + 数据原语 · 35 min · 锚点:Hour Capsule</p></a>
  <a class="cell" href="18-paradigm-overview.html"><span class="cell-num">4</span><h3>7 个已验证玩法范式</h3><p>每个 1 张 poster + 1 句配方 · 50 min</p></a>
  <a class="cell" href="26-golden-2s.html"><span class="cell-num">5</span><h3>设计原则 + 反例</h3><p>2 秒规则 · 反例汇总 · 30 min</p></a>
  <a class="cell" href="31-style-library.html"><span class="cell-num">6</span><h3>制作技巧 + 工作流</h3><p>美术 + agent 沟通 + 上线 checklist · 40 min</p></a>
</div>
""", """
<p>提示:建议在第 3 节后休息一次,第 5 节前再休一次。如果时间紧可以砍 Part 4,把范式拆给同学课后自学。</p>
""",
short_en="Agenda",
body_en="""
<span class="eyebrow"><span class="dot"></span>Agenda · ~3.5 hours</span>
<h2 class="title">Seven parts.<br/>Each anchored to <em>a real case</em>.</h2>
<div class="grid" style="grid-template-columns: 1fr 1fr 1fr;">
  <a class="cell" href="02-positioning.html"><span class="cell-num">1</span><h3>What AlterU is</h3><p>The 4-layer model · 30 min · anchor: landing hero</p></a>
  <a class="cell" href="07-identity-hooks.html"><span class="cell-num">2</span><h3>Making the identity layer real</h3><p>4 identity hooks · 35 min · anchor: Kiss Wall</p></a>
  <a class="cell" href="12-platform-overview.html"><span class="cell-num">3</span><h3>What the platform gives you</h3><p>AI quartet + data primitives · 35 min · anchor: Hour Capsule</p></a>
  <a class="cell" href="18-paradigm-overview.html"><span class="cell-num">4</span><h3>Seven proven paradigms</h3><p>One poster + one recipe each · 50 min</p></a>
  <a class="cell" href="26-golden-2s.html"><span class="cell-num">5</span><h3>Design principles + anti-patterns</h3><p>The 2-second rule · live failure log · 30 min</p></a>
  <a class="cell" href="31-style-library.html"><span class="cell-num">6</span><h3>Craft + workflow</h3><p>Art tips + talking to your agent + ship checklist · 40 min</p></a>
</div>
""",
notes_en="""
<p>Pacing: take a break after Part 3 and again before Part 5. If you're tight on time, cut Part 4 — the seven paradigms work as homework reading.</p>
""")


# ═════════════════════════════════════════════════════════════════════
# Part 1 — AlterU 是什么
# ═════════════════════════════════════════════════════════════════════

# 02 一句话定位
add("positioning", "Part 1 · 定位", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Part 1 · 一句话</span>
  <h1 class="title">Another you,<br/>one tap <em>away</em>.</h1>
  <p class="sub">
  Identity-driven mini-games in a single endless feed.<br/>
  Open. Swipe. Play.<br/>
  <strong class="pink">Your AI self becomes the protagonist.</strong>
  </p>
  <p class="micro">— alteru.app · landing hero · 2026</p>
</div>
<div class="col-visual">
  <img src="assets/worlds/hero-vista.png" alt="A vast 3D dream chamber — the AlterU identity layer."/>
</div>
""", """
<p>这张是 landing hero 的原话。请同学先朗读两遍。重点圈:<strong>Identity-driven</strong> + <strong>Your AI self becomes the protagonist</strong>。</p>
<p>问大家:什么是 identity-driven?不是"用户登录",是"游戏的主角就是你"。
后面整个 Part 2 都在拆这件事。</p>
<p>提醒:AlterU 是<strong>独立新品牌</strong>(试美国市场),跟 Aigram chat 是两个品牌,不要混着讲。
底层桥层叫 Aigram 是技术细节,只在 endpoint 表里出现。</p>
""",
short_en="Part 1 · Positioning",
body_en="""
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Part 1 · The one line</span>
  <h1 class="title">Another you,<br/>one tap <em>away</em>.</h1>
  <p class="sub">
  Identity-driven mini-games in a single endless feed.<br/>
  Open. Swipe. Play.<br/>
  <strong class="pink">Your AI self becomes the protagonist.</strong>
  </p>
  <p class="micro">— alteru.app · landing hero · 2026</p>
</div>
<div class="col-visual">
  <img src="assets/worlds/hero-vista.png" alt="A vast 3D dream chamber — the AlterU identity layer."/>
</div>
""",
notes_en="""
<p>Have the room read the landing hero copy aloud — twice. Circle two phrases: <strong>"Identity-driven"</strong> and <strong>"Your AI self becomes the protagonist."</strong></p>
<p>Ask: what does identity-driven mean? It is <em>not</em> "users log in." It means <strong>the game's protagonist is literally you</strong>. The whole Part 2 unpacks that.</p>
<p>Heads up: AlterU is a <strong>standalone new brand</strong> (testing the US market). It's not part of Aigram — Aigram is the underlying tech bridge, a detail that only shows up in the endpoint table. Don't conflate them in front of the audience.</p>
""")

# 03 4 层模型 overview
add("four-layers", "Part 1 · 4 层", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>Part 1 · 用户钦定的 4 层模型</span>
<h2 class="title">从外到内拆 AlterU。<br/><em>只有第 2 层</em>是真差异化。</h2>
<div class="grid">
  <div class="cell"><span class="cell-num">1</span><span class="tag">体感层</span><h3>形式 · Form</h3><p>TikTok 式全屏竖向 scroll feed。用户<strong>感觉到</strong>就够了,不要写进 hero 文案——任何 mini-game 集合都能宣称这个。</p></div>
  <div class="cell" style="border-color: var(--brand-pink); box-shadow: 0 0 0 1px var(--brand-pink-dim), 0 18px 40px rgba(245,177,199,0.10);"><span class="cell-num">2</span><span class="tag">🔑 差异化</span><h3>身份 · Identity</h3><p>你的 AI 自我走进<strong>别人的</strong>游戏:bartender / locksmith / boss / neighbour。Cross-user identity 是 AlterU 和"通用 mini-game 集合"的<strong class="pink">唯一</strong>真正差别。</p></div>
  <div class="cell"><span class="cell-num">3</span><span class="tag">作品层</span><h3>内容 · Content</h3><p>AI-native(vision / gen-image / LLM)+ <strong>手做</strong>。每个游戏有作者声音,不是 procedural slop。混合 register:After Dark FMV → sensory toys → action。</p></div>
  <div class="cell"><span class="cell-num">4</span><span class="tag">机制层</span><h3>社交 · Social</h3><p>Feed-as-verb：动别人内容 → 推作者。score_beat、"kept your stone"、cross-game notify。用户钦定的主攻方向，但不放 landing。</p></div>
</div>
""", """
<p>核心要立刻钉死：<strong>形式层是体感，不放台词里</strong>。说"我们是 TikTok 式游戏 feed"和说"我们是有 News Feed 的社交 app"一样空洞——Instagram / Snapchat / X 都有 feed。</p>
<p>所有 AlterU 的产品决策、玩法选型、视觉规范，都从"<strong>这游戏的 identity 层在哪里</strong>"反推。后面 Part 2 会把这条规则拆开。</p>
""")

# 04 形式层
add("form-layer", "Part 1 · 形式层", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>第 1 层 · 形式</span>
  <h2 class="title">TikTok 全屏，<br/>竖向 scroll <em>feed</em>。</h2>
  <p class="sub">
    玩家不是"打开"游戏，是"<strong>刷</strong>"到游戏。
    一屏一个游戏。划下来是新游戏，划上去回到刚才的。
  </p>
  <ul class="bullets">
    <li><strong>~2 秒看不懂就划走</strong> · 在公交、排队、睡前的人</li>
    <li>带着零上下文、零教程耐心、近乎零的耐心</li>
    <li>看图形 / 动效 / 反馈，不读文字</li>
    <li><span class="dim">这是体感前提，不是宣传点。</span></li>
  </ul>
</div>
<div class="col-visual">
  <img src="assets/worlds/crossover-seam-vertical.png" alt="vertical scroll feed seam"/>
</div>
""", """
<p>让同学闭眼想象自己昨晚刷 TikTok 的状态——划两个广告划走，划一个看不懂的划走，划到下一个有趣的停下来 5 秒。</p>
<p>我们做的游戏要在那"下一个"里被停下来。后面"黄金 2 秒"规则全部从这里推。</p>
""")

# 05 身份层（核心）
add("identity-layer", "Part 1 · 身份层 🔑", "split flip", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>第 2 层 · 身份 · 唯一的差异化</span>
  <h2 class="title">Your AI self<br/>walks <em>into</em><br/>other people's games.</h2>
  <p class="sub">
    你的头像、你做的东西、你 follow 的人——<strong>都会出现在别人游戏里</strong>。
    当 boss、当 NPC、出现在 kiss wall 的画面里、当 block-hop 的邻居。
  </p>
  <p class="sub">
    <strong class="pink">Every scroll is personal in a way TikTok can only fake.</strong>
  </p>
  <p class="micro">— alteru.app · identity section</p>
</div>
<div class="col-visual">
  <img src="assets/identity/walks-in.png" alt="A character walking into a game world"/>
</div>
""", """
<p>这一张是整个培训的脊梁。请同学朗读 landing 这段原话两遍。</p>
<p>对比锚点：Instagram 的 feed 是<strong>关于你</strong>的（你 follow 的人发的内容）；TikTok 的 feed 是<strong>给你</strong>的（算法挑的）。AlterU 的 feed 是<strong>有你在里面</strong>的——你是别人游戏里的角色。</p>
<p>"TikTok can only fake"这句很硬：TikTok 的"个性化"是算法层的，AlterU 的"个性化"是内容层的（游戏画面里就有你）。后续所有 product decision 都用这条衡量。</p>
""")

# 06 内容 + 社交层
add("content-social", "Part 1 · 内容 + 社交层", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>第 3 层 · 第 4 层</span>
<h2 class="title">内容 + 社交 = 让身份层<br/><em>真的活起来</em>。</h2>
<div class="grid">
  <div class="cell">
    <span class="tag">第 3 层 · 内容</span>
    <h3>AI-native + 手做</h3>
    <p><strong>AI-native</strong>：vision 看你的物品、gen-image 出关于你的画面、LLM 写关于你的台词。</p>
    <p style="margin-top:8px;"><strong>手做</strong>：每个游戏有<strong class="pink">作者声音</strong>。不是 procedural slop。混合 register：After Dark 黑色 FMV、sensory toys、action、daily collectibles 都能并存。</p>
  </div>
  <div class="cell">
    <span class="tag">第 4 层 · 社交</span>
    <h3>Feed-as-verb</h3>
    <p>浏览 ≠ 点赞。<strong>动别人内容 → 推作者</strong>。</p>
    <p style="margin-top:8px;">已成型 pattern：<br/>· score_beat: "你被 @xxx 超了"<br/>· kept your stone (Pebble Pocket)<br/>· kissed your portrait (Kiss Wall)<br/>· marked your card (Daily Arcana)<br/>· cross-game notify chain</p>
  </div>
  <div class="cell" style="grid-column: span 2; background: var(--surface-1); border: 0;">
    <p class="sub" style="max-width: none; margin: 0;">
    👉 <strong class="pink">关键判断题</strong>：当你给 AlterU 设计一个新游戏的时候，问自己——
    "这个游戏的<strong>身份层</strong>在哪里、<strong>内容层</strong>是 AI 写的还是手做的、<strong>社交动词</strong>是什么？"
    答不出来 → 它就是个普通 mini-game，不是 AlterU 游戏。
    </p>
  </div>
</div>
""", """
<p>第 3、4 层不像第 2 层那么独有，但它们是<strong>让第 2 层真的活起来</strong>的机制——没有 AI-native，你的身份进游戏只能靠 sticker face；没有 social verb，玩家不会知道"自己出现在别人游戏里"。</p>
<p>底部那条问句是工作模板。每次接到新游戏想法时直接问这 3 件事。</p>
""")


# ═════════════════════════════════════════════════════════════════════
# Part 2 — 身份层怎么落地（本次重点深化）
# ═════════════════════════════════════════════════════════════════════

# 07 身份 4 hooks
add("identity-hooks", "Part 2 · 4 种身份钩子", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>Part 2 · 身份层怎么落地</span>
<h2 class="title">把"身份"<br/>拆成 <em>4 个</em>抓手。</h2>
<div class="grid">
  <div class="cell"><span class="cell-num">1</span><span class="tag">身体钩</span><h3>你的脸 · 你的 portrait</h3><p>Kiss Wall 的吻图用你的 portrait 做 img2img；Block Hop 商店里能换成"你"。<br/><strong>最强但最难做对</strong>——做错就变 sticker face。</p></div>
  <div class="cell"><span class="cell-num">2</span><span class="tag">作品钩</span><h3>你做的东西出现</h3><p>Hour Capsule 的胶囊上烧 <span class="pink">@username #00042</span> 戳；Daily Arcana 抽到的牌进 Wall；Pebble Pocket 收的石头进 Tide feed。</p></div>
  <div class="cell"><span class="cell-num">3</span><span class="tag">环境钩</span><h3>你的物品被 AI 看见</h3><p>Trash or Treasure 拍你家东西；Fit Check 拍你衣橱；Field Guide 拍你身边物。<br/>Vision 链是<strong class="pink">心理拥有感</strong>最强的入口。</p></div>
  <div class="cell"><span class="cell-num">4</span><span class="tag">网络钩</span><h3>你 follow 的人在画面里</h3><p>Cross-user wall（saves/get/data/list 拉最近 6 个用户）；leaderboard 行点头像跳 profile；notify chain 让你"看到自己出现在朋友那里"。</p></div>
</div>
""", """
<p>这 4 个 hook 不是 4 选 1，是<strong>组合套餐</strong>。一个完整的 AlterU 游戏通常会同时用 2-3 个。</p>
<p>例：Kiss Wall = ① 身体钩（你的脸进画）+ ④ 网络钩（吻别人的画→推作者）。
Hour Capsule = ② 作品钩（你的戳）+ ④ 网络钩（Wall 显示朋友最近胶囊）。</p>
<p>设计师可以用这个 4 格当 brainstorm matrix：每个新 idea 至少要打中 1 个 hook。打不中 → 还不算 AlterU 游戏。</p>
""")

# 08 案例 Kiss Wall
add("case-kiss-wall", "Part 2 · 案例 · Kiss Wall", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>身份案例 · Kiss Wall</span>
  <h2 class="title">吻别人的画。<br/>AI 把<em>你的脸</em>融进去。</h2>
  <ul class="bullets">
    <li><strong>首吻锁 prompt</strong> → gen-image 用对方 portrait 当 ref 出 duet 画面</li>
    <li><strong>等待变玩法</strong>：2.6s "化学浴显影"代替 spinner（img 从 blur(12px) brightness(0.18) → 全 1.0）</li>
    <li><strong>SVG filter chain</strong>（feTurbulence + Gaussian + displacement）让边缘像化学晕染</li>
    <li><strong>黑白 silver gelatin 锁</strong> · UX 决定不是审美决定（粉印反差）</li>
    <li><strong>身份钩 ①</strong>：你的脸 · <strong>身份钩 ④</strong>：吻别人的画 → 推作者 notify</li>
  </ul>
  <p class="micro pink" style="margin-top: 24px;">UUID 7a5b620c · 单日 9 commits ship</p>
</div>
<div class="col-visual">
  <img src="assets/posters/kiss-wall.png" alt="Kiss Wall poster"/>
</div>
""", """
<p>讲 Kiss Wall 的关键 talking point：<strong>"5-8s 等图不能 spinner 糊过去——等待本身要是玩法"</strong>。
这一条可以套到任何 gen-image 的游戏，是通用解。</p>
<p>讲一个真实失败：v1 我做了 SEAL 按钮 + curtain 帘子糊等待，用户原话"交互太糟糕"砍了，才悟出"化学浴显影"的设计。让同学体会"等待"不是工程问题是<strong>玩法设计问题</strong>。</p>
<p>另一个不显式但很重要的 lesson：写风格 prompt 前必须先 Read 库里现有 asset，否则风格脑补→上线立刻被骂。</p>
""")

# 09 案例 Hour Capsule
add("case-hour-capsule", "Part 2 · 案例 · Hour Capsule", "split flip", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>身份案例 · Hour Capsule</span>
  <h2 class="title">每小时，<br/>给你封一个<em>真空袋</em>。</h2>
  <ul class="bullets">
    <li>LLM 决定本小时主题 + gen-image 烧上真 MFG 时间戳</li>
    <li>每个袋子左下角 <span class="pink">@username #00042</span> 主人戳</li>
    <li>3 tier 稀有度（80/15/5 银/金 α + flourish）</li>
    <li><strong>真新闻 ticker</strong>：抓 HN 实时新闻当 "FROM THE WIRE" 主角条，冻进 artifact 自己</li>
    <li><strong>身份钩 ②</strong>：你的戳烧死在画面里 · <strong>身份钩 ④</strong>：Wall 显示朋友们这小时的胶囊</li>
    <li><strong>Demo 模式范本</strong>：浏览器外打开也是真 demo，不是 landing 兜底</li>
  </ul>
  <p class="micro pink" style="margin-top: 24px;">UUID d62fb4ed · Seal Press fork</p>
</div>
<div class="col-visual">
  <img src="assets/posters/hour-capsule.png" alt="Hour Capsule poster"/>
</div>
""", """
<p>Hour Capsule 教学价值最高：它一次示范了<strong>所有 AI 4 件套</strong>的串联（LLM 决定主题 → gen-image 出袋子 → 外部 fetch HN 新闻 → upload 存档），以及<strong>身份戳怎么烧死在画面里</strong>。</p>
<p>关键深度点：<strong>"freeze-backstage-with-artifact"</strong> — fetched HN 新闻要冻进胶囊 artifact 自己，不能让它在创建瞬间蒸发。否则下次打开胶囊，那条新闻就消失了。这是个一旦明白就再也不会忘的设计原则。</p>
""")

# 10 案例 Block Hop + Daily Arcana
add("case-blockhop-arcana", "Part 2 · 案例 · Block Hop + Daily Arcana", "split flip", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>身份案例 · 两条不同路径</span>
  <h2 class="title">同一个身份层，<br/><em>不同</em>表现方式。</h2>
  <div style="margin-top: 16px;">
    <span class="tag">Block Hop · 等距 voxel</span>
    <h3 style="font-family: Montserrat; margin: 10px 0 8px; font-size: 19px; color: var(--text-1);">身份钩 ①：当上 voxel 角色</h3>
    <p style="font-size: 14px; line-height: 1.55; color: var(--text-3); margin: 0;">30 个角色商店——<strong style="color: var(--text-1);">Crossy Road 那种文化 caricature</strong>，不是"穿不同制服的普通人"。Shelf It v3 因 silhouette 不可识别被否，v4 才过关。</p>
  </div>
  <div style="margin-top: 24px;">
    <span class="tag">Daily Arcana · 私密机制</span>
    <h3 style="font-family: Montserrat; margin: 10px 0 8px; font-size: 19px; color: var(--text-1);">身份钩 ② + ④：抽到的牌进 Wall</h3>
    <p style="font-size: 14px; line-height: 1.55; color: var(--text-3); margin: 0;"><strong style="color: var(--text-1);">v1 全私密</strong>→ 每张牌只有自己看 → 社交价值 0。D 套件改造：每抽自动 publish 到 Wall + ♥ + notify，<strong style="color: var(--text-1);">私密玩具变社交引擎</strong>。</p>
  </div>
</div>
<div class="col-visual" style="display: grid; grid-template-rows: 1fr 1fr; gap: 16px; height: 70vh; max-height: 660px; align-items: stretch;">
  <div style="overflow: hidden; border-radius: 14px; box-shadow: 0 20px 50px rgba(0,0,0,0.55);"><img src="assets/posters/block-hop.png" alt="Block Hop" style="width: 100%; height: 100%; object-fit: cover; display: block;"/></div>
  <div style="overflow: hidden; border-radius: 14px; box-shadow: 0 20px 50px rgba(0,0,0,0.55);"><img src="assets/extra/daily-arcana.png" alt="Daily Arcana" style="width: 100%; height: 100%; object-fit: cover; display: block;"/></div>
</div>
""", """
<p>这一对对比：<strong>身份层不一定靠"出你的脸"实现</strong>。Block Hop 让你"扮演一个文化符号"也是身份层；Daily Arcana 让"你抽的牌进别人 Wall"也是身份层。</p>
<p>关键提醒：<strong>很多设计师做 Daily Arcana v1 那种"私密抽卡"会觉得已经完成了</strong>——其实少了第 4 个身份钩（网络），它就只是个单机玩具。</p>
""")

# 11 假 identity 反例
add("fake-identity", "Part 2 · 反例 · 假 identity", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>什么时候 identity 是<em class="pink">假</em>的</span>
  <h2 class="title">把脸贴上去<br/><em>不算</em>身份层。</h2>
  <ul class="bullets">
    <li><strong class="danger">Sticker face / 卡通贴纸脸</strong>——粘贴 ≠ 融入。Hold-it-Together v1、Build-a-Boyfriend 早期都被否过</li>
    <li><strong class="danger">Avatar 只显示在 HUD 角落</strong>——不进游戏画面 = 不是身份</li>
    <li><strong class="danger">"你的名字"作为打字气泡</strong>——文字层 ≠ 视觉层</li>
    <li><strong class="ok">真融入</strong>：img2img / 烧字进画面 / Voxel 角色风格化 / 当 NPC / 当 boss</li>
  </ul>
  <p class="sub" style="margin-top: 24px;">
  关键 test：<strong class="pink">关掉你的头像，游戏还成立吗？</strong>
  能成立 = identity 层只是装饰，不算真做了。
  </p>
</div>
<div class="col-visual">
  <img src="assets/gen/fake-identity.jpg" alt="A 'fake identity' smiley-face sticker peeling off an immersive 3D game scene — the world clearly continues past the sticker as if it doesn't belong" style="max-height: 75vh; max-width: 100%; aspect-ratio: 1/1; width: auto; height: auto; object-fit: cover; border-radius: 18px;"/>
</div>
""", """
<p>这一张是<strong>把"身份层"和"装饰品"分开</strong>的关键测试。</p>
<p>讲 Hold-it-Together 这例：v1 是 Reigns 滑卡 + 卡通脸贴纸，玩家原话"看不下去"——根因 = 卡通脸是<strong>装饰</strong>，不是真融入。改成堆叠物理塔（图里这版）之后玩家说好玩——但 identity 其实<strong>退到抽象层</strong>了（"你的内心崩塌"，没有具象 face）。</p>
<p>所以这不是说"必须有脸"，而是说<strong>不要假装有 identity</strong>。要么真做要么不做。</p>
""")


# ═════════════════════════════════════════════════════════════════════
# Part 3 — 平台给你的能力
# ═════════════════════════════════════════════════════════════════════

# 12 平台能力 overview
add("platform-overview", "Part 3 · 平台能力", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>Part 3 · 平台给你的能力</span>
<h2 class="title">AI 4 件套 +<br/>4 件<em>数据原语</em>。</h2>
<div class="grid" style="grid-template-columns: repeat(4, 1fr); gap: 14px;">
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">AI</span><h3 style="font-size: 17px; margin-bottom: 8px;">🎨 gen-image</h3><p style="font-size: 13px; line-height: 1.5;">文生图 / 图生图 · ~5-8s · 烧字进画面（中央 74% 安全区）</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">AI</span><h3 style="font-size: 17px; margin-bottom: 8px;">💬 game-chat</h3><p style="font-size: 13px; line-height: 1.5;">OpenAI 兼容 LLM · ~2-4s · system prompt 决定 AI "嗓音"</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">AI</span><h3 style="font-size: 17px; margin-bottom: 8px;">👁️ recognize</h3><p style="font-size: 13px; line-height: 1.5;">看图 → labels / attributes / parts / caption · ~2-5s</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">AI</span><h3 style="font-size: 17px; margin-bottom: 8px;">☁️ upload</h3><p style="font-size: 13px; line-height: 1.5;">blob → R2 公网 URL · ~1-2s · 喂回 gen-image / recognize</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">DATA</span><h3 style="font-size: 17px; margin-bottom: 8px;">🏆 排行榜</h3><p style="font-size: 13px; line-height: 1.5;">每游戏独立榜 · 点头像跳 profile · 冠军 pill pattern</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">DATA</span><h3 style="font-size: 17px; margin-bottom: 8px;">💾 云存档</h3><p style="font-size: 13px; line-height: 1.5;">session_id 锚定 · 返回最近 6 用户存档 = 天然 cross-user wall</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">DATA</span><h3 style="font-size: 17px; margin-bottom: 8px;">📊 事件 / 统计</h3><p style="font-size: 13px; line-height: 1.5;">day_click_count · continuous_days · 每日一次 / streak 机制</p></div>
  <div class="cell" style="padding: 18px 18px 20px; border-color: var(--brand-pink);"><span class="tag">DATA</span><h3 style="font-size: 17px; margin-bottom: 8px;">🔔 跨用户 notify</h3><p style="font-size: 13px; line-height: 1.5;">动别人内容 → 推作者 · self-guard + 24h dedupe + 单日上限</p></div>
</div>
""", """
<p>设计师只要知道"<strong>我能让游戏画一张图、说话、看玩家、记住玩家、给玩家发通知</strong>"，剩下工程师自然会接。</p>
<p>重点是<strong>会想到去用这些能力</strong>。后面 6 张 slide 每个细讲 1 个真实游戏怎么用。</p>
<p>Endpoint 路径（备查）：所有 4 件 AI 套件都走 <code>chat.aiwaves.tech/aigram/api/{gen-image, game-chat, recognize, upload}</code>。CORS=`*`，浏览器外也能直 fetch（这是 demo 模式的基础）。</p>
""")

# 13 gen-image
add("gen-image", "Part 3 · gen-image", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>能力 · gen-image</span>
  <h2 class="title">文生图 / 图生图<br/>≈ <em>5-8s</em>。</h2>
  <ul class="bullets">
    <li><strong>txt2img</strong>：给文字 prompt → 一张 1:1 图</li>
    <li><strong>img2img</strong>：给参考图 + 文字 → 风格化变体（这是身份钩 ① 的引擎）</li>
    <li><strong>烧字不稳</strong>：SD 渲染文字精度差 · 别在 prompt 里依赖文字精确出现</li>
    <li><span class="danger">⚠️ 测 plate prompt <strong>必须带 ref_url</strong></span> · 只测 txt2img 看似好，加 ref_url 后玩家原照被拼进画面（Fit Check 教训）</li>
    <li><strong>烧字进画面</strong>是 AlterU 标志做法 · Hour Capsule 烧 <code>@user #00042</code>、Pulp Hour 烧封面文案</li>
  </ul>
  <p class="micro pink" style="margin-top: 24px;">5-8s 等待是 <strong>玩法机会</strong>，不是 loading 凑合 — 见 Part 4 范式 6</p>
</div>
<div class="col-visual">
  <img src="assets/posters/hour-capsule.png" alt="Hour Capsule (gen-image showcase)"/>
</div>
""", """
<p>反复强调：<strong>5-8 秒是"用户体验"的关键时间窗</strong>，不是工程参数。当作 loading 处理 → 用户划走；当作玩法 → 用户多停 5 秒。Kiss Wall / Hour Capsule 都把这段时间做成了"显影"仪式。</p>
<p>另一个深度点：<strong>烧字进画面 = identity 钩 ②（作品钩）的最简实现</strong>。任何"我的作品"都可以靠烧字升级到"有我标识的作品"。</p>
""")

# 14 vision
add("vision", "Part 3 · Vision", "split flip", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>能力 · recognize (Vision)</span>
  <h2 class="title">让 AI <em>看</em>玩家拍的照。</h2>
  <ul class="bullets">
    <li>输入：玩家拍照 → upload → recognize</li>
    <li>输出：<code>labels / attributes / parts / caption / confidence</code></li>
    <li>结构化结果再喂给 LLM 出文字 / gen-image 出风格化图</li>
    <li><strong>身份钩 ③（环境钩）的引擎</strong>——AI 看你的东西 = 心理拥有感最强</li>
    <li>已落地：Trash or Treasure / Fit Check / Field Guide / Mugshot Booth / Pet Filter</li>
  </ul>
  <p class="sub" style="margin-top: 18px;">
  <strong class="pink">Vision 把游戏从"AI 给你看东西"翻转成"你给 AI 看东西"</strong>——
  这个翻转改变玩家心理位置，传播性天然强。
  </p>
</div>
<div class="col-visual">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
    <img src="assets/extra/trash-or-treasure.png" alt="Trash or Treasure" style="width:100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 14px;"/>
    <img src="assets/extra/fit-check.png" alt="Fit Check" style="width:100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 14px;"/>
  </div>
</div>
""", """
<p>Vision 是 AlterU 未来主攻方向之一。它独有的是<strong>玩家主动给 AI 拍东西</strong>这一动作——主动 = 强承诺 = 强情感投入。</p>
<p>所以 Vision 类游戏几乎天然有传播性，玩家会自己截屏发朋友圈。Trash or Treasure / Fit Check 都是这个范式的产物。</p>
""")

# 15 LLM
add("llm", "Part 3 · LLM", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>能力 · game-chat (LLM)</span>
  <h2 class="title">让游戏<em>说话</em>。</h2>
  <ul class="bullets">
    <li>OpenAI 兼容格式 · system prompt + user → assistant text</li>
    <li>多轮历史可维护（Pulp Hour 短篇对话）</li>
    <li><strong>关键</strong>：system prompt 决定 AI 嗓音 · 永远写"角色化、有性格"</li>
    <li>反例：默认 ChatGPT-friendly 平淡语气 = AI slop 直接的 UI</li>
  </ul>
  <p class="sub" style="margin-top: 18px;">
  真实嗓音案例：
  </p>
  <ul class="bullets">
    <li><strong>Trash or Treasure</strong>：温柔毒舌 · "KEEP it. You'll regret tossing this."</li>
    <li><strong>Hour Capsule</strong>：博物学家 · "Manufactured 14:32, Tuesday. Limited run of one."</li>
    <li><strong>Pulp Hour</strong>：黑色一刻 · 6 段视觉 hit 短篇</li>
  </ul>
</div>
<div class="col-visual">
  <img src="assets/posters/pulp-hour.png" alt="Pulp Hour"/>
</div>
""", """
<p>这一张关键是<strong>让设计师意识到 LLM 不是"返回正确答案的盒子"，是"返回角色台词的盒子"</strong>。</p>
<p>system prompt 写好整个游戏会有<strong>灵魂</strong>。写糟糕就是 ChatGPT 套皮。
Trash or Treasure 的"温柔毒舌"语气定下来后，整个游戏的气场就有了。</p>
<p>实际能多深？建议同学课后挑一个游戏写一段 system prompt，看 AI 回的是不是"那个游戏角色应该说的话"。</p>
""")

# 16 数据原语
add("data-primitives", "Part 3 · 数据原语", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>能力 · 数据原语 4 件套</span>
<h2 class="title">让游戏<em>记住</em>玩家、<br/>让玩家<em>互相看见</em>。</h2>
<div class="grid">
  <div class="cell">
    <span class="tag">🏆</span>
    <h3>排行榜</h3>
    <p>一行代码接（<code>useGameScore</code>）· 每游戏独立榜 · 点行跳作者 profile</p>
    <p style="margin-top:10px;"><strong>Pattern</strong>：在游戏首屏角落放一个 <strong class="pink">冠军 pill</strong>（22px 头像 + 金王冠）——划到这屏就能看到 #1 是谁，瞬间感受到"有人在玩"。</p>
  </div>
  <div class="cell">
    <span class="tag">💾</span>
    <h3>云存档</h3>
    <p>session_id 锚定 · 返回<strong>最近 6 用户</strong>的存档（不是你一人的）</p>
    <p style="margin-top:10px;"><strong>意外发现</strong>：这个 API 同时就是"作品 wall / 跨用户 feed"的<strong class="pink">天然数据源</strong>——一个 hook 两件事，所有 cross-user wall 都走它。</p>
  </div>
  <div class="cell">
    <span class="tag">📊</span>
    <h3>事件 + 统计</h3>
    <p>触发事件 · 拉聚合统计（day_click_count / day_user_count / continuous_days）</p>
    <p style="margin-top:10px;"><strong>坑</strong>：每日机制不能 <code>lastTapDay===today || stats.*</code>——平台 stats 跨 UTC midnight 不重置 → OR 永真 → <strong class="danger">玩家被永久锁</strong>。已踩 2 次。</p>
  </div>
  <div class="cell" style="border-color: var(--brand-pink); box-shadow: 0 0 0 1px var(--brand-pink-dim);">
    <span class="tag">🔔</span>
    <h3>跨用户 notify（重点）</h3>
    <p>动别人内容 → 推作者一条通知（外显 = 平台头像 + 文本 + 图）</p>
    <p style="margin-top:10px;"><strong>3 铁律</strong>：<br/>✓ self-guard（不给自己发）<br/>✓ 24h dedupe（同动作同对方 24h 1 次）<br/>✓ 作者上限（单日 ≤ 5）</p>
  </div>
</div>
""", """
<p>关键深度点：<strong>云存档 API 一物两用</strong>——它既是"我的存档"也是"看别人最近做了什么"，这是 AlterU 所有 cross-user wall（Daily Arcana / Pulp Hour / Hour Capsule）的基础设施。</p>
<p>Notify 是把单机变社交的最小可行机制——不是聊天、不是评论、不是好友——就是一条"有人动了你的东西"。它是 feed 时代的多巴胺触发器。</p>
<p>设计任何新游戏，day-one 就问：<strong>这游戏的 notify 是什么</strong>？</p>
""")

# 17 demo mode
add("demo-mode", "Part 3 · Demo 模式", "split flip", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>能力 · 外部 Demo 模式</span>
  <h2 class="title">分享出去的链接，<br/>核心 AI 循环<em>依然能跑</em>。</h2>
  <p class="sub">
    AI 4 件套的 endpoint CORS = <code>*</code>，意味着把游戏 URL 发到 Twitter / 朋友圈，
    对方直接点开，<strong class="pink">浏览器里就是真 demo</strong>——不是降级 landing。
  </p>
  <ul class="bullets">
    <li><code>!isInAigram</code> 时，hook 层兜底 phantom 数据：示例排行、假计数器、demo CTA</li>
    <li>Hour Capsule <code>FieldDemoCTA</code> 是模板——poster 当示例袋 + 唯一一个粉填 CTA → App Store</li>
    <li>这是<strong>第二个用户旅程</strong>，不是工程兜底——day-one 就要设计</li>
  </ul>
  <p class="sub" style="margin-top: 18px;">
  Empty state 必须<strong>分两种模式</strong>：
  </p>
  <ul class="bullets" style="margin-top: 8px;">
    <li><code>!isInAigram</code> · 浏览器预览 → "Open in AlterU"</li>
    <li><code>isInAigram && length===0</code> · 真在 app 里但还没数据 → "Invite friends" / "Be the first"</li>
    <li><span class="danger">永远错</span>：一句文案覆盖两种情况</li>
  </ul>
</div>
<div class="col-visual">
  <img src="assets/posters/hour-capsule.png" alt="Hour Capsule demo mode"/>
</div>
""", """
<p>这一条对产品/营销同学非常关键——意味着<strong>每个游戏自带传播 demo</strong>。
不用做单独 landing 页，分享 URL 直接是体验。</p>
<p>Empty state 那条是已上线游戏中招过的真实失误（tag-youre-it lobby），讲的时候可以让设计师审审自己手上 wireframe 有没有把"在 app 里但没数据"和"还没进 app"分开。</p>
""")


# ═════════════════════════════════════════════════════════════════════
# Part 4 — 7 个已验证玩法范式
# ═════════════════════════════════════════════════════════════════════

# 18 范式 overview
add("paradigm-overview", "Part 4 · 7 个范式", "matrix-4", """
<span class="eyebrow"><span class="dot"></span>Part 4 · 7 个已验证范式</span>
<h2 class="title">从这 7 个里挑一个，<br/><em>往里塞</em>你的 idea。</h2>
<div class="grid" style="grid-template-columns: repeat(4, 1fr);">
  <div class="poster-wall" style="grid-column: span 4; grid-template-columns: repeat(7, 1fr);">
    <div class="ptile"><img src="assets/posters/river-row.png" alt=""/><span class="pname">① Physical</span></div>
    <div class="ptile"><img src="assets/posters/block-hop.png" alt=""/><span class="pname">② Crossy Road</span></div>
    <div class="ptile"><img src="assets/posters/shelf-it.png" alt=""/><span class="pname">③ Tycoon</span></div>
    <div class="ptile"><img src="assets/posters/hour-capsule.png" alt=""/><span class="pname">④ LLM Rotation</span></div>
    <div class="ptile"><img src="assets/extra/trash-or-treasure.png" alt=""/><span class="pname">⑤ Vision</span></div>
    <div class="ptile"><img src="assets/posters/kiss-wall.png" alt=""/><span class="pname">⑥ Wait = Play</span></div>
    <div class="ptile"><img src="assets/extra/bubble-wrap-eternal.png" alt=""/><span class="pname">⑦ Sensory</span></div>
  </div>
</div>
<p class="sub" style="margin-top: 32px;">
每个范式都有：<strong>已上线案例</strong> + <strong>核心配方</strong> + <strong>已踩坑</strong> + <strong>可 fork 的源码骨架</strong>。
后面 7 张 slide 每张一个范式。
</p>
""", """
<p>这一页是导航图。让同学心里有个 mental map——下一次接到 idea 时，先去这 7 个范式里挑一个最近的，再开始变形。</p>
<p>讲完这页可以让同学自己挑一个范式做"自家 idea"的练习，下课后交。</p>
""")

# 19 物理手感
add("paradigm-physical", "Part 4 · ① Physical", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>范式 ① · 物理 + 即时手感</span>
  <h2 class="title">手指碰下去，<br/><em>立刻</em>有物理反馈。</h2>
  <ul class="bullets">
    <li><strong>单一输入</strong>：按住 / 拖动 / tap，不要 2 个以上</li>
    <li><strong>撞击 4 件套</strong>：屏幕 shake + 闪白 + 浮 -N + vignette</li>
    <li><strong>程序化 Web Audio</strong>（不用音效文件，省体积省加载）</li>
    <li><strong>FOV swing</strong>主载速度感（52°→82°）</li>
    <li>已上线：<strong>River Row</strong>（划船）/ <strong>Sky Leap</strong>（蓄力跳）/ <strong>Hold It Together</strong>（堆叠塔）</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
    <strong class="pink">用户口味标签</strong>：物理 / 堆叠 / 合成 / 手速即时感<br/>
    <strong class="danger">用户反感</strong>：Reigns 类滑卡 / 纯文字决策 / 卡通贴纸风
  </p>
</div>
<div class="col-visual">
  <img src="assets/posters/river-row.png" alt="River Row"/>
</div>
""", """
<p>这一类是<strong>留存王</strong>。手感对了，玩家反复刷。但手感对不对完全是<strong>调参艺术</strong>——FOV swing、镜头跟随、撞击 4 件套都要现场试。让工程师早点跑出可玩 build，2 周内打磨 30 次比 PRD 写 50 页有用。</p>
""")

# 20 跨道避让
add("paradigm-crossy", "Part 4 · ② Crossy Road", "split flip", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>范式 ② · 等距 voxel 跨道</span>
  <h2 class="title">过马路、<br/>跳格、<em>避让</em>。</h2>
  <ul class="bullets">
    <li>等距 voxel 视角 · 单 tap 跳格 / swipe 换向</li>
    <li><strong>角色商店</strong>：14+ 免费 + 16 个 $20 解锁 + Random 格</li>
    <li>天气 / 灯光 / 道具池按关卡 cycle 切换</li>
    <li>已上线：<strong>Block Hop</strong>（NYC 过马路）/ <strong>Block Party</strong>（俯视射击僵尸）</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
    <strong class="pink">美术铁律</strong>：Crossy Road audience bar = <strong>文化 caricature</strong>，不是"穿不同制服的普通人"。
    Shelf It v3 因 silhouette 不可识别被否，v4 才过关。
  </p>
</div>
<div class="col-visual">
  <img src="assets/posters/block-hop.png" alt="Block Hop"/>
</div>
""", """
<p>这是 AlterU 的"角色商店"承载范式——角色是 identity 钩 ① 的入口。设计师介入最重的点是<strong>30 个角色 caricature 设计</strong>。
讲一遍 Shelf It 角色 4 轮迭代史：v1 parametrize → v2 bespoke 但单 silhouette → v3 极端比例还是被骂 → v4 Crossy Road 文化 caricature 才过。
教训：<strong>iconic 文化符号 ≠ 穿戏服的人</strong>。</p>
""")

# 21 经营优化
add("paradigm-tycoon", "Part 4 · ③ Tycoon", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>范式 ③ · 经营优化（等距俯视）</span>
  <h2 class="title">选品 → 自动卖 →<br/><em>日终</em>结算。</h2>
  <ul class="bullets">
    <li>主题选品 → NPC 人流 → 日终 P&L 小票</li>
    <li>难度脊柱：成长扩张 + 租金棘轮 + 里程碑目标 + 破产重开</li>
    <li>3 条再投资升级（招客 / 加价 / 理货）</li>
    <li>经济铁律：<strong class="pink">COGS-at-sale</strong>（成交才结进货成本）</li>
    <li>已上线：<strong>Shelf It</strong>（陈列经营）</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
  <strong class="pink">关键调参杠杆</strong>：<code>START_CASH</code> / 公比 / <code>RENT_PER_UNIT</code>。<br/>
  HUD 数字超 10K 必须用 K/M/B 压缩格式。
  </p>
</div>
<div class="col-visual">
  <img src="assets/posters/shelf-it.png" alt="Shelf It"/>
</div>
""", """
<p>这一类设计师可以介入很深——难度曲线、UI 信息密度、店员/顾客 AI 状态机都是设计活。<strong>永远先调难度，再调美术</strong>。</p>
<p>真实事故：第一次 modest 一档难度不够（公比 1.3→1.42），玩家"在开始之前就已经超目标了"；二次收紧（1.42→1.55 + RENT 9→11）才合理。
教训：shelf-it margin/branch/attach 复利杠杆多，实际 cash 增长 > framework 默认 1.2x，调难度不能小步。</p>
""")

# 22 LLM 轮换
add("paradigm-llm", "Part 4 · ④ LLM 主题轮换", "split flip", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>范式 ④ · LLM 主题轮换</span>
  <h2 class="title">每<em>小时</em>、每<em>天</em>、<br/>给玩家一个新主题。</h2>
  <ul class="bullets">
    <li>LLM 决定"今天/这小时"的主题 + gen-image 烧时间戳 / @username</li>
    <li><strong>3 层多元保底</strong>：domain 锚 + avoid list + 时事 bonus</li>
    <li><strong>滚动库存 + 倒计时预告</strong> = 替代"明天回来"的活跃信号</li>
    <li>AI/fetch 上下文<strong>冻进 artifact 自己</strong>，不要现 fetch</li>
    <li>已上线：<strong>Hour Capsule</strong>（每小时）/ <strong>Pulp Hour</strong>（每 2 天）/ <strong>Daily Arcana</strong>（每日）</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
  通用解：任何"看起来更新中"的游戏都可以用<strong class="pink">滚动库存 + 倒计时</strong> pattern——
  不是回访型机制，是<strong>scroll-feed 偶遇时的活跃度信号</strong>。
  </p>
</div>
<div class="col-visual">
  <img src="assets/posters/pulp-hour.png" alt="Pulp Hour"/>
</div>
""", """
<p>难点是保鲜——划到第 5 个胶囊 / 第 5 张封面，玩家还觉得新鲜，靠的是 3 层保底里的 avoid list。否则 LLM 会一直生成相似 cluster。</p>
<p>Pulp Hour 之前 4 张硬编码封面永不变 → 用户质问"为什么永远都是那些故事" → 改成每 2 天一张新封面 + 顶部红色倒计时 chip。教训：<strong>玩家划到这屏的那一次，就要看到"还有 X 小时下一张"</strong>，不需要他记得明天回来。</p>
""")

# 23 vision 触发
add("paradigm-vision", "Part 4 · ⑤ Vision", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>范式 ⑤ · Vision 触发</span>
  <h2 class="title">玩家拍照<br/>→ AI <em>判决/品评</em>。</h2>
  <ul class="bullets">
    <li>玩家拍 → upload → recognize → game-chat 出文字 → gen-image 出画面</li>
    <li>整条链 ~ 10-15s（等待变玩法是必修，见范式 ⑥）</li>
    <li>身份钩 ③（环境钩）的引擎 · 心理拥有感最强</li>
    <li>已上线：<strong>Trash or Treasure</strong>（拍家里东西）/ <strong>Fit Check</strong>（拍衣橱）</li>
    <li>路线图：mood-reader / mugshot-booth / pet-filter / album-cover-generator</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
  <strong class="danger">⚠️ 反例</strong>：第一版风格 prompt 脑补不看库 → ship 立刻被骂"风格不一"。
  写风格 prompt 前<strong>必须先 Read 库里现有 asset</strong>。
  </p>
</div>
<div class="col-visual">
  <img src="assets/extra/trash-or-treasure.png" alt="Trash or Treasure"/>
</div>
""", """
<p>Vision 链是 AlterU 未来一段时间的主攻方向。讲的时候让设计师感受<strong>主动 ≠ 被动</strong>——
让 AI 出图给玩家看是 0；让玩家拍东西给 AI 看，玩家心理位置完全不一样，传播性也高得多。</p>
""")

# 24 等待变玩法
add("paradigm-wait", "Part 4 · ⑥ Wait = Play", "split flip", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>范式 ⑥ · 等待变玩法</span>
  <h2 class="title">5-8s 出图，<br/>不能<em>糊</em>过去。</h2>
  <ul class="bullets">
    <li>玩家<strong>第一个输入</strong>触发 prompt（不是按 GENERATE）</li>
    <li>等待 = <strong>化学浴显影</strong>视觉过程（img 起始 blur(12px) brightness(0.18) → 全 1.0）</li>
    <li>SVG filter chain（feTurbulence + Gaussian + displacement）让几何变化学</li>
    <li>12 步 iris bloom（CSS animation on SVG <code>r: 0 → 180</code>）</li>
    <li>已上线：<strong>Kiss Wall</strong>（canonical）</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
  通用解：<strong class="pink">任何用 gen-image 的游戏</strong>都套这个 pattern。
  Kiss Wall 单日 9 commit 上线，整个等待期变成"暗房显影 + 渐渐出现一个人脸"的仪式感。
  </p>
</div>
<div class="col-visual" style="flex-direction: column; gap: 14px;">
  <img src="assets/gen/darkroom-develop.jpg" alt="Three trays of chemistry bath developing a portrait — 5-8s reveal ritual" style="width: 100%; height: 38vh; object-fit: cover; border-radius: 14px;"/>
  <img src="assets/posters/kiss-wall.png" alt="Kiss Wall" style="width: 100%; height: 30vh; object-fit: cover; border-radius: 14px;"/>
</div>
""", """
<p>这个 pattern 一旦理解，会改变同学对"loading"的看法。
loading 不是"挡着用户看不到，让他等"，是"用户主动期待 → 慢慢揭开"。</p>
<p>右上这张图是给培训生成的"化学浴显影"参考——同样的视觉语言可以套到任何 gen-image 等待场景。Kiss Wall 早期 SEAL 按钮 + curtain 帘子糊等待，用户原话"交互太糟糕"砍了 SEAL 才悟。</p>
""")

# 25 sensory toy
add("paradigm-sensory", "Part 4 · ⑦ Sensory Toy", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>范式 ⑦ · Sensory Toy</span>
  <h2 class="title">没有目标。<br/>就是个<em>玩具</em>。</h2>
  <ul class="bullets">
    <li>没有"游戏结束" · 没有规则 · 就是单点感官反馈</li>
    <li>通常 < 100 行 game logic + 极强的程序化美术</li>
    <li>设计师从"我想看见的画面"反推（一颗水珠在玻璃上滑、风让风铃响）</li>
    <li>已上线：<strong>Bubble Wrap</strong> · Marbles · Wind Chime · Crack Tap · Magnet Drop · Stack · Frosted Window · Layer Pop · Liquid Drop · Ghost Garden · Murmuration</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
  <strong class="pink">社交化</strong>靠 score-beat 衍生（"@xxx 摸的次数比你多"）——
  但因为分数连续，必须用 <strong>notifiedTargets Set</strong> 去重，否则每秒发 notify 风暴。
  </p>
</div>
<div class="col-visual">
  <img src="assets/extra/bubble-wrap-eternal.png" alt="Bubble Wrap"/>
</div>
""", """
<p>Sensory toy 是"零教程"原则的极致形态——完全没规则，纯感官。设计师可以从一个"我想看见的画面"反推（一颗水珠在玻璃上滑、一阵风让风铃响）。</p>
<p>它没有 identity 钩 ① / ② / ③，但有 ④（"看朋友比我摸的多/少"）。所以 sensory toy 在 AlterU 里也能 fit 进 identity 模型——只是用网络钩落地。</p>
""")


# ═════════════════════════════════════════════════════════════════════
# Part 5 — 设计原则 + 反例
# ═════════════════════════════════════════════════════════════════════

# 26 黄金 2 秒
add("golden-2s", "Part 5 · 黄金 2 秒", "callout", """
<span class="eyebrow"><span class="dot"></span>Part 5 · 设计原则 ①</span>
<p class="big-quote">
玩家划到你这屏的前 2 秒<br/>
必须发生 <em>3</em> 件事。
</p>
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; max-width: 1080px; margin: 32px auto 0;">
  <div class="cell" style="text-align: left;">
    <span class="cell-num">1</span>
    <h3>看见</h3>
    <p>一个有趣 / 陌生 / 挑逗的画面（视觉钩子）</p>
  </div>
  <div class="cell" style="text-align: left;">
    <span class="cell-num">2</span>
    <h3>识别</h3>
    <p>这是个<strong>游戏</strong>，不是广告、不是 UI 教程</p>
  </div>
  <div class="cell" style="text-align: left;">
    <span class="cell-num">3</span>
    <h3>动手</h3>
    <p>知道现在要<strong>干啥</strong>——一个清晰的可触发动作</p>
  </div>
</div>
<p class="quote-attr" style="margin-top: 40px;">违反这条 → 立刻被划走</p>
""", """
<p>把这 3 件事当 hard rule。讲完后让同学打开自己手机 TikTok 试一遍——划到一个新游戏 / 广告，2 秒内能不能看出"这是什么、要干啥"。能 = 黄金 2 秒过；不能 = 划。</p>
""")

# 27 不假设回访
add("no-return", "Part 5 · 不假设回访", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>Part 5 · 设计原则 ②</span>
<h2 class="title">假设这是<br/><em>唯一一次</em>见面。</h2>
<div class="grid">
  <div class="cell">
    <span class="tag danger">反例</span>
    <h3>❌ 回访型机制</h3>
    <p>"每日签到 7 天送 X"<br/>"明天解锁下一关"<br/>"回来就有福利"</p>
    <p style="margin-top:10px;" class="dim">这些假设玩家会记得明天回来——但 scroll-feed 里 90% 玩家就这一次见面。</p>
  </div>
  <div class="cell" style="border-color: var(--brand-pink);">
    <span class="tag ok">正解</span>
    <h3>✅ 滚动库存 + 倒计时预告</h3>
    <p>每 N 小时上一个新内容<br/>顶部红色每秒 chip<br/>第一格 "COMING NEXT" 封蜡</p>
    <p style="margin-top:10px;" class="dim">划到这屏 = 立刻看到"还有 12 小时"——不需要玩家记得明天回来。Pulp Hour pattern。</p>
  </div>
  <div class="cell" style="grid-column: span 2;">
    <h3>🚨 死亡 chip 铁律</h3>
    <p><code>upcomingCover()</code> 永远要 non-null，否则倒计时 chip + 预告位双消失 = <strong class="danger">"游戏死了"</strong>的视觉信号。
    补给流程：每 N 天在 COVERS 末尾加一条 + 跑生成脚本。</p>
  </div>
</div>
""", """
<p>这一条对产品同学反直觉，因为 retention 工程师天天讲签到、push 通知、reactivation——但 AlterU 的 feed-native 设计里，<strong>"回访"是奢侈，不是默认</strong>。</p>
""")

# 28 英文 + empty state
add("english-empty", "Part 5 · 英文 + Empty state", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Part 5 · 设计原则 ③ + ④</span>
  <h2 class="title">默认英文。<br/>Empty state 分<em>两种</em>。</h2>
  <p class="sub"><strong>🇺🇸 文案铁律</strong></p>
  <ul class="bullets">
    <li>Feed 里游戏标题、UI、按钮、烧字、AI 台词、品牌物料 —— <strong class="pink">全英文</strong></li>
    <li>中文只能作为 i18n 可切换备选，不做默认</li>
    <li><span class="danger">高频翻车</span>：中文占位文案忘了换 → ship 上去毁整屏调性</li>
  </ul>
  <p class="sub" style="margin-top: 24px;"><strong>🪟 Empty state 分两种</strong></p>
  <ul class="bullets">
    <li><code>!isInAigram</code>（浏览器预览）→ "Open in AlterU"</li>
    <li><code>isInAigram && length===0</code>（真在 app 但空）→ "Invite friends" / "Be the first"</li>
    <li><span class="danger">永远错</span>：两种情况用一句文案覆盖</li>
  </ul>
</div>
<div class="col-visual" style="background: var(--surface-2); border-radius: 22px; border: 1px solid var(--border); padding: 32px; align-items: stretch; flex-direction: column; gap: 16px;">
  <div style="text-align: center; opacity: 0.55;">
    <p class="micro">浏览器预览</p>
    <h3 style="font-family: Montserrat; margin: 8px 0 12px;">Empty</h3>
    <p style="color: var(--text-3); font-size: 14px;">"Open in AlterU to play with friends"</p>
  </div>
  <hr style="border: 0; border-top: 1px dashed var(--border); margin: 8px 0;"/>
  <div style="text-align: center;">
    <p class="micro pink">真在 app 里 · 没数据</p>
    <h3 style="font-family: Montserrat; margin: 8px 0 12px;">Empty</h3>
    <p style="color: var(--text-2); font-size: 14px;">"Be the first to leave a mark."</p>
  </div>
</div>
""", """
<p>英文这条用户已经强调过 5-6 次，是产品 owner 的硬规则。讲清楚原因：AlterU 是为美国市场做的新品牌，中文占位文案出现在 feed 里会直接毁掉品牌定位。</p>
<p>Empty state 那条已上线游戏中过招——讲的时候直接打开 UI 让同学审审自己的 wireframe。</p>
""")

# 29 反例汇总
add("anti-examples", "Part 5 · 反例汇总", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>Part 5 · 真实反例 · 真实用户原话</span>
<h2 class="title">"<em>太复杂</em>" · "<em>没耐心</em>" ·<br/>"<em>social 太弱</em>"</h2>
<div class="grid">
  <div class="cell">
    <h3>Hold It Together v1</h3>
    <p class="micro pink">"玩法不好玩"</p>
    <p>Reigns 滑卡 + 卡通脸贴纸 → 玩家以为"读图答题" → 划走。<br/><strong>修法</strong>：堆叠物理塔（matter-js 真物理）✅</p>
  </div>
  <div class="cell">
    <h3>Last Pour v1</h3>
    <p class="micro pink">"太平淡了"</p>
    <p>Wong-Kar-wai 哲学克制独白 → feed 里看不出张力 → 划走。<br/><strong>修法</strong>：吸血鬼 + 哥特 + 6 段视觉 hit ✅</p>
  </div>
  <div class="cell">
    <h3>Sky Leap 充能环</h3>
    <p class="micro pink">"嫌复杂"</p>
    <p>引导动画教 hold + release → 玩家嫌 setup → 划走。<br/><strong>修法</strong>：1 个共用手指 icon，0 文字 ✅</p>
  </div>
  <div class="cell">
    <h3>Daily Arcana v1</h3>
    <p class="micro pink">"私密 ≈ 社交 0"</p>
    <p>每张牌只有自己看 → 没有"分享" → 没有 traction。<br/><strong>修法</strong>：D 套件（Wall + ♥ + notify）✅</p>
  </div>
  <div class="cell">
    <h3>Pebble Pocket v1.2</h3>
    <p class="micro pink">"social 太弱"</p>
    <p>Tide feed 没有动词 → 作者不知道有人看 → 二次价值 0。<br/><strong>修法</strong>：🐚 Keep + notify chain（feed-needs-a-verb）✅</p>
  </div>
  <div class="cell">
    <h3>Shelf It 角色 v1-v3</h3>
    <p class="micro pink">"还差怪物系列那么精彩"</p>
    <p>普通人穿不同制服 → silhouette 一样 → 没 iconic 感。<br/><strong>修法</strong>：v4 Crossy Road 文化 caricature（NYPD / FDNY / Notorious BIG）✅</p>
  </div>
</div>
""", """
<p>每一行展开 1 分钟讲。让设计师感受到——这些被否的设计在<strong>设计稿阶段看起来都很合理</strong>，是在玩家手上才暴露。
所以"设计稿过审"≠"上线没问题"，必须用真用户测真 build。</p>
""")

# 30 V1 visceral
add("v1-visceral", "Part 5 · V1 视觉强度", "split flip", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Part 5 · 视觉 register</span>
  <h2 class="title">Feed 要的是<br/>直接 <em>感官冲击</em>。</h2>
  <p class="sub">
  每个钩子 2 秒内可读出"<strong class="pink">不对</strong>"。
  Wong-Kar-wai 哲学克制<strong>不适合</strong> feed，留给长片。
  </p>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 18px;">
    <div style="background: var(--surface-2); border: 1px solid var(--ok); border-radius: 12px; padding: 14px 16px;">
      <p class="micro ok" style="margin: 0 0 8px;">✅ 写动词 + 可视化</p>
      <ul class="bullets" style="font-size: 13px; gap: 4px;">
        <li>"pours blood"</li>
        <li>"fangs descend"</li>
        <li>"tooth in drink"</li>
        <li>"candle bends toward her"</li>
      </ul>
    </div>
    <div style="background: var(--surface-2); border: 1px solid var(--danger); border-radius: 12px; padding: 14px 16px;">
      <p class="micro danger" style="margin: 0 0 8px;">❌ 抽象名词 / 文学克制</p>
      <ul class="bullets" style="font-size: 13px; gap: 4px;">
        <li>"a memory"</li>
        <li>"a silence"</li>
        <li>"restraint"</li>
      </ul>
    </div>
  </div>
</div>
<div class="col-visual">
  <img src="assets/gen/visceral-cinema.jpg" alt="Visceral noir cinema reference: blood drop, tooth in teacup, bent candle flame" style="max-height: 60vh; max-width: 100%; aspect-ratio: 1/1; width: auto; height: auto; object-fit: cover; border-radius: 18px;"/>
</div>
""", """
<p>Last Pour v1 这一课 8 视频改完才悟。讲一遍原案 → 用户原话"太平淡" → v2 吸血鬼+哥特+6 段视觉 hit。同框架，错的只是 register intensity。</p>
<p>右边这张图是给培训现场生成的 visceral 参考——单帧里 3 个 visceral hit（血滴 + 茶杯里的牙齿 + 被歪斜的烛火），符合 feed 2 秒规则。讲的时候让同学问自己："我 ship 的下一个游戏，2 秒能读出几个 visceral hit？"</p>
""")


# ═════════════════════════════════════════════════════════════════════
# Part 6 — 制作技巧（美术 + 跟 agent 沟通）
# ═════════════════════════════════════════════════════════════════════

# 31 视觉风格库
add("style-library", "Part 6 · 视觉风格库", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>Part 6 · 美术 · 视觉风格 menu</span>
<h2 class="title">从这里<em>挑一种</em>，<br/>不要从 0 设计。</h2>
<div class="grid" style="grid-template-columns: repeat(4, 1fr); gap: 14px;">
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">📣 漫画</span><h3 style="font-size: 16px; margin-bottom: 6px;">美式漫画 HUD</h3><p style="font-size: 12.5px; line-height: 1.5;">Bangers + 墨线 + 硬投影<br/><strong class="pink">Sky Leap · Shelf It · Block Party · Atomic</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">🧊 voxel</span><h3 style="font-size: 16px; margin-bottom: 6px;">Low-poly voxel A</h3><p style="font-size: 12.5px; line-height: 1.5;">软倒角 ≤ 4% / 三值受光<br/><strong class="pink">Sky Leap 角色 · Lowpoly Lab · Block Party 怪</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">🏙️ voxel</span><h3 style="font-size: 16px; margin-bottom: 6px;">Low-poly voxel B</h3><p style="font-size: 12.5px; line-height: 1.5;">锐利等距 / 平面着色<br/><strong class="pink">Shelf It · Block Hop · Helix Drop</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">💾 retro</span><h3 style="font-size: 16px; margin-bottom: 6px;">BSOD Pixel</h3><p style="font-size: 12.5px; line-height: 1.5;">暗复古游戏机 · CRT 扫描线<br/><strong class="pink">BSOD · Bell Tower · Crystal Ball Collective</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">💥 pop-art</span><h3 style="font-size: 16px; margin-bottom: 6px;">Comic Book BAM</h3><p style="font-size: 12.5px; line-height: 1.5;">halftone · Lichtenstein 风<br/><strong class="pink">Tag You're It · Mirror Pop</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">🕹️ 街机</span><h3 style="font-size: 16px; margin-bottom: 6px;">80s 街机绿 + 热粉</h3><p style="font-size: 12.5px; line-height: 1.5;">霓虹灯泡边框 / 单字体<br/><strong class="pink">Trash or Treasure · Confession Booth</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">💎 glass</span><h3 style="font-size: 16px; margin-bottom: 6px;">Liquid-glass 磨砂梦幻</h3><p style="font-size: 12.5px; line-height: 1.5;">Fredoka · 渐变粉<br/><strong class="pink">Sky Leap 后期 · Murmur · Spin Lock</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">📖 编辑</span><h3 style="font-size: 16px; margin-bottom: 6px;">Catalog 编辑杂志</h3><p style="font-size: 12.5px; line-height: 1.5;">邮购目录插画 / 烧字<br/><strong class="pink">Fit Check · Pulp Hour · Hour Capsule · The Couturier</strong></p></div>
</div>
""", """
<p>这一张是设计师的"视觉风格 menu"。<strong>新游戏几乎不应该从 0 设计风格</strong>——我们沉淀的 8 种风格各有标杆游戏可参考。</p>
<p>选风格之前先打开标杆游戏感受 10 分钟，比看 figma 截图有效 5 倍。</p>
<p>提醒：每个游戏选 1 种风格，不混搭。混搭 = 视觉混乱 = 被划走。</p>
""")


# 32 Voxel + Caricature 铁律
add("voxel-caricature", "Part 6 · Voxel + Caricature 铁律", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>美术 · 低多边形 + 文化符号</span>
  <h2 class="title">看起来精致<br/>vs <em>业余</em>的<br/>分水岭。</h2>
  <p class="sub" style="margin-top: 16px;"><strong class="pink">Voxel 7 条铁律</strong>（角色 / 道具通用）</p>
  <ul class="bullets" style="font-size: 14px;">
    <li>① 比例 <strong>1:1.3:1.5</strong>（头:躯干:腿）</li>
    <li>② 倒角 ≤ 4%（软倒角看起来"高级"）</li>
    <li>③ 三值受光 / 不要平面色</li>
    <li>④ 单一饱和强调色（其余降饱和）</li>
    <li>⑤ 接地阴影 + AO（圆形径向渐变 ≠ 椭圆裁切）</li>
    <li>⑥ 单一视觉语言（族 A 或族 B，不混）</li>
    <li>⑦ 细节 ≥ 1 体素（更小就砍）</li>
  </ul>
  <p class="micro pink" style="margin-top: 18px;">canonical: Lowpoly Lab familyA / familyB · 已 ship: Sky Leap / Block Hop / Block Party / Shelf It</p>
</div>
<div class="col-visual" style="flex-direction: column; gap: 14px; align-items: stretch;">
  <div style="background: var(--surface-2); border: 1px solid var(--brand-pink); border-radius: 16px; padding: 20px 22px;">
    <p class="micro pink" style="margin: 0 0 10px;">Crossy Road caricature · 5 铁律</p>
    <ul class="bullets" style="font-size: 13.5px; gap: 9px;">
      <li>① <strong>iconic 文化符号</strong>（甜甜圈 NYPD / FDNY / Notorious BIG / Fonzie），不是"穿戏服的人"</li>
      <li>② <strong>极端比例</strong>——把人变形到一眼认出</li>
      <li>③ <strong>emissive 自发光强调</strong>（哨子 / 麦克风 / 警徽）</li>
      <li>④ <strong>silhouette 单独看必须能认出</strong>——黑剪影测试</li>
      <li>⑤ <strong>extender</strong>（帽檐 / 大衣摆 / 大头戴）</li>
    </ul>
    <p style="margin: 14px 0 0; font-size: 12.5px; color: var(--text-3);">
    ❌ Shelf It v1-v3 因 silhouette 不可识别被否（普通人穿不同制服）<br/>
    ✅ v4 Crossy Road 文化 caricature 才过关
    </p>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px;">
    <img src="assets/posters/sky-leap.png" alt="" style="aspect-ratio: 1/1; object-fit: cover; border-radius: 8px;"/>
    <img src="assets/posters/block-hop.png" alt="" style="aspect-ratio: 1/1; object-fit: cover; border-radius: 8px;"/>
    <img src="assets/extra/block-party.png" alt="" style="aspect-ratio: 1/1; object-fit: cover; border-radius: 8px;"/>
  </div>
</div>
""", """
<p>这是设计师做角色 / 道具时的两组硬规则：<strong>左侧 voxel 7 条管"造型精致"，右侧 caricature 5 条管"文化辨识"</strong>。</p>
<p>讲一遍 Shelf It 角色 4 轮迭代史让同学体感——v3 还是被骂"silhouette 一样"，v4 改 Crossy Road 文化符号才过。
锚点用户原话：<strong>"天天过马路那样的审美倾向"</strong>。</p>
<p>提醒：sensory toy 类游戏可以违反 caricature 铁律（没有角色 roster），但 voxel 7 条铁律永远要守。</p>
""")


# 33 gen-image 实战技巧
add("gen-image-craft", "Part 6 · gen-image 实战技巧", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>美术 · gen-image 4 条实战</span>
<h2 class="title">出图<em>不翻车</em>的<br/>4 个钩子。</h2>
<div class="grid">
  <div class="cell">
    <span class="cell-num">1</span>
    <span class="tag">必带</span>
    <h3>测 plate prompt 一定带 ref_url</h3>
    <p>只测 txt2img 看似好，加 ref_url 后玩家原照被拼进画面 — <strong class="pink">Fit Check 真踩过</strong>。</p>
    <p style="margin-top:8px;" class="dim">同款坑：Build-a-Boyfriend tier 卡烧字、Hour Capsule MFG 时间戳。任何 plate 都 ref + 真照测一次。</p>
  </div>
  <div class="cell">
    <span class="cell-num">2</span>
    <span class="tag">前置</span>
    <h3>写风格 prompt 前先 Read 库</h3>
    <p>第一版风格 prompt 脑补不看库 → ship 立刻被骂"风格不一"——<strong class="pink">Kiss Wall 9 commit 中 5 个</strong>都是因此。</p>
    <p style="margin-top:8px;" class="dim">已有 asset 是真相，prompt 是描述。先 Read 后写，否则脑补必出错。同样适用于角色锚定（The Bidding · The Couturier · The Locksmith）。</p>
  </div>
  <div class="cell">
    <span class="cell-num">3</span>
    <span class="tag">身份钩</span>
    <h3>烧字进画面 = 身份钩 ②</h3>
    <p><strong class="pink">Hour Capsule</strong> <code>@user #00042</code> / <strong class="pink">Pulp Hour</strong> 红色 COMING NEXT chip / <strong class="pink">Build-a-Boyfriend</strong> tier 标签 / <strong class="pink">Daily Arcana</strong> 牌面 username。</p>
    <p style="margin-top:8px;" class="dim">SD 文字精度差 — 别依赖 prompt 精确出字，烧字用 HTML overlay 或 Canvas 后处理。</p>
  </div>
  <div class="cell">
    <span class="cell-num">4</span>
    <span class="tag">玩法</span>
    <h3>5-8s 等待 = 玩法</h3>
    <p>不是 spinner 糊过去：<strong class="pink">Kiss Wall</strong> 化学浴显影 · <strong class="pink">Hour Capsule</strong> sealing 工序耳语 · <strong class="pink">Fit Check</strong> developing 药丸 · <strong class="pink">Field Guide</strong> 翻档案动画。</p>
    <p style="margin-top:8px;" class="dim">范式 ⑥ 通用解：第一个输入 lock prompt → 进入显影 / 显形 / 拆封 / 翻档案的仪式。</p>
  </div>
</div>
""", """
<p>这一张是给已经听完 Part 3 / 4 的同学的"上手实战"。4 个钩子全部是真踩过坑总结的。</p>
<p>关键深度点：<strong>SD 文字渲染精度差 = 烧字一律走 HTML / Canvas overlay 层</strong>。Hour Capsule 的 MFG 时间戳 / Pulp Hour 的 chip 文案，所有"看似烧进图的字"实际都是 HTML 叠加在 gen-image 出的底图上。</p>
""")


# ═════════════════════════════════════════════════════════════════════
# Part 6 续 — 跟 agent 沟通
# ═════════════════════════════════════════════════════════════════════

# 34 Agent 沟通: 先看再做
add("agent-explore-first", "Part 6 · 跟 Agent · 先看再做", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Agent · 先看再做</span>
  <h2 class="title">让 agent <em>先看</em><br/>再让它<em>动手</em>。</h2>
  <p class="sub">
  Agent 最常翻车的不是写错代码，是<strong class="pink">没看现状直接动手</strong>——
  脑补一份风格、脑补一个 API、脑补一个 pattern。
  </p>
  <ul class="bullets" style="font-size: 15px;">
    <li>✅ <strong>"先 explore 这个游戏的 X，再决定怎么改"</strong> — 让它 Read 现有 asset / 现有代码 / 现有 skill</li>
    <li>✅ <strong>"看一下 [[score-beat-run-end-vs-sensory-toy]] 这个 pattern 怎么写的"</strong> — 用 skill 名当 anchor，比口头描述准</li>
    <li>✅ <strong>"参考 Kiss Wall 的 chemistry-bath develop 过程"</strong> — 给已上线游戏的 URL，比 PRD 强</li>
    <li>❌ "做一个像 X 的功能" — 漏掉了"先看 X 怎么做的"</li>
  </ul>
  <p class="sub" style="margin-top: 20px;">
  真实事故：<strong class="pink">Kiss Wall v1 prompt 脑补不看库</strong> → ship 立刻被骂；<strong class="pink">The Bidding Paula 不指定 head/body ratio</strong> → 11 岁角色被画成婴儿。
  都是"动手前没看"的代价。
  </p>
</div>
<div class="col-visual" style="height: 100%;">
  <img src="assets/gen/speak-to-agent.jpg" alt="A designer talking to an AI agent across a desk"
       style="max-height: 70vh; aspect-ratio: 1/1; width: auto; object-fit: cover;"/>
</div>
""", """
<p>这条是整个"跟 agent 沟通"章的总规则。其他规则都是它的展开。</p>
<p>讲法：让同学回想自己最近一次让 ChatGPT / Claude 做事翻车的场景——大多数时候是"我没让它先看，它脑补了"。
agent 写代码时也一样——你不让它 Read 库里现有 asset，它脑补一个看似合理的风格 → ship → 被打脸。</p>
<p>实际用法是给 agent 明确的"先 explore + 再 decide + 再 implement"三阶段。
explore 用 read-only agent (Explore subagent)，decide 用 Plan agent，implement 才 Edit/Write。</p>
""")


# 35 Agent 沟通: prompt 套路
add("agent-prompt-craft", "Part 6 · 跟 Agent · prompt 套路", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>Agent · 4 条 prompt 套路</span>
<h2 class="title">让 agent<br/>说话<em>像那个游戏</em>。</h2>
<div class="grid">
  <div class="cell">
    <span class="cell-num">1</span>
    <span class="tag">嗓音</span>
    <h3>system prompt 角色化</h3>
    <p>不要让 LLM 默认 ChatGPT-friendly 平淡嗓音。</p>
    <p style="margin-top:8px;" class="dim">✅ <strong class="pink">Trash or Treasure</strong> 温柔毒舌 / <strong class="pink">Hour Capsule</strong> 博物学家 / <strong class="pink">Pulp Hour</strong> 黑色一刻 / <strong class="pink">Daily Arcana</strong> 塔罗师 / <strong class="pink">The Locksmith</strong> 锁匠</p>
  </div>
  <div class="cell">
    <span class="cell-num">2</span>
    <span class="tag">锚点</span>
    <h3>4 层 elevator + skill 名当 anchor</h3>
    <p>把 idea 说成"身份钩 X + 范式 Y + skill [[Z]] pattern"。</p>
    <p style="margin-top:8px;" class="dim">例：<code>"做一个 sensory-toy + 身份钩 ④（网络）+ [[score-beat-run-end-vs-sensory-toy]]"</code> 比"做一个泡泡纸玩具，可以看到好友戳的次数"准 10 倍。</p>
  </div>
  <div class="cell">
    <span class="cell-num">3</span>
    <span class="tag">参考</span>
    <h3>给已上线游戏 URL + reference video</h3>
    <p>"像 Crossy Road 但角色是 X" / "像 Suika 但合成 X" / "像 Murmur 但触发是 Y"。</p>
    <p style="margin-top:8px;" class="dim">Build-a-Boyfriend = Suika fork · Block Hop = Crossy Road fork · Hour Capsule = Seal Press fork。<strong class="pink">让 agent 站在巨人肩膀上</strong>，不是从 0 写。</p>
  </div>
  <div class="cell">
    <span class="cell-num">4</span>
    <span class="tag">反馈</span>
    <h3>反馈语言模板化</h3>
    <p>同样的反馈短语对应不同 pattern：</p>
    <p style="margin-top:8px;" class="dim">"<strong>太复杂</strong>" → 砍规则 / 砍 setup<br/>"<strong>social 太弱</strong>" → 加 verb + notify<br/>"<strong>看不下去</strong>" → 砍卡通脸 sticker<br/>"<strong>没耐心</strong>" → 砍引导 / 用 1 个手指 icon<br/>"<strong>太平淡</strong>" → 加 visceral hit</p>
  </div>
</div>
""", """
<p>讲法：每条都给一个真实例子。<strong>第 4 条最有用</strong>——这些短语本身已经成为我们沟通的 ontology，agent 听到立刻知道往哪改。</p>
<p>建议同学把这 4 条 prompt 套路存进自己的 system prompt 模板，下次开 idea 时直接套。</p>
""")


# 36 Agent 沟通: build → verify, 不 build → claim
add("agent-build-verify", "Part 6 · 跟 Agent · build → verify", "callout", """
<span class="eyebrow"><span class="dot"></span>Agent · 最后一条最重要</span>
<p class="big-quote">
<em>"Build"</em> 不等于 <em>"Done"</em>。<br/>
让 agent <strong class="pink">自己跑 verify</strong>。
</p>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px; max-width: 1100px; margin: 36px auto 0;">
  <div class="cell" style="text-align: left; border-color: var(--danger);">
    <span class="tag danger">反例</span>
    <h3>Build → Claim done</h3>
    <p style="font-size: 14px;">"我做完了 X 功能 ✓"——但没跑测试、没 grep 验证、没 curl bundle 看是否真部署上去。</p>
    <p style="margin-top:8px; font-size: 13.5px; color: var(--text-3);">真实事故：<strong class="danger">2026-06-02 final-stream vs last-cigarette 同 UUID 撞车</strong> · <strong class="danger">2026-05-31 sweep 用 grep -l 漏 vital-signs</strong> · push 成功 ≠ deploy 成功</p>
  </div>
  <div class="cell" style="text-align: left; border-color: var(--ok);">
    <span class="tag ok">正解</span>
    <h3>Build → Verify → Ship</h3>
    <p style="font-size: 14px; margin-bottom: 8px;"><strong>Pre-ship 5 道 grep checkpoint</strong>：</p>
    <ol style="margin: 0; padding-left: 18px; color: var(--text-3); font-size: 13.5px; line-height: 1.7;">
      <li><code>grep -L</code> 找<strong class="ok">缺失</strong>，不是 <code>-l</code> 找存在</li>
      <li>Edit 后 grep 文件再 git add（防 stale no-op）</li>
      <li><code>git -C abs-path</code>，cwd 会漂</li>
      <li>curl bundle URL 验证新 class 在不在</li>
      <li>UUID 唯一性脚本通过</li>
    </ol>
  </div>
</div>
<p class="quote-attr" style="margin-top: 32px;">让 agent 走完 verify 再说 "done" · pre-ship-verify skill</p>
""", """
<p>这一张钉死整个 "agent 沟通"章的硬底线。讲的时候让同学问自己——
"我让 agent 做完事，我有没有让它<strong>验证</strong>？还是只接受了它说的 'done'？"</p>
<p>5 道 grep 是 2026-05-31 一整天踩坑后总结。Push 成功不等于 deploy 成功，这条具体可以演示：找一个游戏的 bundle URL，curl 一下看有没有最新 class，让同学体感。</p>
""")


# ═════════════════════════════════════════════════════════════════════
# Part 7 — 工作流 + 上线 checklist
# ═════════════════════════════════════════════════════════════════════

# 37 工作流时间轴
add("workflow", "Part 7 · 工作流时间轴", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>Part 7 · 一个 AlterU 游戏的诞生</span>
<h2 class="title">从立项<br/>到玩家实玩反馈。</h2>
<div class="grid" style="grid-template-columns: repeat(4, 1fr);">
  <div class="cell"><span class="cell-num">1</span><h3>立项 · 30秒</h3><p>Elevator pitch + <strong>4 层判断</strong>：身份钩在哪？内容怎么 AI-native？社交动词？范式归类？</p></div>
  <div class="cell"><span class="cell-num">2</span><h3>概念 · 1天</h3><p>3 张 mockup（首屏 / 玩中 / 结束）+ reference video + 范式 + 风格</p></div>
  <div class="cell"><span class="cell-num">3</span><h3>MVP · 3-5天</h3><p>Fork 范式标杆 → wipe UUID → 跑通 golden path · 不做美术/音效/社交</p></div>
  <div class="cell"><span class="cell-num">4</span><h3>Feel · 5-7天</h3><p>撞击 4 件套 + 音效 4 件套 + 视觉 polish · 决定"留存"的关键阶段</p></div>
  <div class="cell"><span class="cell-num">5</span><h3>社交化 · 2-3天</h3><p>身份钩 ④ 落地：leaderboard + notify + cross-user wall · <strong class="pink">day-one 烤进设计</strong>，不要补</p></div>
  <div class="cell"><span class="cell-num">6</span><h3>上线 · 半天</h3><p>UUID 唯一性 + meta.json + 海报 + push + 部署验证</p></div>
  <div class="cell"><span class="cell-num">7</span><h3>观察 · 持续</h3><p>用户实玩反馈 → 同类反馈 ≥ 2 次 = 设计层 bug，不是 polish</p></div>
  <div class="cell" style="background: var(--brand-pink-dim); border-color: var(--brand-pink); display: flex; flex-direction: column; justify-content: center;">
    <h3 class="pink">⚠️ 不要</h3>
    <p>跳第 5 步 → 社交化补的成本是 5× · useGameSave 数据结构要改一遍 · 已栽过太多次</p>
  </div>
</div>
""", """
<p>讲这一张时，让设计师感受到<strong>立项的 30 秒比 PRD 50 页有用</strong>。
Elevator pitch 不通过 4 层判断（身份钩 + AI-native + 社交动词 + 范式归类），不要进 MVP。</p>
""")

# 38 社交化必修
add("social-musts", "Part 7 · 社交化必修 4 招", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>Part 7 · day-one 烤进设计</span>
<h2 class="title">不管你做哪个范式，<br/>这 <em>4 招</em>必修。</h2>
<div class="grid">
  <div class="cell">
    <span class="cell-num">1</span>
    <h3>Score-beat notify</h3>
    <p>提交分数后，找到刚被超的人 → 推"你被 @xxx 超了"<br/><strong>有分数的游戏都有</strong>·已上线 14 个</p>
  </div>
  <div class="cell">
    <span class="cell-num">2</span>
    <h3>Feed needs a verb</h3>
    <p>浏览列表里每条都给一个动词（KEEP / ♥ / KISS）<br/>动词触发 publish + notify + 角标 + chip<br/><strong>有 wall/feed 的游戏都有</strong></p>
  </div>
  <div class="cell">
    <span class="cell-num">3</span>
    <h3>Cross-user wall</h3>
    <p>用 <code>save/get/data/list</code> 返回的"最近 6 用户存档"做跨用户 feed<br/><strong>能保留 artifact 的游戏都有</strong>（Daily Arcana / Pulp Hour / Hour Capsule）</p>
  </div>
  <div class="cell" style="border-color: var(--brand-pink);">
    <span class="cell-num">4</span>
    <h3>Notify 三铁律</h3>
    <p>✓ <strong>self-guard</strong>（不给自己发）<br/>✓ <strong>24h dedupe</strong>（同动作同对方 24h 1 次）<br/>✓ <strong>作者上限</strong>（单日 ≤ 5）</p>
  </div>
</div>
""", """
<p>反复强调：这 4 招不要"以后再加"。day-one 烤进设计。否则上线后再补社交=半个月+所有 useGameSave 数据结构要改一遍。这是真踩过的事故。</p>
""")

# 39 FAQ — 平台已经把上线工程化自动化了，所以原 checklist 不再适用，改成 FAQ
add("faq", "Part 7 · FAQ", "matrix-2x2", """
<span class="eyebrow"><span class="dot"></span>Part 7 · 散场前 · 常被问到的问题</span>
<h2 class="title">最后这 <em>6 个</em>，<br/>大家都会问。</h2>
<div class="grid" style="grid-template-columns: 1fr 1fr 1fr; gap: 14px; align-content: start;">
  <div class="cell" style="padding: 18px 18px 22px; border-color: var(--brand-pink); box-shadow: 0 0 0 1px var(--brand-pink-dim);">
    <span class="tag">Q1</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">我做完游戏怎么发布？</h3>
    <p style="font-size: 13px; line-height: 1.55;">在平台内预览页打开看效果 → 满意了点<strong class="pink">"发布"按钮</strong>。入库自动完成，不用碰 UUID / meta.json / 部署脚本。<strong>你只负责到"满意"为止</strong>。</p>
  </div>
  <div class="cell" style="padding: 18px 18px 22px;">
    <span class="tag">Q2</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">我必须用 AI 吗？</h3>
    <p style="font-size: 13px; line-height: 1.55;">不一定。<strong class="pink">Sensory toy</strong> 完全靠手做也很棒（Bubble Wrap / Marbles / Wind Chime）。但<strong>身份层 + 社交动词</strong>几乎不能少——否则不算 AlterU 游戏。</p>
  </div>
  <div class="cell" style="padding: 18px 18px 22px;">
    <span class="tag">Q3</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">5-8s 生图等待怎么办？</h3>
    <p style="font-size: 13px; line-height: 1.55;">等待<strong class="pink">变成玩法</strong>，不要 spinner 糊过去。化学浴显影 / 拆封 / 显形 / 翻档案的视觉仪式。Kiss Wall canonical 范式 ⑥。</p>
  </div>
  <div class="cell" style="padding: 18px 18px 22px;">
    <span class="tag">Q4</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">新手教程要不要做？</h3>
    <p style="font-size: 13px; line-height: 1.55;">不要。任何教程都假设玩家有耐心读 → 划走。<strong class="pink">第一次失败本身就是教程</strong>。Sky Leap 把充能环教学砍成 1 个共用手指 icon。</p>
  </div>
  <div class="cell" style="padding: 18px 18px 22px;">
    <span class="tag">Q5</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">用户反馈短语对应改什么？</h3>
    <p style="font-size: 12.5px; line-height: 1.6;">"<strong>太复杂</strong>" → 砍规则<br/>"<strong>social 太弱</strong>" → 加 verb + notify<br/>"<strong>看不下去</strong>" → 砍卡通脸贴纸<br/>"<strong>没耐心</strong>" → 砍引导 setup<br/>"<strong>太平淡</strong>" → 加 visceral 感官冲击</p>
  </div>
  <div class="cell" style="padding: 18px 18px 22px;">
    <span class="tag">Q6</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">不会编程能做吗？</h3>
    <p style="font-size: 13px; line-height: 1.55;">可以。AlterU 给 maker 两种<strong class="pink">零代码模式</strong>：<br/>① <strong>One sentence</strong> — 一句话描述,AI 补完美术 / 代码 / 声音 / 台词。<br/>② <strong>Remix</strong> — 从 feed 挑一个游戏,改规则 / 换世界,发布你的版本。</p>
  </div>
</div>
""", """
<p>这一节给学员"散场前确认"的机会。每个问题都是新人最常踩的疑虑。如果时间够，可以让每个 Q 让一两个学员说自己的理解，再给标准答案。</p>
<p><strong>Q1 是平台简化后的关键消息</strong>——很多老 deck 还在讲 UUID / meta.json / 部署脚本，实际上平台已经把这些自动化了。设计师/产品<strong>只负责到"满意"为止</strong>，点发布即入库。所以用粉色描边突出这一格。</p>
<p><strong>Q5 反馈语言模板</strong>是这套 deck 最实用的"日常工具"。建议同学保存进自己的 system prompt 模板，下次开 idea 时直接套。</p>
<p><strong>Q6 对应 landing 的 Makers 3-card</strong>（One sentence / Remix / Soon）。这是 maker 最大顾虑的问题——给他们"零门槛"心理安全感。如果讲师被问 "AlterU 和 Aigram 什么关系"：AlterU = 独立新品牌（试美国市场，App Store 端）；Aigram = 底层技术 infra（iframe 桥 + API）。对外只说 AlterU，Aigram 只在 endpoint 表里出现。这个不放进幻灯片，对外 maker 不需要知道。</p>
""")


# ═════════════════════════════════════════════════════════════════════
# 34 — Thank you / 资源
# ═════════════════════════════════════════════════════════════════════
add("resources", "Resources", "split", """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>End · Q&A + 资源</span>
  <h1 class="title">3 句话<br/><em>带走</em>。</h1>
  <ul class="bullets" style="font-size: 18px;">
    <li><strong>AlterU = identity-driven feed</strong> · 不是又一个 mini-game 集合。每个新 idea 先过 4 层判断。</li>
    <li><strong>AI 不是 spinner，是玩法</strong> · gen-image 5-8s 等待要变成显影 / 显形 / 拆封的仪式。</li>
    <li><strong>day-one 烤进社交化</strong> · Score-beat / Feed-needs-a-verb / Cross-user wall / Notify 不能上线后补。</li>
  </ul>
  <p class="sub" style="margin-top: 32px;"><strong>课后练习</strong>：挑一个你感兴趣的 idea，按 Slide 17 的 4 层模型 elevator 试一遍——身份钩在哪？内容怎么 AI-native？社交动词？范式？</p>
  <p class="micro" style="margin-top: 24px;">Resources · alteru.app · RUNTIME.md · 30+ 标杆游戏源码 · Q&A 现在开始</p>
</div>
<div class="col-visual">
  <img src="assets/worlds/hero-vista.png" alt="Hero vista"/>
</div>
""", """
<p>散场前 5 分钟，让同学把这 3 句默念一遍。然后留 30 分钟问答 + 现场 elevator 练习（让 2-3 个同学说自己的 idea 走 4 层判断）。</p>
<p>课后建议同学挑 2 个标杆游戏完整玩 30 分钟（推荐：Kiss Wall + Hour Capsule，覆盖最多深度点）。</p>
""")


# ═════════════════════════════════════════════════════════════════════
# HTML template + write files
# ═════════════════════════════════════════════════════════════════════

# ═════════════════════════════════════════════════════════════════════
# Helpers — part grouping, menu, outline
# ═════════════════════════════════════════════════════════════════════

import re


def filename(idx):
    if idx == 0:
        return "index.html"
    return f"{idx:02d}-{SLIDES[idx]['slug']}.html"


PART_LABEL_ZH = {
    "intro": "开场",
    "p1": "Part 1 · AlterU 是什么",
    "p2": "Part 2 · 身份层怎么落地",
    "p3": "Part 3 · 平台能力",
    "p4": "Part 4 · 7 个范式",
    "p5": "Part 5 · 设计原则",
    "p6": "Part 6 · 制作技巧",
    "p7": "Part 7 · 工作流",
    "end": "结尾",
}
PART_LABEL_EN = {
    "intro": "Intro",
    "p1": "Part 1 · What AlterU Is",
    "p2": "Part 2 · Identity Layer",
    "p3": "Part 3 · Platform Capabilities",
    "p4": "Part 4 · 7 Paradigms",
    "p5": "Part 5 · Design Principles",
    "p6": "Part 6 · Craft Tips",
    "p7": "Part 7 · Workflow",
    "end": "Resources",
}


def get_part_key(short):
    """Derive a part-key from the slide's `short` field (e.g. 'Part 3 · 平台能力')."""
    m = re.match(r'Part\s+(\d+)', short)
    if m:
        return f"p{m.group(1)}"
    if 'Cover' in short or 'Agenda' in short:
        return "intro"
    return "end"


def make_menu_html(current_idx, lang):
    """Render the contents drawer markup, with the current slide highlighted."""
    parts_order = ["intro", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "end"]
    by_part = {k: [] for k in parts_order}
    for idx, slide in enumerate(SLIDES):
        key = get_part_key(slide["short"])
        by_part.setdefault(key, []).append((idx, slide))

    labels = PART_LABEL_ZH if lang == "zh" else PART_LABEL_EN
    short_field = "short" if lang == "zh" else "short_en"

    rows = []
    for k in parts_order:
        items = by_part.get(k, [])
        if not items:
            continue
        rows.append(f'<div class="menu-section">')
        rows.append(f'<div class="menu-section-title">{labels.get(k, k)}</div>')
        for idx, slide in items:
            cls = "menu-item current" if idx == current_idx else "menu-item"
            short = slide.get(short_field, slide["short"])
            rows.append(
                f'<a class="{cls}" href="{filename(idx)}">'
                f'<span class="menu-num">{idx:02d}</span>'
                f'<span>{short}</span>'
                f'</a>'
            )
        rows.append('</div>')
    return "\n".join(rows)


def make_action_bar():
    return (
        '<div class="action-bar">\n'
        '  <a class="outline-link" href="outline.html" title="Overview">'
        '<span data-only="zh">大纲</span><span data-only="en">Outline</span></a>\n'
        '  <button class="menu-btn" id="menu-btn" title="Menu (M)">'
        '<span data-only="zh">菜单</span><span data-only="en">Menu</span></button>\n'
        '  <button class="lang-btn" id="lang-btn" title="Language (L)">'
        '<span class="lang-zh">中</span><span style="opacity:.4;margin:0 4px;">/</span>'
        '<span class="lang-en">EN</span></button>\n'
        '</div>\n'
    )


def make_drawer_html(current_idx):
    menu_zh = make_menu_html(current_idx, "zh")
    menu_en = make_menu_html(current_idx, "en")
    return f'''  <div class="menu-backdrop" id="menu-backdrop"></div>
  <aside class="menu-drawer" id="menu-drawer" aria-hidden="true">
    <div class="menu-head">
      <h3><span data-only="zh">目录</span><span data-only="en">Contents</span></h3>
      <button class="menu-close" id="menu-close">
        <span data-only="zh">关闭 esc</span><span data-only="en">Close esc</span>
      </button>
    </div>
    <div data-only="zh">
{menu_zh}
    </div>
    <div data-only="en">
{menu_en}
    </div>
    <div class="menu-foot">
      <span data-only="zh">快捷键：<kbd>M</kbd> 菜单 · <kbd>L</kbd> 中/EN · <kbd>S</kbd> 备忘 · <kbd>F</kbd> 全屏 · <kbd>← →</kbd> 翻页</span>
      <span data-only="en">Keys: <kbd>M</kbd> menu · <kbd>L</kbd> language · <kbd>S</kbd> speaker notes · <kbd>F</kbd> fullscreen · <kbd>← →</kbd> navigate</span>
    </div>
  </aside>
'''


PENDING_BADGE_EN = (
    '<div style="margin-bottom:16px;">'
    '<span class="pill" style="background:rgba(255,200,80,0.10); border-color:rgba(255,200,80,0.32); color:#ffcb55;">'
    'Translation in progress · showing 中文 fallback'
    '</span></div>'
)


PAGE_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-lang="zh">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="icon" type="image/svg+xml" href="assets/brand/alteru.svg" />
  <title>{N}/{T} · {short} · AlterU Training</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="_shared.css" />
  {prefetch_next}
  {prefetch_prev}
  <script>
    /* Apply lang BEFORE first paint to avoid flicker.
       Priority: URL ?lang=en|zh > localStorage > default zh.
       URL param also persists into localStorage so subsequent navigation
       inside the deck keeps the same lang. */
    (function(){{
      try {{
        var urlLang = new URLSearchParams(location.search).get('lang');
        var l;
        if (urlLang === 'en' || urlLang === 'zh') {{
          l = urlLang;
          localStorage.setItem('alteru-training-lang', l);
        }} else {{
          l = localStorage.getItem('alteru-training-lang') || 'zh';
        }}
        document.documentElement.setAttribute('data-lang', l);
      }} catch(e) {{}}
    }})();
  </script>
</head>
<body>
  <div class="slide-progress"><div class="fill" style="width: {progress:.2f}%"></div></div>

  <div class="brand-strip">
    <img src="assets/brand/alteru.svg" alt="AlterU"/>
    <span class="brand-name">AlterU</span>
    <span class="brand-sep"></span>
    <span class="brand-context">
      <span data-only="zh">{short}</span>
      <span data-only="en">{short_en}</span>
    </span>
  </div>

{action_bar}
{drawer}

  <section class="slide {layout}">
    <div data-only="zh">
{body}
    </div>
    <div data-only="en">
{body_en}
    </div>
  </section>

  <div class="speaker-notes" id="speaker-notes">
    <h4><span data-only="zh">{notes_label_zh}</span><span data-only="en">{notes_label_en}</span></h4>
    <div data-only="zh">
{notes}
    </div>
    <div data-only="en">
{notes_en}
    </div>
  </div>

  <div class="slide-page-tag">{N:02d} / {T:02d}</div>

  <div class="slide-nav">
    <a class="prev {prev_disabled}" href="{prev_href}">
      <span data-only="zh">← 上页</span><span data-only="en">← Prev</span>
    </a>
    <a class="next {next_disabled}" href="{next_href}">
      <span data-only="zh">下页 →</span><span data-only="en">Next →</span>
    </a>
  </div>

  <script>
    (function(){{
      const PREV = "{prev_href}";
      const NEXT = "{next_href}";
      const FIRST = "index.html";
      const LAST = "{last_href}";

      function setLangBtn(lang) {{
        document.querySelectorAll('.lang-btn .lang-zh, .lang-btn .lang-en').forEach(el => el.classList.remove('lang-active'));
        const target = document.querySelector('.lang-btn .lang-' + lang);
        if (target) target.classList.add('lang-active');
      }}
      function toggleLang() {{
        const cur = document.documentElement.getAttribute('data-lang') || 'zh';
        const next = cur === 'zh' ? 'en' : 'zh';
        document.documentElement.setAttribute('data-lang', next);
        try {{ localStorage.setItem('alteru-training-lang', next); }} catch(e) {{}}
        setLangBtn(next);
      }}
      setLangBtn(document.documentElement.getAttribute('data-lang') || 'zh');

      const drawer = document.getElementById('menu-drawer');
      const backdrop = document.getElementById('menu-backdrop');
      function toggleMenu() {{
        const open = drawer.classList.toggle('open');
        backdrop.classList.toggle('open', open);
        drawer.setAttribute('aria-hidden', open ? 'false' : 'true');
      }}
      function closeMenu() {{
        drawer.classList.remove('open');
        backdrop.classList.remove('open');
        drawer.setAttribute('aria-hidden', 'true');
      }}
      document.getElementById('menu-btn').addEventListener('click', toggleMenu);
      document.getElementById('menu-close').addEventListener('click', closeMenu);
      backdrop.addEventListener('click', closeMenu);
      document.getElementById('lang-btn').addEventListener('click', toggleLang);

      document.addEventListener('keydown', (e) => {{
        if (e.metaKey || e.ctrlKey || e.altKey) return;
        if (e.key === 'Escape') {{ closeMenu(); return; }}
        if (drawer.classList.contains('open') && (e.key === 'ArrowRight' || e.key === 'ArrowLeft' || e.key === 'ArrowUp' || e.key === 'ArrowDown' || e.key === ' ')) return;
        if (e.key === 'ArrowRight' || e.key === ' ' || e.key === 'PageDown' || e.key === 'ArrowDown') {{
          if (NEXT) location.href = NEXT;
        }} else if (e.key === 'ArrowLeft' || e.key === 'PageUp' || e.key === 'ArrowUp') {{
          if (PREV) location.href = PREV;
        }} else if (e.key === 's' || e.key === 'S') {{
          document.getElementById('speaker-notes').classList.toggle('visible');
        }} else if (e.key === 'f' || e.key === 'F') {{
          if (!document.fullscreenElement) document.documentElement.requestFullscreen();
          else document.exitFullscreen();
        }} else if (e.key === 'm' || e.key === 'M') {{
          toggleMenu();
        }} else if (e.key === 'l' || e.key === 'L') {{
          toggleLang();
        }} else if (e.key === 'o' || e.key === 'O') {{
          location.href = 'outline.html';
        }} else if (e.key === 'Home') {{
          location.href = FIRST;
        }} else if (e.key === 'End') {{
          location.href = LAST;
        }}
      }});
    }})();
  </script>
</body>
</html>
"""


OUTLINE_TEMPLATE = """<!DOCTYPE html>
<html lang="en" data-lang="zh">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <link rel="icon" type="image/svg+xml" href="assets/brand/alteru.svg" />
  <title>Outline · AlterU Training</title>
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;600;700;800;900&family=Inter:wght@400;500;600&family=JetBrains+Mono:wght@400;500&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="_shared.css" />
  <style>
    html, body {{ overflow: auto; height: auto; }}
    body {{ overflow-x: hidden; }}
  </style>
  <script>
    (function(){{
      try {{
        var l = localStorage.getItem('alteru-training-lang') || 'zh';
        document.documentElement.setAttribute('data-lang', l);
      }} catch(e) {{}}
    }})();
  </script>
</head>
<body>
  <div class="brand-strip">
    <img src="assets/brand/alteru.svg" alt="AlterU"/>
    <span class="brand-name">AlterU</span>
    <span class="brand-sep"></span>
    <span class="brand-context">
      <span data-only="zh">培训大纲</span>
      <span data-only="en">Training Outline</span>
    </span>
  </div>

  <div class="action-bar">
    <a class="outline-link" href="index.html" title="Back to deck">
      <span data-only="zh">回 deck</span><span data-only="en">Back to deck</span>
    </a>
    <button class="lang-btn" id="lang-btn">
      <span class="lang-zh">中</span><span style="opacity:.4;margin:0 4px;">/</span>
      <span class="lang-en">EN</span>
    </button>
  </div>

  <main class="outline-page">
    <div class="outline-head">
      <h1>
        <span data-only="zh">在 AlterU 上做一个<em>游戏</em>。</span>
        <span data-only="en">Building a game <em>on AlterU</em>.</span>
      </h1>
      <p>
        <span data-only="zh">{TOTAL} 张 slide 全貌 · 半天 3.5 小时 · 设计 + 产品向 · 点任意一张跳过去</span>
        <span data-only="en">All {TOTAL} slides · ~3.5 hours · Design + Product · Click any tile to open</span>
      </p>
    </div>

{parts_html}
  </main>

  <script>
    function setLangBtn(lang) {{
      document.querySelectorAll('.lang-btn .lang-zh, .lang-btn .lang-en').forEach(el => el.classList.remove('lang-active'));
      const t = document.querySelector('.lang-btn .lang-' + lang);
      if (t) t.classList.add('lang-active');
    }}
    function toggleLang() {{
      const cur = document.documentElement.getAttribute('data-lang') || 'zh';
      const next = cur === 'zh' ? 'en' : 'zh';
      document.documentElement.setAttribute('data-lang', next);
      try {{ localStorage.setItem('alteru-training-lang', next); }} catch(e) {{}}
      setLangBtn(next);
    }}
    setLangBtn(document.documentElement.getAttribute('data-lang') || 'zh');
    document.getElementById('lang-btn').addEventListener('click', toggleLang);

    /* Resize thumbnails to fit their tile width */
    function sizeThumb(frame) {{
      const iframe = frame.querySelector('iframe');
      if (!iframe) return;
      const w = frame.clientWidth;
      const scale = w / 1440;
      iframe.style.transform = 'scale(' + scale.toFixed(4) + ')';
      iframe.style.width = '1440px';
      iframe.style.height = '810px';
      frame.style.height = (810 * scale).toFixed(0) + 'px';
    }}
    function sizeAllThumbs() {{
      document.querySelectorAll('.outline-thumb .thumb-frame').forEach(sizeThumb);
    }}
    window.addEventListener('load', sizeAllThumbs);
    window.addEventListener('resize', sizeAllThumbs);

    /* Lazy-mount iframes that are still using data-src.
       Only when a thumb is within 600px of the viewport do we promote
       data-src → src, kicking off its HTML/CSS/image fetches. This drops
       the initial outline.html fetch graph from ~200 requests to ~20. */
    function mountThumb(thumb) {{
      const iframe = thumb.querySelector('iframe[data-src]');
      if (!iframe) return;
      iframe.src = iframe.dataset.src;
      iframe.removeAttribute('data-src');
      iframe.addEventListener('load', () => sizeThumb(thumb.querySelector('.thumb-frame')), {{ once: true }});
    }}
    if ('IntersectionObserver' in window) {{
      const io = new IntersectionObserver((entries) => {{
        entries.forEach(entry => {{
          if (entry.isIntersecting) {{
            mountThumb(entry.target);
            io.unobserve(entry.target);
          }}
        }});
      }}, {{ rootMargin: '600px 0px' }});
      document.querySelectorAll('.outline-thumb').forEach(t => {{
        if (t.querySelector('iframe[data-src]')) io.observe(t);
      }});
    }} else {{
      /* Fallback: just mount everything */
      document.querySelectorAll('.outline-thumb').forEach(mountThumb);
    }}

    document.addEventListener('keydown', (e) => {{
      if (e.key === 'l' || e.key === 'L') toggleLang();
      else if (e.key === 'Escape' || e.key === 'b' || e.key === 'B') location.href = 'index.html';
    }});
  </script>
</body>
</html>
"""


def make_outline_parts_html():
    parts_order = ["intro", "p1", "p2", "p3", "p4", "p5", "p6", "p7", "end"]
    by_part = {k: [] for k in parts_order}
    for idx, slide in enumerate(SLIDES):
        key = get_part_key(slide["short"])
        by_part.setdefault(key, []).append((idx, slide))

    blocks = []
    part_num = 0
    for k in parts_order:
        items = by_part.get(k, [])
        if not items:
            continue
        part_num += 1
        label_zh = PART_LABEL_ZH.get(k, k)
        label_en = PART_LABEL_EN.get(k, k)
        blocks.append(f'<section class="outline-part">')
        blocks.append(f'  <div class="outline-part-head">')
        blocks.append(f'    <span class="num">§ {part_num:02d}</span>')
        blocks.append(f'    <h2><span data-only="zh">{label_zh}</span><span data-only="en">{label_en}</span></h2>')
        blocks.append(f'  </div>')
        blocks.append(f'  <div class="outline-grid">')
        for idx, slide in items:
            fname = filename(idx)
            short_zh = slide["short"]
            short_en = slide["short_en"]
            # IntersectionObserver-style lazy mount: only embed iframe src for
            # the first 4 thumbnails; the rest carry data-src and are upgraded
            # to live iframes as they scroll into view. This stops the page
            # from kicking off 41 simultaneous HTML fetches on initial load.
            iframe_attrs = (
                f'src="{fname}"' if idx < 4
                else f'data-src="{fname}"'
            )
            blocks.append(
                f'<a class="outline-thumb" href="{fname}">'
                f'<div class="thumb-frame">'
                f'<iframe {iframe_attrs} loading="lazy" scrolling="no" tabindex="-1" aria-hidden="true"></iframe>'
                f'</div>'
                f'<div class="thumb-meta">'
                f'<span class="thumb-num">{idx:02d}</span>'
                f'<span class="thumb-title"><span data-only="zh">{short_zh}</span><span data-only="en">{short_en}</span></span>'
                f'</div>'
                f'</a>'
            )
        blocks.append('  </div>')
        blocks.append('</section>')
    return "\n".join(blocks)


def main(mode="external"):
    """mode = 'external' (default, polished for makers) or 'internal' (trainer
    edition with explicit 'speaker notes' label). The two modes share the same
    SLIDES content; only the notes-label chrome differs. Internal mode is
    emitted into ./internal/ so both versions can be served side-by-side."""
    # Patch SLIDES with English translations from translations.py
    try:
        import translations
        translations.apply(SLIDES)
    except Exception as e:
        print(f"[warn] translations.apply failed: {e}")

    base = Path("/Users/yin/alteru-training")
    out_dir = base if mode == "external" else (base / "internal")
    out_dir.mkdir(parents=True, exist_ok=True)
    T = len(SLIDES)

    if mode == "internal":
        notes_label_zh = "讲师备忘 · 按 S 关闭"
        notes_label_en = "Speaker Notes · S to close"
    else:
        notes_label_zh = "备忘 · 按 S 关闭"
        notes_label_en = "Notes · S to close"

    for idx, slide in enumerate(SLIDES):
        prev_href = filename(idx - 1) if idx > 0 else ""
        next_href = filename(idx + 1) if idx < T - 1 else ""
        prev_disabled = "disabled" if not prev_href else ""
        next_disabled = "disabled" if not next_href else ""
        progress = (idx + 1) / T * 100
        last_href = filename(T - 1)

        notes_zh = slide["notes"].strip() or '<p class="dim">（这一页没有额外备忘）</p>'
        if slide.get("notes_en"):
            notes_en = slide["notes_en"].strip()
        else:
            notes_en = '<p class="dim">(No additional notes for this slide.)</p>'

        if slide.get("body_en"):
            body_en = slide["body_en"].strip()
        else:
            body_en = PENDING_BADGE_EN + slide["body"].strip()

        # Prefetch the adjacent slides so navigation feels instant. Browsers
        # treat rel=prefetch as low-priority, so it doesn't compete with
        # current-page critical resources.
        prefetch_next = f'<link rel="prefetch" href="{next_href}" as="document">' if next_href else ""
        prefetch_prev = f'<link rel="prefetch" href="{prev_href}" as="document">' if prev_href else ""

        page = PAGE_TEMPLATE.format(
            N=idx + 1, T=T,
            short=slide["short"],
            short_en=slide["short_en"],
            layout=slide["layout"],
            body=slide["body"].strip(),
            body_en=body_en,
            notes=notes_zh,
            notes_en=notes_en,
            notes_label_zh=notes_label_zh,
            notes_label_en=notes_label_en,
            prev_href=prev_href,
            next_href=next_href,
            prev_disabled=prev_disabled,
            next_disabled=next_disabled,
            progress=progress,
            last_href=last_href,
            action_bar=make_action_bar(),
            drawer=make_drawer_html(idx),
            prefetch_next=prefetch_next,
            prefetch_prev=prefetch_prev,
        )

        # Auto-add loading="lazy" + decoding="async" to <img> tags that don't
        # already specify them. Cover (idx 0) keeps eager — hero needs to be
        # paintable at first frame.
        if idx > 0:
            page = re.sub(
                r'<img(?![^>]*\bloading=)([^>]*)>',
                r'<img loading="lazy" decoding="async"\1>',
                page,
            )

        if mode == "internal":
            page = (page
                    .replace('href="_shared.css"', 'href="../_shared.css"')
                    .replace('src="assets/', 'src="../assets/')
                    .replace('href="assets/', 'href="../assets/'))

        fname = filename(idx)
        (out_dir / fname).write_text(page, encoding="utf-8")
        numbered = f"{idx:02d}-{slide['slug']}.html"
        if fname != numbered:
            (out_dir / numbered).write_text(page, encoding="utf-8")

    # Outline page
    outline_html = OUTLINE_TEMPLATE.format(
        TOTAL=T,
        parts_html=make_outline_parts_html(),
    )
    if mode == "internal":
        outline_html = (outline_html
                        .replace('href="_shared.css"', 'href="../_shared.css"')
                        .replace('src="assets/', 'src="../assets/')
                        .replace('href="assets/', 'href="../assets/')
                        .replace('href="index.html"', 'href="index.html"'))  # stay in /internal/
    (out_dir / "outline.html").write_text(outline_html, encoding="utf-8")

    # README
    nav_md = ["# AlterU Training Slides\n",
              f"**{T} 张 slide · 半天 3.5 小时**\n\n",
              "## 入口\n",
              "- `index.html` — 演讲入口（cover）\n",
              "- `outline.html` — 全貌大纲页（缩略图预览）\n\n",
              "## 翻页 / 快捷键\n",
              "- `← / →` 或 `↑ / ↓` · `Space` — 翻页\n",
              "- `M` — 目录抽屉 · `O` — 大纲页 · `Esc` — 关闭抽屉\n",
              "- `L` — 中 / EN 切换（localStorage 记忆）\n",
              "- `F` — 全屏 · `S` — 讲师备忘 · `Home / End` — 首 / 尾\n\n",
              "## 顺序\n"]
    for idx, slide in enumerate(SLIDES):
        nav_md.append(f"- {idx:02d} · `{filename(idx)}` — {slide['short']}\n")
    (out_dir / "README.md").write_text("".join(nav_md), encoding="utf-8")

    print(f"Wrote {T} slides + outline.html + README.md to {out_dir}")


if __name__ == "__main__":
    main(mode="external")
    main(mode="internal")
