# n8n → Claude Code (headless) — wiring the skills to the intake page

The setup in `n8n-workflow-setup.md` sends the document to the Anthropic API with
`AUDIT-ENGINE-PROMPT.md` pasted in as the system prompt. That works, but **an API call
cannot read this repository** — so it cannot load `.claude/skills/`, cannot open
`standards-of-precedence.md`, and cannot follow a skill's router into its `checks/` files.

This file replaces the model node with a call to **Claude Code running locally**, which can.

Prerequisites, both already true here: n8n self-hosted on the same machine as Claude Code, and
`claude` working from a terminal.

```
[Web page]
   → POST multipart  →  [Webhook node]
   → [Write Binary File]      save the upload into intake/incoming/
   → [Execute Command]        scripts/audit-document.sh <path> <hint>
   → [Read Binary File]       read the report path the script printed
   → [Respond to Webhook]     return it to the page
   → [Gmail]                  optional copy to yourself
```

The skills do the work. n8n only moves files and shells out.

## 1. Webhook node

- Method **POST**, path e.g. `compliance-audit`
- **Binary Data on** so the file arrives as binary
- Response mode: **Using Respond to Webhook node** — the audit takes longer than the
  default immediate response

Your page posts `multipart/form-data` with the file plus an optional `doc_type` text field.

## 2. Write Binary File node

- File Name:
  `/absolute/path/to/nexus-aurea/compliance-auditor/intake/incoming/{{ $execution.id }}-{{ $binary.data.fileName }}`

Use the real absolute path to your clone. `intake/incoming/` is gitignored — see step 6.

## 3. Execute Command node — the important one

```
/absolute/path/to/nexus-aurea/scripts/audit-document.sh "{{ $json.fileName }}" "{{ $json.doc_type || '' }}"
```

The script runs Claude Code with `-p` (one prompt, then exit), points it at the document,
tells it to pick the matching skill and run every check file, writes the report and sidecar,
commits and pushes, then prints the report path as its last line.

**Permission flag — confirmed working.** `--permission-mode acceptEdits` is correct and is the
script's default. Verified on the operator's laptop 2026-09-07 against Claude Code as installed
there; a headless run started and completed the skill chain without stalling on an approval.

It matters because headless mode cannot show an approval prompt: a run that needs one hangs
rather than failing, which looks like a slow job and isn't. If a future Claude Code version
renames the flag, check `claude --help | grep -i permission` and override without editing the
script:

```bash
export CLAUDE_AUDIT_FLAGS="--whatever-the-new-flag-is"
```

n8n does not inherit your shell profile. Set the variable in n8n's own environment (or in the
service unit / `docker-compose.yml` that starts it), not just in `.bashrc`.

Also confirm n8n can see `claude`: n8n often runs with a minimal `PATH`. If the node reports
"command not found", call the script with the absolute path — the script itself checks for
`claude` and exits 69 with a clear message rather than failing silently.

## 4. Read + Respond

- **Read Binary File** — path is the script's stdout, the report file
- **Respond to Webhook** — send it back to your page. Markdown renders fine in a browser.

## 5. Timeout

A full audit — router plus five or six check files, on a photograph — takes longer than a
typical HTTP default. Raise the Execute Command node's timeout, and any reverse-proxy timeout
in front of n8n, to **several minutes**. A truncated run looks like a failure but has usually
already written the report; check `compliance-auditor/intake/runs.log`.

## 6. Keep uploads out of git

`intake/incoming/` holds whatever people upload, which may be unredacted. Per the standing rule
in `CLAUDE.md`, that must not be committed. Confirm `.gitignore` carries:

```
compliance-auditor/intake/incoming/
compliance-auditor/intake/runs.log
```

The script redacts contact details **in the report**; the source upload is a separate matter and
stays out of the repository.

## 6b. What the script accepts as input

The usage line says `<image-or-pdf>`, but the check is `[ -f ]` — any readable file passes,
including a markdown transcription. That is deliberate: it makes the fixture in
`audit-lab/test-fixtures/` usable as a smoke test without hunting for a photograph.

**Be aware of what a text fixture does not test.** It exercises the check files and the report
shape, but never the image-reading path — so the "cannot verify from image" discipline, which
matters on a real photograph of a form, is not exercised at all. A markdown fixture cannot fail
that check because there is no image to fail on.

Test with a real photograph before trusting the intake page with one.

## 7. Exit codes

| Code | Meaning |
|---|---|
| 0 | Report written; path on the last line of stdout |
| 64 | Called with no file argument |
| 66 | File does not exist at that path |
| 69 | `claude` not on PATH — the n8n PATH problem above |
| 70 | Ran, but produced no report file — read `runs.log` and the node's stderr |

Branch on these in n8n rather than treating any non-zero as one failure.

## What this changes downstream

Reports land in `compliance-auditor/audit-reports/` and are pushed. The daily refresh routine
(`docs/agentic-os/README.md`) reads that folder at 07:00 Eastern and updates the command centre,
so a document audited today shows on the dashboard tomorrow morning.

To close that gap, add a second Execute Command node after the audit that fires the refresh
immediately — or ask in a session and it can be run on demand.

## Keeping the old path

`n8n-workflow-setup.md` still works and needs no laptop. It runs the monolithic prompt rather
than the skills, so it has no `checks/` files, no sidecar log, and no repo access. Useful as a
fallback when the laptop is off; not the same audit.
