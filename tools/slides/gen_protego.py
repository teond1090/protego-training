"""The Protego course slides, as HTML (render with render_slides.py).

Same layout as the TPP RV deck — white slide, heading, rows, the right 640px
kept empty for the presenter so she never covers a word — in Protego's navy
(#10254C) and blue (#2891CD), measured from the Protego partner presentation.

Every fact on these slides comes from the Protego plan terms, the $14
addendum or the tenant letters.
"""
import base64, pathlib, re
HERE = pathlib.Path(__file__).resolve().parent
OUT = HERE / 'html-protego'; OUT.mkdir(exist_ok=True)
MEDIA = HERE.parent.parent / 'media'
b64 = lambda f: "data:image/png;base64," + base64.b64encode((MEDIA / f).read_bytes()).decode()
LOGO, SHIELD = b64('protego-logo.png'), b64('protego-shield.png')

NAVY, BLUE, TEAL = "#10254C", "#2891CD", "#2BA7C9"
CSS = f"""
*{{box-sizing:border-box;margin:0;padding:0}}
body{{width:1920px;height:1080px;font-family:'Segoe UI',Arial,sans-serif;background:#fff;overflow:hidden}}
.slide{{width:1920px;height:1080px;position:relative;background:#fff;padding:96px 640px 0 120px}}
/* the right 640px is reserved for the presenter, so nothing is ever covered */
.stage{{width:100%}}
.kick{{font-size:27px;font-weight:800;letter-spacing:6px;text-transform:uppercase;color:{BLUE};margin-bottom:18px}}
h1{{font-size:76px;color:{NAVY};font-weight:800;letter-spacing:-1.5px;line-height:1.04}}
h1 em{{color:{BLUE};font-style:normal}}
.lede{{font-size:34px;color:#5d6878;margin-top:24px;line-height:1.35}}
.rows{{margin-top:52px}}
.row{{display:flex;gap:30px;align-items:flex-start;margin-bottom:34px}}
.ic{{width:74px;height:74px;border-radius:50%;background:{BLUE};flex:none;display:flex;
  align-items:center;justify-content:center;color:#fff;font-size:33px;font-weight:800}}
.row .t{{font-size:36px;font-weight:800;color:{NAVY};line-height:1.2}}
.row .d{{font-size:28px;color:#5d6878;margin-top:8px;line-height:1.35}}
table{{width:100%;border-collapse:collapse;margin-top:50px;font-size:36px}}
th{{background:{NAVY};color:#fff;text-align:left;padding:26px 34px;font-size:30px}}
th:last-child,td:last-child{{text-align:right}}
td{{padding:28px 34px;color:{NAVY};font-weight:700;border-bottom:2px solid #eef2f6}}
tr:nth-child(even) td{{background:#f4f8fc}}
td.fee{{color:{BLUE};font-weight:800}}
.pill{{display:inline-block;margin-left:18px;padding:6px 18px;border-radius:30px;background:#e8f3fb;
  color:{NAVY};font-size:22px;font-weight:800;letter-spacing:.5px;vertical-align:middle}}
.note{{font-size:27px;color:#5d6878;margin-top:26px;line-height:1.4}}
.grid{{display:flex;flex-wrap:wrap;gap:24px;margin-top:48px}}
.tile{{flex:0 0 calc((100% - 48px)/3);min-width:0;background:#f1f6fb;border-radius:18px;padding:28px 26px}}
.tile > b{{display:block;font-size:30px;color:{NAVY};margin-bottom:8px;line-height:1.2}}
.tile span{{font-size:25px;color:#5d6878;line-height:1.3}}
.flag{{margin-top:44px;background:#fff5d6;border-left:12px solid #e0b23c;border-radius:14px;
  padding:30px 36px;font-size:31px;color:#1b2330;line-height:1.35}}
.foot{{position:absolute;bottom:52px;left:120px;right:640px;display:flex;align-items:center;gap:14px;
  font-size:24px;color:#9aa5b1;font-weight:700}}
.foot img{{height:34px}}
.big{{font-size:150px;font-weight:800;color:{BLUE};line-height:1}}
.title-slide{{background:linear-gradient(135deg,{NAVY} 0%,#173569 60%,#1d4583 100%)}}
.title-slide h1{{color:#fff;font-size:92px}}
.title-slide .kick{{color:#8fd0f0}}
.title-slide .lede{{color:#cdd9ea}}
.title-slide .foot{{display:none}}
.logo-pill{{display:inline-block;background:#fff;border-radius:22px;padding:26px 38px;margin-bottom:64px}}
.logo-pill img{{height:92px;display:block}}
.contact{{margin-top:48px;background:#f1f6fb;border-radius:20px;padding:38px 42px}}
.contact b{{display:block;font-size:44px;color:{NAVY}}}
.contact span{{display:block;font-size:30px;color:#5d6878;margin-top:8px}}
"""
def page(body, cls=""):
    return (f"<html><head><meta charset='utf-8'><style>{CSS}</style></head><body>"
            f"<div class='slide {cls}'><div class='stage'>{body}</div>"
            f"<div class='foot'><img src='{SHIELD}'><span>Protego Protection</span></div>"
            f"</div></body></html>")
