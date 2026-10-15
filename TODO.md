# TODO

## 4. Data quality

- [ ] **Confirm what the eBird "historic" endpoint returns.** It seems to return one record per species per day (either the most recent or the first-submitted observation), not every sighting. The existing data agrees: it never has more than one row per species, location and day. Check this against the eBird API docs. If it's right, `bird_count` is the count from a single checklist, which matters for trend analysis. Full checklist data comes from different endpoints.
- [ ] **Pick up late checklists.** People often submit checklists days later, so fetching only yesterday misses some. Loads are now safe to re-run, so the daily job can fetch the last 3–7 days.
- [ ] **Revisit the count filter.** [cleanup.py:40](Pipeline/cleanup.py#L40) drops any count over 75, which throws out real flocks (geese and gulls at John Heinz, for example). Counts recorded as "X" (present, not counted) are dropped too.
- [ ] **Make API calls more robust.** Add request timeouts, retries and status codes in error messages. Replace the bare `except:` at [analysis.py:61](Analysis/analysis.py#L61).

## 5. Ship it

- [ ] **Schedule the runs.** Use `cron` or `launchd` for the daily run, plus a monthly backfill.
- [ ] **Use `logging` instead of `print`.**
- [ ] **Rewrite the README.** Cover setup, the `.env` variables, how to run each mode, and the table schema.
- [ ] **Build the Tableau dashboard** the README promises.
