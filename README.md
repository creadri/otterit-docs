# Whitepapers & Governance

Vendor-agnostic network security whitepapers and governance documents. Ready to use, adapt, and share.

**Author:** Adrien Nelis — Network Security Architect
**License:** [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) — reuse freely, attribution required.

---

## Contents

### Whitepapers

| Document | Status | Description |
|----------|--------|-------------|
| [Firewall Automation: Simplify First](Automation/Automation.md) | published | When automation makes sense, what to do first, and how to avoid the common traps |

### Governance

| Document | Status | Description |
|----------|--------|-------------|
| [Firewall Governance](Governances/Firewall%20Governance.md) | draft | Rule policy, nomenclature, lifecycle, ownership, and review cadence |

### Slides

| Deck | Description |
|------|-------------|
| [Firewall Automation](Automation/Automation.slides.md) | Marp slide deck — companion to the whitepaper |

---

## Structure

```
whitepapers/
├── Automation/
│   ├── Automation.md           # Whitepaper
│   ├── Automation.slides.md    # Marp slide deck
│   ├── diagrams/               # D2 source + rendered SVGs
│   └── .research/              # Raw research notes (not published)
├── Governances/
│   └── Firewall Governance.md
└── scripts/
    └── d2-render.sh            # Render all D2 diagrams to SVG
```

---

### AI assistance

AI tools are used selectively throughout this project — as an accelerator, not a ghostwriter.

**In scope:**
- Improving written English clarity and tone
- Translation
- D2 Diagram building assist
- Deep research and source aggregation
- Review and critique of existing content
- Drafting slide presentations from completed documents

**Out of scope:**
- Writing documentation from scratch
- Defining structure, argument, or conclusions

All analysis, positions, and judgements are human-authored.


---

## Tooling

**Edit:** [Obsidian](https://obsidian.md) or any Markdown editor.

**Diagrams:** [D2](https://d2lang.com) — source files in `diagrams/*.d2`, rendered to `diagrams/*.svg`.

```bash
# Render all diagrams
bash scripts/d2-render.sh
```

**Slides:** [Marp](https://marp.app)

```bash
# Export slides to PDF
marp Automation/Automation.slides.md --pdf
```

---

## Contributing

Fork, adapt, reuse — CC BY 4.0. Attribution: **Adrien Nelis**.
Open an issue or PR for corrections and additions.