S = []
def add(n, body, cls=""): S.append((n, page(body, cls)))
row = lambda n, t, d: f"<div class='row'><div class='ic'>{n}</div><div><div class='t'>{t}</div><div class='d'>{d}</div></div></div>"
tile = lambda t, d: f"<div class='tile'><b>{t}</b><span>{d}</span></div>"

# ---------- part 1: welcome + why Protego exists ----------
add('01-title', f"""<div class='logo-pill'><img src='{LOGO}'></div>
<div class='kick'>Manager &amp; CSR Certification Training</div>
<h1>Protego Manager Training</h1>
<div class='lede'>The plan, the addendum, coverage, claims and opt-outs &mdash; everything you need at the counter.</div>""", 'title-slide')

add('02-gap', "<div class='kick'>Why Protego exists</div><h1>The gap Protego fills</h1><div class='rows'>"
  + row(1, "The lease requires protection", "Every tenant needs protection for what they store.")
  + row(2, "The facility doesn&rsquo;t insure it", "That&rsquo;s printed on the addendum the tenant signs.")
  + row(3, "Homeowner&rsquo;s policies fall short", "Many exclude or limit off-site storage &mdash; tenants find out after a loss.")
  + "</div>")

add('03-not-insurance', "<div class='kick'>The words you use matter</div><h1>A <em>protection plan</em> &mdash; not insurance</h1><div class='rows'>"
  + row(1, "Not an insurance policy", "The plan terms say so, in plain words.")
  + row(2, "You&rsquo;re not an insurance agent", "And the facility isn&rsquo;t an insurance company.")
  + row(3, "Claims don&rsquo;t touch personal insurance", "No premium increase, no mark on their claims history.")
  + "</div><div class='flag'>Say <b>&ldquo;protection plan&rdquo;</b> &mdash; every time.</div>")

# ---------- part 2: plans & presenting ----------
add('04-rates', """<div class='kick'>Plans &amp; pricing</div><h1>Three protection levels</h1>
<table><tr><th>Protection limit</th><th>Monthly fee</th></tr>
<tr><td>$2,000<span class='pill'>Basic &middot; auto-enroll</span></td><td class='fee'>$14</td></tr>
<tr><td>$3,000</td><td class='fee'>$18</td></tr>
<tr><td>$5,000</td><td class='fee'>$26</td></tr></table>
<div class='note'>Effective the moment payment is received &mdash; no waiting period, no application.</div>""")

add('05-present', "<div class='kick'>At the counter</div><h1>How to offer it</h1><div class='rows'>"
  + row(1, "Ask <em style='color:#2891CD;font-style:normal'>which</em>, not whether", "&ldquo;Which level of protection do your belongings need?&rdquo;")
  + row(2, "Frame it daily", "$14 a month is under 50&cent; a day &mdash; less than most deductibles.")
  + row(3, "Look at what&rsquo;s going in", "Storing more than $2,000? That&rsquo;s your cue to talk about $3,000 or $5,000.")
  + "</div>")

# ---------- part 3: the addendum ----------
add('06-addendum', "<div class='kick'>What the tenant signs</div><h1>The Protego addendum</h1><div class='rows'>"
  + row(1, "Records the limit they chose", "$2,000, $3,000 or $5,000.")
  + row(2, "Lists what the plan covers", "Read before anything ever happens.")
  + row(3, "Gets signed", "Proof the tenant accepted the plan &mdash; kept with the lease.")
  + "</div>")

add('07-decline', "<div class='kick'>When a tenant declines</div><h1>Signing the decline isn&rsquo;t the end</h1><div class='rows'>"
  + row(1, "They sign the decline line", "At the bottom of the addendum.")
  + row(2, "They submit their policy", "At MyOwnPolicy.com.")
  + row(3, "The plan stays on until approved", "Protego remains on their account until the opt-out is approved.")
  + "</div><div class='flag'>Tell them the next step <b>right then, at the counter.</b></div>")

# ---------- part 4: coverage & exclusions ----------
add('08-covered', "<div class='kick'>What&rsquo;s covered</div><h1>Covered causes of loss</h1><div class='grid'>"
  + tile("Fire &amp; explosion", "Plus smoke and hail")
  + tile("Burglary", "With visible forced entry")
  + tile("Vandalism", "And malicious mischief")
  + tile("Roof leak", "And water damage")
  + tile("Windstorm", "That first damages the building")
  + tile("Collapse", "Of the building")
  + "</div><div class='note'>Rodent damage is covered up to $500.</div>")

add('09-burglary', "<div class='kick'>Know these cold</div><h1>Burglary &amp; water</h1><div class='rows'>"
  + row(1, "Visible forced entry", "Damage to the unit itself &mdash; a missing lock is not forced entry.")
  + row(2, "A police report", "Required for every burglary claim.")
  + row(3, "Roof leak: covered. Flood: not", "No flood, surface water, or sewer and drain backup.")
  + "</div><div class='flag'><b>$250 burglary deductible</b> per incident &mdash; <b>waived</b> with a disc, cylinder or Noke lock and proof: a photo of the damaged lock, or the receipt.</div>")

