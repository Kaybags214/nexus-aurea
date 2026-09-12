# Check 4 — Air Waybill entry

The dry ice entry lives in Nature and Quantity of Goods, or in Handling Information.

- [ ] The dry ice entry is present in one of those fields
- [ ] UN1845 and the proper shipping name appear
- [ ] Number of packages containing dry ice is shown
- [ ] Net quantity **per package in kg** appears here, not only on the DGD
- [ ] Temperature-control instruction present where the product is temperature-controlled

Expected shape of a correct entry:

```
UN1845 Dry ice, 3 x 2.5 kg
```

Package count plus per-package weight. A shipment total alone does not satisfy this.

## When check 1 said no DGD is required

The AWB entry is then the **only** place the dry ice is declared. Its absence is Critical with
no fallback document to carry it.

Broader AWB completeness — parties, check digit, chargeable weight — belongs to `awb-review`.
Note anything you spot and leave it there.
