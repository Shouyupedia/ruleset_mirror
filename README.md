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

- Updated from: `fc82f36c372e51c81054ab8f5d2af792eae2377f`
- Upstream head: `71e8d4593e3d15f9581f5d7b1ea9969c8b7a450f`
- Time (UTC): 2026-07-24 19:47:35Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 22
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 0

### Skipped file list
(none)

<!-- END_GUARD_REPORT -->
