# ruleset mirror

## Binary rule sets

GitHub Actions compiles supported sources alongside the original files:

- `Clash/domainset/*.txt` becomes domain-behavior `*.mrs`.
- CIDR-only `Clash/ip/*.txt` becomes ipcidr-behavior `*.mrs`.
- `sing-box/{domainset,non_ip,ip}/*.json` becomes `*.srs`.

Mihomo MRS does not support classical rule sets. `Clash/non_ip` and IP files
containing unsupported rules such as `IP-ASN` remain available in source form
and are not converted into incomplete binaries.

Human pushes to matching source paths trigger the compiler directly. Scheduled
upstream synchronization calls the same reusable compiler explicitly after its
source commit is pushed, because pushes made with `GITHUB_TOKEN` do not create
another push-triggered workflow run.

<!-- BEGIN_GUARD_REPORT -->
## Auto Update Guard Report

- Updated from: `184f6c48121833ecf81113f4d97919d610f32188`
- Upstream head: `733a1d5c6c97baf721e26c8f6313b65b94971123`
- Time (UTC): 2026-08-29 07:06:27Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 18
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1583, changed=3965, add=3068, del=897, base_lines=1252, new_lines=3423)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1580, changed=3965, add=3068, del=897, base_lines=1253, new_lines=3424)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1586, changed=3959, add=3065, del=894, base_lines=1246, new_lines=3417)

<!-- END_GUARD_REPORT -->
