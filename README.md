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

- Updated from: `b19a112f78bb184f2ff064ae21fed8b0a7dd6f93`
- Upstream head: `f2dff33caa40b1d6269d7a75ef4eb761f709a430`
- Time (UTC): 2026-07-23 08:44:32Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 17
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 0

### Skipped file list
(none)

<!-- END_GUARD_REPORT -->
