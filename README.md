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

- Updated from: `10954881762bb77d17b1be0c93ebe6c968aa929f`
- Upstream head: `ec444ad906583c6ae78cfcb18666c269fda0a1e9`
- Time (UTC): 2026-08-09 19:01:54Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 38
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 1

### Skipped file list
- `Internal/sukka_ubo_url_redirect_filters.txt` (ratio=1.9255, changed=362, add=181, del=181, base_lines=187, new_lines=188)

<!-- END_GUARD_REPORT -->
