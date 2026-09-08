# 05 — Client-Intake Portal: Pre-Deployment Checklist

**Status:** A gate to run against the portal. **Not an audit of it.**

The portal is built and committed to a local repository, is not deployed, and has no real
credentials configured. It is not in `kaybags214/nexus-aurea` or `kaybags214/Nexus-Core`, so I could
not read a single line of it. Nothing below is a finding about your code — every item is a question
to answer against it.

**The timing is the opportunity.** Right now the portal holds no client data and no live
credentials. That is the cheapest moment in its entire lifetime to fix a secrets-handling or
retention defect. After deployment, every one of these items costs ten times as much and some
become unfixable — a credential committed to git history is a rotation, not an edit.

Read alongside `07-client-document-custody.md`, which decides *where* anything this portal collects
is allowed to live.

---

## A. Secrets and configuration

- [ ] No credential, API key, token, connection string, or password in the repository — **including
      git history.** Run `git log -p | grep -niE 'api[-_]?key|secret|token|password|bearer'` over
      the full history, not just the working tree.
- [ ] `.env` is git-ignored, and a committed `.env.example` documents every required variable with
      placeholder values only.
- [ ] No secret reaches the client bundle. Anything in frontend JavaScript is public — a "hidden"
      API key in a React build is a published API key.
- [ ] Secrets come from the deployment platform's secret store, never from a file on the server.
- [ ] Session signing key, CSRF secret, and any encryption key are generated per environment. No
      shared default, no key committed anywhere, no key reused between staging and production.
- [ ] A written rotation procedure exists — what to rotate, in what order, and who does it.

## B. Authentication and access

- [ ] No default, seeded, or hardcoded accounts survive into production.
- [ ] Password storage uses a modern KDF (bcrypt / scrypt / Argon2). Never SHA-256, never MD5,
      never unsalted.
- [ ] MFA for every staff/admin account. `docs/cloud-architecture.md` already lists MFA as a Phase 1
      guiding principle — this is where it becomes real.
- [ ] Session cookies: `HttpOnly`, `Secure`, `SameSite=Lax` or stricter, with a bounded lifetime.
- [ ] Authorisation is enforced **server-side on every request.** A hidden UI element is not access
      control. Confirm a logged-in client cannot reach another client's submission by changing an ID
      in the URL — test it, don't assume it.
- [ ] Rate limiting on login, password reset, and upload endpoints.
- [ ] Account lockout or progressive delay after repeated failures.

## C. File upload — the highest-risk surface

This portal exists to receive shipping documents, so upload *is* the product. It is also where the
worst outcomes live.

- [ ] MIME type **and** extension validated against an allow-list (`application/pdf`, `image/jpeg`,
      `image/png`). Allow-list, never deny-list — a deny-list fails on the first type nobody thought
      of.
- [ ] Content sniffed, not trusted. A `.pdf` extension proves nothing about the bytes.
- [ ] Maximum file size and maximum file count enforced **server-side**.
- [ ] Uploads stored **outside the web root**, or in object storage — never in a publicly servable
      directory.
- [ ] Stored filenames are generated (UUID), never the client-supplied name. Client filenames are
      an attack surface (path traversal) and can themselves carry client identity.
- [ ] Uploaded files are never executed, interpreted, or served with a `Content-Type` derived from
      user input.
- [ ] Malware scanning, or a documented decision not to and why.
- [ ] SHA-256 computed at upload — this is the same document identity the workflows need (finding
      C-4, fix F-3). Compute it once, at the front door, and it flows through everything downstream.

## D. Data handling — the part that matters most here

Everything in `07-client-document-custody.md` applies. The portal is the front door to it.

- [ ] Documents are **never** committed to git by any code path. Verify the upload directory is
      git-ignored *and* that no backup, export, or logging routine writes into a tracked path.
- [ ] Extracted field values — names, addresses, phone numbers — are never written to application
      logs. Log the `submission_id` and the document hash; never the contents.
- [ ] Error pages and stack traces never echo document content or field values back to the browser.
- [ ] TLS enforced end to end. HTTP redirects to HTTPS; HSTS set.
- [ ] Encryption at rest for the document store.
- [ ] The retention schedule from `07` §5 is implemented, not just written — something actually
      deletes at the stated interval.
- [ ] A deletion-on-request procedure exists and has been tested once.
- [ ] Database backups are encrypted and access-controlled to the same standard as the live data.
      A backup is a full copy of everything you are protecting.

## E. Client consent — blocking

- [ ] The portal presents, and records acceptance of, the client agreement covering **third-party AI
      processing** of submitted documents (`07` §5).
- [ ] Consent is recorded with a timestamp and the agreement version, and is retrievable per client.
- [ ] The portal does not forward any document to the n8n pipeline before consent is recorded.

**This is a hard gate.** `compliance-auditor/n8n-workflow-setup.md` already states the rule. A portal
that accepts a client document and pipes it to a third-party API without recorded consent is the one
failure mode here that is a client-relationship problem and a regulatory problem simultaneously.

## F. Web application basics

- [ ] Parameterised queries throughout. No string-concatenated SQL.
- [ ] Output encoding / framework auto-escaping on. No `dangerouslySetInnerHTML` or equivalent on
      user-supplied content.
- [ ] CSRF protection on every state-changing request.
- [ ] Security headers: `Content-Security-Policy`, `X-Content-Type-Options: nosniff`,
      `Referrer-Policy`, `X-Frame-Options` (or CSP `frame-ancestors`).
- [ ] Dependencies audited (`npm audit` / `pip-audit` / equivalent) with no unresolved high or
      critical findings.
- [ ] Debug mode off. Verbose errors off. Directory listing off.
- [ ] Admin and internal routes are not publicly reachable, or are behind separate authentication.

## G. Operations

- [ ] Application logs capture authentication events, uploads, and access to submissions — with
      identifiers, never contents (per D).
- [ ] Logs are retained long enough to investigate an incident and no longer than necessary.
- [ ] An incident procedure exists: who is contacted, in what order, and what gets told to affected
      clients.
- [ ] Deployment is reproducible — a documented process, not a manual sequence held in memory.
- [ ] Backups are restore-tested. An untested backup is a hypothesis.

---

## Ordering

Do not treat this as a flat list to grind through.

| Priority | Sections | Why |
|---|---|---|
| **Blocking — before any deployment** | A, C, D, E | Secrets, upload handling, data custody, consent. These are the ones that are expensive or impossible to fix afterwards. |
| **Before any client touches it** | B, F | Auth and web hygiene. Fixable post-deploy, but not while a real client is using it. |
| **Before it is relied upon** | G | Operational maturity. |

## Then, and only then

Once A–E pass, the portal can be pushed to a private remote for proper review. **Push it before it
holds client data, not after** — reviewing it while it is still empty is free.

I can run a real audit of it at that point. This checklist is a proxy for one, and it is not the
same thing.
