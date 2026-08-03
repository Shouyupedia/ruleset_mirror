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

- Updated from: `fb169ea87a682b071256efcecbf8306303303fc4`
- Upstream head: `b4d580b7ad5e046e4b2e00904b2bf9bdd3af975c`
- Time (UTC): 2026-08-03 15:17:27Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 17
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 1

### Skipped file list
- `Internal/sukka_ubo_url_redirect_filters.txt` (ratio=1.9255, changed=362, add=181, del=181, base_lines=187, new_lines=188)

<!-- END_GUARD_REPORT -->
