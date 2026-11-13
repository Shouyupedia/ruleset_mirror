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

- Updated from: `7976252321f6405c8f68cff04d9ff4cf2c7fc9f7`
- Upstream head: `aea855e71197f27e1ec3a05056e59944a0170906`
- Time (UTC): 2026-11-13 19:44:31Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 23
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 13

### Skipped file list
- `Clash/ip/ai.txt` (ratio=0.9406, changed=523, add=519, del=4, base_lines=41, new_lines=556)
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1776, changed=4057, add=3125, del=932, base_lines=1252, new_lines=3445)
- `Clash/non_ip/domestic_cdn.txt` (ratio=0.5556, changed=20, add=17, del=3, base_lines=22, new_lines=36)
- `LegacyClashPremium/ip/ai.txt` (ratio=0.9423, changed=523, add=519, del=4, base_lines=40, new_lines=555)
- `LegacyClashPremium/non_ip/domestic_cdn.txt` (ratio=0.5714, changed=20, add=17, del=3, base_lines=21, new_lines=35)
- `List/ip/ai.conf` (ratio=0.9406, changed=523, add=519, del=4, base_lines=41, new_lines=556)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1773, changed=4057, add=3125, del=932, base_lines=1253, new_lines=3446)
- `List/non_ip/domestic_cdn.conf` (ratio=0.5556, changed=20, add=17, del=3, base_lines=22, new_lines=36)
- `Surfboard/ip/ai.conf` (ratio=0.9423, changed=523, add=519, del=4, base_lines=40, new_lines=555)
- `Surfboard/non_ip/domestic_cdn.conf` (ratio=0.5714, changed=20, add=17, del=3, base_lines=21, new_lines=35)
- `sing-box/ip/ai.json` (ratio=0.9417, changed=517, add=516, del=1, base_lines=34, new_lines=549)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1785, changed=4053, add=3123, del=930, base_lines=1246, new_lines=3439)
- `sing-box/non_ip/domestic_cdn.json` (ratio=0.6061, changed=20, add=18, del=2, base_lines=17, new_lines=33)

<!-- END_GUARD_REPORT -->
