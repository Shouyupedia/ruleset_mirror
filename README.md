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

- Updated from: `d7fca6ec75f3cf738aa88cbf91898328f689fa5e`
- Upstream head: `73d980b62d5503d80d9b0dc91a4aaa16daf7608c`
- Time (UTC): 2026-08-01 19:35:00Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 21
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 1

### Skipped file list
- `Internal/sukka_ubo_url_redirect_filters.txt` (ratio=1.9255, changed=362, add=181, del=181, base_lines=187, new_lines=188)

<!-- END_GUARD_REPORT -->
