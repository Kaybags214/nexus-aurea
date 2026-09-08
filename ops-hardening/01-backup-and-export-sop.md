# 01 — Backup & Export SOP

**Run this before any workflow is changed.** No hardening step in `02-hardening-report.md` may be
applied until a verified backup of that workflow exists.

There is currently **no backup of any workflow**. `nexus-core/automation/` and
`nexus-core/ai-configs/` are empty. If the n8n Cloud tenant were lost today, all five workflows
would be gone.

---

## 1. Why you have to run this, not me

This session has no n8n Cloud credential and no n8n API access. I cannot export, back up, read, or
change any live workflow. That is by design for today — objective 5 says the hardening report comes
*before* any change — but it also means the backup step is yours.

Do not paste an n8n API key into this session to work around that. There is no step below that
needs one.

---

## 2. Export procedure (n8n Cloud UI, ~5 minutes for all five)

For each of the five workflows:

1. Open the workflow in n8n Cloud.
2. **Note the active state before you touch anything** — Active or Inactive, top right. Record it.
3. `⋯` menu (top right) → **Download**. This writes `<Workflow Name>.json`.
4. Do not click Save, Activate, or Deactivate. Downloading does not modify the workflow.

Repeat for: Market Watch, Class 3 Flammable Liquids, Class 8 Corrosive Materials,
Class 9 Miscellaneous Dangerous Goods, Physical AI — Shipment Capture Sandbox.

Also export the **credential inventory** — not the credentials:
`Credentials` list → screenshot or note **name, type, and which workflows use each**. Never export,
copy, or send credential values.

---

## 3. What an n8n export does and does not contain

| Contains | Does not contain |
|---|---|
| Node types, parameters, positions, connections | Credential secrets (values are stored server-side) |
| **Credential names and IDs** — `{"id": "...", "name": "Anthropic account"}` | API keys, tokens, passwords |
| **Webhook paths and IDs** — enough to reconstruct a live URL | The webhook's auth secret value |
| Prompt text, expressions, code node bodies | Execution data / past run payloads |
| **Any secret hardcoded into a parameter, header, or code node** | — |

That last row is the risk. Header values, `Authorization` strings, and anything typed directly into
an HTTP node's parameters are exported **in cleartext**.

---

## 4. Sanitise before the export touches git

Run this against every export before committing. Do not skip it because "there shouldn't be
anything in there" — the point of the check is that you don't yet know.

```bash
# Adjust the path to wherever you saved the downloads.
cd ~/Downloads/n8n-exports

# 1. Look for anything secret-shaped.
grep -rniE 'api[-_]?key|secret|token|bearer|password|passwd|authorization|sk-ant|ghp_|github_pat' *.json

# 2. Look for live webhook hosts and full URLs.
grep -rnoE 'https?://[A-Za-z0-9._-]+\.[A-Za-z]{2,}[^"]*' *.json | sort -u

# 3. Look for pinned test data — real document contents get pinned here and forgotten.
grep -rn '"pinData"' *.json
```

For each hit: replace the value with a placeholder (`"<REDACTED — set in n8n credential store>"`),
or delete the `pinData` block entirely. Keep credential **names** — they are the map of what is
wired to what, and they carry no secret.

Then confirm the file is clean and still valid JSON:

```bash
python3 -c "import json,sys; [json.load(open(f)) for f in sys.argv[1:]]; print('valid JSON')" *.json
```

---

## 5. Where backups go

Two tiers, because they have different risk profiles.

**Tier 1 — sanitised structure, committed to git.**
`nexus-core/automation/workflow-backups/YYYY-MM-DD/<workflow-name>.sanitised.json`

This is the version-controlled record of workflow structure. It is what makes a change reviewable:
you can diff the proposed hardening against it. It must never contain a secret.

**Tier 2 — raw export, never committed.**
Encrypted storage outside git — a password manager attachment, or an encrypted volume. This is your
actual disaster-recovery copy. Keep it, but keep it out of the repository.

A `.gitignore` rule has been added to `nexus-aurea` to make an accidental raw commit harder:

```
n8n-exports/
*.raw.json
*.credentials.json
```

That is a backstop, not a control. The control is §4.

---

## 6. Restore test

A backup you have never restored is not a backup. Once, after the first export:

1. In n8n Cloud, `Workflows` → `Import from File` → pick the sanitised Class 9 export.
2. It imports as a **new, inactive** workflow. Rename it `ZZ — restore test — DELETE ME`.
3. Confirm the node graph matches the original and that credential fields show as unset
   (expected — secrets are not in the export; you re-select them from the credential store).
4. Delete the test workflow.

Do not activate it. Do not attach credentials to it. Two workflows sharing a webhook path will
conflict.

---

## 7. Backup cadence

- **Before every change** — export the specific workflow first, no exceptions.
- **Weekly** — export all five, sanitise, commit the diff. The diff is the change log.
- **After any change** — export again and commit, so the repository reflects live state.

---

## 8. Pre-change checklist

Do not proceed to `02-hardening-report.md` until every line is true:

- [ ] All five workflows exported.
- [ ] Active/inactive state recorded for each.
- [ ] Credential inventory noted (names and types only).
- [ ] §4 sanitisation run; every hit reviewed and resolved.
- [ ] Sanitised copies committed to `nexus-core/automation/workflow-backups/<date>/`.
- [ ] Raw copies stored encrypted, outside git.
- [ ] Restore test performed once and the test workflow deleted.
- [ ] Proposed changes reviewed and approved by you — not applied by anyone else first.
