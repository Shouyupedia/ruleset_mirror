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

- Updated from: `cfb76f0b8850c85c04c6be360d9cc3feb10b1a3e`
- Upstream head: `f9164a127b7aa9d036a12a8b144106564e5e9091`
- Time (UTC): 2026-07-22 19:49:53Z
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
