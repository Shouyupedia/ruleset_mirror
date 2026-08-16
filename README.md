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

- Updated from: `64af54a098497074b89a48e0fc8bcbeb5de61a8a`
- Upstream head: `fd2d2cd378c4ea3d1587db5d16813a95cee51600`
- Time (UTC): 2026-08-16 07:00:02Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 11
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 2

### Skipped file list
- `Internal/mtproto-dc-config.json` (ratio=0.6375, changed=102, add=48, del=54, base_lines=160, new_lines=154)
- `Internal/sukka_ubo_url_redirect_filters.txt` (ratio=1.9255, changed=362, add=181, del=181, base_lines=187, new_lines=188)

<!-- END_GUARD_REPORT -->
