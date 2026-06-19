"""English translations for AlterU training slides.

Each entry maps a slide slug to its EN short title, body HTML, and speaker notes.
build.py imports this and patches SLIDES[i]['short_en' / 'body_en' / 'notes_en']
when a translation exists.

Translation style: kept tight (title + 1 sub + key bullets), preserving the
core teaching point of each slide. Chinese deck still has the full narrative
and game-specific anecdotes — English version is the lecture-ready essence.
"""

TR = {

# ───── Intro ────────────────────────────────────────────────────────
"cover": {"short": "Cover"},  # already inlined in build.py
"agenda": {"short": "Agenda"},  # already inlined

# ───── Part 1 · What AlterU Is ──────────────────────────────────────
"positioning": {"short": "Part 1 · Positioning"},  # already inlined

"four-layers": {
    "short": "Part 1 · 4 Layers",
    "body": """
<span class="eyebrow"><span class="dot"></span>Part 1 · The 4-layer model</span>
<h2 class="title">Strip AlterU outside-in.<br/><em>Only layer 2</em> is the real differentiator.</h2>
<div class="grid">
  <div class="cell"><span class="cell-num">1</span><span class="tag">felt</span><h3>Form</h3><p>TikTok-style vertical scroll feed. Users just <strong>feel</strong> this layer. Never put it in the hero copy — every mini-game collection can claim it.</p></div>
  <div class="cell" style="border-color: var(--brand-pink); box-shadow: 0 0 0 1px var(--brand-pink-dim), 0 18px 40px rgba(245,177,199,0.10);"><span class="cell-num">2</span><span class="tag">🔑 differentiator</span><h3>Identity</h3><p>Your AI self walks into <strong>other people's</strong> games — bartender / locksmith / boss / neighbour. Cross-user identity is the <strong class="pink">only</strong> real gap between AlterU and any generic mini-game collection.</p></div>
  <div class="cell"><span class="cell-num">3</span><span class="tag">artifact</span><h3>Content</h3><p>AI-native (vision / gen-image / LLM) + <strong>hand-made</strong>. Every game has an author voice — never procedural slop. Mixed register: After Dark FMV → sensory toys → action.</p></div>
  <div class="cell"><span class="cell-num">4</span><span class="tag">mechanic</span><h3>Social</h3><p>Feed-as-verb. Touch someone's content → notify them. score_beat, "kept your stone," cross-game notify. Director-mandated focus, kept off the landing page.</p></div>
</div>
""",
    "notes": """
<p>Nail this immediately: <strong>the Form layer is felt, not claimed</strong>. Saying "we are a TikTok-style game feed" is as empty as saying "we are an app with a news feed."</p>
<p>Every product decision, gameplay choice, and visual rule downstream of this slide should be reverse-engineered from "<strong>where is this game's identity layer?</strong>" Part 2 unpacks it.</p>
""",
},

"form-layer": {
    "short": "Part 1 · Form Layer",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Layer 1 · Form</span>
  <h2 class="title">TikTok full-screen,<br/>vertical scroll <em>feed</em>.</h2>
  <p class="sub">
    Players don't "open" a game — they <strong>swipe into</strong> one. One game per screen.
    Swipe down for new, up for the last one. Same physics as TikTok.
  </p>
  <ul class="bullets">
    <li><strong>~2 seconds and they swipe away</strong> · people on the bus, in queues, in bed</li>
    <li>Zero context, zero tutorial patience, near-zero attention</li>
    <li>They read images / motion / feedback — not text</li>
    <li><span class="dim">This is the substrate. Not a selling point.</span></li>
  </ul>
</div>
<div class="col-visual">
  <img src="assets/worlds/crossover-seam-vertical.png" alt="vertical scroll feed seam"/>
</div>
""",
    "notes": """
<p>Have the room close their eyes and recall last night's TikTok session — swipe through two ads, swipe past one confusing thing, stop for five seconds on something interesting. <strong>Our games need to be in that "next thing" bucket.</strong></p>
<p>Every "golden 2 seconds" rule downstream is derived from this slide.</p>
""",
},

"identity-layer": {
    "short": "Part 1 · Identity 🔑",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Layer 2 · Identity · the only differentiator</span>
  <h2 class="title">Your AI self<br/>walks <em>into</em><br/>other people's games.</h2>
  <p class="sub">
    Your avatar, your work, the people you follow — <strong>all of them show up inside the games</strong>.
    As bosses, NPCs, the face on a kiss wall, the neighbour in a block-hop.
  </p>
  <p class="sub">
    <strong class="pink">Every scroll is personal in a way TikTok can only fake.</strong>
  </p>
  <p class="micro">— alteru.app · identity section</p>
</div>
<div class="col-visual">
  <img src="assets/identity/walks-in.png" alt="A character walking into a game world"/>
</div>
""",
    "notes": """
<p>This is the spine of the entire deck. Read the landing copy aloud — twice.</p>
<p>Anchor for comparison: Instagram's feed is <strong>about you</strong> (people you follow); TikTok's feed is <strong>for you</strong> (algorithm-picked). AlterU's feed has <strong>you inside it</strong> — you're a character in someone else's game.</p>
<p>"TikTok can only fake" is the sharp line: their personalization lives at the algorithm layer. Ours lives at the <strong>content layer</strong> — your face is in the actual game art. Use this as the litmus test for every product decision.</p>
""",
},

"content-social": {
    "short": "Part 1 · Content + Social",
    "body": """
<span class="eyebrow"><span class="dot"></span>Layer 3 · Layer 4</span>
<h2 class="title">Content + social =<br/>making the identity layer<br/><em>actually live</em>.</h2>
<div class="grid">
  <div class="cell">
    <span class="tag">Layer 3 · Content</span>
    <h3>AI-native + hand-made</h3>
    <p><strong>AI-native</strong>: vision sees your stuff, gen-image renders pictures of you, LLM writes lines about you.</p>
    <p style="margin-top:8px;"><strong>Hand-made</strong>: every game has an <strong class="pink">author voice</strong>. Never procedural slop. Mixed register: After Dark noir FMV, sensory toys, action, daily collectibles — all sit side by side in the feed.</p>
  </div>
  <div class="cell">
    <span class="tag">Layer 4 · Social</span>
    <h3>Feed-as-verb</h3>
    <p>Browsing ≠ tapping ♥. <strong>Touch someone's content → notify them.</strong></p>
    <p style="margin-top:8px;">Shipped patterns:<br/>· score_beat: "You just got passed by @xxx"<br/>· kept your stone (Pebble Pocket)<br/>· kissed your portrait (Kiss Wall)<br/>· marked your card (Daily Arcana)<br/>· cross-game notify chains</p>
  </div>
  <div class="cell" style="grid-column: span 2; background: var(--surface-1); border: 0;">
    <p class="sub" style="max-width: none; margin: 0;">
    👉 <strong class="pink">The litmus test:</strong> when you pitch a new AlterU game, you should be able to answer —
    "Where's the <strong>identity hook</strong>? Is the <strong>content</strong> AI-written or hand-crafted? What's the <strong>social verb</strong>?"
    If you can't, it's just a mini-game, not an AlterU game.
    </p>
  </div>
</div>
""",
    "notes": """
<p>Layers 3 and 4 aren't unique to AlterU on their own — what they do is <strong>let layer 2 actually live</strong>. Without AI-native content, identity collapses into a sticker-face hack. Without a social verb, players never realize they're inside someone else's game.</p>
""",
},

# ───── Part 2 · Identity Layer ──────────────────────────────────────
"identity-hooks": {
    "short": "Part 2 · 4 Identity Hooks",
    "body": """
<span class="eyebrow"><span class="dot"></span>Part 2 · making the identity layer real</span>
<h2 class="title">Unpack "identity"<br/>into <em>4 hooks</em>.</h2>
<div class="grid">
  <div class="cell"><span class="cell-num">1</span><span class="tag">body hook</span><h3>Your face · your portrait</h3><p>Kiss Wall's kiss illustrations use your portrait via img2img; Block Hop's shop lets you play "as you." <br/><strong>Strongest, hardest to do right</strong> — done wrong it becomes sticker face.</p></div>
  <div class="cell"><span class="cell-num">2</span><span class="tag">artifact hook</span><h3>Your work shows up</h3><p>Hour Capsule stamps <span class="pink">@username #00042</span> onto every vacuum-sealed bag; Daily Arcana cards land on the Wall; Pebble Pocket stones float into the Tide feed.</p></div>
  <div class="cell"><span class="cell-num">3</span><span class="tag">environment hook</span><h3>AI sees your stuff</h3><p>Trash or Treasure shoots your desk; Fit Check shoots your closet; Field Guide shoots whatever's nearby. The vision pipeline gives the <strong class="pink">strongest sense of ownership</strong> — you handed the AI something real.</p></div>
  <div class="cell"><span class="cell-num">4</span><span class="tag">network hook</span><h3>People you follow appear</h3><p>Cross-user wall (save/get/data/list pulls the last 6 users); leaderboard rows that tap into a profile; notify chains that surface "you showed up at a friend's place."</p></div>
</div>
""",
    "notes": """
<p>The four hooks aren't pick-one — they're a <strong>combo platter</strong>. A complete AlterU game usually fires 2-3 of them.</p>
<p>Examples: Kiss Wall = ① body + ④ network. Hour Capsule = ② artifact + ④ network.</p>
<p>Designers can use the 2x2 as a brainstorm matrix: every idea must hit at least one hook. Misses none = not yet an AlterU game.</p>
""",
},

"case-kiss-wall": {
    "short": "Part 2 · Case · Kiss Wall",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Identity case · Kiss Wall</span>
  <h2 class="title">Kiss someone's portrait.<br/>AI <em>folds your face</em> in.</h2>
  <ul class="bullets">
    <li><strong>First kiss locks the prompt</strong> → gen-image uses the other person's portrait as ref, outputs a duet plate</li>
    <li><strong>Wait = play</strong>: 2.6s "darkroom develop" replaces the spinner (img starts at blur(12px) brightness(0.18), eases to 1.0)</li>
    <li><strong>SVG filter chain</strong> (feTurbulence + Gaussian + displacement) makes geometric edges feel chemical</li>
    <li><strong>Silver-gelatin lock</strong>: monochrome by UX choice (not aesthetic), so pink UI overlays read against the plate</li>
    <li><strong>Identity hook ①</strong> (your face) + <strong>hook ④</strong> (kiss someone's plate → notify the author)</li>
  </ul>
  <p class="micro pink" style="margin-top: 24px;">UUID 7a5b620c · shipped in 9 commits, one day</p>
</div>
<div class="col-visual">
  <img src="assets/posters/kiss-wall.png" alt="Kiss Wall poster"/>
</div>
""",
    "notes": """
<p>Key talking point: <strong>you cannot hide a 5-8s gen-image call behind a spinner — the wait itself has to be the play</strong>. The chemistry-bath develop is a generalizable pattern for every gen-image game.</p>
<p>Real-world lesson: v1 had a SEAL button + curtain. Player feedback was literal: "the interaction is awful." We cut SEAL, and only then did we land on the darkroom-develop ritual.</p>
""",
},

"case-hour-capsule": {
    "short": "Part 2 · Case · Hour Capsule",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Identity case · Hour Capsule</span>
  <h2 class="title">Every hour,<br/>we seal a <em>vacuum bag</em> for you.</h2>
  <ul class="bullets">
    <li>LLM picks the hour's subject + gen-image bakes a real MFG timestamp into the bag</li>
    <li>Bottom-left of every bag: <span class="pink">@username #00042</span> ownership stamp</li>
    <li>3-tier rarity (80/15/5, silver/gold α + flourish)</li>
    <li><strong>Real news ticker</strong>: HN headlines surface as "FROM THE WIRE" hero strip, frozen into the artifact</li>
    <li><strong>Identity ②</strong> (stamp baked into the picture) + <strong>④</strong> (Wall shows your friends' bags this hour)</li>
    <li><strong>Demo mode canon</strong>: open the URL outside Aigram and the core loop still works — it's a real demo, not a fallback landing</li>
  </ul>
  <p class="micro pink" style="margin-top: 24px;">UUID d62fb4ed · forked from Seal Press</p>
</div>
<div class="col-visual">
  <img src="assets/posters/hour-capsule.png" alt="Hour Capsule poster"/>
</div>
""",
    "notes": """
<p>Hour Capsule packs the most teaching value: it threads <strong>all four AI primitives</strong> — LLM picks subject → gen-image bakes the bag → external fetch grabs HN news → upload stores the artifact — and shows how to bake an identity stamp into the picture.</p>
<p>Deep point: <strong>freeze-backstage-with-artifact</strong> — the HN news has to be frozen into the capsule itself, not re-fetched on view. Otherwise re-opening the bag later loses the news. Once you grok this it sticks forever.</p>
""",
},

"case-blockhop-arcana": {
    "short": "Part 2 · Case · Block Hop + Daily Arcana",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Identity case · two routes</span>
  <h2 class="title">Same identity layer,<br/><em>different</em> surfaces.</h2>
  <div style="margin-top: 16px;">
    <span class="tag">Block Hop · isometric voxel</span>
    <h3 style="font-family: Montserrat; margin: 10px 0 8px; font-size: 19px; color: var(--text-1);">Hook ①: become a voxel character</h3>
    <p style="font-size: 14px; line-height: 1.55; color: var(--text-3); margin: 0;">30-character shop — <strong style="color: var(--text-1);">Crossy Road cultural caricature</strong>, not "regular people in different uniforms." Shelf It v3 got rejected over silhouette parity; v4 finally cleared the bar.</p>
  </div>
  <div style="margin-top: 24px;">
    <span class="tag">Daily Arcana · private mechanic</span>
    <h3 style="font-family: Montserrat; margin: 10px 0 8px; font-size: 19px; color: var(--text-1);">Hook ② + ④: your card lands on the Wall</h3>
    <p style="font-size: 14px; line-height: 1.55; color: var(--text-3); margin: 0;"><strong style="color: var(--text-1);">v1 was fully private</strong> — every card was only seen by the drawer → social value zero. The D-suite retrofit: auto-publish + ♥ + notify, turning a <strong style="color: var(--text-1);">private toy into a social content engine overnight</strong>.</p>
  </div>
</div>
<div class="col-visual" style="display: grid; grid-template-rows: 1fr 1fr; gap: 16px; height: 70vh; max-height: 660px; align-items: stretch;">
  <div style="overflow: hidden; border-radius: 14px; box-shadow: 0 20px 50px rgba(0,0,0,0.55);"><img src="assets/posters/block-hop.png" alt="Block Hop" style="width: 100%; height: 100%; object-fit: cover; display: block;"/></div>
  <div style="overflow: hidden; border-radius: 14px; box-shadow: 0 20px 50px rgba(0,0,0,0.55);"><img src="assets/extra/daily-arcana.png" alt="Daily Arcana" style="width: 100%; height: 100%; object-fit: cover; display: block;"/></div>
</div>
""",
    "notes": """
<p>The contrast: <strong>the identity layer doesn't have to surface your face</strong>. Block Hop lets you play <em>as a cultural symbol</em> — that counts. Daily Arcana shoves your card onto a shared Wall — also identity.</p>
<p>Reminder: a lot of designers ship Daily Arcana v1 (private draw) and think they're done — they've missed hook ④ (network), making it a single-player toy.</p>
""",
},

"fake-identity": {
    "short": "Part 2 · Anti-pattern · Fake Identity",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>When identity is <em class="pink">fake</em></span>
  <h2 class="title">Stickering on a face<br/><em>doesn't count</em>.</h2>
  <ul class="bullets">
    <li><strong class="danger">Sticker face / cartoon decals</strong> — paste ≠ fold-in. Hold-it-Together v1 and early Build-a-Boyfriend both got rejected here</li>
    <li><strong class="danger">Avatar only in the HUD corner</strong> — if it's not in the playfield, it's not identity</li>
    <li><strong class="danger">Your name as a text bubble</strong> — text layer ≠ visual layer</li>
    <li><strong class="ok">Real fold-in</strong>: img2img / baked-into-picture / voxel restyled to you / cast as NPC / cast as boss</li>
  </ul>
  <p class="sub" style="margin-top: 24px;">
  Litmus: <strong class="pink">turn off the user's avatar — does the game still hold up?</strong>
  If yes, identity was decoration, not the design.
  </p>
</div>
<div class="col-visual">
  <img src="assets/extra/hold-it-together.png" alt="Hold It Together v2"/>
</div>
""",
    "notes": """
<p>This slide separates "identity layer" from "decoration." Walk through Hold-it-Together: v1 was Reigns + cartoon sticker face — player verdict "can't watch this." Root cause: sticker is decoration, not real fold-in. v2 (stacked stress tower in matter-js) plays well — but identity has <strong>receded to abstract</strong> ("your inner state collapsing"), no concrete face anywhere.</p>
<p>So the rule isn't "you must have a face." It's <strong>don't fake the identity layer</strong>. Either commit to it or remove it.</p>
""",
},

# ───── Part 3 · Platform Capabilities ───────────────────────────────
"platform-overview": {
    "short": "Part 3 · Platform Capabilities",
    "body": """
<span class="eyebrow"><span class="dot"></span>Part 3 · what the platform hands you</span>
<h2 class="title">An AI quartet +<br/>4 <em>data primitives</em>.</h2>
<div class="grid" style="grid-template-columns: repeat(4, 1fr); gap: 14px;">
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">AI</span><h3 style="font-size: 17px; margin-bottom: 8px;">🎨 gen-image</h3><p style="font-size: 13px; line-height: 1.5;">txt2img / img2img · ~5-8s · burn-in works inside the safe 74% center band</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">AI</span><h3 style="font-size: 17px; margin-bottom: 8px;">💬 game-chat</h3><p style="font-size: 13px; line-height: 1.5;">OpenAI-compatible LLM · ~2-4s · system prompt sets the voice</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">AI</span><h3 style="font-size: 17px; margin-bottom: 8px;">👁️ recognize</h3><p style="font-size: 13px; line-height: 1.5;">See the picture → labels / attributes / parts / caption · ~2-5s</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">AI</span><h3 style="font-size: 17px; margin-bottom: 8px;">☁️ upload</h3><p style="font-size: 13px; line-height: 1.5;">blob → R2 public URL · ~1-2s · feed it back into gen-image / recognize</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">DATA</span><h3 style="font-size: 17px; margin-bottom: 8px;">🏆 leaderboard</h3><p style="font-size: 13px; line-height: 1.5;">One board per game · tap a row → open their profile · "Champion pill" pattern</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">DATA</span><h3 style="font-size: 17px; margin-bottom: 8px;">💾 cloud save</h3><p style="font-size: 13px; line-height: 1.5;">session_id-keyed · returns the last 6 users' saves = cross-user wall for free</p></div>
  <div class="cell" style="padding: 18px 18px 20px;"><span class="tag">DATA</span><h3 style="font-size: 17px; margin-bottom: 8px;">📊 events / stats</h3><p style="font-size: 13px; line-height: 1.5;">day_click_count · continuous_days · daily-once / streak mechanics</p></div>
  <div class="cell" style="padding: 18px 18px 20px; border-color: var(--brand-pink);"><span class="tag">DATA</span><h3 style="font-size: 17px; margin-bottom: 8px;">🔔 cross-user notify</h3><p style="font-size: 13px; line-height: 1.5;">Touched someone's content → push them a note · self-guard + 24h dedupe + daily cap</p></div>
</div>
""",
    "notes": """
<p>Designers don't need to memorize endpoints. They need to <strong>know what the box can do</strong>: paint, talk, see, remember, alert. The next 6 slides drill into each with a real game.</p>
<p>Tech ref (if asked): all four AI ops POST to <code>chat.aiwaves.tech/aigram/api/{gen-image, game-chat, recognize, upload}</code>. CORS is <code>*</code>, so games run in any browser origin — that's the demo-mode foundation.</p>
""",
},

"gen-image": {
    "short": "Part 3 · gen-image",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Capability · gen-image</span>
  <h2 class="title">Text or image in,<br/>picture out in <em>5-8s</em>.</h2>
  <ul class="bullets">
    <li><strong>txt2img</strong>: prompt → one 1:1 image</li>
    <li><strong>img2img</strong>: ref image + prompt → restyled variant (the engine for hook ①)</li>
    <li><strong>Burn-in is unreliable</strong>: SD can't render text crisply — never depend on the prompt to spell anything correctly</li>
    <li><span class="danger">⚠️ Test every plate <strong>with ref_url</strong></span> · txt2img-only tests can pass while img2img stitches the player's photo straight into the frame (Fit Check lesson)</li>
    <li><strong>Baking text into the picture</strong> is an AlterU signature — Hour Capsule <code>@user #00042</code>, Pulp Hour cover lines, Build-a-Boyfriend tier tags</li>
  </ul>
  <p class="micro pink" style="margin-top: 24px;">The 5-8s wait is a <strong>play opportunity</strong>, not a loading state — see paradigm 6.</p>
</div>
<div class="col-visual">
  <img src="assets/posters/hour-capsule.png" alt="Hour Capsule (gen-image showcase)"/>
</div>
""",
    "notes": """
<p>Drill the point: <strong>5-8 seconds is a UX window, not an engineering parameter</strong>. Treated as loading → user swipes. Treated as play → user lingers another 5s. Kiss Wall and Hour Capsule both turn it into a develop ritual.</p>
<p>Deeper note: <strong>baked text = the simplest implementation of identity hook ② (artifact)</strong>. Any "thing you made" can be upgraded to "a thing with your stamp on it" by burning in a username + index.</p>
""",
},

"vision": {
    "short": "Part 3 · Vision",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Capability · recognize (vision)</span>
  <h2 class="title">Let AI <em>look</em> at what the player shot.</h2>
  <ul class="bullets">
    <li>Input: player shoots photo → upload → recognize</li>
    <li>Output: <code>labels / attributes / parts / caption / confidence</code></li>
    <li>Feed the structured result into LLM for words and gen-image for stylized art</li>
    <li><strong>Engine for identity hook ③</strong> (environment) — AI looking at <em>your</em> stuff = strongest sense of ownership</li>
    <li>Shipped: Trash or Treasure / Fit Check / Field Guide / Mugshot Booth / Pet Filter</li>
  </ul>
  <p class="sub" style="margin-top: 18px;">
  <strong class="pink">Vision flips "AI shows you things" into "you show AI things."</strong>
  That flip changes the player's psychological position — and tends to come with built-in virality.
  </p>
</div>
<div class="col-visual">
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 12px;">
    <img src="assets/extra/trash-or-treasure.png" alt="Trash or Treasure" style="width:100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 14px;"/>
    <img src="assets/extra/fit-check.png" alt="Fit Check" style="width:100%; aspect-ratio: 1/1; object-fit: cover; border-radius: 14px;"/>
  </div>
</div>
""",
    "notes": """
<p>Vision is one of AlterU's main bets for the next stretch. The thing nothing else has is <strong>the player aiming a camera at the AI</strong> — active commitment, strong investment, share-friendly output.</p>
""",
},

"llm": {
    "short": "Part 3 · LLM",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Capability · game-chat (LLM)</span>
  <h2 class="title">Let the game <em>talk</em>.</h2>
  <ul class="bullets">
    <li>OpenAI-compatible · system + user → assistant text</li>
    <li>Multi-turn history if you need it (Pulp Hour short pieces)</li>
    <li><strong>Key rule</strong>: system prompts must be <strong>in-character</strong>. Default ChatGPT-friendly = soul-dead UI.</li>
    <li>Real voices: Trash or Treasure (snarky-but-tender) · Hour Capsule (curator) · Pulp Hour (noir) · Daily Arcana (tarot reader) · The Locksmith</li>
  </ul>
</div>
<div class="col-visual">
  <img src="assets/posters/pulp-hour.png" alt="Pulp Hour"/>
</div>
""",
    "notes": """
<p>Land this: the LLM is not "a box that returns correct answers." It's "<strong>a box that returns lines a specific character would say</strong>."</p>
<p>A good system prompt gives the whole game a soul. A bad one is ChatGPT in a costume. Have students write a system prompt for one of our games after class and check the output for in-character voice.</p>
""",
},

"data-primitives": {
    "short": "Part 3 · Data Primitives",
    "body": """
<span class="eyebrow"><span class="dot"></span>Capability · 4 data primitives</span>
<h2 class="title">Make the game <em>remember</em><br/>and players <em>see each other</em>.</h2>
<div class="grid">
  <div class="cell">
    <span class="tag">🏆</span>
    <h3>Leaderboard</h3>
    <p>One hook to wire up (<code>useGameScore</code>). One board per game. Tap a row → that user's profile.</p>
    <p style="margin-top:10px;"><strong>Pattern</strong>: put a <strong class="pink">champion pill</strong> (22px avatar + gold crown) on the home screen. Swiping into the game instantly reveals "#1 is @xxx" — proof someone is here.</p>
  </div>
  <div class="cell">
    <span class="tag">💾</span>
    <h3>Cloud save</h3>
    <p>session_id-keyed. Returns the <strong>last 6 users'</strong> saves, not just yours.</p>
    <p style="margin-top:10px;"><strong>Quiet superpower</strong>: this single API is the <strong class="pink">native data source</strong> for any cross-user wall. One hook, two jobs — every Wall in AlterU runs on it.</p>
  </div>
  <div class="cell">
    <span class="tag">📊</span>
    <h3>Events + stats</h3>
    <p>Trigger events, fetch aggregates (day_click_count / day_user_count / continuous_days).</p>
    <p style="margin-top:10px;"><strong>Trap</strong>: daily-once rules cannot be <code>lastTapDay===today || stats.*</code> — platform stats don't reset at UTC midnight, the OR is always true, <strong class="danger">players get permanently locked out</strong>. Already shipped twice.</p>
  </div>
  <div class="cell" style="border-color: var(--brand-pink); box-shadow: 0 0 0 1px var(--brand-pink-dim);">
    <span class="tag">🔔</span>
    <h3>Cross-user notify (key)</h3>
    <p>Touched someone's content → push them a note (platform avatar + text + image).</p>
    <p style="margin-top:10px;"><strong>3 hard rules</strong>:<br/>✓ self-guard (no notify to yourself)<br/>✓ 24h dedupe (same action + same target → once)<br/>✓ author cap (≤ 5 per day per recipient)</p>
  </div>
</div>
""",
    "notes": """
<p>Deep point: <strong>the cloud save API is dual-purpose</strong> — it's both "my save" and "what other people just shipped." That's the substrate under every cross-user Wall (Daily Arcana / Pulp Hour / Hour Capsule).</p>
<p>Notify is the smallest viable mechanic for turning a single-player game into a social one. Not chat, not comments, not friends — just "someone touched your thing." Day-one rule: every new game has to answer "what's the notify?"</p>
""",
},

"demo-mode": {
    "short": "Part 3 · Demo Mode",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Capability · external demo mode</span>
  <h2 class="title">A shared link still<br/><em>runs the core loop</em>.</h2>
  <p class="sub">
    All AI endpoints expose <code>CORS: *</code>. Drop the game URL into Twitter or a group chat;
    the recipient opens it in their browser and <strong class="pink">gets a real demo</strong> — not a fallback landing.
  </p>
  <ul class="bullets">
    <li>On <code>!isInAigram</code>, hook-layer fallback inserts phantom data — example leaderboard, fake counter, demo CTA</li>
    <li>Hour Capsule's <code>FieldDemoCTA</code> is the canon — poster as example bag + one filled-pink CTA → App Store</li>
    <li>This is <strong>a second user journey</strong>, not engineering fallback — design it day one</li>
  </ul>
  <p class="sub" style="margin-top: 18px;">
  Empty state has to be <strong>two-state</strong>:
  </p>
  <ul class="bullets" style="margin-top: 8px;">
    <li><code>!isInAigram</code> · browser preview → "Open in AlterU"</li>
    <li><code>isInAigram && length===0</code> · really in-app but empty → "Invite friends" / "Be the first"</li>
    <li><span class="danger">Wrong forever</span>: one copy for both</li>
  </ul>
</div>
<div class="col-visual">
  <img src="assets/posters/hour-capsule.png" alt="Hour Capsule demo mode"/>
</div>
""",
    "notes": """
<p>Important for PM/marketing: <strong>every game ships with a built-in demo for sharing</strong>. No separate landing page needed — the URL itself is the experience.</p>
<p>The empty-state rule is here because we've shipped it broken (tag-youre-it lobby). Have designers audit their own wireframes — does it distinguish "in-app but empty" from "not in-app yet"?</p>
""",
},

# ───── Part 4 · 7 Paradigms ─────────────────────────────────────────
"paradigm-overview": {
    "short": "Part 4 · 7 Paradigms",
    "body": """
<span class="eyebrow"><span class="dot"></span>Part 4 · 7 proven paradigms</span>
<h2 class="title">Pick one of these seven,<br/>and <em>stuff your idea</em> into it.</h2>
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
Each paradigm comes with: <strong>a shipped reference game</strong> + <strong>a one-line recipe</strong> + <strong>known traps</strong> + <strong>a forkable code skeleton</strong>.
Next 7 slides drill in one per page.
</p>
""",
    "notes": """
<p>This is the navigation map. Give the room a mental shelf — next time they hear an idea, anchor it to one of these seven, then mutate.</p>
""",
},

"paradigm-physical": {
    "short": "Part 4 · ① Physical",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Paradigm ① · physical + tactile</span>
  <h2 class="title">Touch in,<br/><em>physics out</em>, instantly.</h2>
  <ul class="bullets">
    <li><strong>Single input</strong>: hold / drag / tap — never more than one</li>
    <li><strong>Impact quartet</strong>: screen shake + flash + floating "-N" + vignette</li>
    <li><strong>Procedural Web Audio</strong> (no sound files — saves payload size)</li>
    <li><strong>FOV swing</strong> carries the sense of speed (52° → 82°)</li>
    <li>Shipped: <strong>River Row</strong> (rowing) / <strong>Sky Leap</strong> (charged jump) / <strong>Hold It Together</strong> (stress tower)</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
    <strong class="pink">Player taste tag</strong>: physical / stacking / merge / instant tactile<br/>
    <strong class="danger">Player allergy</strong>: Reigns-style card swipe / pure-text decisions / cartoon stickers
  </p>
</div>
<div class="col-visual">
  <img src="assets/posters/river-row.png" alt="River Row"/>
</div>
""",
    "notes": """
<p>This category is the retention king. Once the touch feel is right, players come back to swipe more. But "right" is <strong>tuning art</strong> — FOV swing, camera follow, the impact quartet, all of it has to be felt live. Have engineering ship a playable build by week 1 and iterate touch tuning 30 times, not write a 50-page PRD.</p>
""",
},

"paradigm-crossy": {
    "short": "Part 4 · ② Crossy Road",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Paradigm ② · isometric voxel cross-the-lanes</span>
  <h2 class="title">Cross the street,<br/>hop, <em>dodge</em>.</h2>
  <ul class="bullets">
    <li>Isometric voxel · single tap to hop, swipe to turn</li>
    <li><strong>Character shop</strong>: ~14 free + 16 at $20 + a Random tile</li>
    <li>Weather / lighting / hazard pool cycles per level</li>
    <li>Shipped: <strong>Block Hop</strong> (NYC traffic) / <strong>Block Party</strong> (top-down zombie shooter)</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
    <strong class="pink">Art rule</strong>: the Crossy Road audience bar = <strong>cultural caricature</strong>, not "regular humans in different outfits." Shelf It v3 got rejected because silhouettes weren't distinguishable; v4 finally cleared it.
  </p>
</div>
<div class="col-visual">
  <img src="assets/posters/block-hop.png" alt="Block Hop"/>
</div>
""",
    "notes": """
<p>This is AlterU's character-shop carrier — characters are the entry point for identity hook ①. Designers do their heaviest work on the <strong>30-character caricature lineup</strong>.</p>
<p>Tell the Shelf It roster history: v1 parametric → v2 bespoke but silhouettes still matched → v3 still wrong → v4 Crossy-Road cultural caricature finally landed. Lesson: <strong>iconic cultural symbols ≠ people in costumes</strong>.</p>
""",
},

"paradigm-tycoon": {
    "short": "Part 4 · ③ Tycoon",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Paradigm ③ · isometric tycoon</span>
  <h2 class="title">Pick stock → auto-sell →<br/><em>day-end</em> reconcile.</h2>
  <ul class="bullets">
    <li>Pick inventory → NPC foot traffic → end-of-day P&L receipt</li>
    <li>Difficulty spine: scaling expansion + rent ratchet + milestone goals + bankruptcy restart</li>
    <li>3 reinvestment upgrades (attract / markup / restock)</li>
    <li>Economy rule: <strong class="pink">COGS-at-sale</strong> (book cost only when sold)</li>
    <li>Shipped: <strong>Shelf It</strong> (merchandising sim)</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
  <strong class="pink">Tuning levers</strong>: <code>START_CASH</code> / multiplier / <code>RENT_PER_UNIT</code>.<br/>
  HUD numbers > 10K need K/M/B compact format.
  </p>
</div>
<div class="col-visual">
  <img src="assets/posters/shelf-it.png" alt="Shelf It"/>
</div>
""",
    "notes": """
<p>Designers can go deep here — difficulty curve, HUD information density, customer/employee AI state machines all live in design's hands. <strong>Always tune difficulty before art</strong>.</p>
<p>Real incident: first cut was modest (multiplier 1.3 → 1.42), and players said "I beat the goal before starting." We had to tighten twice (1.42 → 1.55 + rent 9 → 11). Lesson: Shelf It has so many compounding levers that cash growth outruns the default 1.2x framework assumption.</p>
""",
},

"paradigm-llm": {
    "short": "Part 4 · ④ LLM Rotation",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Paradigm ④ · LLM theme rotation</span>
  <h2 class="title">Every <em>hour</em>, every <em>day</em>,<br/>a fresh subject.</h2>
  <ul class="bullets">
    <li>LLM picks "today's / this hour's" subject + gen-image bakes the time + username</li>
    <li><strong>3-layer diversity floor</strong>: domain anchor + avoid-list + topical bonus</li>
    <li><strong>Rolling inventory + countdown teaser</strong> is the substitute for "come back tomorrow"</li>
    <li>Freeze AI/fetch context <strong>into the artifact itself</strong> — never re-fetch on view</li>
    <li>Shipped: <strong>Hour Capsule</strong> (hourly) / <strong>Pulp Hour</strong> (every 2 days) / <strong>Daily Arcana</strong> (daily)</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
  Generalizable solve: any game that needs to look "in-progress" can use a <strong class="pink">rolling inventory + countdown</strong> — it's not a retention mechanic, it's a sign-of-life signal for the random scroll-by viewer.
  </p>
</div>
<div class="col-visual">
  <img src="assets/posters/pulp-hour.png" alt="Pulp Hour"/>
</div>
""",
    "notes": """
<p>The hard part is freshness. Bag #5 still feels new because the 3-layer floor has an avoid-list. Without it, the LLM clusters around similar subjects.</p>
<p>Pulp Hour: the original 4 hard-coded covers never changed → players asked "why is it always the same stories?" → switch to a new cover every 2 days + countdown chip. Lesson: the moment the user scrolls into your screen, they should see "12 hours until the next one" — you don't need them to remember to come back.</p>
""",
},

"paradigm-vision": {
    "short": "Part 4 · ⑤ Vision",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Paradigm ⑤ · vision-triggered</span>
  <h2 class="title">Player shoots →<br/>AI <em>judges / praises</em>.</h2>
  <ul class="bullets">
    <li>Player shoots → upload → recognize → game-chat for words → gen-image for art</li>
    <li>Full chain ~ 10-15s (wait-as-play is mandatory, see paradigm ⑥)</li>
    <li>Engine for identity hook ③ (environment) — peak ownership feel</li>
    <li>Shipped: <strong>Trash or Treasure</strong> (shoot your stuff) / <strong>Fit Check</strong> (shoot your closet)</li>
    <li>Roadmap: mood-reader / mugshot-booth / pet-filter / album-cover-generator</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
  <strong class="danger">⚠️ Anti-pattern</strong>: the first version of any style prompt that's written without first reading the existing library will get shipped and immediately roasted. <strong>Read first, prompt second.</strong>
  </p>
</div>
<div class="col-visual">
  <img src="assets/extra/trash-or-treasure.png" alt="Trash or Treasure"/>
</div>
""",
    "notes": """
<p>Vision is one of AlterU's main bets. Walk the room through "active vs passive": showing AI-generated art to a player is zero commitment. Having the player aim a camera at their own stuff is a strong commitment — and the share-ability rises with it.</p>
""",
},

"paradigm-wait": {
    "short": "Part 4 · ⑥ Wait = Play",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Paradigm ⑥ · the wait is the play</span>
  <h2 class="title">5-8s gen-image,<br/><em>not</em> a spinner.</h2>
  <ul class="bullets">
    <li>The player's <strong>first input</strong> locks the prompt — not a "Generate" button</li>
    <li>The wait IS a <strong>darkroom develop</strong> — img starts at blur(12px) brightness(0.18), eases to 1.0</li>
    <li>SVG filter chain (feTurbulence + Gaussian + displacement) makes geometric edges feel chemical</li>
    <li>12-step iris bloom (CSS animation on SVG <code>r: 0 → 180</code>)</li>
    <li>Shipped: <strong>Kiss Wall</strong> (canonical)</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
  Generalizable: <strong class="pink">any gen-image game</strong> can adopt this. Kiss Wall shipped it in 9 commits in a day — the entire wait became a "darkroom developing a face" ritual.
  </p>
</div>
<div class="col-visual">
  <img src="assets/posters/kiss-wall.png" alt="Kiss Wall"/>
</div>
""",
    "notes": """
<p>Once a designer groks this they stop thinking of "loading" as something to hide. Loading becomes <strong>"the player is actively anticipating, slowly revealing"</strong>.</p>
<p>Original Kiss Wall had a SEAL button + curtain hiding the wait. Player verdict: "the interaction is awful." Killing SEAL was the moment the develop ritual clicked.</p>
""",
},

"paradigm-sensory": {
    "short": "Part 4 · ⑦ Sensory Toy",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Paradigm ⑦ · sensory toy</span>
  <h2 class="title">No goal.<br/>Just a <em>toy</em>.</h2>
  <ul class="bullets">
    <li>No "game over" · no rules · just a single sensory-feedback loop</li>
    <li>Usually < 100 lines of game logic + obsessively crafted procedural art</li>
    <li>Designers start from "what do I want to see?" (water bead on glass, wind chime stirred by breath)</li>
    <li>Shipped: <strong>Bubble Wrap</strong> · Marbles · Wind Chime · Crack Tap · Magnet Drop · Stack · Frosted Window · Layer Pop · Liquid Drop · Ghost Garden · Murmuration</li>
  </ul>
  <p class="sub" style="margin-top: 16px;">
  <strong class="pink">Socializing</strong> rides on score-beat ("@xxx popped more than you") — but since the score is continuous, you need a <strong>notifiedTargets Set</strong> to dedupe, or you'll send a notification storm.
  </p>
</div>
<div class="col-visual">
  <img src="assets/extra/bubble-wrap-eternal.png" alt="Bubble Wrap"/>
</div>
""",
    "notes": """
<p>Sensory toy is "zero tutorial" pushed to its limit — no rules at all, just sensation. Designers reverse-engineer from "the image I want to see" (a water bead sliding on glass, a chime stirred by breath).</p>
<p>It has no hooks ①②③, but it has ④ (network: "more / less than your friends") — so even sensory toys fit the identity model, just through the network hook.</p>
""",
},

# ───── Part 5 · Design Principles ───────────────────────────────────
"golden-2s": {
    "short": "Part 5 · The Golden 2 Seconds",
    "body": """
<span class="eyebrow"><span class="dot"></span>Part 5 · Design principle ①</span>
<p class="big-quote">
Three things must happen<br/>in the first <em>2 seconds</em>.
</p>
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 18px; max-width: 1080px; margin: 32px auto 0;">
  <div class="cell" style="text-align: left;">
    <span class="cell-num">1</span>
    <h3>SEE</h3>
    <p>An image that's interesting / strange / provocative — a visual hook</p>
  </div>
  <div class="cell" style="text-align: left;">
    <span class="cell-num">2</span>
    <h3>IDENTIFY</h3>
    <p>"This is a <strong>game</strong>" — not an ad, not a UI tutorial</p>
  </div>
  <div class="cell" style="text-align: left;">
    <span class="cell-num">3</span>
    <h3>ACT</h3>
    <p>Know what to <strong>do right now</strong> — one clear triggerable action</p>
  </div>
</div>
<p class="quote-attr" style="margin-top: 40px;">Miss this → swipe</p>
""",
    "notes": """
<p>Use these three as a hard rule. After this slide, have everyone open TikTok on their phone — swipe into a new game or ad, and try to read "what is this / what do I do" in 2 seconds. If yes → golden 2 passed. If not → swipe.</p>
""",
},

"no-return": {
    "short": "Part 5 · No Return Assumed",
    "body": """
<span class="eyebrow"><span class="dot"></span>Part 5 · Design principle ②</span>
<h2 class="title">Assume this is<br/>the <em>only</em> time you'll meet.</h2>
<div class="grid">
  <div class="cell">
    <span class="tag danger">anti-pattern</span>
    <h3>❌ Retention mechanics</h3>
    <p>"7-day check-in unlock"<br/>"Tomorrow's level unlocks at midnight"<br/>"Come back for a bonus"</p>
    <p style="margin-top:10px;" class="dim">These assume the player remembers to return. In a scroll feed, ~90% of players are first-timers and one-timers.</p>
  </div>
  <div class="cell" style="border-color: var(--brand-pink);">
    <span class="tag ok">solve</span>
    <h3>✅ Rolling inventory + countdown</h3>
    <p>New content every N hours<br/>Red ticking chip on top<br/>"COMING NEXT" sealed slot</p>
    <p style="margin-top:10px;" class="dim">Swiping in = immediate sight of "12 hours to next." No memory required. (Pulp Hour pattern.)</p>
  </div>
  <div class="cell" style="grid-column: span 2;">
    <h3>🚨 The death-chip rule</h3>
    <p><code>upcomingCover()</code> must always be non-null. If the countdown chip + teaser slot both vanish, that's the <strong class="danger">"game is dead"</strong> visual signal. Resupply rule: every N days append a new entry + run the generator.</p>
  </div>
</div>
""",
    "notes": """
<p>Counterintuitive for PMs because retention engineers live on check-ins, push notifications, reactivation. AlterU's feed-native design treats <strong>return as a luxury, not the default</strong>.</p>
""",
},

"english-empty": {
    "short": "Part 5 · English + Empty States",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Part 5 · Design principles ③ + ④</span>
  <h2 class="title">English by default.<br/>Empty state has <em>two</em> modes.</h2>
  <p class="sub"><strong>🇺🇸 Copy rule</strong></p>
  <ul class="bullets">
    <li>Every player-visible string in the feed — title, UI, buttons, baked text, AI dialogue, brand collateral — is <strong class="pink">English</strong></li>
    <li>Chinese only exists as an i18n-switchable secondary, never the default</li>
    <li><span class="danger">High-frequency footgun</span>: Chinese placeholder text left in, shipped to feed, ruins the brand tone</li>
  </ul>
  <p class="sub" style="margin-top: 24px;"><strong>🪟 Two empty states</strong></p>
  <ul class="bullets">
    <li><code>!isInAigram</code> (browser preview) → "Open in AlterU"</li>
    <li><code>isInAigram && length===0</code> (in-app but empty) → "Invite friends" / "Be the first"</li>
    <li><span class="danger">Wrong forever</span>: one copy for both</li>
  </ul>
</div>
<div class="col-visual" style="background: var(--surface-2); border-radius: 22px; border: 1px solid var(--border); padding: 32px; align-items: stretch; flex-direction: column; gap: 16px;">
  <div style="text-align: center; opacity: 0.55;">
    <p class="micro">browser preview</p>
    <h3 style="font-family: Montserrat; margin: 8px 0 12px;">Empty</h3>
    <p style="color: var(--text-3); font-size: 14px;">"Open in AlterU to play with friends"</p>
  </div>
  <hr style="border: 0; border-top: 1px dashed var(--border); margin: 8px 0;"/>
  <div style="text-align: center;">
    <p class="micro pink">in-app · no data</p>
    <h3 style="font-family: Montserrat; margin: 8px 0 12px;">Empty</h3>
    <p style="color: var(--text-2); font-size: 14px;">"Be the first to leave a mark."</p>
  </div>
</div>
""",
    "notes": """
<p>The English rule has been escalated by the product owner 5-6 times. AlterU is a new brand testing the US market — Chinese placeholders in the feed directly damage positioning.</p>
<p>The empty-state rule landed because we shipped it wrong (tag-youre-it lobby). Have designers audit their own wireframes — split "in-app empty" from "not in-app yet."</p>
""",
},

"anti-examples": {
    "short": "Part 5 · Anti-pattern Roll Call",
    "body": """
<span class="eyebrow"><span class="dot"></span>Part 5 · Real rejections · real player quotes</span>
<h2 class="title">"<em>too complex</em>" · "<em>no patience</em>" ·<br/>"<em>social is weak</em>"</h2>
<div class="grid">
  <div class="cell">
    <h3>Hold It Together v1</h3>
    <p class="micro pink">"the gameplay isn't fun"</p>
    <p>Reigns-style swipe + cartoon sticker face → players thought "image quiz" → swipe.<br/><strong>Fix</strong>: physics stress-tower (matter-js) ✅</p>
  </div>
  <div class="cell">
    <h3>Last Pour v1</h3>
    <p class="micro pink">"too flat"</p>
    <p>Wong-Kar-wai philosophical monologue → no tension in feed → swipe.<br/><strong>Fix</strong>: vampire + gothic + 6 visceral hits ✅</p>
  </div>
  <div class="cell">
    <h3>Sky Leap charge ring</h3>
    <p class="micro pink">"feels complex"</p>
    <p>Animated hold + release tutorial → players hated setup → swipe.<br/><strong>Fix</strong>: one shared finger icon, zero text ✅</p>
  </div>
  <div class="cell">
    <h3>Daily Arcana v1</h3>
    <p class="micro pink">"private = social zero"</p>
    <p>Every card seen only by you → no share surface → no traction.<br/><strong>Fix</strong>: D-suite (Wall + ♥ + notify) ✅</p>
  </div>
  <div class="cell">
    <h3>Pebble Pocket v1.2</h3>
    <p class="micro pink">"social is weak"</p>
    <p>Tide feed had no verb → authors never knew anyone saw them → secondary value zero.<br/><strong>Fix</strong>: 🐚 Keep + notify chain (feed-needs-a-verb) ✅</p>
  </div>
  <div class="cell">
    <h3>Shelf It roster v1-v3</h3>
    <p class="micro pink">"not as exciting as the monsters"</p>
    <p>Regular people in different uniforms → identical silhouettes → no iconicity.<br/><strong>Fix</strong>: v4 Crossy-Road cultural caricature (NYPD / FDNY / Notorious BIG) ✅</p>
  </div>
</div>
""",
    "notes": """
<p>Walk each row in a minute. The crucial point: <strong>at the design-doc stage these all looked reasonable</strong>. They only surfaced as failures in real player hands. So "design review passed" ≠ "ready to ship" — you must test against real players with a real build.</p>
""",
},

"v1-visceral": {
    "short": "Part 5 · V1 Visceral Register",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Part 5 · visual register</span>
  <h2 class="title">Feed demands<br/><em>visceral impact</em>, directly.</h2>
  <p class="sub">
  Every hook must read "<strong class="pink">something's off</strong>" within 2 seconds.
  Wong-Kar-wai philosophical restraint is <strong>wrong for feed</strong> — save it for long-form.
  </p>
  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 14px; margin-top: 18px;">
    <div style="background: var(--surface-2); border: 1px solid var(--ok); border-radius: 12px; padding: 14px 16px;">
      <p class="micro ok" style="margin: 0 0 8px;">✅ verbs + visible objects</p>
      <ul class="bullets" style="font-size: 13px; gap: 4px;">
        <li>"pours blood"</li>
        <li>"fangs descend"</li>
        <li>"tooth in drink"</li>
        <li>"candle bends toward her"</li>
      </ul>
    </div>
    <div style="background: var(--surface-2); border: 1px solid var(--danger); border-radius: 12px; padding: 14px 16px;">
      <p class="micro danger" style="margin: 0 0 8px;">❌ abstract nouns / literary restraint</p>
      <ul class="bullets" style="font-size: 13px; gap: 4px;">
        <li>"a memory"</li>
        <li>"a silence"</li>
        <li>"restraint"</li>
      </ul>
    </div>
  </div>
</div>
<div class="col-visual">
  <img src="assets/gen/visceral-cinema.jpg" alt="Visceral noir cinema reference" style="max-height: 60vh; max-width: 100%; aspect-ratio: 1/1; width: auto; height: auto; object-fit: cover; border-radius: 18px;"/>
</div>
""",
    "notes": """
<p>Last Pour v1 took 8 videos before this clicked. Walk the room through the original ("too flat") → v2 (vampire + gothic + 6 visceral hits). Same framework, only the register intensity was wrong.</p>
<p>The image on the right was generated for this training — a single frame with three visceral hits (blood drop + tooth in teacup + bent candle flame), all readable in 2 seconds. Ask the room: "On the next thing I ship, how many visceral hits can a viewer read in 2 seconds?"</p>
""",
},

# ───── Part 6 · Craft + Agents ──────────────────────────────────────
"style-library": {
    "short": "Part 6 · Style Library",
    "body": """
<span class="eyebrow"><span class="dot"></span>Part 6 · Craft · visual style menu</span>
<h2 class="title">Pick <em>from this menu</em>,<br/>don't design from scratch.</h2>
<div class="grid" style="grid-template-columns: repeat(4, 1fr); gap: 14px;">
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">📣 comic</span><h3 style="font-size: 16px; margin-bottom: 6px;">American comic HUD</h3><p style="font-size: 12.5px; line-height: 1.5;">Bangers + ink lines + hard shadow<br/><strong class="pink">Sky Leap · Shelf It · Block Party · Atomic</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">🧊 voxel</span><h3 style="font-size: 16px; margin-bottom: 6px;">Low-poly voxel A</h3><p style="font-size: 12.5px; line-height: 1.5;">Soft bevel ≤ 4% / 3-value shading<br/><strong class="pink">Sky Leap characters · Lowpoly Lab · Block Party monsters</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">🏙️ voxel</span><h3 style="font-size: 16px; margin-bottom: 6px;">Low-poly voxel B</h3><p style="font-size: 12.5px; line-height: 1.5;">Sharp isometric / flat shading<br/><strong class="pink">Shelf It · Block Hop · Helix Drop</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">💾 retro</span><h3 style="font-size: 16px; margin-bottom: 6px;">BSOD pixel</h3><p style="font-size: 12.5px; line-height: 1.5;">Dark retro console · CRT scanlines<br/><strong class="pink">BSOD · Bell Tower · Crystal Ball Collective</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">💥 pop-art</span><h3 style="font-size: 16px; margin-bottom: 6px;">Comic book BAM</h3><p style="font-size: 12.5px; line-height: 1.5;">Halftone · Lichtenstein-style<br/><strong class="pink">Tag You're It · Mirror Pop</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">🕹️ arcade</span><h3 style="font-size: 16px; margin-bottom: 6px;">80s arcade green + hot pink</h3><p style="font-size: 12.5px; line-height: 1.5;">Neon bulb edges / single font<br/><strong class="pink">Trash or Treasure · Confession Booth</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">💎 glass</span><h3 style="font-size: 16px; margin-bottom: 6px;">Liquid-glass frosted dream</h3><p style="font-size: 12.5px; line-height: 1.5;">Fredoka · gradient pink<br/><strong class="pink">Sky Leap (late) · Murmur · Spin Lock</strong></p></div>
  <div class="cell" style="padding: 16px 16px 18px;"><span class="tag">📖 editorial</span><h3 style="font-size: 16px; margin-bottom: 6px;">Catalog editorial</h3><p style="font-size: 12.5px; line-height: 1.5;">Catalog-illustration plate / baked type<br/><strong class="pink">Fit Check · Pulp Hour · Hour Capsule · The Couturier</strong></p></div>
</div>
""",
    "notes": """
<p>The "visual style menu" for designers. <strong>New games should almost never design a visual style from scratch</strong> — we've codified 8 styles, each with shipped reference games.</p>
<p>Before picking, have the designer open the reference game and feel it for 10 minutes. Better than 50 figma screenshots.</p>
<p>Reminder: pick one per game, don't mix. Mixing = visual chaos = swipe.</p>
""",
},

"voxel-caricature": {
    "short": "Part 6 · Voxel + Caricature Rules",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Craft · low-poly + cultural caricature</span>
  <h2 class="title">The line between<br/>looking <em>premium</em><br/>and looking amateur.</h2>
  <p class="sub" style="margin-top: 16px;"><strong class="pink">Voxel 7 rules</strong> (characters + props)</p>
  <ul class="bullets" style="font-size: 14px;">
    <li>① Ratio <strong>1:1.3:1.5</strong> (head : torso : legs)</li>
    <li>② Bevel ≤ 4% (soft bevel = "premium" read)</li>
    <li>③ 3-value shading / never flat color</li>
    <li>④ One saturated accent color (everything else desaturated)</li>
    <li>⑤ Ground contact shadow + AO (round radial gradient — never an ellipse mask, it shows edges)</li>
    <li>⑥ One visual language (family A or family B, never mixed)</li>
    <li>⑦ Details ≥ 1 voxel (smaller = invisible, cut it)</li>
  </ul>
  <p class="micro pink" style="margin-top: 18px;">Canon: Lowpoly Lab familyA / familyB · Shipped: Sky Leap / Block Hop / Block Party / Shelf It</p>
</div>
<div class="col-visual" style="flex-direction: column; gap: 14px; align-items: stretch;">
  <div style="background: var(--surface-2); border: 1px solid var(--brand-pink); border-radius: 16px; padding: 20px 22px;">
    <p class="micro pink" style="margin: 0 0 10px;">Crossy Road caricature · 5 rules</p>
    <ul class="bullets" style="font-size: 13.5px; gap: 9px;">
      <li>① <strong>Iconic cultural symbols</strong> (donut-NYPD / FDNY / Notorious BIG / Fonzie), not "people in costumes"</li>
      <li>② <strong>Exaggerated proportions</strong> — deform the figure until it's instantly recognizable</li>
      <li>③ <strong>Emissive accent</strong> (whistle / mic / badge) carrying a small glow</li>
      <li>④ <strong>Silhouette test</strong>: must be readable in pure black silhouette</li>
      <li>⑤ <strong>Extenders</strong> (hat brim / coat tail / oversized head gear)</li>
    </ul>
    <p style="margin: 14px 0 0; font-size: 12.5px; color: var(--text-3);">
    ❌ Shelf It v1-v3 rejected: silhouettes weren't distinguishable<br/>
    ✅ v4 Crossy Road cultural caricature finally cleared
    </p>
  </div>
  <div style="display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px;">
    <img src="assets/posters/sky-leap.png" alt="" style="aspect-ratio: 1/1; object-fit: cover; border-radius: 8px;"/>
    <img src="assets/posters/block-hop.png" alt="" style="aspect-ratio: 1/1; object-fit: cover; border-radius: 8px;"/>
    <img src="assets/extra/block-party.png" alt="" style="aspect-ratio: 1/1; object-fit: cover; border-radius: 8px;"/>
  </div>
</div>
""",
    "notes": """
<p>Two sets of hard rules for designers shipping characters / props: <strong>left side governs craft quality, right side governs cultural readability</strong>.</p>
<p>Walk Shelf It's 4-round roster history. v3 still got "silhouettes look the same"; v4 with Crossy Road cultural caricature finally landed. Player quote: <strong>"the same taste sensibility as Crossy Road."</strong></p>
<p>Note: sensory toys can ignore caricature rules (no roster), but always keep the 7 voxel rules.</p>
""",
},

"gen-image-craft": {
    "short": "Part 6 · gen-image Field Notes",
    "body": """
<span class="eyebrow"><span class="dot"></span>Craft · gen-image · 4 field notes</span>
<h2 class="title">How to ship pictures<br/>that <em>don't blow up</em>.</h2>
<div class="grid">
  <div class="cell">
    <span class="cell-num">1</span>
    <span class="tag">mandatory</span>
    <h3>Test plates with ref_url</h3>
    <p>txt2img-only tests pass; add ref_url and the player's photo stitches into the frame. <strong class="pink">Fit Check learned this in production.</strong></p>
    <p style="margin-top:8px;" class="dim">Same trap: Build-a-Boyfriend tier card burn-in, Hour Capsule MFG stamps. Every plate test = ref + real photo, no exceptions.</p>
  </div>
  <div class="cell">
    <span class="cell-num">2</span>
    <span class="tag">precondition</span>
    <h3>Read the library before writing a style prompt</h3>
    <p>v1 prompts written from imagination, never reading the library → shipped, immediately roasted as "style drifted." <strong class="pink">5 of Kiss Wall's 9 commits</strong> were this.</p>
    <p style="margin-top:8px;" class="dim">Existing assets are truth; prompts describe them. Read first, prompt second. Same for character anchor sheets (The Bidding · The Couturier · The Locksmith).</p>
  </div>
  <div class="cell">
    <span class="cell-num">3</span>
    <span class="tag">identity</span>
    <h3>Baked text = identity hook ②</h3>
    <p><strong class="pink">Hour Capsule</strong> <code>@user #00042</code> / <strong class="pink">Pulp Hour</strong> red COMING NEXT chip / <strong class="pink">Build-a-Boyfriend</strong> tier tags / <strong class="pink">Daily Arcana</strong> card-face username.</p>
    <p style="margin-top:8px;" class="dim">SD text rendering is imprecise — never rely on the prompt to spell anything. Bake type via HTML overlay or Canvas post-processing.</p>
  </div>
  <div class="cell">
    <span class="cell-num">4</span>
    <span class="tag">play</span>
    <h3>5-8s wait = play</h3>
    <p>Not a spinner: <strong class="pink">Kiss Wall</strong> develop / <strong class="pink">Hour Capsule</strong> sealing whisper / <strong class="pink">Fit Check</strong> developing pill / <strong class="pink">Field Guide</strong> archive flip.</p>
    <p style="margin-top:8px;" class="dim">Generalizable: first input → lock prompt → enter the develop / form / unseal / archive-flip ritual.</p>
  </div>
</div>
""",
    "notes": """
<p>This slide is the "now actually do it" sheet after Parts 3 and 4. All four notes are real production scars.</p>
<p>Deeper point: <strong>SD text rendering is fragile = bake type via HTML / Canvas overlay always</strong>. Hour Capsule's MFG timestamp and Pulp Hour's chip are HTML layered on top of the gen-image base, not from the prompt.</p>
""",
},

"agent-explore-first": {
    "short": "Part 6 · Agents · Explore First",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>Agents · explore before you build</span>
  <h2 class="title">Let your agent <em>look</em><br/>before you let it <em>act</em>.</h2>
  <p class="sub">
  The #1 thing an agent gets wrong is not bad code — it's
  <strong class="pink">acting without reading the current state</strong>:
  imagining a style, an API, a pattern.
  </p>
  <ul class="bullets" style="font-size: 15px;">
    <li>✅ <strong>"First explore X in this game, then decide what to change"</strong> — make it Read the assets / code / skill before deciding</li>
    <li>✅ <strong>"Check how [[score-beat-run-end-vs-sensory-toy]] is implemented"</strong> — skill names are sharper anchors than verbal descriptions</li>
    <li>✅ <strong>"Reference Kiss Wall's chemistry-bath develop process"</strong> — pointing at a shipped game beats writing a PRD</li>
    <li>❌ "Build a feature like X" — missed step: first see how X is done</li>
  </ul>
  <p class="sub" style="margin-top: 20px;">
  Real incidents: <strong class="pink">Kiss Wall v1 prompts written from imagination</strong> → roasted on ship; <strong class="pink">The Bidding's Paula without head/body ratio</strong> → 11-year-old rendered as a baby. Both = "act before look."
  </p>
</div>
<div class="col-visual" style="height: 100%;">
  <img src="assets/gen/speak-to-agent.jpg" alt="A designer talking to an AI agent across a desk"
       style="max-height: 70vh; aspect-ratio: 1/1; width: auto; object-fit: cover;"/>
</div>
""",
    "notes": """
<p>This is the master rule for the whole "talking to your agent" chapter. The rest are corollaries.</p>
<p>Have the room recall the last time ChatGPT / Claude got something wrong — most cases come down to "I didn't make it look, it imagined." Agents writing code repeat the pattern: if you don't make them Read the existing library, they invent a plausible-looking style → ship → roast.</p>
<p>The practical move is to give the agent an explicit three-phase script: <strong>explore (read-only agent) → decide (planning agent) → implement (edit agent)</strong>.</p>
""",
},

"agent-prompt-craft": {
    "short": "Part 6 · Agents · Prompt Craft",
    "body": """
<span class="eyebrow"><span class="dot"></span>Agents · 4 prompt patterns</span>
<h2 class="title">Make the agent<br/>sound <em>like that game</em>.</h2>
<div class="grid">
  <div class="cell">
    <span class="cell-num">1</span>
    <span class="tag">voice</span>
    <h3>In-character system prompt</h3>
    <p>Never let the LLM default to ChatGPT-friendly mush.</p>
    <p style="margin-top:8px;" class="dim">✅ <strong class="pink">Trash or Treasure</strong> snarky-but-tender / <strong class="pink">Hour Capsule</strong> curator / <strong class="pink">Pulp Hour</strong> noir / <strong class="pink">Daily Arcana</strong> tarot reader / <strong class="pink">The Locksmith</strong></p>
  </div>
  <div class="cell">
    <span class="cell-num">2</span>
    <span class="tag">anchor</span>
    <h3>4-layer elevator + skill names</h3>
    <p>Restate the idea as "identity hook X + paradigm Y + skill [[Z]] pattern."</p>
    <p style="margin-top:8px;" class="dim">e.g. <code>"sensory-toy + identity hook ④ (network) + [[score-beat-run-end-vs-sensory-toy]]"</code> is 10x more precise than "a bubble-wrap toy that shows your friends' tap counts."</p>
  </div>
  <div class="cell">
    <span class="cell-num">3</span>
    <span class="tag">reference</span>
    <h3>Shipped URL + reference video</h3>
    <p>"Like Crossy Road but characters are X" / "Like Suika but the merge is X" / "Like Murmur but the trigger is Y."</p>
    <p style="margin-top:8px;" class="dim">Build-a-Boyfriend = Suika fork. Block Hop = Crossy Road fork. Hour Capsule = Seal Press fork. <strong class="pink">Stand on shoulders</strong> instead of writing from zero.</p>
  </div>
  <div class="cell">
    <span class="cell-num">4</span>
    <span class="tag">feedback</span>
    <h3>Template your feedback language</h3>
    <p>The same player short-phrases map to specific patterns:</p>
    <p style="margin-top:8px;" class="dim">"<strong>too complex</strong>" → cut rules / cut setup<br/>"<strong>social is weak</strong>" → add a verb + notify<br/>"<strong>can't watch this</strong>" → cut cartoon sticker face<br/>"<strong>no patience</strong>" → cut tutorial / 1 finger icon<br/>"<strong>too flat</strong>" → add visceral hits</p>
  </div>
</div>
""",
    "notes": """
<p>Walk each one with a real example. <strong>Pattern 4 is the most actionable</strong> — these phrases have become our shared ontology; the agent hears them and immediately knows the direction.</p>
<p>Suggest students save these four into their personal system-prompt template, ready for the next idea.</p>
""",
},

"agent-build-verify": {
    "short": "Part 6 · Agents · Build → Verify",
    "body": """
<span class="eyebrow"><span class="dot"></span>Agents · the last rule is the most important</span>
<p class="big-quote">
"<em>Build</em>" doesn't mean "<em>Done</em>".<br/>
Make the agent <strong class="pink">verify itself</strong>.
</p>
<div style="display: grid; grid-template-columns: 1fr 1fr; gap: 18px; max-width: 1100px; margin: 36px auto 0;">
  <div class="cell" style="text-align: left; border-color: var(--danger);">
    <span class="tag danger">anti-pattern</span>
    <h3>Build → Claim done</h3>
    <p style="font-size: 14px;">"I shipped feature X ✓" — no tests run, no grep verification, no curl on the bundle to confirm the deploy.</p>
    <p style="margin-top:8px; font-size: 13.5px; color: var(--text-3);">Real incidents: <strong class="danger">2026-06-02 final-stream vs last-cigarette shared a UUID</strong> · <strong class="danger">2026-05-31 sweep using grep -l missed vital-signs</strong> · push success ≠ deploy success.</p>
  </div>
  <div class="cell" style="text-align: left; border-color: var(--ok);">
    <span class="tag ok">correct path</span>
    <h3>Build → Verify → Ship</h3>
    <p style="font-size: 14px; margin-bottom: 8px;"><strong>Pre-ship 5-grep checklist:</strong></p>
    <ol style="margin: 0; padding-left: 18px; color: var(--text-3); font-size: 13.5px; line-height: 1.7;">
      <li><code>grep -L</code> finds <strong class="ok">absence</strong>, not <code>-l</code> for presence</li>
      <li>Grep edited file after every Edit before <code>git add</code> (defends stale no-op)</li>
      <li><code>git -C abs-path</code> — cwd drifts</li>
      <li>curl bundle URL to confirm the new class is in</li>
      <li>UUID uniqueness script passes</li>
    </ol>
  </div>
</div>
<p class="quote-attr" style="margin-top: 32px;">Ship only after verify · pre-ship-verify skill</p>
""",
    "notes": """
<p>Hard bottom line for the whole "talking to your agent" chapter. Ask the room: <strong>"When my agent says 'done,' did I make it verify? Or did I accept the claim?"</strong></p>
<p>The 5 greps came out of a full day of failures on 2026-05-31. Push success ≠ deploy success — demonstrate live by curl'ing a game's bundle URL to check for a recently shipped class. Let the room feel the gap.</p>
""",
},

# ───── Part 7 · Workflow ────────────────────────────────────────────
"workflow": {
    "short": "Part 7 · Workflow Timeline",
    "body": """
<span class="eyebrow"><span class="dot"></span>Part 7 · One AlterU game, beginning to end</span>
<h2 class="title">From pitch<br/>to first player feedback.</h2>
<div class="grid" style="grid-template-columns: repeat(4, 1fr);">
  <div class="cell"><span class="cell-num">1</span><h3>Pitch · 30s</h3><p>Elevator + <strong>the 4-layer check</strong>: where's the identity hook? how's content AI-native? what's the social verb? which paradigm?</p></div>
  <div class="cell"><span class="cell-num">2</span><h3>Concept · 1 day</h3><p>3 mockups (open / play / end) + reference video + paradigm + style choice</p></div>
  <div class="cell"><span class="cell-num">3</span><h3>MVP · 3-5 days</h3><p>Fork the reference game → wipe UUID → get the golden path running. No art, no SFX, no social yet.</p></div>
  <div class="cell"><span class="cell-num">4</span><h3>Feel · 5-7 days</h3><p>Impact quartet + sound quartet + visual polish — the retention-defining phase.</p></div>
  <div class="cell"><span class="cell-num">5</span><h3>Social · 2-3 days</h3><p>Identity hook ④: leaderboard + notify + cross-user wall · <strong class="pink">bake in day one</strong>, do not retrofit</p></div>
  <div class="cell"><span class="cell-num">6</span><h3>Ship · half day</h3><p>UUID uniqueness + meta.json + poster + push + deploy verification</p></div>
  <div class="cell"><span class="cell-num">7</span><h3>Watch · ongoing</h3><p>Live player feedback → if the same complaint shows up ≥ 2x, it's a design bug not a polish issue</p></div>
  <div class="cell" style="background: var(--brand-pink-dim); border-color: var(--brand-pink); display: flex; flex-direction: column; justify-content: center;">
    <h3 class="pink">⚠️ Don't</h3>
    <p>Skip phase 5 → retrofitting social costs 5× · useGameSave schema has to be re-cut · we've shipped this mistake too many times</p>
  </div>
</div>
""",
    "notes": """
<p>Hammer the 30-second elevator. <strong>If the pitch can't clear the 4-layer check (identity hook + AI-native + social verb + paradigm), don't enter MVP.</strong></p>
""",
},

"social-musts": {
    "short": "Part 7 · Social Musts",
    "body": """
<span class="eyebrow"><span class="dot"></span>Part 7 · Bake into day-one design</span>
<h2 class="title">Whichever paradigm you pick,<br/>these <em>4 moves</em> are mandatory.</h2>
<div class="grid">
  <div class="cell">
    <span class="cell-num">1</span>
    <h3>Score-beat notify</h3>
    <p>After score submit, find who just got passed → push them "you just got passed by @xxx"<br/><strong>Any game with a score gets this</strong> · 14 shipped</p>
  </div>
  <div class="cell">
    <span class="cell-num">2</span>
    <h3>Feed needs a verb</h3>
    <p>Every row in any browse / Wall / feed has a verb (KEEP / ♥ / KISS)<br/>Verb fires publish + notify + badge + chip<br/><strong>Any game with a wall / feed gets this</strong></p>
  </div>
  <div class="cell">
    <span class="cell-num">3</span>
    <h3>Cross-user wall</h3>
    <p>Use <code>save/get/data/list</code>'s "last 6 users' saves" as the source for a cross-user feed<br/><strong>Any game that keeps artifacts gets this</strong> (Daily Arcana / Pulp Hour / Hour Capsule)</p>
  </div>
  <div class="cell" style="border-color: var(--brand-pink);">
    <span class="cell-num">4</span>
    <h3>Notify 3 hard rules</h3>
    <p>✓ <strong>self-guard</strong> (no self-notify)<br/>✓ <strong>24h dedupe</strong> (same action + same target → once per 24h)<br/>✓ <strong>author cap</strong> (≤ 5 per day per recipient)</p>
  </div>
</div>
""",
    "notes": """
<p>Drill: do not "add social later." Bake it in day one. Retrofitting takes half a month and re-cuts every useGameSave schema. We've eaten this multiple times.</p>
""",
},

"faq": {
    "short": "Part 7 · FAQ",
    "body": """
<span class="eyebrow"><span class="dot"></span>Part 7 · Before we wrap · the recurring questions</span>
<h2 class="title">Six things<br/>everyone <em>asks</em>.</h2>
<div class="grid" style="grid-template-columns: 1fr 1fr 1fr; gap: 14px; align-content: start;">
  <div class="cell" style="padding: 18px 18px 22px; border-color: var(--brand-pink); box-shadow: 0 0 0 1px var(--brand-pink-dim);">
    <span class="tag">Q1</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">How do I ship?</h3>
    <p style="font-size: 13px; line-height: 1.55;">Open the preview <em>inside the platform</em> → check the result → tap the <strong class="pink">Publish</strong> button. Registration is automated. <strong>You're done at "happy"</strong> — no UUIDs, no meta.json, no deploy scripts.</p>
  </div>
  <div class="cell" style="padding: 18px 18px 22px;">
    <span class="tag">Q2</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">Do I have to use AI?</h3>
    <p style="font-size: 13px; line-height: 1.55;">No. <strong class="pink">Sensory toys</strong> are pure hand-craft (Bubble Wrap / Marbles / Wind Chime). But the <strong>identity layer + social verb</strong> are nearly always required — otherwise it isn't really an AlterU game.</p>
  </div>
  <div class="cell" style="padding: 18px 18px 22px;">
    <span class="tag">Q3</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">What about the 5-8s gen-image wait?</h3>
    <p style="font-size: 13px; line-height: 1.55;">Turn the wait <strong class="pink">into the play</strong> — never a spinner. Darkroom develop / sealing / form / archive flip. Kiss Wall is the canon (paradigm ⑥).</p>
  </div>
  <div class="cell" style="padding: 18px 18px 22px;">
    <span class="tag">Q4</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">Should I add a tutorial?</h3>
    <p style="font-size: 13px; line-height: 1.55;">No. Tutorials assume patience → swipe. <strong class="pink">The first failure is the tutorial</strong>. Sky Leap cut its charge-ring animation down to one shared finger icon.</p>
  </div>
  <div class="cell" style="padding: 18px 18px 22px;">
    <span class="tag">Q5</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">Mapping player feedback?</h3>
    <p style="font-size: 12.5px; line-height: 1.6;">"<strong>too complex</strong>" → cut rules<br/>"<strong>social weak</strong>" → add verb + notify<br/>"<strong>can't watch this</strong>" → drop sticker face<br/>"<strong>no patience</strong>" → drop setup / tutorial<br/>"<strong>too flat</strong>" → add visceral hits</p>
  </div>
  <div class="cell" style="padding: 18px 18px 22px;">
    <span class="tag">Q6</span>
    <h3 style="font-size: 16px; margin-bottom: 8px;">Can I build without coding?</h3>
    <p style="font-size: 13px; line-height: 1.55;">Yes. AlterU gives makers two <strong class="pink">zero-code modes</strong>:<br/>① <strong>One sentence</strong> — describe the game in one line, AI fills in art / code / sound / voice.<br/>② <strong>Remix</strong> — pick a game from the feed, twist the rules, swap the world, ship your version.</p>
  </div>
</div>
""",
    "notes": """
<p>The wrap-up Q&A. Each question is something newcomers stumble on. If you have time, let one or two attendees take a crack at each Q before you give the canonical answer.</p>
<p><strong>Q1 is the key updated message</strong> — older versions of this deck still walked people through UUID / meta.json / deploy scripts. The platform automated all of that. Designers and PMs <strong>are done at "happy"</strong>, then tap Publish. Q1 is pink-bordered for a reason.</p>
<p><strong>Q5 is the most useful daily tool</strong> in the whole deck. Have students paste these mappings into their personal system-prompt template — next time an idea comes in, they can route by phrase.</p>
<p><strong>Q6 lines up with the landing Makers 3-card</strong> (One sentence / Remix / Soon). This is the question that gives makers the "no barrier" psychological green light. If anyone asks "what's the relationship between AlterU and Aigram": AlterU = standalone new brand (US market, App Store). Aigram = underlying tech infra (iframe bridge + API). Externally always say AlterU; Aigram only shows up in the endpoint table. Don't put this on the slide — outside makers don't need to know.</p>
""",
},

# ───── End ──────────────────────────────────────────────────────────
"resources": {
    "short": "Resources",
    "body": """
<div class="col-text">
  <span class="eyebrow"><span class="dot"></span>End · Q&A + resources</span>
  <h1 class="title">Three lines<br/>to <em>take home</em>.</h1>
  <ul class="bullets" style="font-size: 18px;">
    <li><strong>AlterU = identity-driven feed</strong> · not another mini-game collection. Run every idea through the 4-layer check first.</li>
    <li><strong>AI isn't a spinner — it's the play</strong> · the 5-8s gen-image wait must become the develop / form / unseal ritual.</li>
    <li><strong>Bake social on day one</strong> · score-beat / feed-needs-a-verb / cross-user wall / notify cannot be retrofitted.</li>
  </ul>
  <p class="sub" style="margin-top: 32px;"><strong>Homework</strong>: pick an idea you care about and run it through the elevator on Slide 7 — where's the identity hook? how's the content AI-native? what's the social verb? which paradigm?</p>
  <p class="micro" style="margin-top: 24px;">Resources · alteru.app · RUNTIME.md · 30+ shipped reference games · Q&A starts now</p>
</div>
<div class="col-visual">
  <img src="assets/worlds/hero-vista.png" alt="Hero vista"/>
</div>
""",
    "notes": """
<p>In the last 5 minutes, have everyone silently re-read those three lines. Then 30 minutes Q&A + on-the-spot elevator practice (2-3 students walk their idea through the 4-layer check live).</p>
<p>Homework: pick two reference games and play each for 30 minutes (recommended: Kiss Wall + Hour Capsule — covers the most depth).</p>
""",
},

}


def apply(slides):
    """Mutate each SLIDES entry in place, filling _en fields from TR."""
    for s in slides:
        tr = TR.get(s["slug"])
        if not tr:
            continue
        # Only overwrite if the EN field isn't already inlined in build.py
        if not s.get("body_en") and tr.get("body"):
            s["body_en"] = tr["body"]
        if not s.get("notes_en") and tr.get("notes"):
            s["notes_en"] = tr["notes"]
        if tr.get("short") and s.get("short_en") == s.get("short"):
            # only override the fallback short_en, not an explicitly set one
            s["short_en"] = tr["short"]
