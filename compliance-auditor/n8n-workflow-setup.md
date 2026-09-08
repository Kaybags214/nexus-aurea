# n8n Workflow Setup — Compliance Auditor (photo in → audit out)

The self-hosted, hands-off version. You send a photo of a document to a webhook (or email it in),
n8n runs it through a vision model using `AUDIT-ENGINE-PROMPT.md`, and you get the audit back by
email + committed to the repo. Same brain as the in-chat option, automated.

This mirrors your `market-watch/n8n-analysis-prompt.md` setup — same Anthropic node, same billing model.

## Flow overview

```
[Webhook / Email Trigger]  →  [Set: doc_type + notes]  →  [Anthropic Chat Model (vision)]
        →  [Basic LLM Chain: AUDIT-ENGINE-PROMPT]  →  [Format audit]
        →  [Gmail: send report]  →  [GitHub: commit to compliance-auditor/audit-reports/]
```

## Nodes

1. **Trigger — pick one**
   - **Webhook node** (`n8n-nodes-base.webhook`): method POST, binary/form-data enabled so an image
     can be uploaded. You get a URL like `https://<your-n8n>/webhook/compliance-audit`. POST the
     photo there from your phone (a Shortcut/Tasker button works well).
   - **Gmail Trigger** (`n8n-nodes-base.gmailTrigger`): watch a dedicated label/address; attachments
     become the document images. Easiest for "just email a pic of the paperwork."

2. **Set node** — capture `doc_type` (optional) and `notes` (optional) fields. Leave blank to let
   the model auto-detect the document.

3. **Anthropic Chat Model** (`@n8n/n8n-nodes-langchain.lmChatAnthropic`)
   - Credential: your Anthropic API key (console.anthropic.com) — same one as market-watch.
   - Model: `claude-opus-5` (vision-capable). A cheaper `claude-sonnet` model is fine for routine
     legible documents; use Opus for messy photos or dense DG paperwork.
   - Pass the image as an input attachment on the message (the binary from the trigger).

4. **Basic LLM Chain** (`@n8n/n8n-nodes-langchain.chainLlm`) — attach the model underneath.
   - **System prompt:** paste the whole block from `AUDIT-ENGINE-PROMPT.md`.
   - **User message:** the "User message (n8n / API)" block from that same file.

5. **Gmail — Send** — email the audit to yourself. Subject:
   `Compliance Audit — {{ $json.doc_type || 'auto' }} — {{ $now.format('yyyy-MM-dd') }}`.

6. **GitHub node** (`n8n-nodes-base.github`) — Create/Update file
   - Repo: `Kaybags214/nexus-aurea`
   - Path: `compliance-auditor/audit-reports/audit_{{ $now.format('yyyy-MM-dd') }}_{{ $json.doc_type || 'doc' }}.md`
   - Content: the formatted audit.
   - Commit message: `Compliance audit {{ $now.format('yyyy-MM-dd') }} — {{ $json.doc_type }}`.

## Billing

Anthropic API is pay-per-use, separate from any subscription — same as your market-watch node.
Vision adds image tokens; a single document photo audit typically lands well under $0.10 on Opus,
less on Sonnet.

## Reference standards for the model

The prompt already tells the model to apply the repo's standards. For a fully self-contained n8n run
(no repo access), paste the contents of `standards-of-precedence.md` into the system prompt after the
"Standing rules" section so the model carries the precedence hierarchy inline.

## Privacy

Do not run real customer documents with confidential data through a third-party API without the
customer's agreement. For practice/proof-of-work, redact names before sending — matches the
`audit-lab/` rule.

## Tuning

- Model refuses / says image unreadable → that's correct; reshoot flat, even light, all corners in.
- Missing cross-checks → send all documents for one shipment in a single request (multiple images).
- Too long → add "Keep findings to one line each" to the system prompt.
