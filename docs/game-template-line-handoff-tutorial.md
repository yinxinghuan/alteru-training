# Game Template Line Handoff Tutorial

This document is local-only handoff material for the Game Template Line work. It is intentionally not part of the public `alteru.app/learn/` build.

## Goal

Let a regular AlterU maker create a polished game from one sentence or one photo.

The production model is:

```text
Locked Engine -> Cartridge data -> Generator / Remix flow -> Build / publish
```

The important boundary:

```text
Engine owns mechanics.
Cartridge owns expression.
```

If changing a field can make the game easier, harder, slower, faster, more forgiving, or less readable as a game, keep it in the engine. If it changes theme, visual identity, copy, prompt framing, palette, audio mood, or sprite choice, it can live in the cartridge.

## Current Assets

### Engine #1: Block Party

Path:

```text
/Users/yin/code/games/block-party
```

Purpose:

Top-down survival / collection arcade. This is the canonical one-sentence engine because it has the full pipeline.

Key files:

```text
src/BlockParty/cartridge/types.ts
src/BlockParty/cartridge/spec.ts
src/BlockParty/cartridge/resolve.ts
src/BlockParty/cartridge/generator-prompt.ts
src/BlockParty/cartridge/index.ts
src/BlockParty/cartridge/zombie.ts
src/BlockParty/cartridge/cat-vacuum.ts
src/BlockParty/builders/registry.ts
src/BlockParty/builders/sprites.ts
scripts/gen-cartridge.ts
```

Generate a cartridge:

```bash
cd /Users/yin/code/games/block-party
npx tsx scripts/gen-cartridge.ts --sentence "a cat surviving robot vacuums" --sprites
```

Switch cartridge:

```ts
// src/BlockParty/cartridge/index.ts
import { specToCartridge } from './resolve';
import { genSomethingSpec } from './gen-something';

export const CARTRIDGE = specToCartridge(genSomethingSpec);
```

Verify:

```bash
npm run build
npm run dev
```

What is safe to change:

- `copy`
- `palette`
- enemy names / creature keys / recolors
- `spriteUrl`
- boss display names
- hero roster labels / tints
- `audioMood`

What should stay locked:

- HP
- movement speed
- weapon damage
- spawn rate
- collision shape
- scoring math
- boss behavior
- pickup radius / payout

Known future seams:

- `BossKind` still mixes behavior and visual identity. Split into `BossBehaviour` and `BossSkin` before boss visuals become user-generated.
- Splash wordmark is still theme-coupled.
- Sprite prompt can be tuned, but keep a 3D fallback path.

### Engine #2: 3D Timing / Climb

Shared engine path:

```text
/Users/yin/code/games/_shared/engine-3d
```

Hosts:

```text
/Users/yin/code/games/corporate-climb
/Users/yin/code/games/sky-leap
```

Corporate Climb cartridge files:

```text
cartridge/types.js
cartridge/index.js
cartridge/office.js
cartridge/firefighter.js
```

Switch cartridge:

```js
// cartridge/index.js
import { officeCartridge } from './office.js';
// import { firefighterCartridge } from './firefighter.js';

export const CARTRIDGE = officeCartridge;
```

Verify:

```bash
cd /Users/yin/code/games/corporate-climb
npm run build
npm run dev
```

What cartridge owns here:

- sky colors
- light colors / intensities
- fog
- bloom
- desk / world colors
- motes
- audio mood
- copy and quips

What stays engine-owned:

- timing windows
- jump / climb physics
- combo logic
- scoring
- camera behavior
- fail / replay state machine

Sky Leap currently consumes the shared engine but does not yet have its own cartridge system. If continuing Engine #2, add the Sky Leap cartridge after Corporate Climb is stable.

### Engine #4: Identity Transform

Path:

```text
/Users/yin/code/games/past-life
```

Cartridge files:

```text
src/PastLife/cartridge/types.ts
src/PastLife/cartridge/index.ts
src/PastLife/cartridge/past-life.ts
src/PastLife/cartridge/future-life.ts
```

Purpose:

Photo-native identity toy. The user photo is the main input; the cartridge changes the identity framing.

What cartridge owns:

- generation prompts
- era / future framing
- reading tone
- booking language
- i18n copy
- theme palette / UI language
- media variant list

What engine owns:

- upload
- AI call flow
- waiting ritual
- save / persistence
- Hall wall
- detail page
- sharing / social structure

Verify:

```bash
cd /Users/yin/code/games/past-life
npm run build
npm run dev
```

## Skill

Main skill:

```text
/Users/yin/code/games/.claude/skills/game-cartridge/SKILL.md
```

Current scope:

- Strong for Block Party.
- Documents A path: one sentence -> generated cartridge.
- Documents B path: hand-written cartridge.
- Does not yet cover Sky Leap or Past Life generation in detail.

Future improvement:

Extend `user-game-creation` so the user-facing wizard can call the cartridge pipeline instead of only describing the intended UX.

## Training Deck

Source:

```text
/Users/yin/alteru-training/build.py
```

Current Part 8 should be treated as the public teaching chapter:

- concept
- engine catalog
- boundary contract
- Remix path
- Engine #1 details
- Engine #2 details
- Engine #4 details
- operating model
- CLI how-to

Build:

```bash
cd /Users/yin/alteru-training
python3 build.py
```

Important:

- The training build also writes external `/Users/yin/code/alteru-landing/learn/`.
- This markdown document lives under `docs/` and is not copied by `build.py`.

## Recommended Next Work

1. Finish the public Part 8 chapter and verify generated slide count / menu grouping.
2. Expand `game-cartridge` skill beyond Block Party, or create engine-specific subsections inside it.
3. Add a Sky Leap cartridge system.
4. Add generator support for the 3D timing engine only after the cartridge contract is proven with a second theme.
5. Split Block Party boss behavior from boss skin before generating boss visuals.
6. Extend `user-game-creation` so Path A can actually route to these engines.

## Acceptance Checklist

Before calling a new engine template done:

- There is one canonical engine that is already polished.
- There are at least two cartridges with visibly different themes.
- Swapping cartridge requires one obvious import/export change.
- Build passes for both cartridges.
- Cartridge fields do not include gameplay tuning.
- There is a validation layer if an LLM can emit the cartridge.
- There is a fallback when image generation or sprite loading fails.
- The skill or handoff doc explains the exact command path.

Before calling public tutorial done:

- Part 8 is an independent chapter in menu and outline.
- It teaches the boundary rule, not just commands.
- It explains Remix impact.
- It covers all three current engine categories.
- It has speaker notes for internal teaching.
- `python3 build.py` succeeds.
- `alteru-landing/learn/` is updated only with public slides, not this handoff document.

## Non-Negotiables

- Do not let Path A grow into a complex editor.
- Do not put HP, speed, damage, spawn rates, or scoring into cartridge.
- Do not remove fallback paths for generated assets.
- Do not use fake users to make social surfaces look full.
- Do not make a new engine template from an unpolished game.
- Do not treat a generator as proof. A second working cartridge is proof.
