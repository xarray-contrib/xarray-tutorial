# Handoff: `why-an-index` custom-index tutorial

## The task
Contribute a new "custom indexes" tutorial notebook to the xarray-tutorial repo
(a Jupyter Book).

1. **Read the notebook end-to-end — actually RUN it**, don't assume:
   `pixi run jupyter nbconvert --to notebook --execute intermediate/indexing/why-an-index.ipynb`
   Report its current state.
2. **Work on the examples**: tighten them, make them run cleanly, improve the pedagogy.
3. Where it helps, **base examples on the animations/gifs from earlier tutorial sections**
   for visual continuity. The notebook already reuses `advanced/backends/ocean.gif`
   (the "video time axis" example) — that gif and the animation style of earlier
   sections are the model to follow.
4. **Confirm the target file with the user before editing.**

## The ONE file we work on
- `intermediate/indexing/why-an-index.ipynb` ← OUR notebook (67 cells). The entire task.
- Branch `why-an-index`, off origin/main, baseline commit `d8c4793` already in place.

## DO NOT TOUCH (this derailed a previous session — read this)
- `intermediate/indexing/build_custom_index_1d.ipynb` and **PR #295 "Custom index tutorial"**
  are Emma Marshall's SEPARATE draft on her fork (`e-marshall/xarray-tutorial`, branch
  `custom_index`). It is **prior art / reference ONLY**.
- Never edit it, never branch off `custom_index`. It does not exist on `main`; if it shows
  up in the working tree, ignore it.
- A prior session mistakenly spent effort cleaning up Emma's notebook instead of ours,
  because it anchored on the first PR it found ("the existing branch that adds a start
  here"). Our real work is `why-an-index.ipynb` and was never in Emma's file.

## What the notebook is
Title: *"Why does xarray need an index? (and when a custom one)"*. Intuition-first narrative:
coordinate = array of labels → why scanning is bad → alignment → 1-D index in the wild
(video time axis via `ocean.gif`, `RangeIndex`) → 2-D selection → `NDPointIndex` →
building your own index (1-D rule → regular grid → nonlinear "fisheye" via
`CoordinateTransform`) → "which index, when?" summary.

Full section list (23 headers) is visible by scanning the markdown cells; the arc above
covers it.

## Current xarray API facts (verified against xarray 2025.12, the pinned env)
Check the notebook's custom-index code against these — they are current-API requirements:
- `Index.equals` must be `(self, other, *, exclude=None)` — the old 2-arg form raises a `FutureWarning`.
- `Index.sel` must return an `IndexSelResult`.
- `Index.reindex_like` is `(self, other)` (no `method`/`tolerance`).
- Any **intentional-error cell needs a `raises-exception` cell tag**, or the Jupyter Book
  build (`allow_errors: false` in `_config.yml`) fails.

## Reference material (read-only)
- Custom-index guide: `~/Documents/dev/xarray/doc/internals/how-to-create-custom-index.rst`
- xarray source in `~/Documents/dev/xarray` for `Index` / `PandasIndex` /
  `CoordinateTransform` / `NDPointIndex` / `RangeIndex`.
- Earlier tutorial sections for gif/animation examples (e.g. `advanced/backends/ocean.gif`).

## Environment & workflow
- **pixi** project. Run Python: `pixi run python`. Execute a notebook headless (mirrors the
  book build): `pixi run jupyter nbconvert --to notebook --execute <nb>`.
- Edit notebooks **IN PLACE** via the Jupyter MCP against the user's live JupyterLab
  (they'll paste a URL+token) or `Edit` the `.ipynb` directly. **NEVER** regenerate a
  `.ipynb` from a builder script.
- **Jupyter gotcha (bit us hard last time):** if the MCP warns *"collab socket disconnected /
  split-brain,"* your edits may sit in a local buffer and never reach disk, and a stale
  `.jupyter_ystore.db` RTC cache can serve OLD content to the browser even after a save.
  Fix: ensure **ONE** jupyter server per directory, delete `.jupyter_ystore.db` + `.jupyter/`,
  restart the server. Verify disk truth with `grep`/the contents API, not the browser.

## Housekeeping notes
- Baseline commit `d8c4793` includes the notebook **with outputs** (pre-commit/nbstripout is
  NOT installed in this clone, so outputs weren't stripped). `pre-commit.ci` will strip them
  when this becomes a PR. Fine to keep outputs while developing.
- `pixi.lock` shows as modified in the working tree — local env state, leave it.
- Stray untracked clutter safe to ignore: `Untitled.ipynb`, `intermediate/indexing/Untitled.ipynb`
  (empty), `.jupyter/`, `.jupyter_ystore.db`, `.wrangler/`, `uv.lock`.
- The very first prototype lives at `~/Documents/dev/xarray/.ipynb_checkpoints/why-an-index-checkpoint.ipynb`
  (18 cells, older) — the 67-cell version in this repo supersedes it.

## Suggested opening prompt for the next session
> Read `notes/handoff-why-an-index.md` and continue. Start by running
> `intermediate/indexing/why-an-index.ipynb` end-to-end and reporting its state, then let's
> work on the examples. Confirm you're editing why-an-index.ipynb (NOT Emma's
> build_custom_index_1d.ipynb) before making changes.