add('10-limits', "<div class='kick'>The limits</div><h1>What the plan will pay for</h1><div class='rows'>"
  + row(1, "Inside a locked, fully enclosed unit", "Not vehicles, boats, or anything stored outdoors.")
  + row(2, "$500 in total", "Cash, documents, jewelry and watches.")
  + row(3, "Half the plan limit, up to $2,500", "Electronics, phones, furs, antiques, wine and spirits.")
  + "</div>")

add('11-not-covered', "<div class='kick'>Not covered</div><h1>Exclusions</h1><div class='grid'>"
  + tile("Animals &amp; food", "Never covered")
  + tile("Firearms", "And ammunition")
  + tile("Flammables", "And combustibles")
  + tile("Irreplaceables", "Personal photos, memorabilia")
  + tile("Business use", "Anything tied to a business run on the property")
  + tile("Rodents + perishables", "Rodent cover is void if perishables are stored")
  + "</div><div class='flag'>Rent more than <b>5 days late</b>? The plan ends.</div>")

# ---------- part 5: filing a claim ----------
add('12-claim', "<div class='kick'>Filing a claim</div><h1>How a claim works</h1><div class='rows'>"
  + row(1, "Tell the facility right away", "As soon as it happens, or as soon as it&rsquo;s discovered.")
  + row(2, "File at ProtegoClaims.com", "Within 30 days of discovery. Toll-free number at the bottom of the page.")
  + row(3, "Photos, and don&rsquo;t move anything", "Until the adjuster or facility manager says it&rsquo;s okay.")
  + row(4, "Proof of ownership", "Receipts and records for what they&rsquo;re claiming.")
  + "</div>")

add('13-claim-process', "<div class='kick'>Keep it moving</div><h1>Burglary &amp; the adjuster</h1><div class='rows'>"
  + row(1, "Burglary", "Police report, and you verify a visible sign of forced entry.")
  + row(2, "ClaimsPros", "The claims administrator handles every claim.")
  + row(3, "Answer every call", "If the tenant stops responding, the claim is declined and closed.")
  + "</div>")

add('14-payout', "<div class='kick'>What the plan pays</div><h1>Repair or replace</h1><div class='rows'>"
  + row(1, "The lesser of the two", "Reasonable cost to repair, or to replace with similar quality.")
  + row(2, "Up to the plan limit", "$2,000, $3,000 or $5,000.")
  + row(3, "Clothing &amp; household linens", "Fair market value, taking age and condition into account.")
  + "</div>")

# ---------- part 6: opt-out + close ----------
add('15-optout', """<div class='kick'>Using their own policy</div><h1>The opt-out window</h1>
<div class='big' style='margin-top:40px'>10 days</div>
<div class='lede'>from move-in, to upload their insurance declaration page at <b style='color:#10254C'>MyOwnPolicy.com</b>.</div>""")

add('16-five', "<div class='kick'>The declaration page must show</div><h1>All five details</h1><div class='rows'>"
  + row(1, "An accepted insurance provider", "Major carriers only.")
  + row(2, "Their name exactly as on the lease", "")
  + row(3, "A current expiration date", "Not expired, and not expiring within 30 days.")
  + row(4, "Personal property or off-premises coverage", "Clearly stated.")
  + row(5, "The deductible amount", "Clearly shown.")
  + "</div>")

add('17-after', "<div class='kick'>What happens next</div><h1>After the upload</h1><div class='rows'>"
  + row(1, "Nothing approved in 10 days", "They stay on the $2,000 plan; the charge appears on their invoice.")
  + row(2, "Approved", "The Protego charges come off their account.")
  + row(3, "Upload trouble", "Email support@myownpolicy.com &mdash; answered within one business day.")
  + row(4, "Policy expiring", "They get a notice 10 days ahead. Move-out ends the plan automatically.")
  + "</div>")

add('18-recap', "<div class='kick'>You&rsquo;re ready</div><h1>Protego in one breath</h1><div class='grid'>"
  + tile("Not insurance", "A protection plan")
  + tile("$14 &middot; $18 &middot; $26", "Three levels a month")
  + tile("The addendum", "Signed at every rental")
  + tile("Burglary", "Forced entry + police report")
  + tile("30 days", "To file at ProtegoClaims.com")
  + tile("10 days", "To opt out at MyOwnPolicy.com")
  + "</div>")

add('19-contact', """<div class='kick'>Questions?</div><h1>Don&rsquo;t guess &mdash; ask</h1>
<div class='contact'><b>Teon Delacruz</b><span>Client Success Manager &middot; Direct 623-215-0691</span><span>tdelacruz@tenantpropertyprotection.com</span></div>
<div class='rows' style='margin-top:40px'>"""
  + row("i", "ProtegoTermsConditions.com", "The full plan terms, always available.")
  + "</div>")

for n, h in S: (OUT / f"{n}.html").write_text(h, encoding="utf-8")
print("wrote", len(S), "slides")
