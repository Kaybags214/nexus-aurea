# Gmail intake — client documents into the laptop

Wires `kenya@nexusaureainc.com` to the laptop so a client's email becomes an audit without a
document ever being committed. Forwarding to the Google mailbox is verified working
(2026-09-06).

Read `compliance/02-sops/data-handling.md` first. The one rule that shapes every node below:
**a real client's document and the report about it never enter the repository.**

```
Client emails kenya@nexusaureainc.com
  → [Gmail Trigger]        new mail, has attachment
  → [Filter]               is it actually a document?
  → [Write Binary File]    into the CLIENT store, outside the repo
  → [Execute Command]      audit-document.sh --client
  → [Read File]            the report
  → [Gmail: Create Draft]  reply to the sender — A DRAFT, NEVER SENT
  → [Gmail: Send]          a notification to YOU, saying one is waiting
```

## Step 0 — the client store must exist first

The script refuses to run (exit 78) if this resolves inside the repository. That guard is
deliberate; do not work around it.

```bash
mkdir -p ~/nexus-aurea-client/{incoming,reports,delivered}
chmod 700 ~/nexus-aurea-client
```

**Encrypt it before real client work.** `chmod 700` stops other accounts on the machine; it does
not protect a stolen disk. A `gocryptfs` mount, a LUKS container, or per-file `age` encryption
all satisfy the requirement — check what is available on the machine rather than assuming.

Full-disk encryption alone is not sufficient if the laptop is left unlocked.

## 1. Gmail Trigger

- Credential: the Google account receiving `kenya@nexusaureainc.com`
- Poll: every minute is fine; every 5 is plenty
- Filters: `has:attachment`
- **Download Attachments: on**

Consider a Gmail filter that labels incoming client mail, and triggering on that label. It keeps
newsletters and receipts out of the workflow and gives you a manual override — remove the label
and nothing fires.

## 2. Filter node — is this actually a document?

Drop anything that is not a document before it reaches the audit:

- Attachment MIME type is an image or PDF
- Attachment size is above a floor (signature images are tiny)
- Sender is not an automated address

A junk attachment costs an audit run and clutters the client store.

## 3. Write Binary File — into the client store

```
{{ $env.HOME }}/nexus-aurea-client/incoming/{{ $execution.id }}-{{ $binary.data.fileName }}
```

**Not** `compliance-auditor/intake/incoming/`. That path is inside the repository and is for
practice material.

## 4. Execute Command — the audit

```
/home/kaybags/nexus-aurea/scripts/audit-document.sh --client "{{ $json.fileName }}" "{{ $json.subject }}"
```

`--client` is the whole point: report to the client store, **nothing committed, git never
touched.** The email subject is passed as the document-type hint — clients usually say what
they are sending.

Raise the node timeout to several minutes. A full skill run is not fast.

## 5. Read the report

The script prints the report path on its last line. Read that file.

## 6. Reply to the client — **as a draft, never sent**

Use **Gmail: Create Draft**, not Send. This is not caution for its own sake:

- A finding can be wrong. The UN-number pairings in the current reports are flagged unverified
  precisely because they need a DGR check.
- The verdict blocks a shipment. That decision goes out under your name and your certification.
- The report contains the **unverified** list, which you are supposed to check *before* anyone
  sees the findings.

**Nothing reaches a client until a person has read it.** If any node in this workflow is ever
switched from Draft to Send, that property is gone.

## 7. Notify yourself

A short Gmail send **to yourself** — sender, document type, verdict, how many Criticals. That is
the alert. The draft is waiting; go read it.

Keep client detail out of the notification if it goes anywhere but your own mailbox.

## What this workflow deliberately does not do

- **Does not commit anything.** Client work is invisible to git by design.
- **Does not send to the client.** Drafts only.
- **Does not delete the incoming file.** Retention is a decision, not a side effect — 30 days
  after delivery, per the SOP, and you make it.
- **Does not update the dashboard.** The dashboard counts practice work. Client volume belongs
  in a work log carrying no party names.

## Before the first real client

Not optional, and none of it is code:

1. **Encrypt the client store.** Step 0 above.
2. **Test the whole path on a document with invented parties** — email it to yourself, watch it
   land as a draft.
3. **Be able to say the disclosure list** — `data-handling.md`. Google holds the document first,
   before you touch it.
4. **Have the client agree to the processing** before their paperwork goes through any AI
   service. Your own standing rule.
