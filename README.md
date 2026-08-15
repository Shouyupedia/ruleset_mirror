# ruleset mirror

## Binary rule sets

GitHub Actions compiles supported sources alongside the original files:

- `Clash/domainset/*.txt` becomes domain-behavior `*.mrs`.
- CIDR-only `Clash/ip/*.txt` becomes ipcidr-behavior `*.mrs`.
- `sing-box/{domainset,non_ip,ip}/*.json` becomes `*.srs`.

Mihomo MRS does not support classical rule sets. `Clash/non_ip` and IP files
containing unsupported rules such as `IP-ASN` remain available in source form
and are not converted into incomplete binaries.

<!-- BEGIN_GUARD_REPORT -->
## Auto Update Guard Report

- Updated from: `828ce4c8ea82dec25c09eeafadb5452e4fc8be9d`
- Upstream head: `9fbd0c0b84c14b2552149e7389628b0a08963795`
- Time (UTC): 2026-08-15 18:48:35Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 14
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 2

### Skipped file list
- `Internal/mtproto-dc-config.json` (ratio=0.6625, changed=106, add=50, del=56, base_lines=160, new_lines=154)
- `Internal/sukka_ubo_url_redirect_filters.txt` (ratio=1.9255, changed=362, add=181, del=181, base_lines=187, new_lines=188)

<!-- END_GUARD_REPORT -->
