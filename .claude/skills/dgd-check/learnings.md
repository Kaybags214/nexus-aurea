# Learnings — dgd-check

Append after every run. Newest at the top.

Format:

```
## YYYY-MM-DD — <UN number / shipment ref>
- What the document did that the skill did not expect:
- What the skill got wrong or missed:
- Change to make to SKILL.md:
```

---

## Seeded expectations — replace with real observations

- Section 1 assumes packing instruction limits get verified against a physical DGR copy each
  time. If that proves too slow in practice, the fix is a lookup table in `dgr/01-iata/` for the
  UN numbers actually seen — not skipping the check.
- Unknown which state variations apply on the lanes reviewed here. Once known, name them
  explicitly in section 1 so they stop being a generic reminder.
