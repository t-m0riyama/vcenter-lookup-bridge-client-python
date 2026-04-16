import sys

import click

from vcenter_lookup_bridge_client import ClustersApi
from vcenter_lookup_bridge_client.exceptions import ApiException
from .formatters import output_json, output_table
from .i18n import _

_CLUSTER_COLUMNS = ["name", "vcenter", "datacenter", "num_hosts", "num_cpu_cores", "memory_size_mb"]


@click.group(help=_("Cluster operations"))
def clusters():
    pass


@clusters.command("list", help=_("List clusters"))
@click.option("--clusters", "cluster_names", default=None, help=_("Cluster name(s) (comma-separated)"))
@click.option("--offset", default=0, show_default=True, help=_("Offset for pagination"))
@click.option("--max-results", default=100, show_default=True, help=_("Maximum number of results"))
@click.option("--vcenter", default=None, help=_("vCenter name"))
@click.pass_context
def list_clusters(ctx, cluster_names, offset, max_results, vcenter):
    api = ClustersApi(ctx.obj["api_client"])
    names = [n.strip() for n in cluster_names.split(",")] if cluster_names else None
    try:
        response = api.list_clusters(clusters=names, offset=offset, max_results=max_results, vcenter=vcenter)
    except ApiException as e:
        click.echo(_("Error {status}: {reason}").format(status=e.status, reason=e.reason))
        sys.exit(1)
    if ctx.obj["format"] == "json":
        output_json(response)
    else:
        output_table(response.results, _CLUSTER_COLUMNS)
