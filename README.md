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

- Updated from: `a11a357494914cda360a59a46e0f76cd56ed045c`
- Upstream head: `1fa421d2294570e43b5049d7acab28d79321456d`
- Time (UTC): 2026-08-14 13:44:32Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 22
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 2

### Skipped file list
- `Internal/mtproto-dc-config.json` (ratio=0.5875, changed=94, add=38, del=56, base_lines=160, new_lines=142)
- `Internal/sukka_ubo_url_redirect_filters.txt` (ratio=1.9255, changed=362, add=181, del=181, base_lines=187, new_lines=188)

<!-- END_GUARD_REPORT -->
