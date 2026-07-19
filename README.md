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

- Updated from: `f34a1331dfc1932fada9eec4a54e058ea95bf257`
- Upstream head: `cb49c6a1f70a949639e41f2a3669ffcb74c23ef0`
- Time (UTC): 2026-07-19 03:55:51Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 4
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 0

### Skipped file list
(none)

<!-- END_GUARD_REPORT -->
