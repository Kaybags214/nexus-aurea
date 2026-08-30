# Bill of Lading (Ocean B/L) — Reference Template

Purpose: Field-by-field reference for reviewing an ocean Bill of Lading. Written from common
carrier/NVOCC B/L layouts and the requirements of the US COGSA and the Hague-Visby Rules — original
summary, not a copy of any single proprietary form. Use alongside the AWB reference for air.

## Bill of Lading Type (confirm which one this is)

- **Straight B/L** — consigned to a named party, non-negotiable.
- **Order B/L** — "to order" / "to order of [bank]", negotiable, transferable by endorsement.
- **Bearer B/L** — deliverable to whoever holds it (rare, high risk).
- **Seaway bill / Express release** — non-negotiable, no original needed for release.
- **Master B/L (MBL)** vs **House B/L (HBL)** — MBL issued by the carrier to the NVOCC/forwarder;
  HBL issued by the forwarder to the actual shipper. Confirm they reconcile.

## Header / Identification

- B/L number
- Booking number / export references
- Shipper's reference / forwarder's reference
- Carrier name (and SCAC code)
- Vessel name and voyage number

## Party Information

- Shipper (full name, address)
- Consignee (full name, address — or "TO ORDER" / "TO ORDER OF [bank]" for a negotiable B/L)
- Notify party (name, address — often the same as consignee or a customs broker)

## Routing

- Place of receipt
- Port of loading (POL)
- Port of discharge (POD)
- Place of delivery (final destination)
- Pre-carriage by / vessel / voyage

## Cargo Details

- Number and kind of packages
- Container number(s) and seal number(s)
- Marks and numbers
- Description of goods
- Gross weight (kg) and measurement (CBM)
- HS code (where shown)

## Freight and Charges

- Freight prepaid or freight collect (must be explicit)
- Charges breakdown
- Currency

## Declarations and Signatures

- Number of original B/Ls issued ("number of originals" — critical for release)
- Shipped-on-board date and notation (vs. "received for shipment")
- Place and date of issue
- Carrier / master / agent signature

## Dangerous Goods on Ocean (if applicable)

- IMDG Code applies to sea (not IATA DGR — that is air only).
- UN number, proper shipping name, class/division, packing group, flashpoint (if any).
- Marine pollutant indication where applicable.
- Reference to the Dangerous Goods Declaration / container packing certificate.

## Review / Practice Checklist

- Does the B/L type match the payment/release method (e.g. is a negotiable "to order" B/L intended,
  or should it be straight/seaway)?
- Do container and seal numbers match the packing list and the DG declaration?
- Is "shipped on board" dated and signed (banks require an on-board notation under a letter of credit)?
- Does freight prepaid/collect match the Incoterms on the commercial invoice?
- Do shipper, consignee, notify party, weights, and piece count agree with the invoice and packing list?
- If DG: is the IMDG (not IATA) classification used, and is a marine pollutant flagged if applicable?
- Does the number of original B/Ls issued match what the consignee/bank needs to take delivery?

## Precedence note

For sea freight, **IMDG Code governs dangerous goods, not IATA DGR.** If the same product also moves
by air on another leg, audit that leg against IATA DGR separately. See
`compliance-auditor/standards-of-precedence.md`.

## Sources (blank templates / references — download directly)

- Maersk Bill of Lading sample: https://www.maersk.com/~/media_sc9/maersk/support/files/bill-of-lading-sample.pdf
- ICC / trade references for Hague-Visby Rules and COGSA (search the official texts).
- IMO IMDG Code program page: https://www.imo.org/en/OurWork/Safety/Pages/DangerousGoods-default.aspx
