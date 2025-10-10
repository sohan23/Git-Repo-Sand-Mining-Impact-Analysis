# CATEGORIZATION of previously top-level files

This document lists files that were previously located at the repository root and the new categorized copies that were created during a re-organization pass. The original files at the repo root were NOT deleted (per request); copies were created in appropriate subfolders so it's easier to find related code and data.

## Area files
- Original (left at repo root): `Area.py`, `Area-test.py`, `Area.csv`
- Copies created at: `Reach Wise Divison/Bar Area/`
  - `Reach Wise Divison/Bar Area/Area.py`
  - `Reach Wise Divison/Bar Area/Area-test.py`
  - `Reach Wise Divison/Bar Area/Area.csv`

## Meandering Index files
- Original (left at repo root): `Meandering Index.py`, `Meandering Index-Jupyter.ipynb`
- Copies created at:
  - `Meandering Index/Meandering Index.py`
  - `Meandering Index/Plots/Meandering Index-Jupyter.ipynb`

## Notes and helper scripts
- Original (left at repo root): `import pandas as pd.txt`, `t.txt`
- Copies created at:
  - `notes/import pandas as pd.txt`
  - `data/t.txt`

## Data files
- Original (left at repo root): `Month wise production (in MT) in Yamunanagar.txt`
- Copy created at: `data/Month wise production (in MT) in Yamunanagar.txt`

## Why this was done
- To group related scripts, notebooks and datasets into logical folders (e.g. `Meandering Index/`, `Reach Wise Divison/Bar Area/`, `data/`, `notes/`) so they are easier to locate.
- Originals were preserved at the root to avoid accidental deletions or breaking existing references; you can delete them later if/when you want.

## Next steps (optional)
- Remove the originals at the repository root once you're satisfied with the copies.
- Replace the root originals with small README files that point to the categorized locations (if you want lightweight pointers instead of full files at root).

If you want, I can now remove the root originals or create small pointer READMEs in their place — tell me which option you prefer.
