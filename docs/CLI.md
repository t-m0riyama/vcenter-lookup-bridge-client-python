# vlb CLI Reference

`vlb` is a command-line interface for accessing the vCenter Lookup Bridge API.

---

## Installation

```sh
pip install -e .
```

After installation, the `vlb` command is available:

```sh
vlb --help
```

---

## Authentication

The API server URL and credentials can be provided via **environment variables** or **command-line options**.

| Environment Variable | Option | Description |
|---|---|---|
| `VLB_HOST` | `--host` | API server URL (required) |
| `VLB_USERNAME` | `--username` | Basic auth username |
| `VLB_PASSWORD` | `--password` | Basic auth password |

**Using environment variables (recommended):**

```sh
export VLB_HOST=https://vcenter-lookup-bridge.example.com
export VLB_USERNAME=myuser
export VLB_PASSWORD=mypassword
```

**Passing credentials directly on the command line:**

```sh
vlb --host https://vcenter-lookup-bridge.example.com \
    --username myuser \
    --password mypassword \
    vms list --vm-folders MyFolder
```

---

## Global Options

These options apply to every command and must be placed before the subcommand.

| Option | Default | Description |
|---|---|---|
| `--host` | `$VLB_HOST` | API server URL (required) |
| `--username` | `$VLB_USERNAME` | Basic auth username |
| `--password` | `$VLB_PASSWORD` | Basic auth password |
| `--format [table\|json]` | `table` | Output format |
| `--no-verify-ssl` |  | Disable SSL certificate verification |
| `--version` |  | Show version and exit |

---

## Command Reference

### vms  Virtual Machines

#### `vlb vms list`

List virtual machines in the specified folder(s).

```sh
vlb vms list --vm-folders <folder> [options]
```

| Option | Required | Default | Description |
|---|---|---|---|
| `--vm-folders` |  |  | VM folder name(s), comma-separated |
| `--vcenter` |  |  | Filter by vCenter name |
| `--offset` |  | `0` | Offset for pagination |
| `--max-results` |  | `100` | Maximum number of results |

```sh
# Single folder
vlb vms list --vm-folders Production

# Multiple folders, JSON output
vlb --format json vms list --vm-folders Production,Staging
```

---

#### `vlb vms get <vm_instance_uuid>`

Get detailed information for a VM by its instance UUID.

```sh
vlb vms get <vm_instance_uuid> --vcenter <vcenter>
```

| Argument / Option | Required | Description |
|---|---|---|
| `vm_instance_uuid` |  | Instance UUID of the virtual machine |
| `--vcenter` |  | vCenter name |

```sh
vlb vms get 5012a5f3-7d3b-4c8e-9f1e-2b3c4d5e6f7a --vcenter vc01.example.com
```

---

### hosts  ESXi Hosts

#### `vlb hosts list`

List ESXi hosts.

```sh
vlb hosts list [options]
```

| Option | Required | Default | Description |
|---|---|---|---|
| `--vcenter` |  |  | Filter by vCenter name |
| `--offset` |  | `0` | Offset for pagination |
| `--max-results` |  | `100` | Maximum number of results |

```sh
vlb hosts list --vcenter vc01.example.com
```

---

#### `vlb hosts get <host_uuid>`

Get detailed information for an ESXi host by its UUID.

```sh
vlb hosts get <host_uuid> --vcenter <vcenter>
```

| Argument / Option | Required | Description |
|---|---|---|
| `host_uuid` |  | UUID of the ESXi host |
| `--vcenter` |  | vCenter name |

---

### clusters  Clusters

#### `vlb clusters list`

List clusters.

```sh
vlb clusters list [options]
```

| Option | Required | Default | Description |
|---|---|---|---|
| `--clusters` |  |  | Filter by cluster name(s), comma-separated |
| `--vcenter` |  |  | Filter by vCenter name |
| `--offset` |  | `0` | Offset for pagination |
| `--max-results` |  | `100` | Maximum number of results |

```sh
vlb clusters list --clusters ClusterA,ClusterB
```

---

### datastores  Datastores

#### `vlb datastores list`

List datastores filtered by tag.

```sh
vlb datastores list --tag-category <category> --tags <tags> [options]
```

| Option | Required | Default | Description |
|---|---|---|---|
| `--tag-category` |  |  | Tag category name |
| `--tags` |  |  | Tag name(s), comma-separated |
| `--vcenter` |  |  | Filter by vCenter name |
| `--offset` |  | `0` | Offset for pagination |
| `--max-results` |  | `100` | Maximum number of results |

```sh
vlb datastores list --tag-category Environment --tags Production,Staging
```

---

### portgroups  Port Groups

#### `vlb portgroups list`

List port groups filtered by tag.

```sh
vlb portgroups list --tag-category <category> --tags <tags> [options]
```

| Option | Required | Default | Description |
|---|---|---|---|
| `--tag-category` |  |  | Tag category name |
| `--tags` |  |  | Tag name(s), comma-separated |
| `--vcenter` |  |  | Filter by vCenter name |
| `--offset` |  | `0` | Offset for pagination |
| `--max-results` |  | `100` | Maximum number of results |

```sh
vlb portgroups list --tag-category Network --tags DMZ
```

---

### vm-folders  VM Folders

#### `vlb vm-folders list`

List VM folders.

```sh
vlb vm-folders list [options]
```

| Option | Required | Default | Description |
|---|---|---|---|
| `--vm-folders` |  |  | Filter by folder name(s), comma-separated |
| `--vcenter` |  |  | Filter by vCenter name |
| `--offset` |  | `0` | Offset for pagination |
| `--max-results` |  | `100` | Maximum number of results |

```sh
vlb vm-folders list
vlb vm-folders list --vm-folders Production,Staging
```

