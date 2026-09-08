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

- Updated from: `db5ad5d5626b8c22f4c24b4ebed1b55ec1b06a77`
- Upstream head: `55a647dea370aebaae9ac58b4d56f4ade0bdbc54`
- Time (UTC): 2026-09-08 11:22:00Z
- Threshold: 0.5
- Min changed lines: 10
- Force update: false
- Updated files: 12
- Added files: 0
- Upstream deleted but kept: 0
- Skipped files (ratio>0.5 AND changed>=10): 3

### Skipped file list
- `Clash/ip/china_ip_ipv6.txt` (ratio=1.1597, changed=3965, add=3066, del=899, base_lines=1252, new_lines=3419)
- `List/ip/china_ip_ipv6.conf` (ratio=1.1594, changed=3965, add=3066, del=899, base_lines=1253, new_lines=3420)
- `sing-box/ip/china_ip_ipv6.json` (ratio=1.1600, changed=3959, add=3063, del=896, base_lines=1246, new_lines=3413)

<!-- END_GUARD_REPORT -->
