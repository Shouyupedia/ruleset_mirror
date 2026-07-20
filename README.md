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

- Updated from: `3fed0c011b1e004517320fc2006da0d5b4b136f2`
- Upstream head: `17a9b3c32b857caa59eedb77b7ca295711e723bf`
- Time (UTC): 2026-07-20 19:56:57Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 14
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 0

### Skipped file list
(none)

<!-- END_GUARD_REPORT -->