---

### vm-snapshots  VM Snapshots

#### `vlb vm-snapshots list`

List VM snapshots for VMs in the specified folder(s).

```sh
vlb vm-snapshots list --vm-folders <folder> [options]
```

| Option | Required | Default | Description |
|---|---|---|---|
| `--vm-folders` |  |  | VM folder name(s), comma-separated |
| `--vcenter` |  |  | Filter by vCenter name |
| `--offset` |  | `0` | Offset for pagination |
| `--max-results` |  | `100` | Maximum number of results |

---

#### `vlb vm-snapshots get <vm_instance_uuid>`

List snapshots for a VM by its instance UUID.

```sh
vlb vm-snapshots get <vm_instance_uuid> --vcenter <vcenter> [options]
```

| Argument / Option | Required | Description |
|---|---|---|
| `vm_instance_uuid` |  | Instance UUID of the virtual machine |
| `--vcenter` |  | vCenter name |
| `--offset` |  | Offset for pagination (default: `0`) |
| `--max-results` |  | Maximum number of results (default: `100`) |

---

### events  Events

#### `vlb events list`

List events. Specify a time range using one of the three patterns below.

```sh
vlb events list [time range options] [filter options]
```

**Time range (choose one pattern):**

| Pattern | Options | Description |
|---|---|---|
| ISO 8601 | `--begin-time` / `--end-time` | Specify exact datetimes (e.g. `2026-04-01T00:00:00`) |
| Days ago | `--days-ago-begin` / `--days-ago-end` | Specify how many days ago (integer) |
| Hours ago | `--hours-ago-begin` / `--hours-ago-end` | Specify how many hours ago (integer) |

**Filter options:**

| Option | Description |
|---|---|
| `--event-types` | Event type(s), comma-separated |
| `--event-sources` | Event source(s), comma-separated |
| `--user-names` | Username(s), comma-separated |
| `--ip-addresses` | IP address(es), comma-separated |
| `--vcenter` | Filter by vCenter name |
| `--offset` | Offset for pagination (default: `0`) |
| `--max-results` | Maximum number of results (default: `100`) |

```sh
# Events from the last 24 hours
vlb events list --hours-ago-begin 24 --hours-ago-end 0

# Events from the last 7 days filtered by user
vlb events list --days-ago-begin 7 --days-ago-end 0 --user-names administrator

# Events in a specific date range, JSON output
vlb --format json events list \
    --begin-time 2026-04-01T00:00:00 \
    --end-time 2026-04-15T23:59:59
```

---

### alarms  Alarms

#### `vlb alarms list`

List alarms. Specify a time range using one of the three patterns below.

```sh
vlb alarms list [time range options] [filter options]
```

**Time range (choose one pattern):**

| Pattern | Options | Description |
|---|---|---|
| ISO 8601 | `--begin-time` / `--end-time` | Specify exact datetimes (e.g. `2026-04-01T00:00:00`) |
| Days ago | `--days-ago-begin` / `--days-ago-end` | Specify how many days ago (integer) |
| Hours ago | `--hours-ago-begin` / `--hours-ago-end` | Specify how many hours ago (integer) |

**Filter options:**

| Option | Description |
|---|---|
| `--statuses` | Alarm status(es): `red`, `yellow`, `green`, `gray`  comma-separated |
| `--alarm-sources` | Alarm source(s), comma-separated |
| `--acknowledged [true\|false]` | Filter by acknowledged flag |
| `--vcenter` | Filter by vCenter name |
| `--offset` | Offset for pagination (default: `0`) |
| `--max-results` | Maximum number of results (default: `100`) |

```sh
# Unacknowledged red alarms from the last hour
vlb alarms list --hours-ago-begin 1 --hours-ago-end 0 \
    --statuses red --acknowledged false

# All alarms from the last 3 days in JSON format
vlb --format json alarms list --days-ago-begin 3 --days-ago-end 0
```

---

### vcenters  vCenters

#### `vlb vcenters list`

List the vCenter instances managed by the bridge.

```sh
vlb vcenters list [options]
```

| Option | Required | Default | Description |
|---|---|---|---|
| `--vcenter` |  |  | Filter by vCenter name |
| `--offset` |  | `0` | Offset for pagination |
| `--max-results` |  | `100` | Maximum number of results |

```sh
vlb vcenters list
```

---

### admins  Administration

#### `vlb admins flush-caches`

Clear all cached API responses.

```sh
vlb admins flush-caches
```

---

#### `vlb admins reset-ws-session`

Clear the down-mark for all vCenters.

```sh
vlb admins reset-ws-session
```

---

### healthcheck

Run a health check against the service.

```sh
vlb healthcheck
```

---

## Output Formats

Use `--format` to switch between output formats.

| Value | Description |
|---|---|
| `table` | Human-readable table (default) |
| `json` | JSON output, suitable for scripting and pipelines |

```sh
# Table format (default)
vlb vms list --vm-folders Production

# JSON format
vlb --format json vms list --vm-folders Production

# Combine with jq to extract VM names
vlb --format json vms list --vm-folders Production | jq '.results[].name'
```

---

## Quick Start

```sh
# 1. Set environment variables
export VLB_HOST=https://vcenter-lookup-bridge.example.com
export VLB_USERNAME=myuser
export VLB_PASSWORD=mypassword

# 2. Verify connectivity
vlb healthcheck

# 3. List managed vCenters
vlb vcenters list

# 4. Browse VM folders
vlb vm-folders list

# 5. List VMs in a folder
vlb vms list --vm-folders Production

# 6. Check recent alarms
vlb alarms list --hours-ago-begin 24 --hours-ago-end 0 --statuses red,yellow
```
