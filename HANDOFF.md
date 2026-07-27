# SWE-bench Multimodal — gold-eval repair: handoff

Goal: make **native gold evaluation** pass for the SWE-bench Multimodal **test** split
(510 instances) on the public `swebench` package, as part of open-sourcing MM.
This branch (`port-mm`) ports MM support from the private repo into public and fixes
several defects. Remaining work is blocked by *this dev box's network egress* and must
continue on a machine with normal internet.

## What's on this branch

1. **MM port** — the Multimodal JS repos (openlayers, carbon, quarto, grommet,
   highlightjs, prism, alibaba-fusion/next, lighthouse, scratch-gui, prettier, eslint,
   bpmn-js, + dev-split repos) added to the JS constants, log parsers, and test-spec
   dispatchers. Public's existing JS repos (axios/babel/three.js/…) untouched.
   Verified behavior-identical to the private harness across all 510.
2. **eslint grading fix** — `eslint/eslint` added to `FAIL_ONLY_REPOS`
   (`constants/__init__.py`). Its parser only records failures (mocha `--reporter min`),
   so it must be graded fail-only; otherwise all 11 eslint instances falsely fail.
3. **highlightjs parser fix** — `parse_log_highlightjs`
   (`log_parsers/javascript.py`): the mocha-epilogue strip now anchors on
   `\n[ \t]*\d+ passing` (pending/failing lines are optional) so summary/stack-trace
   lines are never mis-parsed as test names.
4. **MM test-split guard relaxed** — `run_evaluation.py` no longer hard-blocks local
   eval of `SWE-bench/SWE-bench_Multimodal` test.
5. **`scripts/clean_mm_artifacts.py`** — repairs already-baked phantom
   FAIL_TO_PASS/PASS_TO_PASS entries (see below).

## The corrected dataset

The published F2P/P2P lists contain parser-artifact "test" names baked in at
construction time (e.g. `"1 failing.bash"`, `"at /testbed/…:36:32"`, power-assert /
webpack junk). Regenerate a corrected dataset with:

```bash
python scripts/clean_mm_artifacts.py --hf john-b-yang/SWE-bench_Multimodal \
    --split test --out swebench_multimodal_test.corrected.json
# (or --in <local full test json> --out ...)
```

This removed 29 phantom F2P entries across 18 instances; dropping them recovers all
**14 highlightjs** + **2 next** instances under gold. It does NOT fix genuinely-failing
instances.

## How to run gold eval (on a networked machine)

```bash
pip install -e .                       # this branch
export HF_HUB_DISABLE_XET=1            # only if HF Xet backend is unreachable

python -m swebench.harness.run_evaluation \
    --dataset_name swebench_multimodal_test.corrected.json \
    --split test --predictions_path gold \
    --namespace '' --cache_level instance \   # build images locally, KEEP them
    --max_workers <N> --run_id mm-gold
```

- `--namespace ''` builds instance images locally (the image build does
  `git clone https://github.com/<repo>`). Prebuilt images for ~108 carbon/quarto
  instances are NOT on Docker Hub, so local build (or building+pushing) is required.
- `--cache_level instance` keeps built images so you can `docker push` them to the
  `swebench` namespace afterward (override existing). NOTE: carbon images are ~14 GB
  each — build/push/prune in batches; don't try to retain all at once (~1.9 TB).
- Keep `--max_workers` modest for the carbon tail (giant images fill disk fast).

## Network egress required (why this box can't do it)

Containers here have **no outbound internet**; the only host egress is a corporate
proxy that allows npm/HF but blocks `github.com`, `raw.githubusercontent.com`, and
`cdn.jsdelivr.net` (all needed). On the target machine these must be reachable:

- **`github.com`** — image build `git clone` (public repos).
- **`raw.githubusercontent.com`** — openlayers tests download reference `expected.png`.
- **`cdn.jsdelivr.net`** — carbon tests make live HTTP calls at runtime.
- **`registry.npmjs.org`** — npm install during image build.

## Status / expected outcome

Baseline on this box (pull mode, before corrected data): **327 resolved / 427 scored**
(83 carbon/quarto unscored = missing images). With this branch + corrected dataset:
**343** (adds 14 highlightjs + 2 next). On a networked box the env-blocked buckets
(~180: carbon-25 CDN, openlayers-47 PNGs, ~108 missing-image builds) should largely
resolve, leaving only the genuine defects below.

## Remaining genuine defects (~10 — real debugging, not env)

- `alibaba-fusion/next`: **next-870** (whole test file crashes, 79 real fails),
  **next-2131** (`Tree - should render by children` fails),
  **next-101 / next-114** (floating-point + async `Select` tests),
  **next-1720** (`afterEach` hook throws), **next-3345** (headless-focus `activeElement`).
- `grommet`: **grommet-2061**, **grommet-2124** (jest snapshot mismatches).
- `prettier`: **prettier-9514** (jest snapshot mismatch).
- `GoogleChrome/lighthouse`: **lighthouse-1446**.
- `bpmn-io/bpmn-js`: **bpmn-js-1203**.
